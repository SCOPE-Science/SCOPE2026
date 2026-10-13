#!/usr/bin/env python3
"""Exhaustive reproducibility checker for identifying codes of GP(8,3).
Python 3 standard library only. All search domains are finite and explicit.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import csv

N=16
V=range(N)
EDGES = [tuple(sorted((i,(i+1)%8))) for i in range(8)] + [(i,i+8) for i in range(8)] + [tuple(sorted((8+i,8+(i+3)%8))) for i in range(8)]
EDGES=sorted(set(EDGES))
assert len(EDGES)==24
NEIGH=[set() for _ in V]
for x,y in EDGES: NEIGH[x].add(y);NEIGH[y].add(x)
assert all(len(x)==3 for x in NEIGH)

# Separation hypergraph: code iff it hits every closed neighborhood and every
# symmetric difference of distinct closed neighborhoods.
CLOSED=[sum(1<<v for v in {u}|NEIGH[u]) for u in V]
constraints=set(CLOSED)
constraints.update(CLOSED[a]^CLOSED[b] for a,b in combinations(V,2))
assert len(constraints)==136
sizes=Counter(c.bit_count() for c in constraints)
assert sizes=={4:40,6:48,8:48},sizes
small=[c for c in constraints if c.bit_count()<8]
assert len(small)==88
assert all(any(s&c==s for s in small) for c in constraints if c.bit_count()==8)

def hitting(mask):return all(mask & s for s in small)
def direct(mask):
 sig=[mask & m for m in CLOSED]
 return all(sig) and len(set(sig))==N

counts=Counter(); opt=[]; counts_by_split=Counter(); min_n=N
# A and B are the bipartition of the cubic configuration (not outer/inner GP rings).
A={1,3,5,7,8,10,12,14};B=set(V)-A
assert all((u in A)!=(v in A) for u,v in EDGES)
for x in range(1<<N):
 d=direct(x);h=hitting(x)
 assert d==h, ('disagreement',x)
 if d:
  k=x.bit_count();counts[k]+=1
  if k<min_n:min_n=k;opt=[]
  if k==min_n:opt.append(x)
assert min_n==8
EXPECTED={8:584,9:3840,10:5440,11:3888,12:1780,13:560,14:120,15:16,16:1}
assert dict(counts)==EXPECTED,counts
assert len(opt)==584
for x in opt:
 a=sum((x>>i)&1 for i in A)
 counts_by_split[tuple(sorted((a,8-a)))]+=1
assert dict(counts_by_split)=={(0,8):2,(1,7):48,(2,6):72,(3,5):192,(4,4):270},counts_by_split

# Full automorphism group reconstructed by backtracking, imposing every
# adjacency/nonadjacency relation against vertices already assigned.
# A connected BFS source ordering forces every new vertex to have a mapped neighbor.
order=[0];seen={0}
for u in order:
 for v in sorted(NEIGH[u]):
  if v not in seen:order.append(v);seen.add(v)
assert len(order)==N
perms=[]
p=[-1]*N;used=set()
def visit(i):
 if i==N:
  assert all(((u in NEIGH[v])==(p[u] in NEIGH[p[v]])) for u in V for v in V)
  perms.append(tuple(p));return
 u=order[i]
 for t in V:
  if t in used:continue
  if all(((u in NEIGH[w])==(t in NEIGH[p[w]])) for w in order[:i]):
   p[u]=t;used.add(t);visit(i+1);used.remove(t);p[u]=-1
visit(0)
assert len(perms)==96,len(perms)
assert len(set(perms))==96

def image(mask,perm):
 return sum(1<<perm[u] for u in V if (mask>>u)&1)
remaining=set(opt);orbits=[]
while remaining:
 r=min(remaining);orbit={image(r,p) for p in perms}
 assert orbit<=remaining
 a=sum((r>>u)&1 for u in A)
 induced=sum(bool(r>>u&1 and r>>v&1) for u,v in EDGES)
 orbits.append((r,len(orbit),min(a,8-a),max(a,8-a),induced))
 remaining-=orbit
orbits.sort()
expected_orbits=[(255,6),(479,96),(510,48),(975,48),(989,96),(1020,48),(1399,48),(1879,48),(4471,24),(4590,24),(5038,48),(5610,48),(21930,2)]
assert [(a,b) for a,b,*_ in orbits]==expected_orbits,orbits
assert sum(x[1] for x in orbits)==584
csv_path=Path(__file__).with_name('orbits.csv')
with csv_path.open(newline='',encoding='utf-8') as f:
 r=csv.DictReader(f)
 table=[(int(row['representative_mask']),int(row['orbit_size']),int(row['small_side']),int(row['large_side']),int(row['induced_edges'])) for row in r]
assert table==orbits,(table,orbits)
print('VERIFY_PY_OK GP(8,3) vertices=16 edges=24 bipartition=8+8 constraints=136 minimal_constraints=88')
print('VERIFY_PY_OK every_mask=65536 signatures_and_hitting_agree minimum=8 minimum_codes=584')
print('VERIFY_PY_OK polynomial='+','.join(f'{k}:{v}' for k,v in sorted(counts.items())))
print('VERIFY_PY_OK min_bipartition_profiles='+','.join(f'{k}:{v}' for k,v in sorted(counts_by_split.items())))
print('VERIFY_PY_OK automorphisms=96 optimum_orbits=13 orbit_sizes='+','.join(map(str,sorted(v[1] for v in orbits))))
