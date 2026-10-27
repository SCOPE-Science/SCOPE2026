#!/usr/bin/env python3
"""Exact finite certificates accompanying a 2-adic Delannoy valuation theorem."""
from math import comb, factorial
from fractions import Fraction

def nu2(x):
    assert x != 0
    x = abs(x)
    return (x & -x).bit_length()-1

def mod128(f):
    p,q=f.numerator,f.denominator
    a=nu2(q)
    assert p%(2**a)==0
    return (p//(2**a)*pow(q//(2**a),-1,128))%128

# Coefficients of sum_{k=1}^8 2^k binom(4w,k)^2, exactly rational.
poly=[Fraction(1)]
s=[Fraction(0) for _ in range(17)]
for k in range(1,9):
    nxt=[Fraction(0) for _ in range(len(poly)+1)]
    for i,a in enumerate(poly):
        nxt[i]+=(1-k)*a
        nxt[i+1]+=a
    poly=nxt
    for i,a in enumerate(poly):
        for j,b in enumerate(poly):
            s[i+j]+=a*b*Fraction(2**k*4**(i+j),factorial(k)**2)
assert [(j,mod128(x)) for j,x in enumerate(s) if mod128(x)] == [(3,64)]
# Uniform Gauss-valuation tail bound B(k)>=7 for 9<=k<=31.
for k in range(9,32):
    B=k+4-2*nu2(k)-2*sum((k-1)//(2**h) for h in range(3,16))
    assert B>=7,(k,B)
# For k>=32, B(k) >= k/2+4.5-2*log2(k) > 7, monotonic.
# This is an analytical inequality, not a truncated enumeration.
for n in range(1,513):
    d=sum(2**k*comb(n,k)**2 for k in range(n+1))
    z=d-(-1)**n
    expected=3*nu2(n) if n%4==0 else (3*nu2(n+1) if n%4==3 else 2)
    assert nu2(z)==expected,(n,nu2(z),expected)
print('VERIFY_OK: polynomial modulo 128, finite tail bases, and 512 Delannoy valuations')
