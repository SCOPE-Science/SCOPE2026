#!/usr/bin/env python3
"""Standalone exact-arithmetic checks for an equicorrelated Gram interval radius.

Run with Python 3; no external libraries. Finite checks supplement the proof.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import product


def positive_by_ldl(matrix):
    """Exact Schur-complement pivots for symmetric rational matrices."""
    a = [row[:] for row in matrix]
    n = len(a)
    for k in range(n):
        d = a[k][k]
        if d <= 0:
            return False
        for i in range(k + 1, n):
            for j in range(i, n):
                a[j][i] -= a[i][k] * a[j][k] / d
                a[i][j] = a[j][i]
    return True


def vertex(n, rho, u, signs):
    return [[(Fraction(1) if i == j else rho) -
             u * abs(Fraction(1) if i == j else rho) * signs[i] * signs[j]
             for j in range(n)]
            for i in range(n)]


def theoretical_threshold(n, rho):
    with localcontext() as context:
        context.prec = 65
        r = Decimal(rho.numerator) / Decimal(rho.denominator)
        if r < 0:
            return (1+(n-1)*r)/(1-(n-1)*r)
        if r == 0:
            return Decimal(1)
        p, q = n // 2, n - n // 2
        t = 1-r
        k = (r*r + t*(t+n*r)/Decimal(p*q)).sqrt()
        return (k-r)/(k+r)


def check_all():
    checks = 0
    total_vertices = 0
    for n in range(2, 8):
        for rho in (Fraction(-3, 4*(n-1)), Fraction(-1, 3*(n-1)),
                    Fraction(0), Fraction(1, 5), Fraction(2, 5), Fraction(3, 4)):
            ustar = theoretical_threshold(n, rho)
            grid = 1_000_000
            floor = int(ustar * grid)
            lo = Fraction(floor - 1, grid)
            hi = Fraction(floor + 1, grid)
            assert 0 < lo < hi < Fraction(1000002, 1000000)
            assert Decimal(lo.numerator) / Decimal(lo.denominator) < ustar
            assert Decimal(hi.numerator) / Decimal(hi.denominator) > ustar
            has_bad = False
            for bits in product((-1, 1), repeat=n-1):
                signs = (1,) + bits
                assert positive_by_ldl(vertex(n, rho, lo, signs))
                if not positive_by_ldl(vertex(n, rho, hi, signs)):
                    has_bad = True
                total_vertices += 2
            assert has_bad
            c = (1+(n-1)*rho)/(1-rho)
            if rho > 0 and n % 2 == 0:
                assert abs(theoretical_threshold(n, rho) - (
                    Decimal((1/c).numerator)/Decimal((1/c).denominator))) < Decimal('1e-26')
            elif rho > 0:
                assert ustar > Decimal((1/c).numerator)/Decimal((1/c).denominator)
            checks += 1
    print(f'PASS: {checks} independent parameter settings; '
          f'{total_vertices} exact-rational vertex LDL tests; '
          'both sides of each threshold and parity checks.')


if __name__ == '__main__':
    check_all()
