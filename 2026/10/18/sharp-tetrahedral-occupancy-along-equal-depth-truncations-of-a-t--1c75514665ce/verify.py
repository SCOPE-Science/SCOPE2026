#!/usr/bin/env python3
"""Exact, standalone check of the truncated-tetrahedron determinant census.

Requires only Python's standard library. The proof that the finite census
implies a sharp unrestricted extremal theorem is in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def plus(a, b):
    return trim(tuple((a[i] if i < len(a) else 0) +
                      (b[i] if i < len(b) else 0)
                      for i in range(max(len(a), len(b)))))


def neg(a):
    return tuple(-x for x in a)


def minus(a, b):
    return plus(a, neg(b))


def times(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def value(p, x):
    return sum(coef*x**i for i, coef in enumerate(p))


def derivative(p):
    return trim(tuple(i*p[i] for i in range(1, len(p))) or (0,))


def det3(a, b, c):
    return plus(minus(times(a[0], minus(times(b[1], c[2]), times(b[2], c[1]))),
                      times(a[1], minus(times(b[0], c[2]), times(b[2], c[0])))),
                times(a[2], minus(times(b[0], c[1]), times(b[1], c[0]))))


def main():
    one, t = (1,), (0, 1)
    u = minus(one, t)
    w = minus(one, times((2,), t))
    v = minus(plus(one, times((3,), times(t, t))), times((3,), t))
    optimum = times(u, v)
    expected = {
        (0,): 78,
        times(times(t, t), w): 48,
        times(times(t, t), u): 72,
        times(times(t, u), w): 120,
        times(t, times(u, u)): 72,
        times(t, v): 24,
        times(times(u, u), w): 48,
        times(w, w): 3,
        optimum: 24,
        times(w, minus(plus(one, times((2,), times(t, t))), times((2,), t))): 6,
    }
    assert len(expected) == 10 and sum(expected.values()) == 495
    vertices = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    edges = [(i, j) for i in range(4) for j in range(4) if i != j]
    points = [tuple((vertices[i][k], vertices[j][k]-vertices[i][k])
                    for k in range(3)) for i, j in edges]
    found = Counter()
    maximizing_sets = []
    for ix in combinations(range(12), 4):
        q = [points[i] for i in ix]
        difference = [tuple(minus(q[j][k], q[0][k]) for k in range(3))
                      for j in range(1, 4)]
        det = det3(*difference)
        # All nonzero signed determinants keep the same sign for 0 < t < 1/2.
        # The positivity of the ten candidate forms is proved in RESULT.md.
        mid = value(det, Fraction(1, 4))
        if mid < 0:
            det = neg(det)
        elif mid == 0:
            assert det == (0,)
        found[det] += 1
        if det == optimum:
            maximizing_sets.append(ix)
    assert found == expected, (found, expected)
    assert len(maximizing_sets) == 24
    assert sum(found.values()) == 495
    assert value(optimum, Fraction(1, 3)) == Fraction(2, 9)
    assert value(optimum, Fraction(1, 2)) == Fraction(1, 8)
    assert value(optimum, Fraction(0)) == 1
    body_volume = minus(one, times((4,), times(t, times(t, t))))
    assert value(body_volume, Fraction(1, 3)) == Fraction(23, 27)
    assert value(optimum, Fraction(1, 3)) / value(body_volume, Fraction(1, 3)) == Fraction(6, 23)
    assert value(optimum, Fraction(1, 2)) / value(body_volume, Fraction(1, 2)) == Fraction(1, 4)
    numerator = minus(times(derivative(optimum), body_volume),
                      times(optimum, derivative(body_volume)))
    assert numerator == (-4, 12, 3, -32, 24), numerator
    assert value(numerator, Fraction(0)) == -4
    assert value(numerator, Fraction(1, 2)) == Fraction(1, 4)
    low, high = Fraction(432, 1000), Fraction(433, 1000)
    assert value(numerator, low) < 0 < value(numerator, high)
    for _ in range(90):
        middle = (low + high) / 2
        if value(numerator, middle) < 0:
            low = middle
        else:
            high = middle
    root = float((low+high)/2)
    frac = float(value(optimum, (low+high)/2)/value(body_volume, (low+high)/2))
    print('VERIFY_OK vertex_sets=495 distinct_symbolic_volume_forms=10')
    print('VERIFY_OK interior_maximizing_vertex_sets=24 endpoint_ratio_one_third=6/23')
    print(f'VERIFY_OK unique_interior_minimizer_t={root:.15f} ratio={frac:.15f}')


if __name__ == '__main__':
    main()
