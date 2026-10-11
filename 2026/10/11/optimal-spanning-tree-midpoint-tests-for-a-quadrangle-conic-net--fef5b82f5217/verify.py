#!/usr/bin/env python3
"""Exact supplementary check for the spanning-tree midpoint criterion."""
from fractions import Fraction
from itertools import combinations

Q = [(0,0),(1,0),(0,1),(2,3)]
edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

# coefficient basis: x^2, xy, y^2, x, y, 1
def ev(p):
    x,y = map(Fraction,p)
    return [x*x,x*y,y*y,x,y,Fraction(1)]

E=[ev(p) for p in Q]

def rank(a):
    a=[row[:] for row in a]
    if not a: return 0
    r=0
    n=len(a[0])
    for c in range(n):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        q=a[r][c]
        a[r]=[z/q for z in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                q=a[i][c]
                a[i]=[u-q*v for u,v in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    return r

def components(sub):
    adj=[set() for _ in range(4)]
    for k in sub:
        i,j=edges[k]; adj[i].add(j); adj[j].add(i)
    seen=set(); c=0
    for s in range(4):
        if s in seen: continue
        c+=1; stack=[s]; seen.add(s)
        while stack:
            i=stack.pop()
            for j in adj[i]:
                if j not in seen:
                    seen.add(j); stack.append(j)
    return c

assert rank(E)==4
minimal=[]
for mask in range(1<<6):
    sub=[k for k in range(6) if mask>>k & 1]
    rows=[]
    for k in sub:
        i,j=edges[k]
        rows.append([b-a for a,b in zip(E[i],E[j])])
    c=components(sub)
    assert rank(rows)==4-c
    sufficient=(c==1)
    if sufficient and len(sub)==3:
        minimal.append(tuple(edges[k] for k in sub))
assert len(minimal)==16
assert not any(components(sub)==1 for sub in combinations(range(6),2))
print("VERIFY_OK rank(E)=4 minimal_spanning_trees=16 subsets=64")
