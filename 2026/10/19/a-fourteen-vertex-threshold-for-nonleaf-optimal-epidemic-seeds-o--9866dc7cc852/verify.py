#!/usr/bin/env python3
"""Exact vertex-seeded single-contact epidemic on trees; no external dependencies."""
from fractions import Fraction
from functools import lru_cache
from collections import deque

WITNESS=((1,0),(1,2),(0,7),(2,3),(3,4),(4,5),(4,6),(7,8),(7,11),(8,9),(9,10),(11,12),(12,13))

def adjacency(n, edges):
    a=[set() for _ in range(n)]
    for u,v in edges:a[u].add(v);a[v].add(u)
    return a

def canon(n,edges):
    a=adjacency(n,edges)
    # Roots of minimum eccentricity are invariant under tree isomorphism.
    deg=list(map(len,a)); layer=[v for v in range(n) if deg[v]<=1]; left=n
    while left>2:
        left-=len(layer)
        nxt=[]
        for v in layer:
            for w in a[v]:
                deg[w]-=1
                if deg[w]==1:nxt.append(w)
        layer=nxt
    @lru_cache(None)
    def rooted(v,p):return '('+''.join(sorted(rooted(w,v) for w in a[v] if w!=p))+')'
    return min(rooted(v,-1) for v in layer)

def score(n, edges):
    a=adjacency(n,edges)
    @lru_cache(None)
    def incoming(u,parent):
        return Fraction(1)+sum((incoming(v,u) for v in a[u] if v!=parent),Fraction(0))/len(a[u])
    return tuple(Fraction(1)+sum((incoming(v,u) for v in a[u]),Fraction(0))/len(a[u]) for u in range(n))

def main():
    reps={canon(1,()):()}
    counts=[]
    for n in range(1,14):
        counts.append(len(reps))
        for ed in reps.values():
            if n==1: continue
            vals=score(n,ed)
            a=adjacency(n,ed)
            max_all=max(vals)
            max_leaf=max(vals[v] for v in range(n) if len(a[v])==1)
            assert max_all==max_leaf,(n,ed,vals)
        if n<13:
            nxt={}
            for ed in reps.values():
                for v in range(n):
                    new=ed+((v,n),)
                    key=canon(n+1,new)
                    if key not in nxt:nxt[key]=new
            reps=nxt
    assert counts==[1,1,1,2,3,6,11,23,47,106,235,551,1301]
    v=score(14,WITNESS)
    a=adjacency(14,WITNESS)
    allmax=max(v); leafmax=max(v[i] for i in range(14) if len(a[i])==1)
    assert v[0]==Fraction(49,16)
    assert leafmax==Fraction(1763,576)
    assert allmax==v[0] and allmax>leafmax
    print('unlabelled trees sizes 1..13:',counts)
    print('witness values:', [str(q) for q in v])
    print('max interior',allmax,'max leaf',leafmax,'margin',allmax-leafmax)
    print('verification PASS')
if __name__=='__main__':main()
