"""Independent finite checks for the windmill parallel chip-firing orbit census.

Usage: python3 verify_windmill.py
The mathematical proof for arbitrary graph sizes is given separately.
"""
from __future__ import annotations
from collections import Counter
from itertools import product
from math import comb, prod

def A(m):
    return [comb(m, k) * (m-k)**k * (k+1)**(m-k) for k in range(m+1)]

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def predicted(n,m):
    p=[1]
    for _ in range(n):
        p=mul(p,A(m))
    return [ (m*n-k)*x for k,x in enumerate(p)]

def graph(n,m):
    neigh=[[] for _ in range(1+n*m)]
    for p in range(n):
        group=range(1+p*m,1+(p+1)*m)
        for u in group:
            neigh[0].append(u);neigh[u].append(0)
            for v in group:
                if v!=u:neigh[u].append(v)
    return neigh

def step(s,neigh,d):
    f=[int(x>=j) for x,j in zip(s,d)]
    return tuple(x+sum(f[v] for v in neigh[u])-d[u]*f[u] for u,x in enumerate(s))

def direct(n,m):
    neigh=graph(n,m);d=list(map(len,neigh)); hist=Counter(); energies=Counter()
    count=0
    for s in product(*(range(2*x) for x in d)):
        if s[0]<d[0]:
            continue # one phase per primitive two-cycle has its center firing
        y=step(s,neigh,d)
        if y==s:continue
        if step(y,neigh,d)!=s: continue
        assert y[0]<d[0]
        assert all((a>=di)!=(b>=di) for a,b,di in zip(s,y,d))
        hist[sum(s[i]>=d[i] for i in range(1,len(s)))]+=1
        energies[sum(s)]+=1
        count+=1
    expect=predicted(n,m)
    assert [hist.get(k,0) for k in range(n*m+1)]==expect,(n,m,hist,expect)
    assert all(energies[e]==energies[(2*m*m+m)*n-1-e] for e in energies)
    assert 2*sum(e*v for e,v in energies.items())==count*((2*m*m+m)*n-1)
    print('verified',n,m,'orbits',count,'hist',dict(sorted(hist.items())))

if __name__=='__main__':
    for n,m in [(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(4,2),(1,3),(2,3),(1,4)]:
        direct(n,m)
    for m in range(1,10):
        a=A(m); alpha=sum(a); mu=sum(k*w for k,w in enumerate(a))/alpha
        beta=sum((m-k)*w for k,w in enumerate(a))
        assert 0<=mu<m
        for n in [1,2,3,5,10]:
            h=predicted(n,m)
            assert sum(h)==n*beta*alpha**(n-1)
            assert sum(k*value for k,value in enumerate(h)) >= 0
    print('WINDMILL_CHIPFIRING_VERIFY_OK')
