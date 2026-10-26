#!/usr/bin/env python3
"""Exact rational checks for the path strictness identity; stdlib only."""
from fractions import Fraction as Q
from functools import lru_cache

@lru_cache(None)
def alpha(n):
    if n <= 0: return Q(0)
    return Q(1)+sum(alpha(i-2)+alpha(n-i-1) for i in range(1,n+1))/n

def nu(adj):
    total=Q(0)
    for v in range(len(adj)):
        alive=set(range(len(adj)))-{v}-adj[v]
        seen=set()
        for u in alive:
            if u in seen: continue
            stack=[u]; seen.add(u); m=0
            while stack:
                z=stack.pop(); m+=1
                for w in adj[z]:
                    if w in alive and w not in seen:
                        seen.add(w);stack.append(w)
            total+=alpha(m)
    return total

def graph(a,b,ell,shift):
    n=a+b+ell+1
    adj=[set() for _ in range(n)]
    edges=[(i,i+1) for i in range(a+ell)]
    for j in range(a+ell+1,n):
        edges.append(((a if shift else a+ell) if j==a+ell+1 else j-1,j))
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    return adj

def gap(r,s):return alpha(r)+alpha(s)-alpha(r+s)

def predicted(a,b,ell):
    return gap(a,ell)+gap(b,ell)+sum(alpha(a+b+j)+alpha(j)-alpha(a+j)-alpha(b+j) for j in range(1,ell))

for r in range(1,81):
    for s in range(1,81):
        q=gap(r,s)
        assert (q==0)==(r==s==2),(r,s,q)
        assert q>=0
print('SUBADDITIVITY_EQUALITY_CLASSIFICATION_CHECKED r,s<=80')
count=0
for a in range(1,6):
 for b in range(1,6):
  for ell in range(1,6):
   actual=nu(graph(a,b,ell,True))-nu(graph(a,b,ell,False))
   assert actual==predicted(a,b,ell),(a,b,ell,actual,predicted(a,b,ell))
   assert actual>0
   count+=1
assert alpha(5)+alpha(1)-2*alpha(3)==Q(2,15)
print('EXACT_SPIDER_IDENTITY_AND_STRICTNESS_CHECKED',count,'CASES')
print('EXCEPTIONAL_INTERIOR_GAIN',Q(2,15))
print('VERIFY_OK')
