#!/usr/bin/env python3
"""Exact finite checks for Gaussian multinomial polynomial-LCM identities.

Python 3 standard library only. Finite verification is not an infinite proof.
"""
from math import factorial


def compositions(n, r):
    if r == 1:
        yield (n,)
        return
    for a in range(n + 1):
        for tail in compositions(n - a, r - 1):
            yield (a,) + tail


def exponent(n, r, d):
    return (min(n, r * (d - 1)) - n % d) // d


def facvaluation(n, p):
    v = 0
    while n:
        n //= p
        v += n
    return v


def primes_through(n):
    return [p for p in range(2, n + 1)
            if all(p % d for d in range(2, int(p ** 0.5) + 1))]


def cyclotomic_at_integer(d, q, cache):
    if d == 1:
        return q - 1
    if d not in cache:
        v = q ** d - 1
        for e in range(1, d):
            if d % e == 0:
                t = cyclotomic_at_integer(e, q, cache)
                assert v % t == 0
                v //= t
        cache[d] = v
    return cache[d]


def qfactorials(n, q):
    f = [1]
    for t in range(1, n + 1):
        f.append(f[-1] * ((q ** t - 1) // (q - 1)))
    return f


def run():
    tested = 0
    for n in range(1, 19):
        for r in range(2, min(n, 5) + 1):
            ps = primes_through(n)
            observed_d = {d: 0 for d in range(2, n + 1)}
            observed_p = {p: 0 for p in ps}
            for ks in compositions(n, r):
                for d in observed_d:
                    val = n // d - sum(k // d for k in ks)
                    if val > observed_d[d]:
                        observed_d[d] = val
                for p in ps:
                    val = facvaluation(n, p) - sum(facvaluation(k, p) for k in ks)
                    if val > observed_p[p]:
                        observed_p[p] = val
                tested += 1
            for d, val in observed_d.items():
                assert val == exponent(n, r, d), (n, r, d, val)
            for p, val in observed_p.items():
                powers = []
                v = p
                while v <= n:
                    powers.append(v)
                    v *= p
                assert val == sum(exponent(n, r, d) for d in powers), (n, r, p)

    evaluated = 0
    for q in (2, 3):
        for n in range(1, 11):
            f = qfactorials(n, q)
            cache = {1: q - 1}
            phi = {d: cyclotomic_at_integer(d, q, cache)
                   for d in range(2, n + 1)}
            for r in range(2, min(n, 4) + 1):
                for ks in compositions(n, r):
                    denominator = 1
                    for k in ks:
                        denominator *= f[k]
                    assert f[n] % denominator == 0
                    direct = f[n] // denominator
                    by_phi = 1
                    for d in range(2, n + 1):
                        val = n // d - sum(k // d for k in ks)
                        by_phi *= phi[d] ** val
                    assert direct == by_phi, (q, n, r, ks)
                    evaluated += 1
    print('VERIFY_OK row_compositions=%d q_factorizations=%d' % (tested, evaluated))


if __name__ == '__main__':
    run()
