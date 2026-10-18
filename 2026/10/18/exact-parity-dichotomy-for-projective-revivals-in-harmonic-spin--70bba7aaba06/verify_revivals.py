"""Reproduce finite-dimensional matrix calculations for a parity-dependent quantum walk.

This script tests the explicit eight-dimensional reduced operator for a finite range
of odd dimensions. The all-dimension aperiodicity theorem is analytic and does not
follow from these finite tests.
"""
import cmath
import itertools
import math
from fractions import Fraction


def det_fraction(matrix):
    n = len(matrix)
    total = Fraction(0)
    for p in itertools.permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = Fraction(-1 if inv % 2 else 1)
        for i in range(n):
            term *= matrix[i][p[i]]
        total += term
    return total


def reduced_matrix(d, sign):
    m = (d - 1) // 2
    w = cmath.exp(-1j * sign * math.pi / d)
    b = [[0j] * 8 for _ in range(8)]
    b[0][1] = -w**m / d
    b[0][2] = 2 * (m + 1) * w**m / d
    b[0][3] = 2 * w**m / d
    b[1][0] = -w**(m - 1)
    b[2][4] = -w**(m + 1)
    b[3][4] = 2 * w**(m + 1) / d
    b[3][5] = w**(m + 1) / d
    b[3][6] = 2 * m * w**(m + 1) / d
    b[4][1] = 2 * m * w**m / d
    b[4][2] = w**m / d
    b[4][3] = 2 * w**m / d
    b[5][3] = -w**m
    b[6][7] = -w**(m + 2)
    b[7][4] = 2 * w**(m + 1) / d
    b[7][5] = 2 * (m + 1) * w**(m + 1) / d
    b[7][6] = -w**(m + 1) / d
    return b


def det_complex(a):
    a = [row[:] for row in a]
    n = len(a)
    det = 1+0j
    for j in range(n):
        i = max(range(j, n), key=lambda k: abs(a[k][j]))
        if i != j:
            a[j], a[i] = a[i], a[j]
            det *= -1
        v = a[j][j]
        det *= v
        if abs(v) < 1e-12:
            raise AssertionError("unexpected singular matrix")
        for k in range(j + 1, n):
            c = a[k][j] / v
            for l in range(j + 1, n):
                a[k][l] -= c * a[j][l]
    return det


def trace_square(a):
    n = len(a)
    return sum(a[i][j] * a[j][i] for i in range(n) for j in range(n))


def exact_blocks(d):
    m = (d - 1) // 2
    q = Fraction
    B1 = [[q(0),-q(1,d),q(2*(m+1),d),q(2,d)],
          [q(-1),q(0),q(0),q(0)],
          [q(0),q(2*m,d),q(1,d),q(2,d)],
          [q(0),q(0),q(0),q(-1)]]
    B2 = [[q(-1),q(0),q(0),q(0)],
          [q(2,d),q(1,d),q(2*m,d),q(0)],
          [q(0),q(0),q(0),q(-1)],
          [q(2,d),q(2*(m+1),d),-q(1,d),q(0)]]
    return B1, B2


def main():
    count = 0
    for d in range(3, 202, 2):
        B1, B2 = exact_blocks(d)
        assert det_fraction(B1) == 1
        assert det_fraction(B2) == 1
        count += 2
        for sign in (-1, 1):
            a = reduced_matrix(d, sign)
            target = (4*d-8-4*d*math.cos(2*math.pi/d))/d**2
            assert abs(trace_square(a)-target) < 3e-12
            assert abs(det_complex(a)-1) < 3e-10
            count += 2
    assert Fraction(10,9).denominator != 1
    assert Fraction(164,625).denominator != 1
    assert all(8 * (d-1) < d*d for d in range(7,202,2))
    count += 3
    print(f"PASS: {count} deterministic assertions; odd dimensions 3..201, both spin signs.")
    print("Analytic steps not certified by finite testing: all-d factorization and algebraic-integrality obstruction.")


if __name__ == '__main__':
    main()
