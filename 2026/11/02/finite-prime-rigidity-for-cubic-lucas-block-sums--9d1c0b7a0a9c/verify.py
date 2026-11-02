#!/usr/bin/env python3
"""Exact finite checks for the cubic Lucas block-sum prime-support theorem.

All arithmetic uses Python integers; the accompanying proof establishes the
unrestricted assertion. This script tests its algebraic certificate and finite
instances, not an infinite search.
"""
from math import gcd


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(c, a):
    return c * a[0], c * a[1]


def root(e):
    return [(1, 0), (0, 1), (-1, -1)][e % 3]


def norm(a):
    x, y = a
    return x * x - x * y + y * y


norm_certificate = {
    (0, 0): 0,
    (0, 1): 189, (0, 2): 189,
    (1, 0): 39, (2, 0): 39,
    (1, 1): 75, (2, 2): 75,
    (1, 2): 219, (2, 1): 219,
}
for (i, j), expected in norm_certificate.items():
    h = (0, 0)
    for coefficient, exponent in ((9, 2 * j), (-3, i + j), (-1, 2 * i), (-5, 0)):
        h = add(h, scale(coefficient, root(exponent)))
    assert norm(h) == expected, ((i, j), h, norm(h), expected)


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**0.5) + 1))


for p in range(5, 502):
    if not is_prime(p) or p in (7, 13, 73):
        continue
    solutions = [x for x in range(p) if pow(x, 3, p) == 1]
    solutions_y = [y for y in range(p) if pow(y, 3, p) == 27 % p]
    assert all((x, y) == (1, 3 % p) for x in solutions for y in solutions_y
               if (y * y - x * y - x * x - 5) % p == 0), p

L = [2, 1]
for _ in range(2, 610):
    L.append(L[-1] + L[-2])
C = [x ** 3 for x in L]
P = [0]
for value in C:
    P.append(P[-1] + value)


def block(n, k):
    return P[n + k + 1] - P[n + 1]


count = 0
for k in range(2, 601, 2):
    s = [block(n, k) for n in range(10)]
    for n in range(6):
        assert s[n + 4] == 3 * s[n + 3] + 6 * s[n + 2] - 3 * s[n + 1] - s[n]
    d = gcd(*s[:4])
    assert all(v % d == 0 for v in s)
    e = gcd(L[k + 1] ** 3 - 1, L[k + 2] ** 3 - 27)
    assert e % d == 0, k
    q = e // d
    for p in (2, 3, 7, 13, 73):
        while q > 1 and q % p == 0:
            q //= p
    assert q == 1, k
    count += 1

witnesses = [(7, 6, 16, 2, 28), (13, 24, 28, 1080, 28080),
             (73, 34, 148, 3571, 260683)]
for p, k, period, d, e in witnesses:
    assert gcd(*(block(n, k) for n in range(4))) == d
    assert gcd(L[k + 1] ** 3 - 1, L[k + 2] ** 3 - 27) == e
    assert e % p == 0 and d % p != 0
    assert (L[period] % p, L[period + 1] % p) == (2 % p, 1 % p)
    for j in (1, 2, 3):
        length = k + j * period
        if length + 4 >= len(L):
            continue
        assert ((L[length + 1] ** 3 - 1) % p == 0
                and (L[length + 2] ** 3 - 27) % p == 0)
        assert block(0, length) % p != 0

print(f'VERIFY_OK norm_pairs=9 local_primes_tested={sum(is_prime(p) and p not in (7,13,73) for p in range(5,502))} even_lengths={count} witness_classes=3')
