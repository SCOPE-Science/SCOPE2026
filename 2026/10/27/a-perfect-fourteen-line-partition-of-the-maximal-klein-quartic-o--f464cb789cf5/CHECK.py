#!/usr/bin/env python3
"""Exhaustive verification of a finite-field plane-quartic line-cover theorem.

Uses only the Python standard library. Field elements a+b*u are encoded
as a+5*b (0 <= a,b < 5), with u*u = 3 in F_5.
"""
from collections import Counter

FIELD = range(25)
T = 21  # 1 + 4*u in F_25.


def add(x, y):
    return ((x % 5 + y % 5) % 5 + 5 * ((x // 5 + y // 5) % 5))


def mul(x, y):
    a, b = x % 5, x // 5
    c, d = y % 5, y // 5
    return ((a * c + 3 * b * d) % 5 + 5 * ((a * d + b * c) % 5))


def fpow(x, n):
    ans = 1
    for _ in range(n):
        ans = mul(ans, x)
    return ans


def f(x, y, z):
    squares = [mul(a, a) for a in (x, y, z)]
    pure = add(add(mul(squares[0], squares[0]),
                   mul(squares[1], squares[1])),
               mul(squares[2], squares[2]))
    mixed = add(add(mul(squares[0], squares[1]),
                    mul(squares[1], squares[2])),
                mul(squares[2], squares[0]))
    return add(pure, mul(T, mixed))


def dot(p, ell):
    return add(add(mul(p[0], ell[0]), mul(p[1], ell[1])),
               mul(p[2], ell[2]))


def canonical_projective_triples():
    return ([(1, y, z) for y in FIELD for z in FIELD] +
            [(0, 1, z) for z in FIELD] + [(0, 0, 1)])


WITNESS_LINES = [
    (1, 0, 16), (1, 0, 18), (1, 2, 18), (1, 3, 3),
    (1, 4, 15), (1, 7, 9), (1, 12, 13), (1, 17, 9),
    (1, 17, 11), (1, 18, 18), (1, 20, 16), (1, 23, 1),
    (1, 23, 22), (1, 24, 3)
]


def verify():
    assert fpow(5, 2) == 3    # u^2 = 3
    assert len(set(canonical_projective_triples())) == 651
    projective = canonical_projective_triples()
    points = [p for p in projective if f(*p) == 0]
    assert len(points) == 56, len(points)
    incidence = [sum(dot(p, ell) == 0 for p in points)
                 for ell in projective]
    spectrum = Counter(incidence)
    assert spectrum == {0: 63, 1: 168, 2: 196, 4: 224}, spectrum
    assert sum(j * nj for j, nj in spectrum.items()) == 56 * 26
    assert sum(j * (j - 1) // 2 * nj for j, nj in spectrum.items()) == 56 * 55 // 2
    assert len(set(WITNESS_LINES)) == 14
    covers = [[i for i, p in enumerate(points) if dot(p, ell) == 0]
              for ell in WITNESS_LINES]
    assert all(len(block) == 4 for block in covers), covers
    flattened = [i for block in covers for i in block]
    assert len(flattened) == 56
    assert sorted(flattened) == list(range(56))
    print('MAXIMAL_QUARTIC_COVER_OK')
    print('rational_points=56, rational_lines=651, spectrum=' + str(sorted(spectrum.items())))
    print('optimal_line_cover=14, each line meets curve in 4 distinct rational points')


if __name__ == '__main__':
    verify()
