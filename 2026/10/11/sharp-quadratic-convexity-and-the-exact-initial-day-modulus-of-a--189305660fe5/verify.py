"""Deterministic finite checks for a sharp convexity coefficient.

The universally quantified claim is established in the accompanying proof;
finite tests here detect normalization and arithmetic errors only.
"""
from fractions import Fraction
from math import sqrt
from random import Random


def norm_sq(x, t):
    return sum(abs(v) for v in x) ** 2 + t * sum(v * v for v in x)


def coefficient(n, t):
    p, q = n // 2, n - n // 2
    s = sqrt((1 + t / p) * (1 + t / q))
    return (s - 1) / (s + 1)


def witness(n, t, k):
    p, q = n // 2, n - n // 2
    ratio = sqrt((1 + t / q) / (1 + t / p))
    # Positive total A=ratio, negative total B=1.
    d = [ratio / p] * p + [-1 / q] * q
    v = [abs(z) for z in d]
    m = [k * z for z in v]
    unit = sqrt((k * k + coefficient(n, t)) * norm_sq(d, t))
    x = [(a + b) / unit for a, b in zip(m, d)]
    y = [(a - b) / unit for a, b in zip(m, d)]
    return x, y


def check_exact():
    cases = [
        (2, Fraction(1), [Fraction(1), Fraction(-1)], Fraction(1, 3)),
        (4, Fraction(2), [Fraction(1), Fraction(1), Fraction(-1), Fraction(-1)], Fraction(1, 3)),
        (3, Fraction(7), [Fraction(3), Fraction(-2), Fraction(-2)], Fraction(5, 7)),
    ]
    count = 0
    for n, t, d, c in cases:
        assert n == len(d)
        v = list(map(abs, d))
        for k in (1, 2, 3, 8):
            m = [k * a for a in v]
            x = [a + b for a, b in zip(m, d)]
            y = [a - b for a, b in zip(m, d)]
            mean = (norm_sq(x, t) + norm_sq(y, t)) / 2
            assert mean - norm_sq(m, t) == c * norm_sq(d, t)
            assert norm_sq(x, t) == norm_sq(y, t)
            assert norm_sq(x, t) == (k * k + c) * norm_sq(d, t)
            count += 1
    return count


def check_numeric():
    rng = Random(20261010)
    tested = 0
    for n in range(2, 14):
        for t in (0.01, 0.15, 0.8, 1, 1.7, 5, 20):
            c = coefficient(n, t)
            for k in (1, 1.01, 2, 10):
                x, y = witness(n, t, k)
                nx, ny = norm_sq(x, t), norm_sq(y, t)
                assert abs(nx - 1) < 3e-12 and abs(ny - 1) < 3e-12
                m = [(a+b)/2 for a,b in zip(x,y)]
                d = [(a-b)/2 for a,b in zip(x,y)]
                assert abs((nx+ny)/2 - norm_sq(m,t) - c*norm_sq(d,t)) < 3e-12
                eps = 2/sqrt(k*k+c)
                assert abs(2*sqrt(norm_sq(d,t))-eps) < 3e-12
                tested += 1
            for _ in range(800):
                x = [rng.uniform(-5,5) for i in range(n)]
                y = [rng.uniform(-5,5) for i in range(n)]
                m = [(a+b)/2 for a,b in zip(x,y)]
                d = [(a-b)/2 for a,b in zip(x,y)]
                excess = (norm_sq(x,t)+norm_sq(y,t))/2-norm_sq(m,t)-c*norm_sq(d,t)
                scale = 1+norm_sq(x,t)+norm_sq(y,t)
                assert excess >= -1e-12*scale, (n,t,excess)
                tested += 1
    return tested


if __name__ == '__main__':
    rational = check_exact()
    numeric = check_numeric()
    print('Exact rational identities:', rational)
    print('Deterministic numeric witness + random tests:', numeric)
    print('PASS (finite checks only)')
