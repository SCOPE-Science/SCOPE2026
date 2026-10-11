#!/usr/bin/env python3
"""Exact rational checks of the spectral polynomial for inverse 4-site shifts.

The all-positive-exponent rearrangement theorem is proved analytically; these
finite calculations are regression checks, not proof of a continuum claim.
"""
from fractions import Fraction
from itertools import product


def multiplication(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def coeffs(a, b, c):
    zero, one = Fraction(0), Fraction(1)
    R = [[zero for j in range(4)] for i in range(4)]
    for i in range(4):
        R[i][i] = one
    R[0][1] = a
    R[1][2] = b
    R[2][3] = c
    R[0][2] = a * b
    R[1][3] = b * c
    R[0][3] = a * b * c
    Rt = [[R[j][i] for j in range(4)] for i in range(4)]
    M = multiplication(Rt, R)
    p = []
    V = M
    for k in range(1, 5):
        p.append(trace(V))
        V = multiplication(V, M)
    e = [one]
    for k in range(1, 5):
        e.append(sum((-1)**(i - 1) * e[k - i] * p[i - 1]
                     for i in range(1, k + 1)) / k)
    return e[1:]


def predicted(a, b, c):
    x, y, z = a*a, b*b, c*c
    S = x + y + z
    return [4 + S + y * (x + z) + x * y * z,
            6 + 2*S + x*y + x*z + y*z,
            4 + S, Fraction(1)]


def main():
    values = [Fraction(1, 5), Fraction(1, 2), Fraction(1),
              Fraction(3, 2), Fraction(2), Fraction(4)]
    checked = 0
    for a, b, c in product(values, repeat=3):
        assert coeffs(a, b, c) == predicted(a, b, c)
        for middle, rest in ((a, (b,c)), (b, (a,c)), (c, (a,b))):
            e1,e2,e3,e4 = coeffs(rest[0], middle, rest[1])
            S = a*a + b*b + c*c
            assert e2 == 6 + 2*S + (a*b)**2 + (a*c)**2 + (b*c)**2
            assert e3 == 4 + S and e4 == 1
        # Central-coordinate ordering of the only variable coefficient.
        tuples = []
        for middle, u, v in ((a,b,c),(b,a,c),(c,a,b)):
            tuples.append((middle*middle, predicted(u,middle,v)[0]))
        tuples.sort()
        assert all(tuples[k][1] <= tuples[k+1][1] for k in range(2))
        assert all((tuples[k][0] == tuples[k+1][0]) ==
                   (tuples[k][1] == tuples[k+1][1]) for k in range(2))
        checked += 1
    print('WEIGHTED_SHIFT_SCHATTEN_REARRANGEMENT_EXACT_OK', checked)


if __name__ == '__main__':
    main()
