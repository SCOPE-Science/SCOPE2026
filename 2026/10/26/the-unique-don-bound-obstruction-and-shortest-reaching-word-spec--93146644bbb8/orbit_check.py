from collections import Counter,deque
from itertools import product
from pathlib import Path

def maps_for(code):
 return tuple((code>>(3*i))&7 for i in range(8))
def rotcode(code):
 f=maps_for(code)
 out=[0]*8
 for i in range(8):out[(i+1)%8]=(f[i]+1)%8
 return sum(v<<(3*i) for i,v in enumerate(out))
def certificate(code):
 f=maps_for(code);trans=[]
 for s in range(256):
  a=((s<<1)&255)|(s>>7)
  b=0
  for i in range(8):
   if s>>i&1:b|=1<<f[i]
  trans.append((a,b))
 dist={255:0};ways={255:1};firstword={255:''};q=deque([255])
 while q:
  s=q.popleft()
  for k,t in enumerate(trans[s]):
   if t not in dist:
    dist[t]=dist[s]+1;ways[t]=ways[s];firstword[t]=firstword[s]+'ab'[k];q.append(t)
   elif dist[t]==dist[s]+1:ways[t]+=ways[s]
 hard=[s for s in range(1,255) if s.bit_count()==6 and dist.get(s,999)>16]
 assert len(dist)==255 and len(hard)==1 and dist[hard[0]]==17
 return hard[0],ways[hard[0]],firstword[hard[0]]
reps=[]
for l in Path('violation8.txt').read_text().splitlines():
 if l.startswith('REPS:'):continue
 bits=l.split(' ')
 if bits and bits[0].isdigit() and len(bits)>=3 and ',' in bits[2]:reps.append(int(bits[0]))
assert len(reps)==68,len(reps)
classes=Counter();examples={}
for x in reps:
 orbit=[];y=x
 for _ in range(8):orbit.append(y);y=rotcode(y)
 assert y==x and len(set(orbit))==8
 assert x==min(orbit)
 mask,mult,word=certificate(x)
 classes[mult]+=1
 examples.setdefault(mult,(x,maps_for(x),mask,mult,word))
print('classes',dict(sorted(classes.items())))
for k,x in sorted(examples.items()):print('example',k,x)
