"""Independent symbolic and numerical checks for the restricted section cusp.

Run from the extracted research directory:
    python artifacts/verify_cusp.py
Requires SymPy and mpmath (see requirements.txt).
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def test_exact_coefficients():
    t = sp.symbols('t', positive=True)
    a = sp.integrate(t**4 / (t**2 + 2)**4, (t, 0, sp.oo))
    b = sp.integrate(t**6 / (t**2 + 2)**4, (t, 0, sp.oo))
    assert sp.simplify(b - 10 * a) == 0
    i0 = sp.integrate(1 / (1 + t**2 / 2)**2, (t, 0, sp.oo))
    assert sp.simplify(i0 - sp.pi * sp.sqrt(2) / 4) == 0
    n = sp.Integer(8)
    c = 64 * (n - 1) * sp.gamma(n - sp.Rational(1, 2)) / (
        3 * sp.sqrt(sp.pi) * n**sp.Rational(3, 2)
        * sp.sqrt(n - 2) * sp.gamma(n)
    )
    assert sp.simplify(c - 1001 / (1024 * sp.sqrt(3))) == 0
    return float(c)


def direct_integral(n, s):
    half = mp.sqrt(mp.mpf('0.5'))
    r = mp.sqrt(mp.mpf(n - 2) / (2 * n))
    z = -2 * r / (n - 2)
    p = half * mp.cos(s) + r * mp.sin(s)
    q = -half * mp.cos(s) + r * mp.sin(s)
    v = z * mp.sin(s)

    def integrand(t):
        return 1 / ((1 + p*p*t*t) * (1 + q*q*t*t)
                    * (1 + v*v*t*t)**(n - 2))

    return mp.quad(integrand, [0, 1, 10, 100, 1000, mp.inf])


def test_independent_quadrature():
    mp.mp.dps = 45
    i0 = mp.pi * mp.sqrt(2) / 4
    for n in (3, 5, 7, 8, 9, 12):
        beta = mp.mpf(n - 8) / (2 * n)
        cusp = (64 * (n - 1) * mp.gamma(n - mp.mpf('0.5'))
                / (3 * mp.sqrt(mp.pi) * mp.power(n, mp.mpf('1.5'))
                   * mp.sqrt(n - 2) * mp.gamma(n)))
        assert cusp > 0
        err = []
        for raw in ('0.02', '0.01'):
            s = mp.mpf(raw)
            estimate = (direct_integral(n, s)/i0 - 1 - beta*s*s) / (s**3)
            err.append(abs(estimate - cusp))
            assert abs(estimate - cusp) < max(mp.mpf('0.09'), 8 * s * cusp)
        # The normalised cubic residual converges at roughly linear rate.
        assert err[1] < err[0]
    # The two-sided eighth-dimensional null direction raises section volume.
    for sign in (-1, 1):
        s = mp.mpf('0.01') * sign
        assert direct_integral(8, s) > i0


if __name__ == '__main__':
    assert test_exact_coefficients() > 0
    test_independent_quadrature()
    print('VERIFY_OK')
