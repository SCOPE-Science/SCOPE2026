"""Finite exact-arithmetic verification of a coupon-collector likelihood-ratio theorem.

Run with Python 3.9+: python verify.py. The general assertion is proved
mathematically in RESULT.md; this code tests finite instances only.
"""
from fractions import Fraction
from math import factorial


def multiply_polynomials(a, b, top):
    out = [Fraction(0) for _ in range(top + 1)]
    for k, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b[: top + 1 - k]):
            if y:
                out[j + k] += x * y
    return out


def joint_egf(weights, final, n):
    """Exact Pr(completion at n, final type), by exponential generating functions."""
    p = [Fraction(w, sum(weights)) for w in weights]
    co = [Fraction(1)] + [Fraction(0)] * (n - 1)
    for i, q in enumerate(p):
        if i == final:
            continue
        factor = [Fraction(0)] + [q**k / factorial(k) for k in range(1, n)]
        co = multiply_polynomials(co, factor, n - 1)
    return p[final] * factorial(n - 1) * co[n - 1]


def joint_subset_dp(weights, final, n):
    """Independent exact calculation by a finite-state path enumeration."""
    p = [Fraction(w, sum(weights)) for w in weights]
    states = {0: Fraction(1)}
    for _ in range(n - 1):
        nxt = {}
        for mask, probability in states.items():
            for i, q in enumerate(p):
                if i == final:
                    continue
                key = mask | (1 << i)
                nxt[key] = nxt.get(key, Fraction(0)) + probability * q
        states = nxt
    full = ((1 << len(p)) - 1) ^ (1 << final)
    return p[final] * states.get(full, Fraction(0))


def check(weights, max_n):
    m = len(weights)
    prev = {}
    for n in range(m, max_n + 1):
        js = [joint_egf(weights, i, n) for i in range(m)]
        assert all(v > 0 for v in js)
        assert all(v == joint_subset_dp(weights, i, n) for i, v in enumerate(js)), (weights, n)
        for i in range(m):
            for j in range(m):
                if weights[i] >= weights[j]:
                    continue
                odds = js[i] / js[j]
                if (i, j) in prev:
                    assert odds > prev[(i, j)], (weights, n, i, j, odds, prev[(i, j)])
                prev[i, j] = odds
    print('PASS', tuple(weights), 'n=', m, '..', max_n)


if __name__ == '__main__':
    for data in ((1, 2), (1, 2, 5), (1, 1, 3), (1, 2, 3, 5), (1, 1, 3, 10), (2, 3, 4, 7), (1, 2, 3, 10, 30)):
        check(data, 22)
    print('ALL FINITE CHECKS PASS (not a substitute for infinite proof).')
