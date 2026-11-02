#!/usr/bin/env python3
"""Finite arithmetic checks for a density-zero theorem about divisor sums.

The checker tests identities and finite examples, not asymptotic density.
Requires only the Python standard library.
"""
from math import gcd
from fractions import Fraction


def sieve_spf(n):
    spf = list(range(n + 1))
    for i in range(2, int(n ** .5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factor(n, spf):
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        yield p, a


def sigma_square(n, spf):
    out = 1
    for p, a in factor(n, spf):
        out *= (pow(p, 2 * a + 1) - 1) // (p - 1)
    return out


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            return False
    return True


def main():
    cutoffs = {10: 10, 100: 99, 1000: 974,
               10000: 9561, 100000: 93845}
    N = max(cutoffs)
    spf = sieve_spf(N)
    count = 0
    for n in range(1, N + 1):
        d = sigma_square(n, spf)
        if gcd(n, d) == gcd(n * n, d):
            count += 1
        if n in cutoffs:
            assert count == cutoffs[n], (n, count, cutoffs[n])

    examples = 0
    for p in (7, 13, 19, 31, 37):
        roots = [r for r in range(1, p) if (r * r + r + 1) % p == 0]
        assert len(roots) == 2 and all(r % p != 0 for r in roots)
        qs = [q for q in range(2, 1000) if is_prime(q) and q % p == roots[0]]
        q, r = qs[0], qs[1]
        n = p * q * r
        assert (q*q + q + 1) % p == 0
        assert (r*r + r + 1) % p == 0
        d = sigma_square(n, sieve_spf(n))
        assert gcd(n, d) != gcd(n*n, d)
        examples += 1

    # Verify two local CRT factors exactly using all residue classes.
    p, q = 7, 2
    M = p*p*q*q
    count_local = sum((n % p == 0 and n % (p*p) != 0 and
                       n % q == 0 and n % (q*q) != 0)
                      for n in range(M))
    predicted = Fraction(p-1, p*p)*Fraction(q-1, q*q)
    assert Fraction(count_local, M) == predicted

    # The two independent factors are not an assumption for infinitely many primes.
    print(f'VERIFY_OK gcdn_counts=100000 source_cutoffs=5 witness_primes={examples} crt_residues={M}')


if __name__ == '__main__':
    main()
