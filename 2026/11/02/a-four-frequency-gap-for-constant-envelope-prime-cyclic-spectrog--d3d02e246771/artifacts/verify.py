#!/usr/bin/env python3
"""Finite corroboration of the constant-envelope STFT support gap.
Run with Python 3: python artifacts/verify.py
This numerical checker is not a proof of the infinite-prime theorem.
"""
import cmath
import itertools
import math
import random
from collections import Counter


def root(p, x):
    return cmath.exp(2j * math.pi * (x % p) / p)


def stft_size(f, g, p):
    support = 0
    for j in range(p):
        for k in range(p):
            z = sum(f[n] * g[(n-j) % p].conjugate() * root(p, -k*n)
                    for n in range(p))
            if abs(z) > 1e-7:
                support += 1
    return support


def main():
    checks = 0
    for p in (5, 7, 11):
        # The finite combinatorial ingredient: 2/3-point frequency supports
        # always admit an exactly-once nonzero directed difference.
        for size in (2, 3):
            for E in itertools.combinations(range(p), size):
                differences = Counter((u - v) % p for u in E for v in E if u != v)
                assert 1 in differences.values(), (p, E)
                checks += 1
        inv2 = pow(2, -1, p)
        for u in (0, 1, 2):
            for a in (0, 1):
                for b in (0, 2):
                    f = [root(p, (u * inv2 * n*n + a*n) % p) for n in range(p)]
                    g = [root(p, (u * inv2 * n*n + b*n) % p) for n in range(p)]
                    assert stft_size(f, g, p) == p
                    checks += 1
        f = [root(p, inv2 * n*n) for n in range(p)]
        g = [root(p, 2 * inv2 * n*n) for n in range(p)]
        assert stft_size(f, g, p) == p*p
        checks += 1
        h = [cmath.exp(0.3j) if n == 0 else 1.0+0j for n in range(p)]
        s = stft_size(h, h, p)
        assert s == p or s >= 4*p-3, (p, s)
        checks += 1
        rng = random.Random(1000+p)
        for _ in range(36):
            f = [cmath.exp(2j*math.pi*rng.random()) for _ in range(p)]
            g = [cmath.exp(2j*math.pi*rng.random()) for _ in range(p)]
            s = stft_size(f, g, p)
            assert s == p or s >= 4*p-3, (p, s)
            checks += 1
    print(f'PASS: {checks} finite checks on primes 5, 7, 11; no infinite claim certified')


if __name__ == '__main__':
    main()
