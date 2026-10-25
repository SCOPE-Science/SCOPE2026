#!/usr/bin/env python3
"""Independent gap-composition enumerator and adjacency checks, using stdlib only."""
from collections import deque
from itertools import combinations_with_replacement

def configurations(r,m,s):
 L=(r+1)*m+s
 # All weak compositions of s into m slots via combinations with replacement.
 ans=set()
 for mark in combinations_with_replacement(range(m),s):
  extra=[mark.count(i) for i in range(m)]
  for x in range(L):
   loc=[x];cur=x
   for i in range(m-1):
    cur=(cur+r+1+extra[i])%L
    loc.append(cur)
   ans.add(tuple(sorted(loc)))
 return L,ans

def evaluate(r,m,s):
 L,states=configurations(r,m,s)
 ix={v:i for i,v in enumerate(sorted(states))};g=[set() for _ in ix]
 for v,j in ix.items():
  vv=set(v)
  for u in v:
   for d in [-2,-1,1,2]:
    # Two-step changes are possible only if s>=2; we intentionally
    # do not infer neighbors by formulas for the reconfiguration graph.
    if abs(d)>s:continue
    w=(u+d)%L
    if w in vv:continue
    new=tuple(sorted((vv-{u})|{w}))
    h=ix.get(new)
    if h is not None:g[j].add(h)
 assert all(j in g[h] for j,nei in enumerate(g) for h in nei)
 comps=0;seen=set()
 for j in range(len(g)):
  if j in seen:continue
  comps+=1;todo=[j];seen.add(j)
  for u in todo:
   for v in g[u]:
    if v not in seen:seen.add(v);todo.append(v)
 triangles=sum(len(g[u]&g[v]) for u in range(len(g)) for v in g[u] if u<v)//3
 exp_count = [r+1,L,L*(m+1)//2][s]
 exp_degree=[0,2,4][s]
 exp_components=[r+1,1,1][s]
 assert len(ix)==exp_count,(r,m,s,len(ix),exp_count)
 assert all(len(x)==exp_degree for x in g),(r,m,s,'degrees')
 assert comps==exp_components,(r,m,s,'components')
 assert triangles==([0,0,L][s]),(r,m,s,'triangles',triangles)
 if s==1:
  assert len(g)==L and all(len(nei)==2 for nei in g)
 return r,m,s,L,len(ix),sum(map(len,g))//2,comps,triangles

if __name__=='__main__':
 cases=[evaluate(r,m,s) for r in range(2,8) for m in range(2,11) for s in range(3)]
 print('GAP_CHECK_OK',len(cases))
 for row in cases:print(*row)
