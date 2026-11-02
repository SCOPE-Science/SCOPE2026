#!/usr/bin/env python3
"""Exact finite-state coverage identities and rational bounds for a four-cycle."""
from collections import defaultdict
from fractions import Fraction as F
from math import exp, factorial


def intensity_coefficients(a, b):
    """Coefficients of exp(-z) in integral_0^infty exp[-J_A(t)] dt.

    J_A(t) grows with slope a on [0,1], b on [1,2], and 1 beyond 2.
    """
    d = defaultdict(F)
    if a:
        d[F(0)] += 1 / a
        d[a] -= 1 / a
    else:
        d[F(0)] += 1
    if b:
        d[a] += 1 / b
        d[a+b] -= 1 / b
    else:
        d[a] += 1
    d[a+b] += 1
    return {k:v for k,v in d.items() if v}


def expectation_coefficients(mu):
    d = defaultdict(F)
    for mask in range(1, 16):
        A = [i for i in range(4) if mask & (1 << i)]
        N = {((i + j) % 4) for i in A for j in (-1, 0, 1)}
        a = sum((mu[i] for i in A), F(0))
        b = sum((mu[i] for i in N), F(0))
        sign = (-1)**(len(A)+1)
        for exponent, coefficient in intensity_coefficients(a,b).items():
            d[exponent] += sign * coefficient
    return {k:v for k,v in d.items() if v}


def bounds_exp_minus(x):
    # For rational 0 < x <= 1, alternating-series theorem gives
    # T_13(x) < e^(-x) < T_12(x), with strictly decreasing terms.
    assert F(0) < x <= 1
    s = lambda n: sum(((-x)**k / factorial(k) for k in range(n+1)), F(0))
    lo, hi = s(13), s(12)
    assert lo < hi
    return lo, hi


def expression_interval(coeffs):
    low = high = F(0)
    for exponent, coefficient in coeffs.items():
        if exponent == 0:
            low += coefficient
            high += coefficient
        else:
            lo, hi = bounds_exp_minus(exponent)
            low += coefficient * (lo if coefficient > 0 else hi)
            high += coefficient * (hi if coefficient > 0 else lo)
    return low, high


def evaluate(coeffs):
    return sum(float(c) * exp(-float(z)) for z,c in coeffs.items())


def main():
    haar = expectation_coefficients([F(1,4)]*4)
    antipodal = expectation_coefficients([F(1,2),F(0),F(1,2),F(0)])
    expected_haar = {F(0):F(25,3), F(1,4):F(-32,3),
                     F(1,2):F(6), F(3,4):F(-4,3), F(1):F(-4,3)}
    expected_antipodal = {F(0):F(2), F(1,2):F(2), F(1):F(-2)}
    assert haar == expected_haar, (haar, expected_haar)
    assert antipodal == expected_antipodal
    diff = defaultdict(F, haar)
    for exponent, coefficient in antipodal.items():
        diff[exponent] -= coefficient
    diff = {k:v for k,v in diff.items() if v}
    assert diff == {F(0):F(19,3), F(1,4):F(-32,3), F(1,2):F(4),
                    F(3,4):F(-4,3), F(1):F(2,3)}
    lower, upper = expression_interval(diff)
    assert F(6767,100000) < lower < upper < F(677,10000), (lower, upper)
    h, a = evaluate(haar), evaluate(antipodal)
    assert abs(h - 2.5449809469642059) < 1e-13
    assert abs(a - 2.4773024370823822) < 1e-13
    assert lower < F.from_float(h-a) < upper
    print('Exhaustive 15-subset intensity expansion: PASS')
    print('Independent two-clock antipodal formula: PASS')
    print('Rational alternating-Taylor strict inequality: PASS')
    print('E_Haar =',format(h,'.15f'))
    print('E_antipodal =',format(a,'.15f'))
    print('E_Haar - E_antipodal in (',format(float(lower),'.12f'),',',format(float(upper),'.12f'),')')

if __name__ == '__main__':
    main()
