#!/usr/bin/env python3
"""Exact-rational sanity checks for the primitive companion-Lucas binomid classification."""
from fractions import Fraction
from math import gcd

def seq(P,Q,N):
    v=[2,P]
    for n in range(2,N+1):
        v.append(P*v[-1]-Q*v[-2])
    return v

def nomial(v,n,k):
    a=Fraction(1)
    for i in range(k):
        a*=Fraction(v[n-i],v[i+1])
    return a

checked=0
for P in range(-16,17):
    if not P: continue
    for Q in range(-22,23):
        if gcd(abs(P),abs(Q))!=1: continue
        v=seq(P,Q,12)
        if any(x==0 for x in v[1:]): continue
        expected=(abs(P),Q) in {(1,0),(1,1),(2,1)}
        witnesses=[(2,1),(4,2),(6,3)]
        observed=all(nomial(v,n,k).denominator==1 for n,k in witnesses)
        assert expected==observed, (P,Q,expected,observed)
        checked+=1
for P,Q in [(1,0),(-1,0),(1,1),(-1,1),(2,1),(-2,1)]:
    v=seq(P,Q,55)
    assert all(v[n]!=0 for n in range(1,56))
    for n in range(1,56):
        for k in range(n+1):
            assert nomial(v,n,k).denominator==1, (P,Q,n,k)
    for n in range(1,56):
        for m in range(1,n+1):
            if n%m==0:assert v[n]%v[m]==0
assert nomial(seq(2,3,6),6,3)==Fraction(-161,5)
print('VERIFY_OK')
print('coprime_nonzero_short_cases_checked=',checked)
print('all_6_admissible_sign_pairs_through_n=55_binomid=PASS')
print('all_6_admissible_sign_pairs_through_n=55_divisible=PASS')
print('excluded_Q=3_normalized_witness=-161/5=PASS')
print('finite_checks_supplement_symbolic_proof')
