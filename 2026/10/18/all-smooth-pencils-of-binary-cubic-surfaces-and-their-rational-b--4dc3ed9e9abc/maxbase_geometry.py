#!/usr/bin/env python3
from itertools import combinations
from pathlib import Path
s=Path(str(Path(__file__).resolve().parent/'cubic_surface_smooth.bin')).read_bytes()
E=[(a,b,c,3-a-b-c) for a in range(4) for b in range(4-a) for c in range(4-a-b)]
mask=[sum(1<<i for i,e in enumerate(E) if all(e[j]==0 or p>>j&1 for j in range(4))) for p in range(1,16)]
full=[f for f in range(1,len(s)) if s[f] and all((f&m).bit_count()%2==0 for m in mask)]
assert len(full)==28
pencils={tuple(sorted((f,g,f^g))) for f,g in combinations(full,2) if s[f^g]}
assert len(pencils)==56
# Projective rational lines in P3(F2), 35 total
lines={frozenset((u,v,u^v)) for u in range(1,16) for v in range(1,16) if u!=v}
assert len(lines)==35
# Characteristic-2 expression of cubic coefficients in F(su+tv)
def coefficient(f,u,v,degree_u):
 out=0
 for i,e in enumerate(E):
  if not (f>>i)&1: continue
  poly=[1,0,0,0];deg=0
  for j in range(4):
   for _ in range(e[j]):
    v2=[0]*4
    for a in range(deg+1):
     if poly[a]:
      if u>>j&1:v2[a+1]^=1
      if v>>j&1:v2[a]^=1
    poly=v2;deg+=1
  out^=poly[degree_u]
 return out
line_sets={}
for f in full:
 line_sets[f]=set()
 for line in lines:
  u,v=sorted(line)[:2]
  if all(coefficient(f,u,v,k)==0 for k in range(4)):
   line_sets[f].add(line)
assert all(len(x)==15 for x in line_sets.values())
from collections import Counter
common=Counter(len(line_sets[f]&line_sets[g]) for f,g,h in pencils)
print('full point cubics',len(full),'maximal base pencils',len(pencils))
print('rational lines in base:',dict(common))
# orbits under generators 4
idx={e:i for i,e in enumerate(E)}
def subst(f,g):
 n=0
 for i,e in enumerate(E):
  if not(f>>i&1):continue
  if g<3:
   v=list(e);v[g],v[g+1]=v[g+1],v[g];n ^=1<<idx[tuple(v)]
  else:
   import math
   for j in range(e[0]+1):
    if math.comb(e[0],j)&1:
     v=(j,e[1]+e[0]-j,e[2],e[3]);n ^= 1<<idx[v]
 return n
remaining=set(pencils);orbit_sizes=[]
while remaining:
 seed=remaining.pop();q=[seed];known={seed}
 for P in q:
  for t in range(4):
   T=tuple(sorted(subst(f,t) for f in P))
   if T not in known:
    known.add(T);q.append(T)
  
 orbit_sizes.append(len(known));remaining-=known
print('projective pencil orbit sizes',orbit_sizes,'stabilizer',20160//orbit_sizes[0])
assert orbit_sizes==[56]
