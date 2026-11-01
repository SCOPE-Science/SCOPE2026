#!/usr/bin/env python3
"""Finite exact-rational diagnostics for collinear translate and missing-middle formulae."""
from fractions import Fraction as F
from itertools import combinations
import random

Q = lambda x: F(x)

def merge(intervals):
    z=[]
    for a,b in sorted((Q(a),Q(b)) for a,b in intervals if a<b):
        if z and a<=z[-1][1]: z[-1]=(z[-1][0],max(z[-1][1],b))
        else: z.append((a,b))
    return z

def length(intervals): return sum((b-a for a,b in merge(intervals)), F(0))
def shift(S,h): return [(a+h,b+h) for a,b in S]
def meet(S,T): return merge([(max(a,c),min(b,d)) for a,b in S for c,d in T if max(a,c)<min(b,d)])
def un(S,T): return merge(S+T)

def hole_energy(S):
    S=merge(S); m=length(S);left=F(0);res=F(0)
    for i,(a,b) in enumerate(S[:-1]):
        left+=b-a
        res+=(S[i+1][0]-b)*left*(m-left)
    return res

def discrete_hole_triplets(bits):
    n=len(bits)
    return sum(bits[i]*(1-bits[j])*bits[k] for i in range(n) for j in range(i+1,n) for k in range(j+1,n))

def discrete_energy(bits):
    return sum((sum(bits[:j])*sum(bits[j+1:]) for j in range(len(bits)) if not bits[j]),0)

checks=0
rng=random.Random(1773)
for N in range(4,26):
    for trial in range(14):
        bits=[rng.randrange(2) for _ in range(N)]
        assert discrete_hole_triplets(bits)==discrete_energy(bits)
        checks+=1
        S=merge([(F(i),F(i+1)) for i,b in enumerate(bits) if b])
        energy=hole_energy(S)
        left=0;independent=F(0);m=sum(bits)
        for i,b in enumerate(bits):
            if not b: independent+=left*(m-left)
            else: left+=1
        assert energy==independent
        checks+=1
        for a in [1,2,3]:
            for b in [1,2,3]:
                x=meet(S,shift(S,F(a+b)))
                tr=meet(x,shift(S,F(a)))
                defect=length(x)-length(tr)
                u=merge(S+shift(S,F(a))+shift(S,F(a+b)))
                covariance=lambda h:length(meet(S,shift(S,F(h))))
                assert defect>=0
                assert defect==3*length(S)-covariance(a)-covariance(b)-length(u)
                checks+=2
for L in [F(1,3),F(1),F(3),F(17,4)]:
    S=[(F(0),L)]
    for ds in [(F(1,4),F(1,3)),(F(2),F(1,8)),(F(0),F(11))]:
        t=[F(0),ds[0],sum(ds)]
        union=length(merge([seg for h in t for seg in shift(S,h)]))
        predicted=L+sum((min(L,ds[i]) for i in range(2)), F(0))
        assert union==predicted
        checks+=1
for alpha in [F(1,10),F(1,4),F(1,3),F(2,5)]:
    for m in [F(1),F(5,2),F(8)]:
        for h in [F(1,5),F(5,4),F(10)]:
            S=[(F(0),alpha*m),(alpha*m+h,m+h)]
            assert length(S)==m
            assert hole_energy(S)==alpha*(1-alpha)*m*m*h
            checks+=2
print(f'PASS: {checks} exact-rational/discrete diagnostic assertions.')
