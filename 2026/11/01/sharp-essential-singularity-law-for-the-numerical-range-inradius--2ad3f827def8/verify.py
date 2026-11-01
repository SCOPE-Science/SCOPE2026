#!/usr/bin/env python3
"""Geometric finite checks for the numerical-range triangle bounds.

Only standard-library arithmetic is used. Finite checks support, not certify,
limiting estimates proved analytically in RESULT.md.
"""
from math import atan, ceil, cos, dist, exp, log, pi, sin, sqrt


def check(sigma: float, t: float) -> None:
    a = sigma / t
    v = atan(1 / a)
    u_plus = pi + v
    u_minus = pi / 2
    n_q = ceil(exp(u_minus / t))
    n_r = ceil(exp(u_plus / t))
    u_q = t * log(n_q)
    u_r = t * log(n_r)
    q = (exp(-a*u_q)*cos(u_q), -exp(-a*u_q)*sin(u_q))
    r = (exp(-a*u_r)*cos(u_r), -exp(-a*u_r)*sin(u_r))
    p = (1., 0.)
    m = exp(-a*u_plus)/sqrt(1+a*a)
    assert q[0] < 0 and q[1] < 0 and r[0] < 0 and r[1] > 0
    assert n_q >= 2 and n_r > n_q
    cross = lambda x, y: x[0]*y[1]-x[1]*y[0]
    vertices = [p, q, r]
    ds = [abs(cross(vertices[i], vertices[(i+1) % 3])) / dist(vertices[i], vertices[(i+1) % 3]) for i in range(3)]
    assert all(d > 0 for d in ds)
    # A triangle in the actual numerical range gives the rigorous finite lower bound.
    # The imaginary-coordinate spiral maximum is a rigorous universal upper bound.
    assert min(ds) <= m * (1+1e-9)
    assert min(ds)/m > 0.98, (sigma, t, ds, m)
    # The continuous spiral maximum must reproduce its defining trigonometric value.
    assert abs(-exp(-a*u_plus)*sin(u_plus)-m) <= 1e-11*m
    # Numerical logarithmic mesh lies on or just after the specified angle.
    assert u_q >= u_minus-1e-13 and u_r >= u_plus-1e-13
    assert u_q-u_minus < t*exp(-u_minus/t)+1e-11
    assert u_r-u_plus < t*exp(-u_plus/t)+1e-11


def main() -> None:
    cases=[(1.,0.9),(1.,0.5),(1.,0.2),(1.,0.1),(2.,0.1),(.25,.1)]
    for sigma,t in cases:
        check(sigma,t)
    print('PASS: 6 actual spectral triangles; geometric inradius versus spiral upper bound')

if __name__ == '__main__':
    main()
