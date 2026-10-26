#!/usr/bin/env python3
"""Reproduce finite probability identities for nested weak/strict majority on rooted trees."""
from fractions import Fraction
from itertools import product
from math import comb, erf, sqrt, pi, lgamma, log, exp


def tail(n, p, strict=False):
    low = n // 2 + (1 if strict else n % 2)
    return sum((comb(n, k) * p**k * (1-p)**(n-k)
                for k in range(low, n+1)), Fraction())


def iterated(n, d, strict=False):
    p = Fraction(1, 2)
    for _ in range(d):
        p = tail(n, p, strict)
    return p


def direct(bits, n, d, strict=False):
    vals = list(bits)
    for _ in range(d):
        assert len(vals) % n == 0
        vals = [(sum(vals[k:k+n]) * 2 > n if strict else
                 sum(vals[k:k+n]) * 2 >= n)
                for k in range(0, len(vals), n)]
    assert len(vals) == 1
    return bool(vals[0])


def floating_tail(n, p, strict=False):
    if p == 0.0: return 0.0
    if p == 1.0: return 1.0
    lo = n // 2 + (1 if strict else n % 2)
    terms = [(lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)
              +k*log(p)+(n-k)*log(1-p))
             for k in range(lo,n+1)]
    tmax = max(terms)
    return min(1.0, exp(tmax)*sum(exp(t-tmax) for t in terms))


def main():
    seen = 0
    for n, d in ((2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2)):
        for strict in (False,True):
            success=sum(direct(bits,n,d,strict) for bits in product((False,True),repeat=n**d))
            assert Fraction(success,2**(n**d))==iterated(n,d,strict)
            seen+=2**(n**d)
    assert seen==2*(2**2+2**4+2**8+2**3+2**9+2**4+2**16)
    for n in range(1,21):
        for d in range(1,4):
            w=iterated(n,d)
            s=iterated(n,d,strict=True)
            assert w+s==1
            if n%2: assert w==Fraction(1,2)
            else:
                assert w>Fraction(1,2)
                assert (d!=1 or w-Fraction(1,2)==Fraction(comb(n,n//2),2**(n+1)))
    target=(1+erf(1/sqrt(pi)))/2
    assert abs(target - 0.7875312581583189)<1e-14
    last_error = 2
    for n in (40,80,160,320,640,1280):
        p=0.5
        p=floating_tail(n,p)
        p=floating_tail(n,p)
        error=abs(p-target)
        assert error<last_error
        last_error=error
    print('DIRECT_ENUMERATIONS_OK',seen,'leaf-label assignments')
    print('RATIONAL_RECURRENCES_OK (n=1..20; depth=1..3; weak/strict)')
    print('GAUSSIAN_LIMIT_NUMERIC',format(target,'.15f'))
    print('FINITE_SIZE_CONVERGENCE_OK (n=40,80,160,320,640,1280)')
    print('ALL_CHECKS_OK')

if __name__=='__main__': main()
