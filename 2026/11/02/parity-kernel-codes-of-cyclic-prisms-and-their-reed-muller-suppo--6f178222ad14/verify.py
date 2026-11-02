#!/usr/bin/env python3
"""Independent tests for the closed-neighborhood parity code of a cyclic prism.
Usage: python verify.py. Only Python 3 standard library is required.
"""
from collections import Counter
from math import gcd
from itertools import combinations


def closed_rows(n):
    # vertices 0..n-1 are upper rim; n..2n-1 lower rim
    assert n>=3
    N=2*n
    rows=[]
    for v in range(N):
        i=v%n
        layer=v//n
        ids=(v,layer*n+(i-1)%n,layer*n+(i+1)%n,(1-layer)*n+i)
        assert len(set(ids))==4
        rows.append(sum(1<<j for j in ids))
    return rows


def nullspace_basis(rows, N):
    a=list(rows); pivots=[]; r=0
    for col in range(N):
        i=next((i for i in range(r,N) if (a[i]>>col)&1),None)
        if i is None: continue
        a[r],a[i]=a[i],a[r]
        for j in range(N):
            if j!=r and ((a[j]>>col)&1): a[j]^=a[r]
        pivots.append(col)
        r+=1
    free=[col for col in range(N) if col not in pivots]
    basis=[]
    for f in free:
        mask=1<<f
        for i,p in enumerate(pivots):
            if (a[i]>>f)&1:mask|=1<<p
        assert all((row & mask).bit_count()%2==0 for row in rows)
        basis.append(mask)
    return basis


def predicted_pattern(n,first):
    g=gcd(n,4)
    a=[(first>>(i%g))&1 for i in range(n)]
    b=[a[i]^a[(i-1)%n]^a[(i+1)%n] for i in range(n)]
    bits=sum((x<<i) for i,x in enumerate(a))+sum((x<<(n+i)) for i,x in enumerate(b))
    return bits


def verify():
    # Algorithm A: independent row reduction of the full 2n x 2n matrix.
    for n in range(3,65):
        rows=closed_rows(n);basis=nullspace_basis(rows,2*n)
        g=gcd(n,4)
        assert len(basis)==g,(n,'dimension',len(basis),g)
        masks=set()
        for a in range(1<<g):
            t=predicted_pattern(n,a)
            assert all((r&t).bit_count()%2==0 for r in rows)
            masks.add(t)
        assert len(masks)==(1<<g)
        histogram=Counter(x.bit_count() for x in masks)
        expect=Counter({0:1,2*n:1})
        if (1<<g)-2:expect[n]=(1<<g)-2
        assert histogram==expect,(n,histogram,expect)
    # Algorithm C: independently enumerate all linear subspaces of the kernel
    # and derive every generalized Hamming weight (minimal joint support).
    for n in range(3,25):
        g=gcd(n,4)
        words=[predicted_pattern(n,a) for a in range(1<<g)]
        by_dim={}
        for k in range(1,g+1):
            supports=[]
            seen=set()
            for gens in combinations(range(1,1<<g),k):
                span={0}
                for q in gens:span|={a^q for a in tuple(span)}
                if len(span)!=(1<<k):continue
                key=frozenset(span)
                if key in seen:continue
                seen.add(key)
                sup=0
                for a in span:sup|=words[a]
                supports.append(sup.bit_count())
            by_dim[k]=min(supports)
        target=({1:(2*n,) ,2:(n,2*n),4:(n,3*n//2,7*n//4,2*n)})[g]
        assert tuple(by_dim.values())==target,(n,by_dim,target)
    # Algorithm B: brute force independently evaluates each closed-neighborhood
    # constraint for every subset for all cycles with up to 18 vertices.
    for n in range(3,10):
        rows=closed_rows(n)
        hist=Counter()
        for subset in range(1<<(2*n)):
            if all((subset & r).bit_count()%2==0 for r in rows):
                hist[subset.bit_count()]+=1
        expect=Counter({0:1,2*n:1})
        if (1<<gcd(n,4))-2:expect[n]=(1<<gcd(n,4))-2
        assert hist==expect,(n,hist,expect)
    # Code equivalence: eight cyclic-prism length-4 columns are all 4-bit odd vectors.
    columns=[]
    for v in range(8):
        c=0
        for j in range(4):
            if (predicted_pattern(4,1<<j)>>v)&1:c|=1<<j
        columns.append(c)
    assert set(columns)=={m for m in range(16) if m.bit_count()%2==1}
    print('VERIFY_OK: exact 2n x 2n rank and kernel classification for 3<=n<=64;')
    print('brute-force all vertex subsets for 3<=n<=9;')
    print('all 8 Reed-Muller evaluation columns verified for n=4; generalized weights for 3<=n<=24.')

if __name__=='__main__':verify()
