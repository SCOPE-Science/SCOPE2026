"""Independent analytic/numerical checks for the seventh-order planar distance law.

Requires Python 3, scipy, numpy and sympy. It checks an affine-disk identity
for ellipses and compares a curvature-radius family to exact beta integrals.
These finite checks support but do not prove the general asymptotic theorem.
"""
import math
import numpy as np
from scipy.integrate import quad
from sympy import Symbol, acos, pi, sqrt, integrate, series, simplify


def integrate_circle(f):
    return quad(f, 0.0, 2 * math.pi, epsabs=2e-11,
                epsrel=2e-11, limit=400)[0]


def ellipse_curvature_invariants(a, b):
    def speed(theta):
        return math.hypot(a * math.sin(theta), b * math.cos(theta))

    def curvature(theta):
        return a * b / speed(theta) ** 3

    def curvature_derivative_arclength(theta):
        sn = math.sin(theta)
        cs = math.cos(theta)
        return (-3 * a * b * (a*a - b*b) * sn * cs /
                speed(theta) ** 6)

    i4 = integrate_circle(lambda theta: curvature(theta) ** 4 * speed(theta))
    igrad = integrate_circle(lambda theta: curvature_derivative_arclength(theta) ** 2 * speed(theta))
    return i4, igrad


def check_ellipses():
    for a, b in [(1.0, 1.0), (2.0, 1.0), (3.0, 2.0), (1.5, 0.7)]:
        i4, igrad = ellipse_curvature_invariants(a, b)
        # The t^5 coefficient integrated over directions, obtained by
        # fifth-order expansion of the exact affine disk covariogram.
        direct = a*b*integrate_circle(
            lambda phi: (math.cos(phi)**2/a**2 +
                         math.sin(phi)**2/b**2)**2.5 / 320.0)
        curvature = i4/320.0 - igrad/360.0
        assert math.isclose(direct, curvature, rel_tol=2e-10, abs_tol=1e-12)
        print(f'ELLIPSE_AFFINE_DISK_FIFTH_ORDER_OK a={a:g} b={b:g}')


def check_disk():
    r = Symbol('r', positive=True)
    # Unit disk covariogram at separation r.
    g = 2 * acos(r/2) - r/2 * sqrt(4 - r*r)
    # F(r) = (2 pi)/(pi^2) integral_0^r t*g(t) dt.
    f = simplify(integrate(2*r*g/pi, r))
    # Compare derivatives of the antiderivative through order seven.
    trunc = series(f, r, 0, 9).removeO()
    target = r**2 - 4*r**3/(3*pi) + r**5/(30*pi) + r**7/(1120*pi)
    assert simplify(trunc-target) == 0
    print('EXACT_DISK_CDF_SEVENTH_ORDER_OK')


def check_radius_family():
    a = 0.5
    for m in [2, 3, 4]:
        def rho(theta):
            return 1 + a * math.cos(m * theta)

        i4 = integrate_circle(lambda t: rho(t)**(-3))
        igrad = integrate_circle(lambda t: a*a*m*m*math.sin(m*t)**2 /
                                rho(t)**5)
        expected_i4 = math.pi * (2 + a*a)/(1-a*a)**2.5
        expected_igrad = (math.pi*a*a*m*m*(4+a*a) /
                          (4*(1-a*a)**3.5))
        assert math.isclose(i4, expected_i4, rel_tol=2e-10)
        assert math.isclose(igrad, expected_igrad, rel_tol=2e-10)
        c7 = i4 / 2240 - igrad / 2520
        assert (c7 > 0) if m == 2 else (c7 < 0)
        print(f'CURVATURE_RADIUS_SHARP_SIGN_OK m={m} sign={"positive" if c7>0 else "negative"}')


if __name__ == '__main__':
    check_disk()
    check_ellipses()
    check_radius_family()
    print('ALL_SEVENTH_ORDER_COVARIOGRAM_CHECKS_OK')
