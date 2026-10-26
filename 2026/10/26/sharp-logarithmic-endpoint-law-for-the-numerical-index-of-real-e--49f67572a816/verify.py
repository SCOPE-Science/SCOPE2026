#!/usr/bin/env python3
"""Numerical checks for the logarithmic endpoint asymptotics of n(ell_p^2).

The analytic derivation, not finite checks, establishes the theorem.
Only Python's standard library is required.
"""
import math


def radius_in_y(p, y):
    assert p > 2 and 0 < y < 1
    e = 2.0 / p
    return math.exp(0.5*e*math.log(y)) * (1.0 - math.exp((1.0-e)*math.log(y))) / (1.0 + y)


def optimal_y(p):
    assert p > 2
    eta = 1 - 2 / p
    lo, hi = 0.0, 1.0
    # The strictly increasing product tanh(eta*z)*tanh(z) crosses eta once.
    # We use y=e^(-2z), so the algebraic residual is monotone decreasing.
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        residual = (2 / p) * (1 + mid**(2-2/p)) - (2-2/p) * (mid + mid**(1-2/p))
        if residual > 0:
            lo = mid
        else:
            hi = mid
    return 0.5*(lo+hi)


def expected_n(p):
    L = math.log(2*p)
    return 1-(L+1)/p + (L*L+1)/(2*p*p)


def expected_y(p):
    L = math.log(2*p)
    return 1/(2*p) + (1-L)/(2*p*p)


def main():
    print('Numerical index endpoint profile (independent scalar optimizations)')
    worst = 0.0
    for p in (3.0, 5.0, 10.0, 30.0, 100.0, 1000.0):
        y = optimal_y(p)
        value = radius_in_y(p, y)
        # Independent bounded golden-section optimization in the y-variable.
        a, b = 1.e-14, 1.0-1.e-14
        x1 = b-(b-a)*0.6180339887498948
        x2 = a+(b-a)*0.6180339887498948
        for _ in range(240):
            if radius_in_y(p,x1) < radius_in_y(p,x2):
                a = x1
            else:
                b = x2
            x1 = b-(b-a)*0.6180339887498948
            x2 = a+(b-a)*0.6180339887498948
        y_golden = (a+b)/2
        discrepancy = abs(value-radius_in_y(p,y_golden))
        worst = max(worst,discrepancy)
        assert discrepancy < 2e-11, (p, discrepancy)
        L = math.log(2*p)
        print(f'p={p:7.1f}; y={y:.12g}; n={value:.12g}; '
              f'n remainder/(log(2p)^3/p^3)={(value-expected_n(p))*p**3/L**3:.8g}; '
              f'y remainder/(log(2p)^2/p^3)={(y-expected_y(p))*p**3/L**2:.8g}')
    print('worst independent-optimization discrepancy:', worst)
    print('PASS: scalar stationarity, independent maximization, and endpoint residual profiles')

if __name__ == '__main__':
    main()
