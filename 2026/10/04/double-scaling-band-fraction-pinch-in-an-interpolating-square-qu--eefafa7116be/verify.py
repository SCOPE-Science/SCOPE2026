#!/usr/bin/env python3
import math


def source_band_condition(x, t, ell):
    """Equation (32), with k=x/ell."""
    k = x / ell
    s = math.sin(math.pi * t / 4.0)
    c = math.cos(math.pi * t / 4.0)
    lhs = abs(k * k * s * s - c * c)
    rhs = (k * k * s * s + c * c) * abs(math.cos(x))
    return lhs >= rhs - 2e-13


def factor_band_condition(x, t, ell):
    """Equation (34)."""
    k = x / ell
    a = 1.0 / math.tan(math.pi * t / 4.0)
    th = x / 2.0
    st = abs(math.sin(th))
    ct = abs(math.cos(th))
    if st < 1e-14 or ct < 1e-14:
        # Avoid infinities at isolated trigonometric zeros; test nearby instead.
        return source_band_condition(x, t, ell)
    p = (k * abs(math.tan(th)) - a) * (k * abs(1.0 / math.tan(th)) - a)
    return p >= -2e-12


def limit_fraction(tau, ell):
    r = 4.0 * ell / (math.pi * math.pi * tau)
    q = min(r, 1.0 / r)
    return 1.0 - 4.0 / math.pi * math.atan(q)


def finite_fraction(m, tau, ell):
    """Exact cell fraction for t=tau/m, using bisection of equation (34)."""
    t = tau / m
    A = ell / math.tan(math.pi * t / 4.0)
    M = m * math.pi

    def root(sign):
        lo = 1e-14
        hi = math.pi / 2.0

        def f(y):
            x = M + sign * y
            u = math.tan(y / 2.0)
            return (x * u - A) * (x - A * u)

        assert f(lo) < 0.0
        assert f(hi) >= 0.0
        for _ in range(120):
            mid = (lo + hi) / 2.0
            if f(mid) >= 0.0:
                hi = mid
            else:
                lo = mid
        return hi

    yl = root(-1.0)
    yr = root(+1.0)
    a = math.pi / 2.0
    num = ((M - yl) ** 2 - (M - a) ** 2
           + (M + a) ** 2 - (M + yr) ** 2)
    den = (M + a) ** 2 - (M - a) ** 2
    return num / den


def midpoint_fraction(m, tau, ell, n=60000):
    """Direct quadrature of source equation (32), independent of edge bisection."""
    t = tau / m
    M = m * math.pi
    a = math.pi / 2.0
    dx = math.pi / n
    total = 0.0
    spec = 0.0
    for j in range(n):
        x = M - a + (j + 0.5) * dx
        w = 2.0 * x * dx
        total += w
        if source_band_condition(x, t, ell):
            spec += w
    return spec / total


def collapse_scaled(m, ell):
    z = (m - 0.5) * math.pi / ell
    # arccot(z)=atan(1/z) for z>0
    tstar = 4.0 / math.pi * math.atan(1.0 / z)
    return m * tstar


def main():
    # Algebraic equivalence of source equations (32) and (34), both parities.
    for ell in (0.8, 1.0, 1.7):
        for m in (20, 21):
            for t in (0.003, 0.02, 0.17, 0.8):
                M = m * math.pi
                for y in (-1.4, -0.9, -0.25, 0.25, 0.9, 1.4):
                    x = M + y
                    assert source_band_condition(x, t, ell) == factor_band_condition(x, t, ell)

    # Double-scaling convergence on both sides and at the pinch.
    for ell in (1.0, 1.7):
        tc = 4.0 * ell / (math.pi * math.pi)
        for multiple in (0.4, 1.0, 2.5, 10.0):
            tau = multiple * tc
            got = finite_fraction(1000, tau, ell)
            target = limit_fraction(tau, ell)
            tol = 0.002 if multiple == 1.0 else 3e-6
            assert abs(got - target) < tol, (ell, multiple, got, target)

    # Direct quadrature of equation (32) agrees with bisection of equation (34).
    ell = 1.0
    tc = 4.0 * ell / (math.pi * math.pi)
    for multiple in (0.4, 2.5):
        tau = multiple * tc
        a = finite_fraction(120, tau, ell)
        b = midpoint_fraction(120, tau, ell)
        assert abs(a - b) < 8e-5, (multiple, a, b)

    # Reciprocal sides of the scaling curve agree exactly at the limit.
    assert abs(limit_fraction(0.4 * tc, ell) - limit_fraction(2.5 * tc, ell)) < 1e-14

    # The published exact finite-index collapse scale tends to the same critical constant.
    for ell in (1.0, 1.7):
        tc = 4.0 * ell / (math.pi * math.pi)
        assert abs(collapse_scaled(4000, ell) - tc) < 2e-4

    print('VERIFY_OK')


if __name__ == '__main__':
    main()
