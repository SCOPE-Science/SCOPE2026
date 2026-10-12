#!/usr/bin/env python3
"""Exact independent checks for three-species rarefaction crossing theorem."""
from itertools import combinations
from math import comb
from fractions import Fraction
from random import Random

def triplets(N):
    return [(a,b,N-a-b) for a in range(N-2,0,-1) for b in range(min(a,N-a-1),0,-1) if 1<=N-a-b<=b]

def absent_count(prof,N,m):
    return sum(comb(N-x,m) if N-x>=m else 0 for x in prof)

def sign(x):
    return (x>0)-(x<0)

def sign_changes(s):
    s=[v for v in s if v]
    return sum(v!=w for v,w in zip(s,s[1:]))

def integrated_frequency(a,b,N):
    d=[0]*(N+1)
    for v in a:d[v]+=1
    for v in b:d[v]-=1
    f=0;g=0;G=[]
    for j in range(1,N-1):
        f+=d[j];g+=f;G.append(g)
    assert sum(d)==sum(j*d[j] for j in range(1,N+1))==0
    return G

def rhs(a,b,N,m):
    G=integrated_frequency(a,b,N)
    return sum(G[j-1]*(comb(N-j-2,m-2) if N-j-2>=m-2 else 0) for j in range(1,N-1))

max_changes=0
crossing_examples={}
counts={}
for N in range(3,36):
    ps=triplets(N)
    # Independent exhaustive composition generator verifies the partition domain.
    direct=sorted({tuple(sorted((a,b,N-a-b),reverse=True)) for a in range(1,N-1) for b in range(1,N-a)})
    assert sorted(ps)==direct, (N,len(ps),len(direct))
    z=[tuple(absent_count(a,N,m) for m in range(2,N)) for a in ps]
    cross=0
    for i,j in combinations(range(len(ps)),2):
        diff=[u-v for u,v in zip(z[i],z[j])]
        nc=sign_changes([sign(t) for t in diff])
        assert nc<=1, (N,ps[i],ps[j],diff)
        if nc: cross+=1;crossing_examples.setdefault(N,(ps[i],ps[j]))
        max_changes=max(nc,max_changes)
    counts[N]=cross

# Independently check double-summation identity and the single sign transition
# of its integrated signed abundance frequencies for all profiles through 26.
identity_tests=0
for N in range(3,27):
    ps=triplets(N)
    for a,b in combinations(ps,2):
        G=integrated_frequency(a,b,N)
        assert sign_changes([sign(x) for x in G])<=1
        for m in range(2,N):
            d=absent_count(a,N,m)-absent_count(b,N,m)
            assert d==rhs(a,b,N,m), (N,a,b,m,d,rhs(a,b,N,m))
            identity_tests+=1

# All 2x2 minors have the required sign, including zeros and endpoints.
minor_tests=0
for N in range(4,28):
    for j1 in range(1,N-2):
        for j2 in range(j1+1,N-1):
            for m1 in range(2,N-1):
                for m2 in range(m1+1,N):
                    a=comb(N-j1-2,m1-2) if N-j1-2>=m1-2 else 0
                    b=comb(N-j1-2,m2-2) if N-j1-2>=m2-2 else 0
                    c=comb(N-j2-2,m1-2) if N-j2-2>=m1-2 else 0
                    d=comb(N-j2-2,m2-2) if N-j2-2>=m2-2 else 0
                    assert b*c>=a*d,(N,j1,j2,m1,m2,a,b,c,d)
                    minor_tests+=1

A=(6,2,2);B=(5,4,1)
assert counts[10]==1 and crossing_examples[10]==(A,B),crossing_examples.get(10)
assert all(counts[n]==0 for n in range(3,10))
assert [(Fraction(3,1)-Fraction(absent_count(A,10,m),comb(10,m)),Fraction(3,1)-Fraction(absent_count(B,10,m),comb(10,m))) for m in (2,3,4)]==[
    (Fraction(73,45),Fraction(74,45)),
    (Fraction(61,30),Fraction(41,20)),
    (Fraction(163,70),Fraction(242,105)),
]
print('VERIFY_OK')
print('max_reversal_changes',max_changes)
print('triplet_census_upto',35)
print('identity_tests',identity_tests)
print('minor_tests',minor_tests)
print('first_crossing',10,A,B)
print('crossings_at_10_to_20',{n:counts[n] for n in range(10,21)})
