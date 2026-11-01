"""Reproducible numerical smoke checks for the differential-Hilbert row energy.
The infinite-dimensional asymptotic theorem is proved analytically, not by this test.
Run: python verify.py (Python >=3.8, standard library only).
"""
import math


def beta(a, b):
    return math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a+b))


def s_half(n, subintervals=12000):
    """Simpson quadrature for S_n(-1/2), with t=1-u*u."""
    assert n >= 1 and subintervals % 2 == 0

    def f(i):
        if i == 0:
            return 2.0  # removable endpoint singularity
        if i == subintervals:
            return 0.0  # n >= 1
        u = i / subintervals
        z = u*u
        return 2.0 * ((1.0-z)**n) * (-math.log1p(-z)) / z

    a = f(0) + f(subintervals)
    a += 4.0 * sum(f(i) for i in range(1, subintervals, 2))
    a += 2.0 * sum(f(i) for i in range(2, subintervals, 2))
    return a / (3.0 * subintervals)


def row_energy_half(n, delta, s):
    out_exp = 1.5 + delta
    w = math.exp(math.lgamma(out_exp+2) + math.lgamma(n+1)
                 - math.lgamma(n+out_exp+2))
    return (n+1)**2 * w*s


def run():
    c0 = math.gamma(3.5)*math.gamma(0.5)
    assert abs(c0 - 15*math.pi/8) < 1e-12
    for n in (10, 100, 1000):
        s = s_half(n)
        lo = beta(n+1, 0.5)
        hi = lo + 0.5*beta(n, 1.5)
        assert lo-2e-10 <= s <= hi+2e-10, (n, s, lo, hi)
        q = n*row_energy_half(n, 0.0, s)/c0
        assert abs(q-1.0) < 3.0/n, (n, q)
        print('n=%d S_n=%.12g n*E_n(0)/C=%.9f beta_sandwich=PASS' % (n, s, q))
    print('CHECK_OK: exact moment bounds and critical row asymptotic numerical smoke tests')


if __name__ == '__main__':
    run()
