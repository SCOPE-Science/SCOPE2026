#!/usr/bin/env python3
"""Finite exact checks for the coupon-collector terminal singleton law.

All checks are finite rational identities; they do not establish weak convergence.
Requires Python 3 only.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


def law_via_markov(n):
    """Absorb the (unseen, singleton) chain, eliminating self-loops exactly."""
    @lru_cache(None)
    def rec(a, b):
        if a == 0:
            return tuple(Fraction(int(u == b)) for u in range(n + 1))
        out = [Fraction(0) for _ in range(n + 1)]
        if a:
            nxt = rec(a - 1, b + 1)
            for u in range(n + 1):
                out[u] += Fraction(a, a + b) * nxt[u]
        if b:
            nxt = rec(a, b - 1)
            for u in range(n + 1):
                out[u] += Fraction(b, a + b) * nxt[u]
        return tuple(out)
    return rec(n, 0)


def law_via_poisson_joint_integral(n, u):
    """Integrate the exact joint density using Gamma integrals, in rationals."""
    out = Fraction(0)
    for a in range(n-u+1):
        for b in range(a+1):
            out += Fraction((-1)**a * comb(n-u,a) * comb(a,b) * factorial(u-1+b), (u+a)**(u+b))
    return n * comb(n-1,u-1) * out


def main():
    identities = 0
    for n in range(2,11):
        p = law_via_markov(n)
        assert sum(p) == 1
        identities += 1
        assert p[0] == 0
        identities += 1
        for u in range(1,n+1):
            q = law_via_poisson_joint_integral(n,u)
            assert p[u] == q, (n,u,p[u],q)
            identities += 1
        harmonic = sum((Fraction(1,i) for i in range(1,n+1)), Fraction(0))
        mean = sum((u * p[u] for u in range(n+1)), Fraction(0))
        assert mean == harmonic, (n,mean,harmonic)
        identities += 1
        variance = sum(((u-mean)**2 * p[u] for u in range(n+1)), Fraction(0))
        expected_variance = 4*sum((sum((Fraction(1,j) for j in range(1,i+1)), Fraction(0))/i for i in range(1,n+1)), Fraction(0)) - 3*harmonic - harmonic*harmonic
        assert variance == expected_variance, (n,variance,expected_variance)
        identities += 1
    print(f'PASS: {identities} exact rational assertions, n=2..10')
    print('Independent finite-state absorption and integrated Poisson joint law agree.')
    print('Harmonic mean and published finite variance identity also agree.')
    print('Analytic proof, not these finite checks, establishes all-n and limit claims.')

if __name__ == '__main__':
    main()
