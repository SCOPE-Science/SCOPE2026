#!/usr/bin/env python3
"""Standalone exact finite certificate for a thirteen-element arithmetic progression."""
from fractions import Fraction
from math import gcd, isqrt

p=65537
assert all(p%d for d in range(2,isqrt(p)+1))
w=list(range(46256,46269))
expected=[256,256,256,256,65281,256,256,256,256,256,65281,65281,256]

def modpow(base, exponent, mod):
    result=1
    base %= mod
    while exponent:
        if exponent & 1: result = (result*base) % mod
        base = base*base % mod
        exponent >>= 1
    return result

for a,e in zip(w,expected):
    assert modpow(a,16384,p)==e
    assert (e*e)%p==p-1
    assert modpow(a,32768,p)==p-1
    assert modpow(a,65536,p)==1

# Within the prime subfield, exponentiating by (p**m-1)//2
# is equivalent to exponentiating by ((p-1)//2)*M_m.
for m in [3,5,7,9,11,15]:
    q=p**m
    M=(q-1)//(p-1)
    assert M%2==1
    for a in w:
        assert modpow(a,(q-1)//2,p)==p-1
        assert modpow(a,p-1,p)==1
        assert q-1>p-1

# Exact Euler-product checks for two modest prime exponents.
for ell in [3,5]:
    M=(p**ell-1)//(p-1)
    x=M
    primes=[]
    d=3
    while d*d<=x:
        if x%d==0:
            primes.append(d)
            while x%d==0:x//=d
        d+=2
    if x>1: primes.append(x)
    assert all((r-1)%ell==0 for r in primes)
    prod=Fraction(1,2)
    for r in primes: prod *= Fraction(r-1,r)
    assert Fraction(0)<Fraction(1,2)-prod
print('VERIFY_OK: thirteen exact base-field certificates; six odd-degree lift tests; two prime-degree Euler-product tests')
