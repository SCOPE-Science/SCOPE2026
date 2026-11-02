#!/usr/bin/env python3
"""Verify distance-shell identities for hypercube shortest paths.
Only finite checks: the proof of the infinite theorem is in RESULT.md.
"""
import math,itertools,collections,random

def formula(d,k):
    a=[0]*(d+1)
    for j in range(d-k+1):
        for r in range(k//2+1):
            c=math.comb(k,r)-(math.comb(k,r-1) if r else 0)
            a[j+r]+=math.comb(d-k,j)*(k-2*r+1)*c
    return a

def distances(d, path):
    counts=[0]*(d+1)
    for x in range(1<<d):
        v=min((x^p).bit_count() for p in path)
        counts[v]+=1
    return counts

def norm(d,k):
    p=[0]
    for i in range(k):p.append(p[-1]^(1<<i))
    return p

for d in range(1,13):
    for k in range(d+1):
        got=distances(d,norm(d,k));want=formula(d,k)
        assert got==want,(d,k,got,want)
        assert max(i for i,x in enumerate(got) if x)==d-(k+1)//2
        assert sum(got)==1<<d
print('CANONICAL_SHELLS_OK d=1..12 every k')
for d in range(1,7):
    for k in range(1,d+1):
        for start in range(1<<d):
            for coords in itertools.permutations(range(d),k):
                p=[start]
                for c in coords:p.append(p[-1]^(1<<c))
                assert distances(d,p)==formula(d,k)
print('ALL_ROOTED_GEODESICS_OK d=1..6')
# Combinatorial count of all undirected shortest paths of each length.
for d in range(1,11):
    counts={k:(1<< (d-1))*math.comb(d,k)*math.factorial(k) for k in range(1,d+1)}
    minimum=d//2
    best=sum(v for k,v in counts.items() if d-(k+1)//2==minimum)
    expect=(1<<(d-1))*math.factorial(d) if d%2 else (1<<d)*math.factorial(d)
    assert best==expect,(d,best,expect)
print('OPTIMAL_PATH_COUNTS_OK d=1..10')
