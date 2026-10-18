#!/usr/bin/env python3
"""Exact-rational checks for two-patch fluctuation variance.

Usage: python3 check.py
All arithmetic uses Python's standard-library fractions.Fraction.
The finite checks supplement, but do not replace, the analytical proof.
"""
from fractions import Fraction as F
from itertools import product


def solve_3x3(matrix, target):
    augmented = [[F(x) for x in row] + [F(y)]
                 for row, y in zip(matrix, target)]
    for col in range(3):
        pivot = next(i for i in range(col, 3) if augmented[i][col])
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        scale = augmented[col][col]
        augmented[col] = [x / scale for x in augmented[col]]
        for row in range(3):
            if row != col:
                multiplier = augmented[row][col]
                augmented[row] = [u - multiplier * v
                                  for u, v in zip(augmented[row], augmented[col])]
    return tuple(augmented[i][3] for i in range(3))


def variance_from_lyapunov(a, b, A, B, d):
    u, v, w = solve_3x3(
        [[2*(a+d), 0, -2*d],
         [0, 2*(b+d), -2*d],
         [-d, -d, a+b+2*d]],
        [A, B, 0],
    )
    return u + v + 2*w


def variance_formula(a, b, A, B, d):
    return ((a+b+4*d)*(A*(b+d)+B*(a+d)) /
            (2*(a+b+2*d)*(a*b+(a+b)*d)))


def ratio(a, b, d):
    u = a*a*(a+b) + 4*a*(a+b)*d + 2*(3*a+b)*d*d
    w = b*b*(a+b) + 4*b*(a+b)*d + 2*(a+3*b)*d*d
    return u/w


def derivative_numerator(a, b, A, B, d):
    u = a*a*(a+b) + 4*a*(a+b)*d + 2*(3*a+b)*d*d
    w = b*b*(a+b) + 4*b*(a+b)*d + 2*(a+3*b)*d*d
    return (b-a)*(B*u-A*w)


def main():
    count = 0
    for ai, bi, Ai, Bi, di in product((1, 2, 3, 5), (1, 2, 3, 5),
                                     (1, 2, 4), (1, 3),
                                     (0, F(1, 3), 1, 2, 5)):
        a, b, A, B, d = map(F, (ai, bi, Ai, Bi, di))
        assert variance_from_lyapunov(a, b, A, B, d) == variance_formula(a, b, A, B, d)
        # An independently evaluated difference quotient has the derivative's
        # sign except when the derivative vanishes or near an exact crossing.
        h = F(1, 1000000)
        slope = (variance_formula(a, b, A, B, d+h)-
                 variance_formula(a, b, A, B, d-h)) / (2*h) if d > h else None
        if slope is not None and derivative_numerator(a, b, A, B, d) != 0:
            pred = derivative_numerator(a, b, A, B, d)
            # The sign can disagree extremely close to a root; here integer inputs
            # and six-decimal symmetric differences avoid that situation.
            assert (slope > 0) == (pred > 0)
        count += 1
    print('Lyapunov/formula exact-rational cases:', count)

    # Sharp phase boundaries for unequal local return rates.
    for ai in (1, 2, 3, 4):
        for bi in (ai+1, ai+2, ai+4):
            a, b = F(ai), F(bi)
            lo = (a/b)**2
            hi = (3*a+b)/(a+3*b)
            assert lo < hi
            for d in (F(0), F(1, 4), F(1), F(2), F(10), F(100)):
                assert lo <= ratio(a, b, d) < hi
            assert all(ratio(a, b, x) < ratio(a, b, y)
                       for x, y in zip((F(0), F(1, 4), F(1), F(2), F(10)),
                                       (F(1, 4), F(1), F(2), F(10), F(100))))

    # A clean exact example with a unique optimum d=1.
    a, b, A, B = F(1), F(2), F(1, 2), F(1)
    assert (a/b)**2 < A/B < (3*a+b)/(a+3*b)
    assert ratio(a, b, F(1)) == A/B
    assert variance_formula(a, b, A, B, F(0)) == F(1, 2)
    assert variance_formula(a, b, A, B, F(1)) == F(49, 100)
    assert variance_formula(a, b, A, B, F(2)) == F(55, 112)
    assert (A+B)/(a+b) == F(1, 2)
    assert all(derivative_numerator(a, b, A, B, d) < 0
               for d in (F(0), F(1, 4), F(1, 2)))
    assert all(derivative_numerator(a, b, A, B, d) > 0
               for d in (F(2), F(4), F(10)))
    assert derivative_numerator(a, b, A, B, F(1)) == 0
    print('Sharp phase-boundary and exact interior-optimum checks: passed')
    print('Example: a=1,b=2,A=1/2,B=1,d*=1; V(0)=1/2, V(d*)=49/100, V(infinity)=1/2')

if __name__ == '__main__':
    main()
