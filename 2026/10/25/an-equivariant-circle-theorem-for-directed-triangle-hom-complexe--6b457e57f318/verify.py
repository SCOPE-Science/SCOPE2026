#!/usr/bin/env python3
"""Standalone exact finite cross-checks for cyclic-tournament directed Hom complexes."""
import itertools, collections

def cells(n):
    m=(n-1)//2
    directed=lambda i,j: 1 <= (j-i)%n <= m
    out=[]
    def bits(mask):
        while mask:
            t=mask & -mask
            yield t.bit_length()-1
            mask-=t
    def rec(i,a,b,c):
        if i==n:
            if a and b and c: out.append((a,b,c))
            return
        rec(i+1,a,b,c)
        t=1<<i
        if all(directed(i,j) for j in bits(b)) and all(directed(j,i) for j in bits(c)):
            rec(i+1,a|t,b,c)
        if all(directed(j,i) for j in bits(a)) and all(directed(i,j) for j in bits(c)):
            rec(i+1,a,b|t,c)
        if all(directed(j,i) for j in bits(b)) and all(directed(i,j) for j in bits(a)):
            rec(i+1,a,b,c|t)
    rec(0,0,0,0)
    return out

def rank(vectors):
    pivots={}
    for w in vectors:
        while w:
            p=w.bit_length()-1
            if p in pivots: w^=pivots[p]
            else:
                pivots[p]=w
                break
    return len(pivots)

def check(n):
    m=(n-1)//2
    C=cells(n)
    bydim=collections.defaultdict(dict)
    for c in C:
        d=sum(x.bit_count() for x in c)-3
        bydim[d][c]=len(bydim[d])
    ranks=[]
    for d in range(1,max(bydim)+1):
        columns=[]
        for c in bydim[d]:
            v=0
            for i,coord in enumerate(c):
                if coord.bit_count()==1: continue
                for j in range(n):
                    if coord & (1<<j):
                        f=list(c); f[i]^=1<<j
                        v^=1<<bydim[d-1][tuple(f)]
            columns.append(v)
        ranks.append(rank(columns))
    counts=[len(bydim[i]) for i in range(max(bydim)+1)]
    betti=[counts[i]-(ranks[i-1] if i else 0)-(ranks[i] if i<len(ranks) else 0) for i in range(len(counts))]
    assert betti==[1,1]+[0]*(len(betti)-2),(n,betti)
    assert sum((-1)**i*a for i,a in enumerate(counts))==0
    # Nerve criterion independently enumerated by the existence of a 3-cycle.
    dg=lambda i,j:1 <= (j-i)%n <= m
    for mask in range(1,1<<n):
        js=[i for i in range(n) if mask>>i&1]
        feasible=any(all(dg(j,b) and dg(c,j) for j in js) and dg(b,c)
                     for b in range(n) for c in range(n))
        interval=any(all(((j-i)%n)<m for j in js) for i in range(n))
        assert feasible==interval,(n,js,feasible,interval)
    print('CHECK_OK',n,'cells',counts,'mod2_betti',betti)

for n in (5,7,9,11): check(n)
print('CYCLIC_TOURNAMENT_HOM_VERIFY_OK')
