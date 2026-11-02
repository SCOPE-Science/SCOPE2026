#!/usr/bin/env python3
"""Independent exhaustive small-parameter verification of packet-drawing covariance identities."""
from itertools import combinations,product
from fractions import Fraction
from math import comb, log, ceil

def formula(n,s,t,r):
    q=Fraction(n-s,n); p=Fraction(s,n)
    # Avoid 0**0 ambiguity with a convention justified by the underlying binomial law.
    a=Fraction(n,n-1)**(t-1)
    b=Fraction(n-s-1,n-s)**(t-r)
    return n*n*q**t*comb(t,r)*p**r*q**(t-r)*(a*b-1)

def exhaustive(n,s,t):
    packets=list(combinations(range(n),s)); N=len(packets)**t
    Su=0; Sm=[0]*(t+1); Sum=[0]*(t+1)
    for draw in product(packets,repeat=t):
        counts=[0]*n
        for packet in draw:
            for i in packet: counts[i]+=1
        u=counts.count(0); Su+=u
        for r in range(1,t+1):
            m=counts.count(r); Sm[r]+=m; Sum[r]+=u*m
    for r in range(1,t+1):
        got=Fraction(Sum[r],N)-Fraction(Su*Sm[r],N*N)
        expected=formula(n,s,t,r)
        assert got==expected,(n,s,t,r,got,expected)
        assert (got<0 if r==1 else got>0 if r==t else True), (n,s,t,r,got)
    return N,t

if __name__=='__main__':
    cases=draws=assertions=0
    for n in range(2,8):
        for s in range(1,n):
            for t in range(2,5):
                if comb(n,s)**t>150000:continue
                N,k=exhaustive(n,s,t)
                cases+=1;draws+=N;assertions+=k
    n,t,r=6,5,2
    v1,v2=formula(n,1,t,r),formula(n,2,t,r)
    assert v1>0 and v2<0
    # Verify arithmetic impossibility of zero covariance over a wider finite grid.
    for n in range(2,35):
        for s in range(1,n):
            for t in range(2,25):
                seenpos=False
                for r in range(1,t+1):
                    z=formula(n,s,t,r)
                    assert z!=0
                    if seenpos: assert z>0
                    if z>0:seenpos=True
                assert seenpos
    print(f'PASS: {cases} independently enumerated (n,s,t) cases; {draws} ordered packet sequences; {assertions} exact covariance identities; 6,5,2 packet reversal; broad exact-rational sign sweep.')
    print(f'Example covariances: s=1 {v1}, s=2 {v2}')
