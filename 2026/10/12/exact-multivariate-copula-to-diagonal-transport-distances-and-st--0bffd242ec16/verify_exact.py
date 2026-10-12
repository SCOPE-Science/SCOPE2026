#!/usr/bin/env python3
"""Exact finite checks for the natural multivariate copula metric benchmark.

Only Python standard library is needed. Finite checks corroborate, not prove,
the all-dimensional theorem, uniqueness, or large-dimensional expansion.
"""
from fractions import Fraction as F
from math import comb, factorial


def distance_by_irwin_hall(d):
    assert d >= 1
    term = sum((-1)**k*comb(2*d, k)*(d-k)**(2*d+1)
               for k in range(d+1))
    return F(d, 6) - F(term, factorial(2*d+1))


def distance_by_independent_polynomial_integration(d):
    """Integrate E[S F_d(S)] by expanding f_d and F_d on integer cells."""
    total = F(0)
    for m in range(d):
        for j in range(m+1):
            for k in range(m+1):
                sign = (-1)**(j+k)*comb(d, j)*comb(d, k)
                if not sign:
                    continue
                partial = F(0)
                for a in range(d):
                    x = comb(d-1, a)*(m-j)**(d-1-a)
                    for b in range(d+1):
                        y = comb(d, b)*(m-k)**(d-b)
                        partial += x*y*(F(m, a+b+1)+F(1, a+b+2))
                total += sign*partial
    esf = total / (factorial(d)*factorial(d-1))
    return F(2*d, 3) - 2*esf


def main():
    for d in range(1, 9):
        a = distance_by_irwin_hall(d)
        b = distance_by_independent_polynomial_integration(d)
        assert a == b, (d, a, b)
    vals = [distance_by_irwin_hall(d) for d in range(1, 13)]
    assert vals[0] == 0
    assert vals[1] == F(1, 10)
    assert vals[2] == F(181, 840)
    assert all(vals[i+1]>vals[i] for i in range(len(vals)-1))
    assert all(vals[i+2]-2*vals[i+1]+vals[i]>0 for i in range(len(vals)-2))
    print('VERIFY_OK exact double-derivation dimensions 1..8; monotone/convex checks 1..12')

if __name__ == '__main__':
    main()
