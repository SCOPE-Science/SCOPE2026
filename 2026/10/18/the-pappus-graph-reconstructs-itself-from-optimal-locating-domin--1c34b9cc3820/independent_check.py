#!/usr/bin/env python3
"""Independent set-based replay using an LCF rather than affine definition.
The LCF vertex labels are mapped to affine vertices by a fixed explicit isomorphism.
"""
from itertools import combinations
from collections import Counter, deque
N=18
shift=(5,7,-7,7,-7,-5)*3
E={tuple(sorted((i,(i+1)%N))) for i in range(N)}
E|={tuple(sorted((i,(i+shift[i])%N))) for i in range(N)}
assert len(E)==27
adj=[set() for _ in range(N)]
for x,y in E:adj[x].add(y);adj[y].add(x)
assert all(len(a)==3 for a in adj)
# Independent explicit isomorphism: LCF index -> affine coordinate index.
P=(0,9,6,17,4,12,8,16,3,14,2,11,5,13,1,10,7,15)
assert sorted(P)==list(range(N))
aff=set()
for x in range(3):
 for y in range(3):
  for m in range(3):
   d=(y-m*x)%3
   aff.add(tuple(sorted((3*x+y,9+3*m+d))))
assert {tuple(sorted((P[x],P[y]))) for x,y in E}==aff

def ld(T):
    U=set(range(N))-T
    sig=[frozenset(T & adj[v]) for v in U]
    return bool(sig) and all(sig) and len(sig)==len(set(sig))

minima=[]; states=[]
for k in (5,6,7,8):
 cur=[]
 for v in combinations(range(N),k):
  T=frozenset(v)
  if ld(T):cur.append(T)
 if k==5:assert not cur
 if k==6:minima=cur
 if k in (6,7,8):states.extend(cur)
 assert len(cur)=={5:0,6:18,7:540,8:4869}[k]
assert len(states)==5427
hist=Counter(len(a&b) for a,b in combinations(minima,2))
assert hist=={4:27,2:54,1:54,0:18}
# Token move adjacency by single addition or removal, not by bitwise XOR.
ss=set(states);neigh={T:[] for T in ss}
for T in ss:
 for x in range(N):
  if x in T:
   X=T-{x}
  else:X=T|{x}
  if X in ss:neigh[T].append(X)
assert sum(map(len,neigh.values()))==12312
components=[]; unseen=set(ss)
while unseen:
 s=unseen.pop();queue=[s]
 for x in queue:
  for y in neigh[x]:
   if y in unseen:unseen.remove(y);queue.append(y)
 components.append(queue)
assert Counter(map(len,components))=={4419:1,1:1008}
opt_dist=Counter()
for i,s in enumerate(minima):
 d={s:0};Q=deque([s])
 while Q:
  x=Q.popleft()
  for y in neigh[x]:
   if y not in d:d[y]=d[x]+1;Q.append(y)
 for t in minima[i+1:]:
  assert d[t]==len(s^t)
  opt_dist[d[t]]+=1
assert opt_dist=={4:27,8:54,10:54,12:18}
print('LCF_INCIDENCE_ISOMORPHISM_OK')
print('LOCATION_DOMINATION_MIN6_18_CODES_OK')
print('INTERSECTIONS',dict(sorted(hist.items())))
print('TAR8_COMPONENTS',dict(sorted(Counter(map(len,components)).items())))
print('MIN_CODE_HAMMING_GEODESICS',dict(sorted(opt_dist.items())))
print('INDEPENDENT_VERIFY_OK')
