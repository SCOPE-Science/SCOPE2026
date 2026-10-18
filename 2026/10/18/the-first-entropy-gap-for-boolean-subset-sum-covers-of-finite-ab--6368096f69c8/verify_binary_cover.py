#!/usr/bin/env python3
"""Exact finite classification of five Boolean-summands in (Z/5Z)^2.

Only integer arithmetic is used. Run: python3 verify_binary_cover.py
"""
from collections import Counter
from itertools import combinations, product
from math import prod

P = 5
V = tuple((a,b) for a in range(P) for b in range(P))
O = (0,0)
E1,E2 = (1,0),(0,1)

def add(v,w):
    return ((v[0]+w[0])%P,(v[1]+w[1])%P)

def boolean_sums(vectors):
    s={O}
    for v in vectors:
        s |= {add(v,w) for w in s}
    return s

def full_set_census():
    distribution=Counter()
    maximal=set()
    for vectors in combinations(V,5):
        size=len(boolean_sums(vectors))
        distribution[size]+=1
        if size==24:
            maximal.add(vectors)
    assert sum(distribution.values())==53130
    assert max(distribution)==24
    assert len(maximal)==1920
    return distribution,maximal

def normalized_multiset_census():
    # Any spanning five-term multiset may be reordered so the first
    # two entries form a basis, then carried to E1,E2 by an invertible
    # linear transformation. The other entries can repeat or be zero.
    distribution=Counter()
    maxima=0
    repeats=0
    for triple in product(V,repeat=3):
        vectors=(E1,E2)+triple
        size=len(boolean_sums(vectors))
        distribution[size]+=1
        if size==24:
            maxima+=1
            repeats+=(len(set(vectors))<5)
    assert sum(distribution.values())==25**3==15625
    assert max(distribution)==24
    assert maxima==480
    assert repeats==0
    return distribution

def gl_2():
    matrices=[]
    for a,b,c,d in product(range(P),repeat=4):
        if (a*d-b*c)%P:
            matrices.append((a,b,c,d))
    assert len(matrices)==480
    return matrices

def apply(M,v):
    a,b,c,d=M
    x,y=v
    return ((a*x+b*y)%P,(c*x+d*y)%P)

def classify_orbits(maxima):
    pending=set(maxima)
    result=[]
    matrices=gl_2()
    while pending:
        seed=min(pending)
        orbit={tuple(sorted(apply(M,v) for v in seed)) for M in matrices}
        assert orbit <= maxima
        assert len(orbit)==len(orbit & pending)
        result.append((min(orbit),len(orbit)))
        pending-=orbit
    result.sort()
    assert sorted(sz for _,sz in result)==[120,120,240,480,480,480]
    assert len(result)==6
    assert sum(sz for _,sz in result)==len(maxima)==1920
    return result

def prime_factors(n):
    fs=[]
    p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:
                n//=p;e+=1
            fs.append((p,e))
        p+=1
    if n>1:fs.append((n,1))
    return fs

def partitions(n,minimum=1):
    if n==0:
        yield ()
    else:
        for i in range(minimum,n+1):
            for tail in partitions(n-i,i):
                yield (i,)+tail

def all_elementary_divisors(n):
    # Fundamental theorem of finite abelian groups, by prime powers.
    blocks=[]
    for p,e in prime_factors(n):
        blocks.append(tuple((p,part) for part in partitions(e)))
    for choices in product(*blocks):
        r=max(len(part) for _,part in choices)
        ds=[1]*r
        for p,part in choices:
            for j,e in enumerate(reversed(part)):
                ds[-j-1] *= p**e
        ds=tuple(ds)
        assert prod(ds)==n
        assert all(ds[j+1]%ds[j]==0 for j in range(len(ds)-1))
        yield ds

def first_entropy_gap():
    tested=0
    exceptional=[]
    for n in range(2,26):
        entropy=(n-1).bit_length()
        for ds in all_elementary_divisors(n):
            tested+=1
            digits=sum((d-1).bit_length() for d in ds)
            if digits>entropy:
                exceptional.append((n,ds,entropy,digits))
    assert exceptional==[(25,(5,5),5,6)]
    return tested,exceptional

def main():
    distribution,maxima=full_set_census()
    normalized=normalized_multiset_census()
    orbits=classify_orbits(maxima)
    witness=(E1,E1,(2,0),E2,E2,(0,2))
    assert boolean_sums(witness)==set(V)
    groups,exceptions=first_entropy_gap()
    print('VERIFY_OK')
    print('five_distinct_sets',sum(distribution.values()))
    print('maximum_boolean_sumset',max(distribution))
    print('maximum_sets',len(maxima))
    print('normalized_five_multisets',sum(normalized.values()))
    print('normalized_maxima',normalized[24])
    print('orbit_sizes',sorted(n for _,n in orbits))
    print('number_of_orbits',len(orbits))
    print('group_types_through_25',groups,'exception',exceptions)
    print('orbit_representatives')
    for rep,size in orbits:
        print(size,rep)
    print('five_set_sumset_histogram',sorted(distribution.items()))

if __name__=='__main__':
    main()
