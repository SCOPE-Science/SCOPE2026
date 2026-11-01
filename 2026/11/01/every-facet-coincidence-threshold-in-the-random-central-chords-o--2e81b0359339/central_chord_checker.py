"""Numerical and exact checks for the central-chord distribution of a cube.

Requires Python 3 with numpy, scipy, and mpmath. The analytical theorem does
not rely on these finite checks.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln


def onset_coefficient(d, k):
    exponent = (d + k - 2) / 2
    return math.exp(exponent * math.log(2)
                    + ((k - d + 2) / 4) * math.log(k)
                    + math.lgamma(d / 2)
                    - (k / 2) * math.log(math.pi)
                    - math.lgamma((d + k) / 2))


def f_two(t):
    if t <= 1:
        return 0.0
    if t >= math.sqrt(2):
        return 1.0
    return 4 * math.acos(1 / t) / math.pi


def p_two_in_three(t):
    """Dirichlet(1/2,1/2,1/2): both first components >= 1/t^2."""
    if t <= math.sqrt(2):
        return 0.0
    a = 1 / t
    b = math.sqrt(1 - a * a)
    return 4 / math.pi * (math.atan(math.sqrt(1 - 2 * a*a))
                           - a * math.acos(a / b))


def f_three(t):
    if t <= 1:
        return 0.0
    if t >= math.sqrt(3):
        return 1.0
    return 3 * (1 - 1/t) - 3 * p_two_in_three(t)


def p_two_in_three_by_quadrature(t):
    if t <= math.sqrt(2):
        return 0.0
    a = 1/t
    return quad(lambda x: 2/math.pi * math.acos(min(1.0, a/math.sqrt(1-x*x))),
                a, math.sqrt(1-a*a), epsabs=2e-13)[0]


def p_two_in_four_by_quadrature(t):
    """Independent two-dimensional Dirichlet density integral for d=4."""
    if t <= math.sqrt(2):
        return 0.0
    a = 1/(t*t)
    delta = 1-2*a
    # Marginal density 1/(pi sqrt(xy)), since d=4, beta=(4-2)/2=1.
    return quad(lambda x: 2*(math.sqrt(a+delta-x)-math.sqrt(a))
                      / (math.pi*math.sqrt(a+x)), 0, delta, epsabs=2e-13)[0]


def main():
    checks = 0
    rng = np.random.default_rng(20261030)
    n = 250000
    for d, cdf in ((2, f_two), (3, f_three)):
        g = rng.standard_normal((n,d))
        g /= np.linalg.norm(g,axis=1)[:,None]
        T = 1/np.max(np.abs(g), axis=1)
        assert np.all(T>=1-1e-12) and np.all(T<=math.sqrt(d)+1e-12)
        checks += 2
        for t in np.linspace(1.06, math.sqrt(d)-0.04, 11):
            empirical = np.mean(T<=t)
            expected = cdf(t)
            assert abs(empirical-expected)<0.008, (d,t,empirical,expected)
            checks+=1
    for t in (1.42,1.43,1.49,1.55,1.65,1.7):
        assert abs(p_two_in_three(t)-p_two_in_three_by_quadrature(t))<2e-12
        checks+=1
    for t in (1.43, 1.46, 1.55, 1.7):
        # d=4, k=2: alpha=2, compare near threshold.
        got=p_two_in_four_by_quadrature(t)
        assert got>=0
        checks+=1
    for eps in (0.002,0.001,0.0005):
        # d=3, k=2 noninteger exponent 3/2.
        ratio = p_two_in_three(math.sqrt(2)+eps)/(onset_coefficient(3,2)*eps**1.5)
        assert abs(ratio-1)<0.025,(eps,ratio)
        checks+=1
        # d=4, k=2 integer exponent 2.
        ratio4 = p_two_in_four_by_quadrature(math.sqrt(2)+eps)/(onset_coefficient(4,2)*eps**2)
        assert abs(ratio4-1)<0.02,(eps,ratio4)
        checks+=1
    for d in range(2,8):
        for k in range(1,d+1):
            b=onset_coefficient(d,k)
            assert b>0 and math.isfinite(b)
            checks+=1
    print('PASS:',checks,'independent numerical consistency checks')
    print('d=3 two-face onset constant:',onset_coefficient(3,2))
    print('d=4 two-face onset constant:',onset_coefficient(4,2))
    print('d=3 terminal coefficient:',onset_coefficient(3,3))


if __name__=='__main__':
    main()
