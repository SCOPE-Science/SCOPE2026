#!/usr/bin/env python3
"""Exact-rational checks for a frozen-Sylvester square-root iteration."""
from fractions import Fraction as F


def mat(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def add(a, b):
    return mat([[a[i][j] + b[i][j] for j in range(2)] for i in range(2)])


def neg(a):
    return mat([[-a[i][j] for j in range(2)] for i in range(2)])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return mat([[sum((a[i][k] * b[k][j] for k in range(2)), F(0))
                 for j in range(2)] for i in range(2)])


def det(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]


def exact_solve_three(a, b):
    a = [list(row) for row in a]
    b = list(b)
    for k in range(3):
        pivot = next(j for j in range(k, 3) if a[j][k])
        a[k], a[pivot] = a[pivot], a[k]
        b[k], b[pivot] = b[pivot], b[k]
        d = a[k][k]
        a[k] = [x/d for x in a[k]]
        b[k] /= d
        for j in range(3):
            if j != k:
                v = a[j][k]
                a[j] = [a[j][i]-v*a[k][i] for i in range(3)]
                b[j] -= v*b[k]
    return b


def sylvester(z, r):
    a, b, c = z[0][0], z[0][1], z[1][1]
    assert z[0][1] == z[1][0]
    assert r[0][1] == r[1][0]
    u, v, w = exact_solve_three(
        [[2*a, 2*b, 0], [b, a+c, b], [0, 2*b, 2*c]],
        [r[0][0], r[0][1], r[1][1]])
    h = mat([[u, v], [v, w]])
    assert add(mul(z, h), mul(h, z)) == r
    return h


def run():
    x = mat([[4, 0], [0, F(1, 4)]])
    a = mul(x, x)
    z = mat([[F(25, 8), F(1, 2)], [F(1, 2), F(1, 2)]])
    assert a == mat([[16, 0], [0, F(1, 16)]])
    difference = sub(add(z,z), x)
    assert difference == mat([[F(9, 4), 1], [1, F(3, 4)]])
    assert difference[0][0] > 0 and det(difference) == F(11, 16)
    assert z[0][0] > 0 and det(z) == F(21, 16)
    assert mul(x, z) != mul(z, x)
    y1 = add(z, sylvester(z, sub(a, mul(z,z))))
    y2 = add(y1, sylvester(z, sub(a, mul(y1, y1))))
    assert y1 == mat([[F(40841,9744),-F(110,609)],
                      [-F(110,609),F(7241,9744)]])
    assert y1[0][0] > 0 and det(y1) == F(13934861,4521216) > 0
    assert y2 == mat([[F(1928079971,498464064),F(119583745,498464064)],
                      [F(119583745,498464064),-F(398298121,1993856256)]])
    assert det(y2) == -F(89099634797531,107317319122944) < 0
    assert y2[0][0] > 0 and y2[1][1] < 0
    # The strict inequalities are robust under small data perturbations.
    print('VERIFY_OK: exact_Sylvester_solves=2; positive_seed=true; '
          'strict_order=2Z-X_positive; first_iterate_positive=true; '
          'second_iterate_determinant_negative=true')


if __name__ == '__main__':
    run()
