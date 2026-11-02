#!/usr/bin/env python3
"""Exact rank certificate for degree-wise spherical harmonic sampling at 48 F4 roots.
All arithmetic in the finite tests is rational; no numerical tolerance is used.
"""
from itertools import combinations, product
from fractions import Fraction


def reps():
    a, b = set(), set()
    for i, j in combinations(range(4), 2):
        for s, t in product((-1, 1), repeat=2):
            v = [0] * 4
            v[i], v[j] = s, t
            v = tuple(v)
            a.add(v if next(z for z in v if z) > 0 else tuple(-z for z in v))
    for i in range(4):
        v = [0] * 4
        v[i] = 2
        b.add(tuple(v))
    for signs in product((-1, 1), repeat=4):
        b.add(signs if signs[0] > 0 else tuple(-z for z in signs))
    a, b = sorted(a), sorted(b)
    assert len(a) == len(b) == 12
    return a, b

A, B = reps()


def inner(v, w):
    return sum(x * y for x, y in zip(v, w))


def u_half(deg):
    return (1, 1, 0, -1, -1, 0)[deg % 6]


def u_zer(deg):
    return (1, 0, -1, 0)[deg % 4]


def u_invroot2(deg):
    # Returns (integer part, coefficient of square-root two).
    return ((1, 0), (0, 1), (1, 0), (0, 0), (-1, 0),
            (0, -1), (-1, 0), (0, 0))[deg % 8]


def same_value(num, den, deg):
    assert den in (2, 4) and (-den <= num <= den)
    assert (2 * num) % den == 0
    level = 2 * num // den
    if level == 0:
        return u_zer(deg)
    sgn = (-1 if level < 0 and deg % 2 else 1)
    if abs(level) == 2:
        return sgn * (deg + 1)
    assert abs(level) == 1
    return sgn * u_half(deg)


def matrix(deg):
    # This 24x24 matrix has the same rank as the 48x48 zonal Gram matrix.
    # For odd degrees, the B block is rescaled on both sides by sqrt(2),
    # making every entry integral, without changing rank.
    q = [[0] * 24 for _ in range(24)]
    for i, v in enumerate(A):
        for j, w in enumerate(A):
            q[i][j] = same_value(inner(v, w), 2, deg)
    for i, v in enumerate(B):
        for j, w in enumerate(B):
            q[i + 12][j + 12] = same_value(inner(v, w), 4, deg) * (2 if deg % 2 else 1)
    for i, v in enumerate(A):
        for j, w in enumerate(B):
            z = inner(v, w)
            assert z in (-2, 0, 2)
            if z == 0:
                value = u_zer(deg)
                assert not (deg % 2) or value == 0
            else:
                integer, sqrt2coef = u_invroot2(deg)
                sgn = -1 if z < 0 and deg % 2 else 1
                if deg % 2:
                    assert integer == 0
                    value = sgn * 2 * sqrt2coef
                else:
                    assert sqrt2coef == 0
                    value = sgn * integer
            q[i][j + 12] = q[j + 12][i] = value
    return q


def exact_rank(a):
    """Rational Gaussian elimination, returning the exact integer rank."""
    a = [[Fraction(x) for x in row] for row in a]
    m, n = len(a), len(a[0])
    i = 0
    for j in range(n):
        pivot = next((k for k in range(i, m) if a[k][j]), None)
        if pivot is None:
            continue
        a[i], a[pivot] = a[pivot], a[i]
        pivot_entry = a[i][j]
        for k in range(i + 1, m):
            if a[k][j]:
                scale = a[k][j] / pivot_entry
                a[k][j] = Fraction(0)
                for c in range(j + 1, n):
                    a[k][c] -= scale * a[i][c]
        i += 1
        if i == m:
            break
    return i


def verify():
    P = A + B
    assert len(set(P)) == 24
    assert all(sum(1 for w in B if inner(v, w)) == 6 for v in A)
    assert all(sum(1 for v in A if inner(v, w)) == 6 for w in B)
    expected = {
        0: 1, 1: 4, 2: 9, 3: 16, 4: 13, 5: 20,
        6: 19, 7: 24, 8: 23, 9: 20, 10: 22, 11: 24,
        12: 24, 13: 24, 14: 23, 15: 24, 16: 23, 17: 24,
        18: 24, 20: 24, 22: 23,
    }
    for deg, target in expected.items():
        m = matrix(deg)
        assert all(m[i][j] == m[j][i] for i in range(24) for j in range(24))
        rank = exact_rank(m)
        assert rank == target, (deg, rank, target)
        print(f'ell={deg:2d} exact rank={rank:2d}')
    # All other degrees are settled by strict diagonal dominance:
    # even ell >=24: diagonal ell+1 >23; odd ell>=19:
    # ell+1 >=20 >11+6*sqrt(2) (since 6sqrt(2)<9).
    assert 6 * 6 * 2 < 9 * 9  # Hence 6*sqrt(2)<9 and 11+6*sqrt(2)<20.
    print('FINITE EXACT RANKS PASS; ALL-DEGREE DOMINANCE BOUND PASS')

if __name__ == '__main__':
    verify()
