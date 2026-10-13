"""Independent numerical cross-checks for a log-Pareto curvature transition.

No numerical calculation is used as a substitute for the analytical proof.
Uses Python standard library only.
"""
import math


def q(x):
    return x - 1.0 - 1.0 / (1.0 + x) - 2.0 * math.log1p(x)


def B(x):
    return ((x + 2.0) * math.log1p(x) + 2.0) / x


def hprime(x, alpha):
    return (alpha * x / ((x + 1.0) ** 2 * (1.0 + math.log1p(x)) ** (alpha + 2.0))) * (
        (x + 2.0) * math.log1p(x) + 2.0 - alpha * x
    )


def cdf(x, alpha):
    return 1.0 - (1.0 + math.log1p(x)) ** (-alpha)


def bracketed_bisect(fn, lo, hi, n=180):
    flo, fhi = fn(lo), fn(hi)
    assert flo < 0 < fhi, (lo, hi, flo, fhi)
    for _ in range(n):
        m = (lo + hi) / 2.0
        if fn(m) < 0:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2.0


def main():
    xm = bracketed_bisect(q, 0.01, 100.0)
    y = xm + 1.0
    ac = B(xm)
    assert abs(ac - (y + 1.0 / y) / 2.0) < 1e-13
    assert abs(q(xm)) < 2e-14
    assert abs(xm - 4.635674835727276) < 1e-12
    assert abs(ac - 2.9065579375129013) < 1e-12
    for alpha in (0.01, 1.0, 2.0, ac - 0.001, ac):
        for x in (0.001, 0.1, 1.0, xm, 8.0, 30.0, 1000.0):
            assert hprime(x, alpha) >= -1e-14, (x, alpha)
    alpha = 4.0
    assert hprime(xm, alpha) < 0.0
    assert hprime(0.1, alpha) > 0.0
    assert hprime(10000.0, alpha) > 0.0
    delta = cdf(2.0, alpha) - (cdf(4.0/3.0, alpha) + cdf(4.0, alpha))/2.0
    assert 0.00216 < delta < 0.00217
    lam_bound = delta / (2.0*math.e)
    assert 0.00039 < lam_bound < 0.00041
    print(f'minimizer_x={xm:.15f}; alpha_critical={ac:.15f}')
    print(f'alpha4_explicit_delta={delta:.15f}; safe_lambda_upper={lam_bound:.15f}')
    for extra in (1e-2, 1e-3, 1e-4):
        a = ac+extra
        left=bracketed_bisect(lambda x: a-B(x), 1e-5, xm)
        right=bracketed_bisect(lambda x: B(x)-a, xm, 100.0)
        scale=y*math.sqrt(2*extra)
        assert left<xm<right
        assert abs((xm-left)/scale-1)<0.16
        assert abs((right-xm)/scale-1)<0.16
        print(f'delta={extra:g}; roots=({left:.12f}, {right:.12f}); leading_offset={scale:.12f}')
    print('PASS: numerical and exact-formula consistency checks')


if __name__ == '__main__':
    main()
