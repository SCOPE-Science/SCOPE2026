#!/usr/bin/env python3
"""Independent numerical checks for centered radial laws of area-one regular polygons.

Run: python3 check.py
Uses only the Python standard library. Finite tests do not replace the proof.
"""
from math import pi, tan, sin, cos, acos, sqrt, log


def radii(n):
    assert isinstance(n, int) and n >= 3
    a = pi / n
    rho = 1.0 / sqrt(n * tan(a))
    radius = rho / cos(a)
    return rho, radius


def cdf(n, t):
    rho, radius = radii(n)
    if t <= 0:
        return 0.0
    if t <= rho:
        return pi * t * t
    if t >= radius:
        return 1.0
    return pi * t * t - n * (t*t*acos(rho/t) - rho*sqrt(t*t-rho*rho))


def density(n, t):
    rho, radius = radii(n)
    if 0 < t <= rho:
        return 2*pi*t
    if rho < t < radius:
        return 2*t*(pi - n*acos(rho/t))
    return 0.0


def numerical_cdf_from_polar_geometry(n, t, panels=4000):
    """Composite Simpson integration of polar sectors, not circular-cap formula."""
    rho, _ = radii(n)
    alpha = pi / n
    step = alpha / panels
    total = 0.0
    for j in range(panels + 1):
        theta = j*step
        radial_bound = rho/cos(theta)
        y = min(t*t, radial_bound*radial_bound)
        total += (1 if j in (0, panels) else 4 if j % 2 else 2)*y
    return n * (step/3) * total


def crossing(n, m):
    assert 3 <= n < m
    rho_n, _ = radii(n)
    rho_m, radius_m = radii(m)
    def h(t):
        return n*acos(rho_n/t) - m*acos(rho_m/t)
    lo, hi = rho_m, radius_m
    assert h(lo) > 0 and h(hi) < 0
    for _ in range(95):
        mid = (lo + hi) * 0.5
        if h(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def mean_radius(n):
    rho, _ = radii(n)
    a = pi/n
    sec = 1/cos(a)
    return n*rho**3*(sec*tan(a) + log(sec + tan(a)))/3


def simpson(f, left, right, panels=20000):
    step = (right-left)/panels
    acc = f(left)+f(right)
    for j in range(1, panels):
        acc += (4 if j % 2 else 2)*f(left+j*step)
    return acc*step/3


def run():
    checks = 0
    for n in range(3, 19):
        rho, rad = radii(n)
        assert 0 < rho < rad
        assert abs(cdf(n, rad)-1.0)<1e-13
        assert abs(numerical_cdf_from_polar_geometry(n, rad)-1.0)<1e-10
        checks += 3
        for f in (0.22, 0.62, 0.92, 1.04):
            t = rho*f
            a = cdf(n, t)
            b = numerical_cdf_from_polar_geometry(n, t)
            assert abs(a-b)<2e-8, (n, t, a, b)
            checks += 1
        numeric_mean = simpson(lambda x: 1-cdf(n,x), 0, rad, panels=14000)
        assert abs(numeric_mean - mean_radius(n))<1e-9
        checks += 1
    for n in range(3, 19):
        for m in range(n+1, 23):
            rho_n, R_n = radii(n)
            rho_m, R_m = radii(m)
            assert rho_n < rho_m < R_m < R_n or (rho_n < rho_m and R_m < R_n)
            t = crossing(n,m)
            assert rho_m<t<R_m
            assert abs(density(n,t)-density(m,t))<2e-12
            delta = cdf(m,t)-cdf(n,t)
            assert delta>0
            gap_simplified = m*rho_m*sqrt(t*t-rho_m*rho_m) - n*rho_n*sqrt(t*t-rho_n*rho_n)
            assert abs(delta-gap_simplified)<4e-12
            for k in range(201):
                r=R_n*k/200
                gap=cdf(m,r)-cdf(n,r)
                assert gap>-3e-13, (n,m,r,gap)
                assert gap <= delta+3e-12
                checks+=2
            w1=simpson(lambda x:cdf(m,x)-cdf(n,x),0,R_n,panels=12000)
            assert abs(w1-(mean_radius(n)-mean_radius(m)))<2e-9
            checks+=7
    print('PASS', checks, 'deterministic comparisons')
    n,m=4,6
    t=crossing(n,m)
    print('square-hexagon crossing',f'{t:.15f}')
    print('total variation = Kolmogorov distance',f'{cdf(m,t)-cdf(n,t):.15f}')
    print('one-Wasserstein distance',f'{mean_radius(n)-mean_radius(m):.15f}')


if __name__ == '__main__':
    run()
