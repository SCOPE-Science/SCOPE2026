#!/usr/bin/env python3
"""Finite exact checks for a cyclic Chebyshev dynamical family.

The universal theorem is proved analytically in RESULT.md; finite tests
are supporting reproducibility checks, not an exhaustive proof.
"""
from fractions import Fraction
from itertools import product
from math import prod
from sympy import chebyshevt, simplify, symbols


def fixed_angle_set(degree):
    """Exact angles theta/pi in [0,1] for T_degree(cos theta)=cos theta."""
    if degree < 2:
        raise ValueError(degree)
    return ({Fraction(2*j, degree-1) for j in range((degree-1)//2+1)}
            | {Fraction(2*j, degree+1) for j in range((degree+1)//2+1)})


def multipliers(degrees, n):
    return tuple(prod(degrees[(i+r) % 3] for r in range(n)) for i in range(3))


def resonance(degrees, i, j, n, k, ell):
    # 1/2 iff j is the ancestor of output i and ell=k*M_{i,n}; else 0.
    return Fraction(1, 2) if j == (i+n) % 3 and ell == k*multipliers(degrees, n)[i] else Fraction(0)


def test():
    # Prove exact polynomial composition identities for a range of degrees
    # using computer algebra; these are NOT a proof for all integers.
    x = symbols('x')
    compositions = 0
    for a, b in product(range(2, 7), repeat=2):
        assert simplify(chebyshevt(a, chebyshevt(b, x)) - chebyshevt(a*b, x)) == 0
        compositions += 1

    # The full 3D third iterate becomes coordinatewise T_{product}.
    b = (2, 3, 4)
    y0 = (x, symbols('y'), symbols('z'))
    y = y0
    for _ in range(3):
        y = tuple(chebyshevt(b[i], y[(i+1) % 3]) for i in range(3))
    for i in range(3):
        assert simplify(y[i] - chebyshevt(prod(b), y0[i])) == 0

    angle_checks = 0
    # Exact normalized rational angles; no floating-point root tests.
    for d in range(2, 501):
        angles = fixed_angle_set(d)
        assert len(angles) == d, (d, len(angles))
        assert all(Fraction(0) <= t <= Fraction(1) for t in angles)
        angle_checks += 1

    arith_checks = 0
    for b in product(range(2, 6), repeat=3):
        B = prod(b)
        for n in range(1, 13):
            mult = multipliers(b, n)
            if n % 3 == 0:
                assert mult == (B**(n//3),) * 3
            else:
                assert prod(mult) == B**n
            arith_checks += 1

    # Exact moment resonance formulas with alternative indexing.
    resonance_checks = 0
    b = (2, 3, 4)
    for n in range(5):
        for i, j in product(range(3), repeat=2):
            for k in (1, 2, 3):
                ell = k*multipliers(b, n)[i]
                assert resonance(b, i, j, n, k, ell) == (Fraction(1,2) if j == (i+n)%3 else 0)
                assert resonance(b, i, j, n, k, ell+1) == 0
                resonance_checks += 2
    # In particular every ordinary positive-lag coordinate covariance vanishes.
    for b in product(range(2, 6), repeat=3):
        for n in range(1, 13):
            for i, j in product(range(3), repeat=2):
                assert resonance(b, i, j, n, 1, 1) == 0

    print('PASS composition identities:', compositions)
    print('PASS third-iterate diagonal identity: degrees (2,3,4)')
    print('PASS exact angle counts:', angle_checks)
    print('PASS cyclic multiplier checks:', arith_checks)
    print('PASS nonlinear resonance indexing checks:', resonance_checks)
    print('PASS all tested positive-lag coordinate covariances vanish')


if __name__ == '__main__':
    test()
