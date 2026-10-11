#!/usr/bin/env python3
"""Independent recurrence check of the independence polynomial and graph girth."""
from itertools import combinations
from collections import deque
from functools import lru_cache
from math import comb
lines={frozenset((i,(i+1)%7,(i+3)%7)) for i in range(7)}
verts=[frozenset(a) for a in combinations(range(7),3) if frozenset(a) not in lines]
assert len(verts)==28
N=[sum(1<<j for j,b in enumerate(verts) if a.isdisjoint(b)) for a in verts]
assert sum(x.bit_count() for x in N)==84
@lru_cache(None)
def polynomial(mask):
 if not mask:return (1,)
 bit=mask&-mask
 idx=bit.bit_length()-1
 a=polynomial(mask^bit)
 b=polynomial(mask&~(bit|N[idx]))
 out=[0]*max(len(a),len(b)+1)
 for i,x in enumerate(a):out[i]+=x
 for i,x in enumerate(b):out[i+1]+=x
 return tuple(out)
p=polynomial((1<<28)-1)
assert p==(1,28,336,2268,9506,25788,45836,52928,38556,16660,3752,336,14)
assert sum((-1)**j*v for j,v in enumerate(p))==-7
# Undirected BFS: test shortest cycles through each vertex, excluding immediate parent.
girth=28
for source in range(28):
 distance={source:0};parent={source:-1};todo=deque([source])
 while todo:
  u=todo.popleft()
  neighbors=N[u]
  while neighbors:
   bit=neighbors&-neighbors;neighbors^=bit;v=bit.bit_length()-1
   if v not in distance:
    distance[v]=distance[u]+1;parent[v]=u;todo.append(v)
   elif parent[u]!=v:girth=min(girth,distance[u]+distance[v]+1)
assert girth==7
print('COXETER_INDEPENDENT_CHECK_OK','independence_polynomial',p,'I(-1)',-7,'girth',girth, 'memo_states',polynomial.cache_info().currsize)
