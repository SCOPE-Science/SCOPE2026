#!/usr/bin/env python3
"""Exact, direct tests of restrained Italian functions on one-leaf coronas.
Scientific reproducibility program; Python standard library only.
"""
from itertools import product,combinations
from collections import Counter

def direct(n,edges):
    adj=[set() for _ in range(2*n)]
    for a,b in edges:
        adj[a].add(b);adj[b].add(a)
    for v in range(n):
        adj[v].add(v+n);adj[v+n].add(v)
    d=Counter()
    for a in product(range(3),repeat=2*n):
        z={v for v,x in enumerate(a) if x==0}
        if any(not (adj[v]&z) or sum(a[u] for u in adj[v])<2 for v in z): continue
        d[sum(a)]+=1
    return dict(d)

def formula(n,edges):
    adj=[set() for _ in range(n)]
    for a,b in edges: adj[a].add(b);adj[b].add(a)
    zcoef=Counter()
    for bit in range(1<<n):
        Z={j for j in range(n) if bit&(1<<j)}
        if any(not (adj[v]&Z) for v in Z):continue
        b=sum(bool(adj[v]-Z) for v in Z)
        aa=2*(n-len(Z))+b
        from math import comb
        for k in range(aa+1): zcoef[2*n-b+k]+=comb(aa,k)
    return dict(zcoef)

def test():
    tested=0
    for n in range(1,5):
        poss=list(combinations(range(n),2))
        for mask in range(1<<len(poss)):
            e=[p for i,p in enumerate(poss) if (mask>>i)&1]
            d=direct(n,e)
            f=formula(n,e)
            assert d==f,(n,e,d,f)
            tested+=1
    # Five-vertex path and several natural graphs.
    n=5
    families=[[(i,i+1) for i in range(n-1)],list(combinations(range(n),2)),[(0,i) for i in range(1,n)],[(i,(i+1)%n) for i in range(n)],[(0,1),(2,3)]]
    for e in families:
        d=direct(n,e); f=formula(n,e)
        assert d==f,(n,e,d,f)
        tested+=1
    print('verified graphs:',tested)
    for n,e in [(3,list(combinations(range(3),2))), (4,list(combinations(range(4),2))), (5,[(0,i) for i in range(1,5)]), (5,[(i,i+1) for i in range(4)])]:
        p=formula(n,e);minimum=min(p)
        print('n,edges,minimum,count:',n,len(e),minimum,p[minimum])
if __name__=='__main__': test()

def boundary_stats(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    best=-1; count=0
    for mask in range(1<<n):
        Z={v for v in range(n) if mask & (1<<v)}
        if any(not (adj[v] & Z) for v in Z):continue
        b=sum(bool(adj[v]-Z) for v in Z)
        if b>best:best,count=b,1
        elif b==best:count+=1
    return best,count

def run_special_tests():
    for n in range(1,19):
        e=[(v,v+1) for v in range(n-1)]
        b,c=boundary_stats(n,e)
        k=n//3
        if n%3==0: pred=2
        elif n%3==1: pred=1
        else:pred=2*(k+1)
        assert (b,c)==((2*n-2)//3,pred),(n,'path',b,c,pred)
    for n in range(3,19):
        e=[(v,(v+1)%n) for v in range(n)]
        b,c=boundary_stats(n,e)
        k,d=divmod(n,3)
        pred=[3,2*n,n*(2*k+1)][d]
        assert (b,c)==(2*k,pred),(n,'cycle',b,c,pred)
    print('path boundary formula confirmed n=1..18; cycle formula n=3..18')
    for n in range(3,6):
        e=[(v,(v+1)%n) for v in range(n)]
        m=direct(n,e);lo=min(m)
        k,d=divmod(n,3)
        assert (lo,m[lo])==(2*n-2*k,[3,2*n,n*(2*k+1)][d])
        print('direct cycle corona',n,lo,m[lo])

if __name__=='__main__': run_special_tests()
