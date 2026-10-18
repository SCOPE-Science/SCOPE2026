#!/usr/bin/env python3
"""Independent numerical spot checks for a variance-matched Student comparison.

Requires Python 3, scipy. All all-degree claims are proved analytically in RESULT.md.
"""
import math
from fractions import Fraction
from scipy.optimize import brentq
from scipy.special import gammaln
from scipy.stats import norm, t


def hermite(n, x):
    if n == 0:
        return type(x)(1)
    if n == 1:
        return x
    a, b = type(x)(1), x
    for k in range(1, n):
        a, b = b, x*b-k*a
    return b


def log_ratio(x, nu):
    epsilon = nu-2.0
    return (gammaln((nu+1)/2)-gammaln(nu/2)
            +.5*math.log(2/epsilon)+.5*x*x
            -(nu+1)/2*math.log1p(x*x/epsilon))


def crossings(nu):
    sq3 = math.sqrt(3.)
    a = brentq(lambda x: log_ratio(x, nu), 0, sq3, xtol=1e-13)
    upper = 4.
    while log_ratio(upper, nu) <= 0:
        upper *= 2.
        assert upper < 10000
    b = brentq(lambda x: log_ratio(x, nu), sq3, upper, xtol=1e-13)
    scale = math.sqrt((nu-2)/nu)
    h = lambda x: t.logsf(x/scale, nu)-norm.logsf(x)
    r = brentq(h, a, b, xtol=1e-13)
    assert 0 < a < sq3 < b and a < r < b
    assert h((a+r)/2)<0 and h((r+b)/2)>0
    assert log_ratio(0, nu)>0 and log_ratio(sq3, nu)<0
    return a, r, b


def main():
    points = [Fraction(-7, 3), Fraction(-2), Fraction(-1, 2),
              Fraction(0), Fraction(3, 5), Fraction(3, 2),
              Fraction(11, 4)]
    for z in points:
        lhs = z**8/32-Fraction(13,24)*z**6+Fraction(41,16)*z**4-Fraction(33,8)*z**2+Fraction(41,32)
        rhs = hermite(4,z)+hermite(6,z)/3+hermite(8,z)/32
        assert lhs == rhs
    trials = [2.000001, 2.0001, 2.001, 2.01, 2.1,
              2.5, 3.0, 5.0, 10.0, 30.0, 100.0, 1000.0]
    for nu in trials:
        a, r, b = crossings(nu)
        print('nu={:.6g}: a={:.8g}, R={:.8g}, b={:.8g}'.format(nu,a,r,b))
    small_nu=2.000001
    _, r, _=crossings(small_nu)
    H=math.log(1/(small_nu-2))
    boundary_approx=2*H+math.log(2*H)+math.log(8/math.pi)
    assert abs(r*r-boundary_approx)<0.15
    large_nu=1000.
    _, r, _=crossings(large_nu)
    assert abs(r-math.sqrt(3)-1/(math.sqrt(3)*large_nu))<5e-6
    print('PASS: exact Hermite polynomial checks, finite crossings, endpoint consistency.')


if __name__ == '__main__':
    main()
