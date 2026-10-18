#!/usr/bin/env python3
"""Exact finite checks for the prime-power divisor-degree classification.

No packages needed for the multiplicative-order check. With --factor,
SymPy independently factors the polynomials in a second test set.
"""
import sys


def primes_up_to(limit):
    sieve = [True] * (limit + 1)
    if limit >= 0: sieve[0] = False
    if limit >= 1: sieve[1] = False
    for a in range(2, int(limit**.5) + 1):
        if sieve[a]:
            for b in range(a * a, limit + 1, a):
                sieve[b] = False
    return [a for a in range(2, limit + 1) if sieve[a]]


def order(base, mod):
    residue, count = base % mod, 1
    while residue != 1:
        residue = residue * base % mod
        count += 1
    return count


def first_missing(r, a, p):
    n = r**a
    if p == r:
        degrees = [1] * n
    else:
        degrees = [1]
        for j in range(1, a + 1):
            d = order(p, r**j)
            count = (r**j - r**(j - 1)) // d
            degrees.extend([d] * count)
    assert sum(degrees) == n
    reachable = 1
    for d in degrees:
        reachable |= reachable << d
    for m in range(n + 1):
        if not (reachable >> m) & 1:
            return m
    return None


def predicted(r, a, p):
    if r == 2 or p == r or p % r == 1:
        return None
    if p % r != r - 1:
        return 2
    return None if a == 1 or p % (r * r) == r * r - 1 else r + 1


def verify_orders():
    count = 0
    for r in primes_up_to(19):
        for a in range(1, 8):
            if r**a > 625:
                break
            for p in primes_up_to(199):
                got = first_missing(r, a, p)
                expected = predicted(r, a, p)
                assert got == expected, (r, a, p, got, expected)
                count += 1
    print('PASS multiplicative-order/subset-degree tests:', count)
    return count


def verify_factors():
    from sympy import symbols, factor_list, primerange
    X = symbols('X')
    count = 0
    for r in (3, 5, 7, 11):
        for a in range(1, 6):
            n = r**a
            if n > 150:
                continue
            for p in primerange(2, 80):
                degrees = []
                for factor, multiplicity in factor_list(X**n - 1, modulus=p)[1]:
                    degrees.extend([int(factor.as_poly(X).degree())] * multiplicity)
                assert sum(degrees) == n
                bits = 1
                for d in degrees:
                    bits |= bits << d
                got = next((m for m in range(n + 1) if not (bits >> m) & 1), None)
                expected = predicted(r, a, int(p))
                assert got == expected, (r, a, p, got, expected)
                count += 1
    print('PASS direct polynomial factorization tests:', count)
    return count


if __name__ == '__main__':
    verify_orders()
    if '--factor' in sys.argv:
        verify_factors()
