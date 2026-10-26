#!/usr/bin/env python3
"""Independently classify minimum forcing configurations by Franklin graph automorphisms."""
import itertools,collections,json

n=12
V=range(n)
neighbor={i:set() for i in V}
for i in V:
 for j in ((i-1)%n,(i+1)%n,(i+[5,-5][i%2])%n):
  neighbor[i].add(j);neighbor[j].add(i)
# A connected exploration order makes partial adjacency checks decisive.
order=[0]; seen={0}
for v in order:
 for w in sorted(neighbor[v]):
  if w not in seen:order.append(w);seen.add(w)
assert len(order)==12
maps=[]
def search(assignment,used):
 if len(assignment)==n:
  maps.append(dict(assignment)); return
 x=order[len(assignment)]
 for y in V:
  if y in used:continue
  if all(((u in neighbor[x]) == (v in neighbor[y])) for u,v in assignment.items()):
   assignment[x]=y
   search(assignment,used | {y})
   del assignment[x]
search({},set())
assert len(maps)==48

def forces(S):
 b=set(S)
 while len(b)<n:
  can=[next(iter(w)) for u in sorted(b) if len(w:=neighbor[u]-b)==1]
  if not can:return False
  b.update(can)
 return True
bases={frozenset(S) for S in itertools.combinations(V,5) if forces(S)}
assert len(bases)==324
remaining=set(bases); orbits=[]
while remaining:
 S=min(remaining,key=lambda t:tuple(sorted(t)))
 orbit={frozenset(p[v] for v in S) for p in maps}
 assert orbit<=bases
 orbits.append({'representative':sorted(S),'size':len(orbit)})
 remaining-=orbit
assert sorted(o['size'] for o in orbits)==[12,24,24,24,48,48,48,48,48]
# The structural class of each orbit is augmented with its local slide degree and eccentricity.
slide={B:set() for B in bases}
for B in bases:
 for u in B:
  for v in neighbor[u]-B:
   C=(B-{u})|{v}
   if C in bases:slide[B].add(C)
for item in orbits:
 B=frozenset(item['representative'])
 discovered={B:0};todo=collections.deque([B])
 while todo:
  x=todo.popleft()
  for y in slide[x]:
   if y not in discovered:
    discovered[y]=discovered[x]+1;todo.append(y)
 assert len(discovered)==324
 item['slide_degree']=len(slide[B])
 item['slide_eccentricity']=max(discovered.values())
print(json.dumps({'automorphisms':len(maps),'number_of_orbits':len(orbits),
                  'orbits':orbits},sort_keys=True))
