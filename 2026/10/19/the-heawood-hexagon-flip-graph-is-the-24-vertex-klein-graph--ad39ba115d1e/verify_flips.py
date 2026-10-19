#!/usr/bin/env python3
"""Self-contained exact verification of perfect-matching hexagon flips.
Run from the directory containing KLEIN_ADJACENCY.txt and ISOMORPHISM.txt.
"""
from collections import Counter, deque
from itertools import permutations, combinations
from pathlib import Path

N=7
LINES=[{(j+t)%7 for t in (0,1,3)} for j in range(N)]
assert len({frozenset(L) for L in LINES})==7
assert all(sum(x in L for L in LINES)==3 for x in range(N))
P=sorted(p for p in permutations(range(N)) if all(x in LINES[p[x]] for x in range(N)))
assert len(P)==24
assert Path('MATCHINGS.txt').read_text(encoding='utf-8').splitlines()==[''.join(map(str,p)) for p in P]

def bfs(adj,start):
 d={start:0};q=deque([start])
 while q:
  i=q.popleft()
  for j in adj[i]:
   if j not in d:d[j]=d[i]+1;q.append(j)
 return d

# Generate each distinct simple six-cycle by alternating point/line paths.
# Three point indices and three line indices make a six-cycle exactly when
# all six consecutive incidence edges are present.
cycles=set()
for p0,p1,p2 in permutations(range(N),3):
 for l0,l1,l2 in permutations(range(N),3):
  if (p0 in LINES[l0] and p1 in LINES[l0] and
      p1 in LINES[l1] and p2 in LINES[l1] and
      p2 in LINES[l2] and p0 in LINES[l2]):
   cycles.add(frozenset(((p0,l0),(p1,l0),(p1,l1),(p2,l1),(p2,l2),(p0,l2))))
assert len(cycles)==28,len(cycles)

# Flipping a 6-cycle is legitimate if precisely every other cycle edge is
# in the current matching; the replacement must be a perfect matching.
lookup={p:i for i,p in enumerate(P)}
adj=[set() for _ in P]
usage=Counter()
for i,p in enumerate(P):
 matching={(u,p[u]) for u in range(N)}
 for C in cycles:
  common=C&matching
  if len(common)!=3:continue
  # The symmetric-difference of six edges is another perfect matching.
  new=(matching-C)|(C-matching)
  assert len(new)==7 and len({u for u,v in new})==7 and len({v for u,v in new})==7
  q=tuple(dict(new)[u] for u in range(N))
  j=lookup[q]; assert i!=j
  adj[i].add(j)
  usage[C]+=1
assert all(len(x)==7 for x in adj)
assert all(i in adj[j] for i,x in enumerate(adj) for j in x)
assert sum(map(len,adj))//2==84
assert all(n==6 for n in usage.values()) and len(usage)==28

# Validate the external graph isomorphism against a recorded 24 x 24
# adjacency matrix of the 24-vertex Klein graph, entry by entry.
rows=Path('KLEIN_ADJACENCY.txt').read_text(encoding='utf-8').splitlines()
assert len(rows)==24 and all(len(r)==24 and set(r)<={'0','1'} for r in rows)
assert all(rows[u][v]==rows[v][u] for u in range(24) for v in range(24))
assert all(rows[u][u]=='0' and rows[u].count('1')==7 for u in range(24))
phi=[int(t) for t in Path('ISOMORPHISM.txt').read_text(encoding='utf-8').split()]
assert len(phi)==24 and set(phi)==set(range(24))
for u in range(24):
 for v in range(24):
  assert (v in adj[u])==(rows[phi[u]][phi[v]]=='1'),(u,v)

# Distances, common-edge intersection and distance-regularity.
all_dist=[bfs(adj,u) for u in range(24)]
assert all(len(d)==24 for d in all_dist)
for u,d in enumerate(all_dist):
 assert Counter(d.values())==Counter({0:1,1:7,2:14,3:2})
 for v,dist in d.items():
  if dist==0: continue
  inward=sum(d[w]==dist-1 for w in adj[v]);outward=sum(d[w]==dist+1 for w in adj[v])
  assert inward==[0,1,2,7][dist],(u,v,dist,'c')
  assert outward==[7,4,1,0][dist],(u,v,dist,'b')
  common=sum(P[u][k]==P[v][k] for k in range(N))
  assert (dist==1)==(common==4)
  assert (dist==2)==(common in (1,2))
  assert (dist==3)==(common==0)

# Distance three partitions the vertices into eight 3-element sets,
# corresponding precisely to all 3-edge-colourings up to palette rotation.
classes=set()
for u,d in enumerate(all_dist):
 classes.add(frozenset([u]+[v for v in range(24) if d[v]==3]))
assert len(classes)==8 and all(len(c)==3 for c in classes)
assert sum(len(c) for c in classes)==24
for c in classes:
 members=list(c)
 assert all(sum(P[u][k]==P[v][k] for k in range(N))==0 for u,v in combinations(members,2))
 assert len({(k,P[u][k]) for u in c for k in range(N)})==21
 for u in c:
  for other in classes-{c}:
   assert len(adj[u]&other)==1

print('VERIFY_OK: 24 perfect matchings, 28 hexagons, 84 flips, 7-regular')
print('VERIFY_OK: exact 24-vertex Klein-graph adjacency isomorphism')
print('VERIFY_OK: intersection array (7,4,1;1,2,7), diameter 3')
print('VERIFY_OK: 8 antipodal 3-classes = 8 perfect 3-edge-colourings')
