#!/usr/bin/env python3
"""Reproducible supplementary checks for flat-bias consensus results.

Finite computations are not a proof of the infinite-time assertions.
Run with: python3 verify.py
"""
from fractions import Fraction as Q
from math import exp, log, isfinite


def cubic_check():
    # Directed 4-cycle with rational normalized weights and heterogeneous coefficients.
    W = [[Q(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        W[i][(i - 1) % 4] = Q(3, 4)
        W[i][(i + 1) % 4] = Q(1, 4)
    assert all(sum(row) == 1 for row in W)
    x = [Q(0), Q(1, 1), Q(1, 3), Q(2, 3)]
    ratios = []
    for t in range(3):
        old_d = max(x) - min(x)
        assert old_d > 0
        y = []
        for i in range(4):
            # Positive, heterogeneous odd analytic receptive bias, with max ratio <=1/4.
            incr = sum((W[i][j] * Q((i+j)%3+1, 12) * (x[j]-x[i])**3
                        for j in range(4)), Q(0))
            y.append(x[i] + incr)
        assert min(x) <= min(y) <= max(y) <= max(x)
        new_d = max(y) - min(y)
        assert 0 < new_d <= old_d
        assert new_d >= (1-Q(1,2)) * old_d
        ratios.append(float(new_d / old_d))
        x = y
    return ratios


def scalar_check(alpha, steps):
    d = 1.0
    last = None
    for t in range(1, steps+1):
        old = d
        d -= 2 * exp(-d**(-alpha))
        assert 0 < d < old
        assert d / old > 1 - 2/exp(1) - 1e-12
        if t in (1,10,100,1000,steps):
            y = d**(-alpha)
            H = exp(y) / y**(1+1/alpha)
            assert isfinite(H) and H > 0
            last = (t, d, H/(2*alpha*t))
    return last


def analytic_check():
    for m in (1, 3, 5):
        d = Q(1, 2)
        a = Q(1, 4)
        for t in range(2):
            nxt = d - 2*a*d**m
            assert 0 < nxt < d
            d=nxt
        assert d > 0


if __name__ == '__main__':
    ratios = cubic_check()
    print('Exact rational, heterogeneous four-node cycle: 3 transitions checked; bounds passed.')
    for alpha, steps in ((1, 20000), (2, 2000)):
        t, d, Hratio = scalar_check(alpha, steps)
        print(f'Flat bias alpha={alpha}: {t} steps; gap={d:.9g}; H/(2 alpha t)={Hratio:.9g}')
    analytic_check()
    print('Exact rational odd analytic biases, degrees 1, 3, 5: 2 transitions each; passed.')
