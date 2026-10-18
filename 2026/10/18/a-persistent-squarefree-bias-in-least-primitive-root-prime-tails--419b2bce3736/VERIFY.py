#!/usr/bin/env python3
"""Reproduce the finite arithmetic checks for the squarefree primitive-root tail theorem."""
from decimal import Decimal, getcontext
from fractions import Fraction
from math import gcd, isqrt


def primes_to(n):
    prime = bytearray(b'\x01') * (n + 1)
    prime[:2] = b'\x00\x00'
    for j in range(2, isqrt(n) + 1):
        if prime[j]:
            prime[j*j:n+1:j] = b'\x00' * ((n-j*j)//j+1)
    return [j for j in range(2, n + 1) if prime[j]]


def totient_sieve(n):
    phi = list(range(n+1))
    for p in primes_to(n):
        for k in range(p, n+1, p):
            phi[k] -= phi[k]//p
    return phi


def roots(p):
    if p == 2:
        return {1}
    divisors = [ell for ell in primes_to(p-1) if (p-1) % ell == 0]
    return {a for a in range(1, p)
            if all(pow(a, (p-1)//ell, p) != 1 for ell in divisors)}


def squarefree_flags(n):
    arr = bytearray(b'\x01') * (n+1)
    arr[0] = 0
    for p in primes_to(isqrt(n)):
        for m in range(p*p, n+1, p*p):
            arr[m] = 0
    return arr


def main():
    tested = 0
    for p in (2,3,5,7,11,13,17,19):
        root_set = roots(p)
        phi = totient_sieve(p)[p-1]
        assert len(root_set) == phi
        local_ok = sum(1 for a in range(p*p)
                       if a % (p*p) != 0 and a % p not in root_set)
        assert local_ok == p*p - 1 - p*phi
        tested += 2

    # All local constraints have exactly the product cardinality modulo 30^2.
    P = (2,3,5)
    good_sets = {p: roots(p) for p in P}
    R = sum(all(n % (p*p) and n % p not in good_sets[p] for p in P)
            for n in range(900))
    assert R == (4-1-2)*(9-1-3)*(25-1-10) == 70
    tested += 1

    # Independent whole-integer counts for several moving cutoff values.
    N = 100000
    flags = squarefree_flags(N)
    sq = sum(flags)
    roots_by_p = {p: roots(p) for p in (2,3,5,7,11,13)}
    phi = totient_sieve(100000)
    for y in (2,3,5,7,11,13):
        plist = [p for p in roots_by_p if p <= y]
        allcnt = 0
        sfcnt = 0
        for n in range(1,N+1):
            if all(n%p not in roots_by_p[p] for p in plist):
                allcnt += 1
                sfcnt += flags[n]
        expected_all = Fraction(1)
        expected_sf = Fraction(1)
        for p in plist:
            expected_all *= Fraction(p-phi[p-1], p)
            expected_sf *= Fraction(p*p-1-p*phi[p-1], p*p-1)
        assert abs(Fraction(allcnt,N)-expected_all) < Fraction(1,1000)
        assert abs(Fraction(sfcnt,sq)-expected_sf) < Fraction(1,1000)
        tested += 2

    # The infinite-product tail from primes > L is at most 2/L by telescoping.
    # Exact integer interval arithmetic: no floating-point error enters the certificate.
    L = 100000
    phi = totient_sieve(L)
    scale = 10**35
    lower = upper = scale
    for p in primes_to(L):
        f = phi[p-1]
        numer = p * (p*p - 1 - p*f)
        denom = (p*p-1) * (p-f)
        lower = lower*numer // denom
        upper = (upper*numer + denom-1) // denom
    # The omitted correction factors have product in [1-2/L,1].
    lower = lower*(L-2)//L
    assert 59166*scale < 100000*lower
    assert 100000*upper < 59168*scale
    getcontext().prec = 45
    print('OK:',tested,'local/CRT/enumeration assertions')
    print('squarefree-conditioning factor exact rational enclosure:',
          Decimal(lower)/scale, Decimal(upper)/scale)

if __name__ == '__main__':
    main()
