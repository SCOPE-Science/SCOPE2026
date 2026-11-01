"""Supplementary high-precision checks for finite radial Gaussian masks.

This program illustrates, but does not prove, the all-K spectral theorem.
The infinite-family proof is the exponential-polynomial argument in RESULT.md.
"""
from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 90
D = Decimal


def endpoints(k):
    return [(D(m), D(m) + D(1) / 2)
            for m in [4, 30, 120, 350][:k]]


def f(x, bands):
    x = D(x)
    return sum(((-a + x * a.ln()).exp()
                - (-b + x * b.ln()).exp() for a, b in bands), D(0))


def mode_signs(bands, extent):
    return [(f(n + 1, bands) > 0) - (f(n + 1, bands) < 0)
            for n in range(extent)]


def eigenvalue(n, bands):
    # Exact finite-sum gamma/Poisson-CDF representation evaluated to 90 digits.
    return sum(((-a).exp() * sum((a**j / factorial(j)
                                 for j in range(n + 1)), D(0))
                - (-b).exp() * sum((b**j / factorial(j)
                                   for j in range(n + 1)), D(0))
                for a, b in bands), D(0))


def run():
    for k in (1, 2, 3, 4):
        bands = endpoints(k)
        signs = mode_signs(bands, int(bands[-1][1]) + 100)
        observed_modes = [n for n in range(1, len(signs))
                          if signs[n - 1] == 1 and signs[n] == -1]
        assert observed_modes == [4, 30, 120, 350][:k], (k, observed_modes)
        reduced = [v for v in signs if v != 0]
        variations = sum(x != y for x, y in zip(reduced, reduced[1:]))
        assert variations == 2*k - 1, (k, variations)
        for n in (0, 1, 2, 3, 4, 6, 9, 12):
            lhs = eigenvalue(n + 1, bands) - eigenvalue(n, bands)
            rhs = f(n + 1, bands) / D(factorial(n + 1))
            assert abs(lhs - rhs) < D('1e-70'), (k, n, lhs, rhs)
    print('FINITE_ILLUSTRATIONS_OK K=1..4; peaks [4,30,120,350] as selected; 32 adjacent-difference checks')


if __name__ == '__main__':
    run()
