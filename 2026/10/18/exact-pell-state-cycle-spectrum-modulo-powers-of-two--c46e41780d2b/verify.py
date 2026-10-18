#!/usr/bin/env python3
"""Exact finite checks of a modular Pell state-orbit theorem.

The infinite proof uses elementary Smith invariant factors; this program
checks the critical starting identities, recurrence, and finite orbit counts.
"""
from collections import Counter
from math import gcd

def mul(x,y):
    a,b,c,d=x; e,f,g,h=y
    return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)

def smith_valuations_at_two(m):
    a,b,c,d=m
    g=gcd(gcd(abs(a),abs(b)),gcd(abs(c),abs(d)))
    det=a*d-b*c
    assert g and det
    def v2(n):
        k=0
        while n%2 == 0:
            k+=1;n//=2
        return k
    return (v2(g),v2(det//g))

A=(0,1,1,2)
I=(1,0,0,1)
assert smith_valuations_at_two(tuple(A[i]-I[i] for i in range(4))) == (0,1)
A2=mul(A,A)
assert A2 == (1,2,2,5)
assert smith_valuations_at_two(tuple(A2[i]-I[i] for i in range(4))) == (1,1)
A4=mul(A2,A2)
assert A4==(5,12,12,29)
C=tuple((A4[i]-I[i])//4 for i in range(4))
assert C==(1,3,3,7)
assert smith_valuations_at_two(C)==(0,1)
B=A4
for j in range(2,15):
    assert all((B[i]-I[i])%(1<<j)==0 for i in range(4))
    Cj=tuple((B[i]-I[i])//(1<<j) for i in range(4))
    assert smith_valuations_at_two(Cj)==(0,1)
    B=mul(B,B)

def expected(k):
    if k==1:return {1:2,2:1}
    if k==2:return {1:2,2:1,4:3}
    d={1:2,2:1,4:7,1<<k:1<<(k-1)}
    for j in range(3,k): d[1<<j]=3*(1<<(j-1))
    return d

def orbit_census(k):
    m=1<<k; seen=bytearray(m*m); cycles=Counter()
    for a in range(m):
        for b in range(m):
            x=a*m+b
            if seen[x]: continue
            length=0
            u,v=a,b
            while not seen[u*m+v]:
                seen[u*m+v]=1
                u,v=v,(u+2*v)%m
                length+=1
            assert (u,v)==(a,b)
            cycles[length]+=1
    assert all(seen)
    return dict(cycles)

for k in range(1,10):
    measured=orbit_census(k)
    predicted=expected(k)
    assert measured==predicted,(k,measured,predicted)
    assert sum(length*count for length,count in measured.items())==(1<<k)**2
    assert sum(measured.values())==(3 if k==1 else 2**(k+1)-2)
    print('k',k,'cycles',sum(measured.values()),'lengths',dict(sorted(measured.items())))
print('VERIFY_OK')
