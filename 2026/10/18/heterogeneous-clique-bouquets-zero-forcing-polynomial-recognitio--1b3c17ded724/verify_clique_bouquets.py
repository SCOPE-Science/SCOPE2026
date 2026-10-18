#!/usr/bin/env python3
"""Standalone exhaustive verification of ordinary forcing on clique bouquets."""
from itertools import product
from collections import Counter
from math import comb

def graph(sizes):
    V = 1 + sum(sizes)
    nbr=[set() for _ in range(V)]
    start=1
    for r in sizes:
        block=range(start,start+r)
        for x in block:
            nbr[0].add(x);nbr[x].add(0)
            for y in block:
                if y!=x: nbr[x].add(y)
        start+=r
    return nbr

def forces(nbr,sel):
    blue=set(sel)
    while True:
        moves=set()
        for v in blue:
            white=nbr[v]-blue
            if len(white)==1: moves.add(next(iter(white)))
        if not moves: return len(blue)==len(nbr)
        blue.update(moves)

def pred(sizes,blue):
    if all(sum(x in blue for x in range(start,start+r))>=r-1
           for start,r in starts(sizes)):
        return 0 in blue or any(all(x in blue for x in range(start,start+r)) for start,r in starts(sizes))
    return False

def starts(sizes):
    s=1
    for r in sizes:
        yield s,r
        s+=r

def polynomial(sizes):
    A=Counter({0:1});B=Counter({0:1})
    for r in sizes:
        aa=Counter({r:1,r-1:r});bb=Counter({r-1:r})
        A=multiply(A,aa)
        B=multiply(B,bb)
    R=Counter(A)
    for k,v in A.items():R[k+1]+=v
    for k,v in B.items():R[k]-=v
    return {k:v for k,v in R.items() if v}

def multiply(a,b):
    res=Counter()
    for j,x in a.items():
        for k,y in b.items():res[j+k]+=x*y
    return res

def recognize(sizes, zpoly):
    # Strip the predictable valuation, then divide H(z)-H(-1) by z+1.
    s=min(zpoly)-1
    h={k-s:c for k,c in zpoly.items()}
    c=sum(v*(-1)**k for k,v in h.items())
    n=max(h)
    q={n-1:h[n]}
    for j in range(n-1,0,-1):
        q[j-1]=h.get(j,0)-q[j]
    assert q[0]==h.get(0,0)-c
    expected=Counter({0:1})
    for r in sizes: expected=multiply(expected,Counter({0:r,1:1}))
    assert dict(q)==dict(expected), (sizes,q,expected)


def main():
    profiles=0; subsets=0
    for t in range(1,4):
        for sizes in product([2,3,4],repeat=t):
            n=1+sum(sizes)
            if n>12:continue
            nbr=graph(sizes)
            actual=Counter()
            for mask in range(1<<n):
                sel={i for i in range(n) if mask>>i&1}
                b=forces(nbr,sel)
                assert b==pred(sizes,sel),(sizes,sel,b)
                if b:actual[len(sel)]+=1
                subsets+=1
            expected=polynomial(sizes)
            recognize(sizes,expected)
            assert dict(actual)==expected,(sizes,actual,expected)
            profiles+=1
    print('VERIFICATION_OK profiles=%d initial_subsets=%d'%(profiles,subsets))
    for r in (2,3,5):
        for t in (100,1000,10000):
            import math
            lam=1.3
            delta=lam/math.sqrt(t*comb(r,2))
            p=1-delta
            a=p**r+r*p**(r-1)*(1-p)
            b=r*p**(r-1)*(1-p)
            prob=a**t-(1-p)*b**t
            print('asymptotic',r,t,round(prob,6),'target',round(math.exp(-lam*lam),6))

if __name__=='__main__':main()
