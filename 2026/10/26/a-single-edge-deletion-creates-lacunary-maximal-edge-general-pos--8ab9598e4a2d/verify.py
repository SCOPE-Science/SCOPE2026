from collections import Counter, deque
from math import comb
from itertools import combinations

def exact(p,q):
 E=[(a,b) for a in range(p) for b in range(p,p+q) if (a,b)!=(0,p)]
 adj={i:set() for i in range(p+q)}
 for a,b in E:adj[a].add(b);adj[b].add(a)
 eid={frozenset(e):j for j,e in enumerate(E)}
 forb=set()
 for start in range(p+q):
  d={start:0};todo=deque([start])
  while todo:
   x=todo.popleft()
   for y in adj[x]:
    if y not in d:d[y]=d[x]+1;todo.append(y)
  for x in adj[start]:
   for y in adj[x]-{start}:
    for z in adj[y]-{start,x}:
     if d.get(z)==3:
      forb.add(sum(1<<eid[frozenset(e)] for e in [(start,x),(x,y),(y,z)]))
 results=Counter(); maximal=Counter()
 for mask in range(1<<len(E)):
  if any(mask&f==f for f in forb):continue
  k=mask.bit_count();results[k]+=1
  if not any(not(mask>>j&1) and not any((mask|(1<<j))&f==f for f in forb) for j in range(len(E))):
   maximal[k]+=1
 return results,maximal

def predicted(p,q):
 s,t=p-1,q-1
 st=s*t
 results=Counter();maximal=Counter()
 for i in range(t+1):
  for j in range(s+1):
   z=comb(t,i)*comb(s,j)
   free=st-i*j
   for k in range(free+1):results[i+j+k]+=z*comb(free,k)
   if i*j>0 or i==t and j==0 or j==s and i==0:
    maximal[st+i+j-i*j]+=z
 return results,maximal

for p in range(2,5):
 for q in range(p,6):
  if p*q>20:continue
  a,b=exact(p,q);u,v=predicted(p,q)
  print((p,q),'sets',sum(a.values()),'maximal',sum(b.values()),'maximal profile',dict(sorted(b.items())),'match',(a,b)==(u,v))
  assert (a,b)==(u,v)
