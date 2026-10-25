#!/usr/bin/env python3
"""Finite exact check of the constructive upper bound for labeled cycles.
Scientific program; stdlib only. The general theorem has a separate proof.
"""
from collections import deque
from math import isqrt

def parameter(n):
    m=4
    while m*(m+1)//2<n+4:
        m+=1
    return m

def chords(n,m):
    return {(1,j) for j in range(3,m+1)} | {(1,m+2)}

def edges(n,m):
    result={tuple(sorted((j,j%n+1))) for j in range(1,n+1)}
    result|=chords(n,m)
    return result

def reachable_connected(vertices, ed):
    vs=set(vertices)
    if not vs:return False
    seen={next(iter(vs))}
    changed=True
    while changed:
        changed=False
        for u,v in ed:
            if u in vs and v in vs:
                if (u in seen) != (v in seen):
                    seen.add(u); seen.add(v); changed=True
    return seen==vs

def subset_witnesses(m):
    w={0: ()}
    for x in range(2,m+1):
        for s,vs in list(w.items()):
            if s+x not in w:w[s+x]=(*vs,x)
    return w

def verify(n, explicit=False):
    m=parameter(n)
    assert n>=m+4 and m>=4
    T=n*(n+1)//2
    d=subset_witnesses(m)
    assert set(d)==({0,m*(m+1)//2-1}|set(range(2,m*(m+1)//2-2)))
    cover=[False]*(T+1)
    edge_set=edges(n,m)
    if explicit:
        assert len(edge_set)==n+m-1
    for s in range(1,m+5):
        assert s<=n
        cover[s]=True
        if explicit:assert reachable_connected([s],edge_set)
    for r in range(m+3):
        s=T-r
        cover[s]=True
        if explicit:
            verts=list(range(1,n+1)) if r==0 else [x for x in range(1,n+1) if x!=r]
            assert sum(verts)==s and reachable_connected(verts,edge_set)
    for b in range(m+2,n+1):
        h=sum(range(m+2,b+1))
        for q in range(3,m*(m+1)//2-1):
            s=h+q
            assert s<=T
            cover[s]=True
            if explicit:
                verts=[1,*d[q-1],*range(m+2,b+1)]
                assert len(verts)==len(set(verts)) and sum(verts)==s
                assert reachable_connected(verts,edge_set)
    assert all(cover[1:]),(n,m,[x for x in range(1,T+1) if not cover[x]][:10])
    return m

def brute(n,m):
    T=n*(n+1)//2
    ed=edges(n,m)
    seen=set()
    for mask in range(1,1<<n):
        v=[i+1 for i in range(n) if (mask>>i)&1]
        if reachable_connected(v,ed):seen.add(sum(v))
    assert seen==set(range(1,T+1)),(n,m)

for n in range(9,125):verify(n,explicit=n<=22)
for n in (125,240,500,1000,2000):verify(n,explicit=False)
for n in range(9,15):brute(n,parameter(n))
print('VERIFY_OK', 'exhaustive constructive interval coverage 9..124', 'explicit connected witnesses 9..22', 'independent brute connected subsets 9..14', 'large parameters 125,240,500,1000,2000')
