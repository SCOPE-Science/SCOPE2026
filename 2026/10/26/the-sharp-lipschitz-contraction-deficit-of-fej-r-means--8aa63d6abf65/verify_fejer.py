#!/usr/bin/env python3
"""Numerical cross-checks for the sharp periodic Fejer Lipschitz factor.

The analytic argument in RESULT.md, not this finite-grid experiment, proves
its degree-uniform assertions and asymptotic coefficient.
"""
import math

TAU = 2.0 * math.pi


def kernel_ratio(n, t):
    return (math.sin(n*t/2)/math.sin(t/2))**2 / n


def kernel_fourier(n, t):
    return 1.0 + 2.0*sum((1.0-k/n)*math.cos(k*t) for k in range(1,n))


def approximate(n, points):
    vals = [kernel_ratio(n, TAU*(j+0.5)/points) for j in range(points)]
    median = sorted(vals)[points//2]
    lam = sum(abs(x-median) for x in vals)/points
    positive_at_inverse_degree = sum(x>1.0/n for x in vals)/points
    return median, lam, positive_at_inverse_degree


def run():
    for n in [2,3,4,5,7,10,11,20]:
        for j in range(1,41):
            t = TAU*(j+0.12345)/97
            assert abs(kernel_ratio(n,t)-kernel_fourier(n,t)) < 3e-12
    print('Independent kernel formulas agree on tested points.')
    M = 65536
    reference = 4/(math.pi**2)
    for n in [2,3,4,5,7,8,11,20,50,100,200]:
        median, lam, pos = approximate(n, M)
        if n == 2:
            assert abs(lam-2/math.pi) < 2e-7
        if n == 3:
            assert abs(lam-8/(3*math.pi)) < 2e-7
        if n%2 == 1:
            assert abs(n*median-1) < 0.001
            assert abs(pos-0.5) < 1e-4
        print(f'n={n:3d}  n*median={n*median:.7f}  '
              f'L={lam:.9f}  n*(1-L)={n*(1-lam):.8f}')
    print('Predicted limiting coefficient:', f'{reference:.10f}')
    assert abs(200*(1-approximate(200, M)[1])-reference) < 0.001
    print('Finite quadrature checks passed; no infinite claim is certified by samples.')


if __name__ == '__main__':
    run()
