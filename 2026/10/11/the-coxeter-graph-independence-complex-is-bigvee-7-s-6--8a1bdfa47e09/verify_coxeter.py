#!/usr/bin/env python3
"""Reconstruct and verify an acyclic matching for the Coxeter graph independence complex."""
from collections import Counter, deque
from itertools import combinations

lines = [{i,(i+1)%7,(i+3)%7} for i in range(7)]
triples = [frozenset(z) for z in combinations(range(7),3) if set(z) not in lines]
n=len(triples)
assert n==28
adj=[0]*n
for i in range(n):
 for j in range(n):
  if i !=j and triples[i].isdisjoint(triples[j]): adj[i]|=1<<j
assert [a.bit_count() for a in adj]==[3]*n
allfaces=[]
def visit(mask,allowed):
 allfaces.append(mask)
 while allowed:
  bit=allowed&-allowed; allowed^=bit
  visit(mask|bit,allowed&~adj[bit.bit_length()-1])
visit(0,(1<<n)-1)
assert len(allfaces)==196009
fvector=Counter(x.bit_count() for x in allfaces)
assert [fvector[k] for k in range(13)]==[1,28,336,2268,9506,25788,45836,52928,38556,16660,3752,336,14]
remaining=set(allfaces)
matching={}
pivots=[]
for t in range(n):
 scored=[(sum(1 for f in remaining if not f&(1<<i) and (f|(1<<i)) in remaining),i) for i in range(n)]
 count,i=max(scored)
 if count==0:break
 bit=1<<i
 picked=[(f,f|bit) for f in remaining if not f&bit and (f|bit) in remaining]
 assert len(picked)==count
 for f,g in picked:
  remaining.remove(f);remaining.remove(g)
  matching[f]=g
 pivots.append((i,count))
assert len(matching)==98001
assert (0 in matching) and matching[0] == 1<<27
assert Counter(f.bit_count()-1 for f in remaining)==Counter({6:7})
# Restrict reduced matching to nonempty faces, leaving the singleton {27} critical.
matching.pop(0)
remaining.add(1<<27)
assert 0 not in remaining
assert Counter(f.bit_count()-1 for f in remaining)==Counter({0:1,6:7})
assert len(matching)==98000
# For any incident nonempty faces sigma (lower) and tau (upper),
# orient sigma->tau except when (sigma,tau) is a matched pair,
# in which case orient tau->sigma. Check the entire directed Hasse graph.
ids={f:i for i,f in enumerate(allfaces) if f}
indegree=[0]*len(allfaces)
# id ranges leave one hole at zero? face0 appears first, ids range 1..196008, allocate full.
incidences=0
for f in allfaces:
 if not f:continue
 bits=f
 while bits:
  bit=bits&-bits;bits^=bit
  g=f^bit
  if g==0:continue
  incidences+=1
  if matching.get(g)==f: indegree[ids[g]]+=1
  else: indegree[ids[f]]+=1
upper_to_lower={v:k for k,v in matching.items()}
queue=deque(f for f in allfaces if f and indegree[ids[f]]==0)
processed=0
edge_count=0
while queue:
 f=queue.popleft();processed+=1
 if f in upper_to_lower:
  g=upper_to_lower[f]
  indegree[ids[g]]-=1
  edge_count+=1
  if indegree[ids[g]]==0:queue.append(g)
 # Other incidences are from f to an upper face.
 for i in range(n):
  bit=1<<i
  if f&bit:continue
  g=f|bit
  if g not in ids or matching.get(f)==g:continue
  indegree[ids[g]]-=1
  edge_count+=1
  if indegree[ids[g]]==0:queue.append(g)
assert processed==len(allfaces)-1, (processed,len(allfaces)-1)
assert edge_count==incidences
print('COXETER_VERIFY_OK', 'vertices',n,'edges',sum(x.bit_count() for x in adj)//2,
      'nonempty_faces',len(allfaces)-1,'matched_pairs',len(matching),
      'critical',dict(sorted(Counter(f.bit_count()-1 for f in remaining).items())),
      'incidences',incidences,'pivots',pivots,flush=True)
