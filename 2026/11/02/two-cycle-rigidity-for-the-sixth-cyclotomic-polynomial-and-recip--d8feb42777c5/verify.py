#!/usr/bin/env python3
"""Finite exact-arithmetic checks for the cyclotomic two-cycle theorem.

The general theorem is proved by Vieta descent in RESULT.md; numerical tests
are only independent sanity checks within the printed finite ranges.
"""
from fractions import Fraction
from math import gcd


def phi6(z):
    return z*z-z+1


def primes_upto(bound):
    sieve = bytearray(b"\x01")*(bound+1)
    sieve[0:2] = b"\x00\x00"
    for j in range(2, int(bound**0.5)+1):
        if sieve[j]:
            sieve[j*j:bound+1:j] = b"\x00"*((bound-j*j)//j+1)
    return [j for j in range(2,bound+1) if sieve[j]]


def h_from_factors(n):
    m=n; h=1; p=2
    while p*p<=m:
        if m%p==0:
            a=0
            while m%p==0:
                m//=p; a+=1
            h *= (p**(2*a+1)+1)//(p+1)
        p+=1
    if m>1:
        h *= (m**3+1)//(m+1)
    return h


def main():
    bound=5000
    pair_count=0
    for a in range(2,bound+1):
        ga=phi6(a)
        for b in range(a+1,bound+1):
            pair_count += 1
            assert not (ga%b == 0 and phi6(b)%a == 0), (a,b)
    assert pair_count==(bound-1)*(bound-2)//2
    primes=primes_upto(bound)
    prime_pairs=0
    for i,p in enumerate(primes):
        for q in primes[i+1:]:
            prime_pairs+=1
            h=phi6(p)*phi6(q)
            assert h%(p*q)!=0, (p,q)
    for n in range(1,601):
        direct=sum((Fraction(1,gcd(n,i)) for i in range(1,n+1)), Fraction(0,1))
        assert direct==Fraction(h_from_factors(n),n), n
    assert h_from_factors(614341)//614341==486361
    assert h_from_factors(614341)%614341==0
    assert (2*2+1)%5==0 and (5*5+1)%2==0
    print('VERIFY_OK distinct_integer_pairs=%d prime_pairs=%d direct_gcd_sums=600 example_H_614341=486361 Phi4_countercontrast=yes' % (pair_count,prime_pairs))

if __name__=='__main__':
    main()
