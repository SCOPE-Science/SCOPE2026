#!/usr/bin/env python3
"""Finite exact tests and independent quadrature for a Hankel commutator cusp."""
from fractions import Fraction
from math import exp, expm1, log, pi


def moment(j, kind):
    h = Fraction(1, j + 1)
    if kind == 'uniform':
        return h
    if kind == 'two_minus_t':
        return 2*h - Fraction(1, j + 2)
    if kind == 'one_plus_t':
        return h + Fraction(1, j + 2)
    if kind == 'one_minus_t':
        return h - Fraction(1, j + 2)
    raise ValueError(kind)


def finite_test(size, alpha, kind):
    ds = [Fraction(1, m**alpha) for m in range(1, size+1)]
    mat = [[(ds[m]-ds[n])*moment(m+n, kind)
            for n in range(size)] for m in range(size)]
    # The two computations below use independent symmetric and full sums.
    full = sum((entry*entry for row in mat for entry in row), Fraction(0))
    triangular = sum((2*mat[m][n]*mat[m][n]
                      for m in range(size) for n in range(m+1, size)), Fraction(0))
    assert full == triangular
    assert all(mat[m][n] == -mat[n][m] for m in range(size) for n in range(size))
    assert all(mat[m][m] == 0 for m in range(size))
    return full


def continuum(alpha, steps=10000, xmax=40.0):
    # u=exp(-t), so the integrand is smooth on the finite t interval.
    h = xmax / steps
    def f(t):
        e = exp(-t)
        return exp(-t)/(1+e)**2 * expm1(-alpha*t)**2 / alpha
    total = f(0) + f(xmax)
    for j in range(1, steps):
        total += (4 if j % 2 else 2) * f(j*h)
    return total*h/3


def main():
    exact = 0
    for kind in ('uniform', 'two_minus_t', 'one_plus_t', 'one_minus_t'):
        for alpha in (1, 2, 3):
            for size in range(2, 14):
                finite_test(size, alpha, kind)
                exact += 1
    # For the density 2-t, the exact moment difference is 1/((j+1)(j+2)).
    for j in range(50):
        assert moment(j, 'two_minus_t') - moment(j, 'uniform') == Fraction(1, (j+1)*(j+2))
        exact += 1
    vals = [continuum(a) / a for a in (0.1, 0.05, 0.01)]
    target = pi*pi/6
    assert 0 < vals[0] < vals[1] < vals[2] < target
    assert abs(vals[-1] - target) < .08
    print('PASS:', exact, 'exact rational checks; 3 continuum quadratures')
    print('continuum ratios:', ', '.join(f'{v:.9f}' for v in vals))
    print('limit:', f'{target:.9f}')


if __name__ == '__main__':
    main()
