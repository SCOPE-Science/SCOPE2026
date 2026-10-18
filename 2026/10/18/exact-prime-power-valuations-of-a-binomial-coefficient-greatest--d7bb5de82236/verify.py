#!/usr/bin/env python3
"""Exact-integer crosschecks for the binomial gcd identity; finite testing only."""
from math import comb, gcd


def factor(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            a = 0
            while n % d == 0:
                n //= d
                a += 1
            out.append((d, a))
        d += 1 if d == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def vfac(n, p):
    t = 0
    while n:
        n //= p
        t += n
    return t


def vbin(N, K, p):
    return vfac(N, p) - vfac(K, p) - vfac(N-K, p)


def p_exp(p, a, n):
    m = n // p**a
    b = 0
    while p**(b+1) <= m:
        b += 1
    return max(0, a-b), m, b


def formula(n):
    d = 1
    for p, a in factor(n):
        e, _, _ = p_exp(p, a, n)
        d *= p**e
    return d


count = 0
for n in range(3, 241):
    k = n - 1
    for p, a in factor(n):
        target, m, b = p_exp(p, a, n)
        actual = min(vbin(q*k, k, p) for q in range(2, n+1))
        assert target == actual, (n, p, target, actual)
        count += n-1

witnesses = 0
for n in range(3, 6001):
    k = n - 1
    for p, a in factor(n):
        target, m, b = p_exp(p, a, n)
        if target == 0:
            continue
        q = 2 if m == 1 else 1 + p**a * (m-p**b)
        assert 2 <= q <= n
        assert vbin(q*k, k, p) == target, (n, p, q)
        witnesses += 1

for n in range(3, 31):
    k = n - 1
    d = 0
    for q in range(2, n+1):
        d = gcd(d, comb(q*k, k))
    assert d == formula(n), (n, d, formula(n))
    assert n % d == 0
assert formula(9) == 9
assert formula(18) == 9
assert formula(48) == 8
print(f"VERIFY_OK exhaustive_local_terms={count} exact_witnesses={witnesses} gcd_cases=28")
