"""Exact finite consistency checks for the order-k Poisson tail threshold.

Usage: python3 verify.py
This bounded test is not a substitute for the analytic proof.
No external Python packages are required.
"""
from fractions import Fraction
from math import comb, factorial


def normalize(v):
    while len(v) > 1 and not v[-1]:
        v.pop()
    return v


def add(a, b):
    return normalize([(a[i] if i < len(a) else 0) +
                      (b[i] if i < len(b) else 0)
                      for i in range(max(len(a), len(b)))])


def subtract(a, b):
    return add(a, [-t for t in b])


def shift(a, d):
    return [Fraction(0)] * d + a


def scale(a, c):
    return normalize([v * c for v in a])


def product(a, b):
    c = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] += ai * bj
    return normalize(c)


def coefficients(k, end):
    # Coefficient recurrence for exp(L * (z+...+z**k)).
    p = [[Fraction(1)]]
    for n in range(1, end + 1):
        a = [Fraction(0)]
        for j in range(1, min(k, n) + 1):
            a = add(a, scale(shift(p[n-j], 1), Fraction(j, n)))
        p.append(a)
    return p


def S(m):
    return [Fraction(comb(m,j), factorial(j+2)) for j in range(m+1)]


def T(t):
    return [Fraction(comb(t,i), factorial(i+1)) for i in range(t+1)]


def evaluate(a, x):
    ans = Fraction(0)
    for c in reversed(a):
        ans = ans * x + c
    return ans


def run():
    checks = 0
    for k in range(2, 18):
        p = coefficients(k, 6*k)
        q = coefficients(6*k, 6*k)
        for n in range(k+1, 2*k+2):
            correction = [Fraction(0)]
            for a in range(n-k):
                correction = add(correction, shift(q[a], 1))
            assert p[n] == subtract(q[n], correction)
            checks += 1
        for t in range(k-1):
            difference = subtract(p[k+t+2], p[k+t+1])
            assert difference == normalize(shift(subtract(S(k+t), T(t)), 2))
            checks += 1
            gap = subtract(product(S(k), T(t)), S(k+t))
            assert all(c >= 0 for c in gap)
            if t > 0:
                assert any(c > 0 for c in gap)
            checks += 1
        for x in [Fraction(1, 20), Fraction(1, 10), Fraction(1, 5), Fraction(1, 2)]:
            if evaluate(S(k), x) < 1:
                assert all(evaluate(p[n], x) > evaluate(p[n+1], x)
                           for n in range(k, 6*k))
                checks += 1
            if evaluate(S(k), x) > 1:
                assert evaluate(p[k+2], x) > evaluate(p[k+1], x)
                checks += 1
    # Strict bound on the exceptional k=2 first-edge comparison.
    assert evaluate(S(2), Fraction(6, 5)) < 1
    assert evaluate(S(2), Fraction(129, 100)) < 1
    assert evaluate(S(2), Fraction(130, 100)) > 1
    print('PASS:', checks, 'exact polynomial and rational-distribution checks; k=2 root bracket verified.')


if __name__ == '__main__':
    run()
