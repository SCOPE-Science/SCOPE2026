"""Numerically check finite-threshold and asymptotic formulas for globally threshold-reset Brownian walkers.

Requires Python 3.9+ standard library only. Run: python verify_first_passage_tail.py.
All mathematical infinite-limit assertions are proved analytically in RESULT.md; numerical checks are finite corroborations.
"""
from math import erf, erfc, exp, gamma, pi, sqrt, isclose


def log_integral(func, lower=-27.0, upper=55.0, steps=16400):
    """Trapezoid quadrature for integral of f(t) dt via t=exp(y)."""
    step = (upper - lower) / steps
    value = 0.0
    for j in range(steps + 1):
        y = lower + j * step
        w = 0.5 if j in (0, steps) else 1.0
        value += w * exp(y) * func(exp(y))
    return step * value


def stationary_cycle_integral(n):
    return log_integral(lambda t: erf(1.0 / (2.0 * sqrt(t))) ** n)


def limit_coefficient(n, k, jn):
    return 4.0 ** (n / 2.0 - 1.0) * gamma(n / 2.0 - 1.0) / (pi ** (n / 2.0) * jn) * k ** (1.0 - n / 2.0)


def finite_scaled_coefficient(n, k, ratio, jn, scales=None):
    """(R/L)^(n-2) times the exact NESS joint lower-tail probability.

    Thresholds are -a_i*R for a_i in scales; default k unit scales.
    The dimensionless ratio is R/L. Integrate t=(R^2/D)u; D disappears.
    """
    if scales is None:
        scales = (1.0,) * k
    assert len(scales) == k and all(a > 0 for a in scales)
    def fn(u):
        h_product = 1.0
        for a in scales:
            lo = a / (2.0 * sqrt(u))
            hi = (a + 2.0 / ratio) / (2.0 * sqrt(u))
            h_product *= ratio * 0.5 * (erfc(lo) - erfc(hi))
        s = ratio * erf(1.0 / (2.0 * ratio * sqrt(u)))
        return h_product * s ** (n-k)
    return log_integral(fn, lower=-25.0, upper=50.0, steps=15000) / jn


def run():
    tests = 0
    for n in (3, 4, 5, 7):
        jn = stationary_cycle_integral(n)
        assert jn > 0
        tests += 1
        c1 = limit_coefficient(n, 1, jn)
        for ratio in (60., 250.):
            q1 = finite_scaled_coefficient(n, 1, ratio, jn)
            assert abs(q1 / c1 - 1.0) < 0.11
            tests += 1
            for k in (2,n):
                qk = finite_scaled_coefficient(n, k, ratio, jn)
                target = k ** (1.0 - n / 2.0)
                observed = qk / q1
                assert abs(observed / target - 1.0) < 0.003, (n,k,ratio,observed,target)
                tests += 1
        print('N=%d: J_N=%.12g C_N=%.12g; k=2 limit=%.12g' %
              (n,jn,c1,2.0 ** (1.0-n/2.0)))
    for n in (3,4,5,7):
        jn=stationary_cycle_integral(n)
        scales=(0.7,1.3)
        pred=limit_coefficient(n,1,jn)*sum(a*a for a in scales)**(1.0-n/2.0)
        got=finite_scaled_coefficient(n,len(scales),250.,jn,scales=scales)
        assert abs(got / pred-1)<0.09, (n,got,pred)
        tests+=1
    # Exact gamma-algebra consistency tests, independent of quadrature.
    for n in range(3,13):
        assert 0 < 2.0 ** (1.0-n/2.0) < 1
        assert isclose(gamma(n / 2.0), (n / 2.0 - 1.0)*gamma(n/2.0-1.0), rel_tol=1e-13)
        tests += 2
    print('PASS: %d deterministic quadrature/algebra checks' % tests)

if __name__ == '__main__':
    run()
