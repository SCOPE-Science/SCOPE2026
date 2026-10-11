#!/usr/bin/env python3
"""Independent elementary identity and numerical spot checks for the stated theorem.

Requires Python 3 standard library only. Numeric testing is diagnostic, not an
exhaustive proof; the RESULT proof establishes global optimality analytically.
"""
from fractions import Fraction as F
from itertools import permutations
from math import sqrt, isclose
import random


def scalar(c):
    return {} if c == 0 else {(0, 0, 0): F(c)}


def variable(i):
    key = tuple(int(j == i) for j in range(3))
    return {key: F(1)}


def add(*polys):
    result = {}
    for p in polys:
        for ex, co in p.items():
            result[ex] = result.get(ex, F(0)) + co
    return {k: v for k, v in result.items() if v != 0}


def neg(p):
    return {k: -v for k, v in p.items()}


def mul(*polys):
    result = scalar(1)
    for p in polys:
        nxt = {}
        for a, c in result.items():
            for b, d in p.items():
                key = tuple(ai + bi for ai, bi in zip(a, b))
                nxt[key] = nxt.get(key, F(0)) + c * d
        result = {k: v for k, v in nxt.items() if v != 0}
    return result


def power(p, n):
    return mul(*([p] * n))


def div(p, d):
    return {k: v / F(d) for k, v in p.items()}


def exact_polynomial_checks():
    a, b, c = (variable(i) for i in range(3))
    vals = (a, b, c)
    k = ((0, -1, 1), (1, 0, -1), (-1, 1, 0))
    numerator = add(*(div(mul(power(vals[i], 3), vals[j]), 4 * k[i][j])
                      for i in range(3) for j in range(3) if k[i][j]))
    # Pure Fractions are used above; 4/k is an exact signed integer for k= +/-1.
    rhs = neg(div(mul(add(a, neg(b)), add(a, neg(c)),
                      add(b, neg(c)), add(a, b, c)), 4))
    assert numerator == rhs, "fourth-degree Vandermonde identity failed"

    # Verify the zero-sum discriminant identity for arbitrary a,b, c=-a-b.
    y1, y2 = a, b
    y3 = neg(add(a, b))
    s2 = add(power(y1, 2), power(y2, 2), power(y3, 2))
    q = add(power(y1, 3), power(y2, 3), power(y3, 3))
    delta = mul(add(y1, neg(y2)), add(y1, neg(y3)),
                add(y2, neg(y3)))
    assert power(delta, 2) == add(div(power(s2, 3), 2), neg(mul(scalar(3), power(q, 2))))
    print("EXACT_POLYNOMIAL_IDENTITIES_OK")


def bisect(fun, low, high, iterations=100):
    fl = fun(low)
    fh = fun(high)
    assert fl * fh < 0
    for _ in range(iterations):
        mid = (low + high) / 2
        fm = fun(mid)
        if fl * fm <= 0:
            high = mid
            fh = fm
        else:
            low = mid
            fl = fm
    return (low + high) / 2


def radius_ratio(x):
    a, b, c = x
    xx = (a, b, c)
    kx = ((-b + c) / 4, (a - c) / 4, (-a + b) / 4)
    denominator = sum(z ** 4 for z in xx)
    return abs(sum(xx[i] ** 3 * kx[i] for i in range(3))) / denominator


def checks():
    target = sqrt(3 * sqrt(6)) / 16
    t0 = sqrt((sqrt(6) - 2) / 6)
    q0 = -t0 / (sqrt(6) - 1)
    critical = 1 / sqrt(6)
    cubic = lambda z: z ** 3 - z / 2 - q0 / 3
    roots = [bisect(cubic, -2, -critical),
             bisect(cubic, -critical, critical),
             bisect(cubic, critical, 2)]
    x = [t0 + y for y in roots]
    assert isclose(sum(roots), 0, abs_tol=1e-12)
    assert isclose(sum(y*y for y in roots), 1, abs_tol=1e-12)
    assert isclose(sum(y**3 for y in roots), q0, abs_tol=1e-12)
    assert isclose(radius_ratio(x), target, rel_tol=2e-12)
    for perm in permutations(x):
        assert isclose(radius_ratio(perm), target, rel_tol=2e-12)
    randomizer = random.Random(479208)
    for _ in range(60000):
        xx = [randomizer.uniform(-1, 1) for _ in range(3)]
        if sum(abs(xi) for xi in xx) < 1e-8:
            continue
        assert radius_ratio(xx) <= target * (1 + 1e-11)
    print('NUMERICAL_SPOT_CHECKS_OK')
    print('SHARP_RADIUS', format(target, '.16g'))
    print('EXTREMAL_VECTOR', *(format(a, '.13g') for a in x))


if __name__ == '__main__':
    exact_polynomial_checks()
    checks()
