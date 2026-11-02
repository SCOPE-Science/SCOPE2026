#!/usr/bin/env python3
"""Independent finite-field and bit-matrix checks of two-bond honeycomb graph-state theorem."""
from collections import Counter
from itertools import combinations
import random

def gf2_rank(vectors):
    pivots = {}
    for vec in vectors:
        v = vec
        while v:
            j = v.bit_length() - 1
            if j not in pivots:
                pivots[j] = v
                break
            v ^= pivots[j]
    return len(pivots)

def edges(L):
    for i in range(L):
        for j in range(L):
            a = i*L+j
            for ii,jj in ((i,j),((i-1)%L,j),(i,(j-1)%L)):
                yield a, ii*L+jj

def matrix(L):
    rows = [0] * (L*L)
    for a,b in edges(L):
        rows[a] ^= 1 << b
    return rows

def parity(n):
    return n.bit_count() & 1

def roll(word, offset, L):
    mask = (1 << L) - 1
    offset %= L
    return ((word << offset) | (word >> (L-offset))) & mask if offset else word

def image_character(L, i, j):
    # The image in the quotient by 1+x+y has row (1+x)^j x^i
    # reduced modulo (x^L-1)/(x+1) = 1+...+x^(L-1).
    word = 0
    for k in range(j+1):
        if (k & j) == k:  # Lucas theorem for binomial parity
            word ^= 1 << ((i+k) % L)
    if (word >> (L-1)) & 1:
        word ^= (1 << L) - 1
    return word & ((1 << (L-1)) - 1)

def assert_site_characters(L):
    seen = {}
    for i in range(L):
        for j in range(L):
            word = image_character(L,i,j)
            assert word != 0, (L,i,j)
            if L>=7:
                assert word not in seen, (L,(i,j),seen.get(word))
            seen.setdefault(word, (i,j))
    return len(seen)

def check_double_pairs(L, exhaustive=False, samples=0):
    B = matrix(L)
    rk = gf2_rank(B)
    assert rk == L*L-L+1, (L,rk)
    ee=list(edges(L))
    valid = [(a,b,c,d) for (a,b),(c,d) in combinations(ee,2) if a!=c and b!=d] if exhaustive else []
    if not exhaustive:
        rng=random.Random(734629+L)
        while len(valid)<samples:
            a,b=rng.choice(ee)
            c,d=rng.choice(ee)
            if a!=c and b!=d:
                valid.append((a,b,c,d))
    dist=Counter()
    for a,b,c,d in valid:
        Q=B.copy()
        Q[a]^=1<<b
        Q[c]^=1<<d
        gain=gf2_rank(Q)-rk
        dist[gain]+=1
        if L>=7:
            assert gain==2, (L,(a,b),(c,d),gain)
    return rk,len(valid),dict(sorted(dist.items()))

def main():
    print('Binary quotient character distinctness (indices modulo L):')
    for k in range(2,7):
        L=2**k-1
        count=assert_site_characters(L)
        print(f'  L={L}: {count} distinct nonzero classes among {L*L} sites')
    print('Two omitted edges, distinct endpoints, exact binary ranks:')
    for L,samples in ((3,0),(7,0),(15,200),(31,30)):
        rk,checks,dist=check_double_pairs(L,exhaustive=L in (3,7),samples=samples)
        print(f'  L={L}: base rank {rk}, tested {checks} pairs, gains {dist}')
    for L in (3,7,15,31):
        B=matrix(L)
        rk=gf2_rank(B)
        ee=list(edges(L))
        rng=random.Random(L*107)
        for a,b in rng.sample(ee,min(40,len(ee))):
            Q=B.copy();Q[a]^=1<<b
            if L>=7: assert gf2_rank(Q)==rk+1
        print(f'  L={L}: single-edge deletion checks passed ({min(40,len(ee))})')
    print('ALL CHECKS PASSED; finite verification only, general result follows from written proof.')

if __name__=='__main__':
    main()
