"""Numerical checks for finite-sample hemispherical facet deficits.

Run with: python verify.py
Requires: mpmath.
The universal inequalities and strict monotonicity are proved analytically.
"""

import mpmath as mp

mp.mp.dps = 55


def omega(dim):
    return 2 * mp.pi ** (mp.mpf(dim) / 2) / mp.gamma(mp.mpf(dim) / 2)


def limit_facets(d):
    return 2 * omega(d) / omega(d + 1) * mp.pi ** d / d


def original_integral(d, n):
    a = mp.quad(lambda t: (1 - t) ** (n - d) * mp.sin(mp.pi * t) ** (d - 1), [0, 1])
    return 2 * omega(d) / omega(d + 1) * mp.binomial(n, d) * mp.pi * a


def beta_expectation(d, n):
    def sinc_pi(u):
        return mp.sin(mp.pi * u) / (mp.pi * u) if u else mp.mpf(1)

    beta = mp.beta(d, n - d + 1)
    x = mp.quad(lambda u: (u ** (d - 1) * (1 - u) ** (n - d)
                             * sinc_pi(u) ** (d - 1)), [0, 1]) / beta
    return limit_facets(d) * x


def renormalized_deficit(d, n):
    f = original_integral(d, n)
    return (n + 1) * (n + 2) / mp.mpf(d * (d + 1)) * (1 - f / limit_facets(d))


def main():
    max_delta = mp.mpf(0)
    count = 0
    for d in range(2, 10):
        lim = limit_facets(d)
        lower = mp.mpf((d + 2) * (d + 3)) / (d * (d + 1)) * (1 - (d + 1) / lim)
        upper = (d - 1) * mp.pi**2 / 6
        prev = None
        for n in range(d + 1, d + 19):
            a = original_integral(d, n)
            b = beta_expectation(d, n)
            delta = abs(a - b)
            max_delta = max(max_delta, delta)
            assert mp.almosteq(a, b, rel_eps=mp.mpf('1e-38'), abs_eps=mp.mpf('1e-38'))
            renorm = (n + 1) * (n + 2) / mp.mpf(d * (d + 1)) * (1 - a / lim)
            assert renorm + mp.mpf('1e-37') >= lower
            assert renorm < upper
            if prev is not None:
                assert renorm > prev
            if n == d + 1:
                assert mp.almosteq(a, d + 1, abs_eps=mp.mpf('1e-38'))
                assert mp.almosteq(renorm, lower, abs_eps=mp.mpf('1e-38'))
            prev = renorm
            count += 1
    # A separate pointwise diagnostic for the convexity of the sinc-sqrt kernel.
    for j in range(1, 100):
        z = mp.mpf(j) / 100
        qpp = mp.diff(lambda x: mp.sin(mp.pi * mp.sqrt(x)) / (mp.pi * mp.sqrt(x)), z, 2)
        assert qpp > 0
    print('VERIFY_OK cases=', count, 'max_absolute_formula_delta=', mp.nstr(max_delta, 8))


if __name__ == '__main__':
    main()
