#!/usr/bin/env python3
"""Arithmetic regression checks for the spiral-knot Alexander parameter sieve."""
from math import gcd, isqrt

def candidates(D,m):
    out=[]
    if D < 0 or m < 1:
        return out
    for q in range(2,m+1):
        if m % q:
            continue
        if D % (q-1):
            continue
        p=1+D//(q-1)
        if p>=2 and gcd(p,q)==1:
            out.append((p,q,m//q))
    return out

def isprime(n):
    if n<2: return False
    for d in range(2,isqrt(n)+1):
        if n%d==0: return False
    return True

# Any synthetic spiral data satisfying the two source formulas survives the sieve.
checked=0
for p in range(2,60):
    for q in range(2,60):
        if gcd(p,q)!=1:
            continue
        D=(p-1)*(q-1)
        for gamma in range(1,max(2,p-1)):
            m=q*gamma
            assert (p,q,gamma) in candidates(D,m)
            if isprime(m):
                # Since q>=2 and gamma>=1, primality forces gamma=1 and q=m.
                assert gamma==1 and q==m
                assert candidates(D,m)==[(p,q,1)]
            checked+=1

# Source example 6_2 = S(5,2,(1,1,1,-1)): D=4 and |a1|-1=2.
assert candidates(4,2)==[(5,2,1)]
# Source's 8_21 polynomial has D=4 and |a1|-1=3; the forced p=q=3 is not coprime.
assert candidates(4,3)==[]

print(f"VERIFY_OK synthetic_cases={checked} source_6_2=[(5,2,1)] source_8_21=[] prime_gap_unique=true")
