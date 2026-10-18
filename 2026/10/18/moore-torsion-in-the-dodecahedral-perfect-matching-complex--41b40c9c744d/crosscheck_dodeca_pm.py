#!/usr/bin/env python3
"""Independent elementary-collapse and modular-chain check of a perfect-matching complex."""
from collections import Counter,defaultdict
from itertools import combinations
import heapq,json
# Build GP(10,2) by vertex adjacency instead of the certificate's edge recursion.
V=set(range(20)); edge_set=set()
for i in range(10):
 for a,b in ((i,(i+1)%10),(i,i+10),(i+10,10+(i+2)%10)):
  edge_set.add(tuple(sorted((a,b))))
edge=sorted(edge_set); assert len(edge)==30
neigh={u:set() for u in V}
for a,b in edge:neigh[a].add(b);neigh[b].add(a)

# Independent match enumeration: recursive set partition on uncovered vertices.
def generate(uncovered):
 if not uncovered:
  yield frozenset();return
 a=min(uncovered)
 for b in sorted(neigh[a] & uncovered):
  e=tuple(sorted((a,b)))
  for tail in generate(uncovered-{a,b}):yield tail|{e}
matchings=list(generate(V))
assert len(matchings)==36
edge_num={e:i for i,e in enumerate(edge)}
all_faces=set()
for m in matchings:
 es=sorted(edge_num[e] for e in m)
 for r in range(11):
  for selection in combinations(es,r):
   all_faces.add(sum(1<<j for j in selection))
assert len(all_faces)==30504
faces=all_faces-{0}
# Elementary free-face collapses; only a face with precisely one surviving
# immediate coface is removed with that coface.
above=defaultdict(set)
for b in faces:
 if b.bit_count()>=2:
  for i in range(30):
   if b&(1<<i):above[b^(1<<i)].add(b)
heap=[(-a.bit_count(),a) for a in above if len(above[a])==1]
heapq.heapify(heap);pairs=0
while heap:
 _,a=heapq.heappop(heap)
 if a not in faces:continue
 uppers=above[a] & faces
 if len(uppers)!=1:continue
 b=next(iter(uppers))
 assert b.bit_count()==a.bit_count()+1 and b in faces
 for t in (a,b):
  faces.remove(t)
  if t.bit_count()>1:
   for i in range(30):
    if t & (1<<i):
     low=t^(1<<i)
     if low in faces:
      above[low].discard(t)
      if len(above[low])==1:heapq.heappush(heap,(-low.bit_count(),low))
 pairs+=1
levels={d:sorted(f for f in faces if f.bit_count()==d+1) for d in range(4)}
assert [len(levels[d]) for d in range(4)]==[30,231,543,361]
assert len(faces)==1165

def rank_mod_p(d,p):
 ids={face:i for i,face in enumerate(levels[d-1])}
 pivots={}
 for b in levels[d]:
  col={}
  j=0
  for i in range(30):
   if b & (1<<i):
    col[ids[b^(1<<i)]]=(-1 if j%2 else 1)%p;j+=1
  while col:
   k=max(col)
   if k not in pivots:
    inv=pow(col[k],-1,p)
    pivots[k]={i:(v*inv)%p for i,v in col.items() if (v*inv)%p}
    break
   t=col[k]
   for i,v in pivots[k].items():
    z=(col.get(i,0)-t*v)%p
    if z:col[i]=z
    else:col.pop(i,None)
 return len(pivots)
result={}
for p in [2,3,5,101]:
 ranks={d:rank_mod_p(d,p) for d in [1,2,3]}
 betti={d:len(levels[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0) for d in range(4)}
 result[str(p)]={'boundary_ranks':ranks,'reduced_betti':betti}
assert result['2']['reduced_betti']=={0:0,1:0,2:1,3:21}
for p in ['3','5','101']:
 assert result[p]['reduced_betti']=={0:0,1:0,2:0,3:20}
print(json.dumps({'perfect_matchings':len(matchings),'faces_including_empty':len(all_faces),'elementary_collapse_pairs':pairs,'remaining_fvector':[len(levels[d]) for d in range(4)],'modular_checks':result},sort_keys=True,separators=(',',':')))
