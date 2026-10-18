#!/usr/bin/env python3
"""Exact checks of leaf-count regression conditioned on marked-vertex distance.
Usage: python verify.py
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial

def prufer_tree(seq):
    n=len(seq)+2
    deg=[1]*n
    for x in seq: deg[x]+=1
    edges=[]
    for x in seq:
        leaf=next(y for y in range(n) if deg[y]==1)
        edges.append((leaf,x))
        deg[leaf]-=1;deg[x]-=1
    a,b=[i for i,v in enumerate(deg) if v==1]
    edges.append((a,b))
    return edges

def marked_distance(n,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    visited={0};front=[0];d=0
    while front:
        if 1 in front:return d
        nxt=[]
        for x in front:
            for y in adj[x]:
                if y not in visited:visited.add(y);nxt.append(y)
        front=nxt;d+=1
    raise AssertionError('not a tree')

def path_count(n,k):
    x=1
    for j in range(k-1):x*=n-2-j
    return x*(k+1)*Fraction(n**max(n-k-2,0),n**max(k+2-n,0))

def mu(n,k):
    # Equivalent nonnegative-exponent rational representation.
    rr=Fraction(n-1,n)**(n-k-2)
    return (n-k+1-Fraction(2,k+1))*rr

def difference(n,k):
    return Fraction(2*(n-1)-k*(k+1)**2,n*(k+1)*(k+2))*Fraction(n-1,n)**(n-k-3)

def full_check():
    checks=0
    for n in range(2,8):
        counts=defaultdict(int);sums=defaultdict(int); e_non=defaultdict(int);e_end=defaultdict(int)
        for seq in product(range(n),repeat=n-2):
            edges=prufer_tree(seq)
            deg=[0]*n
            for a,b in edges:deg[a]+=1;deg[b]+=1
            k=marked_distance(n,edges)
            counts[k]+=1;sums[k]+=sum(x==1 for x in deg)
            e_non[k]+=sum(x==1 for x in deg[2:])
            e_end[k]+=sum(x==1 for x in deg[:2])
        for k in range(1,n):
            assert counts[k]==path_count(n,k),(n,k,counts[k],path_count(n,k));checks+=1
            assert Fraction(sums[k],counts[k])==mu(n,k),(n,k,Fraction(sums[k],counts[k]),mu(n,k));checks+=1
            r=Fraction(n-1,n)**(n-k-2)
            assert Fraction(e_non[k],counts[k])==(n-k-1)*r;checks+=1
            assert Fraction(e_end[k],counts[k])==Fraction(2*k,k+1)*r;checks+=1
        for k in range(1,n-1):
            assert mu(n,k+1)-mu(n,k)==difference(n,k);checks+=1
    for n in range(2,301):
        xs=[mu(n,k) for k in range(1,n)]
        if n>2:
            signs=[int(xs[i+1]>xs[i])-int(xs[i+1]<xs[i]) for i in range(len(xs)-1)]
            signs2=[int(2*(n-1)>k*(k+1)**2)-int(2*(n-1)<k*(k+1)**2) for k in range(1,n-1)]
            assert signs==signs2;checks+=1
            M=max(xs); actual={k+1 for k,z in enumerate(xs) if z==M}
            k0=next(k for k in range(1,n) if k*(k+1)**2>=2*(n-1))
            wanted={k0,k0+1} if k0*(k0+1)**2==2*(n-1) else {k0}
            assert actual==wanted,(n,actual,wanted);checks+=1
        assert xs[0] == n*Fraction(n-1,n)**(n-2);checks+=1
    print('passed',checks,'exact assertions')

if __name__=='__main__':full_check()
