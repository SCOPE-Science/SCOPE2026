#!/usr/bin/env python3
"""Independent symbolic/local and numerical checks of a two-vertex ball-hull rare-event phase transition.

Dependencies: sympy, mpmath.  This is a finite numerical/symbolic cross-check,
not a replacement for the uniform-asymptotics arguments in RESULT.md.
"""
import math
import sympy as sp
import mpmath as mp

mp.mp.dps = 45
x, t, a, b = sp.symbols('x t a b')
u = 2 * (t + sp.sin(t) * sp.cos(t)) / sp.pi
h = 4 * sp.tan(t) * (t - sp.sin(t) * sp.cos(t))
T = sp.pi * x / 4 + a * x**3 + b * x**5
err = sp.series(u.subs(t, T) - x, x, 0, 7).removeO().expand()
a0 = sp.solve(err.coeff(x, 3), a)[0]
b0 = sp.solve(err.subs(a, a0).coeff(x, 5), b)[0]
H = sp.series(h.subs(t, T.subs({a: a0, b: b0})), x, 0, 8).removeO().expand()
assert sp.simplify(H.coeff(x, 4) - sp.pi**4 / 96) == 0
assert sp.simplify(H.coeff(x, 6) - 11*sp.pi**6 / 11520) == 0
assert sp.simplify(12*H.coeff(x, 4) - sp.pi**4/8) == 0
assert sp.simplify(360*H.coeff(x, 6) - 11*sp.pi**6/32) == 0


def lens(R, ell):
    return 2*R*R*mp.asin(ell/R)-2*ell*mp.sqrt(R*R-ell*ell)


def prob(R, n):
    assert n >= 2 and R >= 1
    def integrand(theta):
        ell = mp.cos(theta)
        h_theta = theta - mp.sin(2*theta)/2
        return (16/mp.pi) * mp.sin(theta)*ell*h_theta * (lens(R, ell)/mp.pi)**(n-2)
    value = mp.quad(integrand, [0, mp.pi/128, mp.pi/16, mp.pi/2])
    return n*(n-1)*value/2


def fixed_radius_coefficient(R):
    q = lens(R, mp.mpf(1)) / mp.pi
    return (mp.pi**2/4)*mp.sqrt(2*q)*(R*R-1)**mp.mpf('1.25'), q


def critical_profile(kappa):
    f = lambda v: (16/(3*mp.pi))*v**4*mp.exp(-4/mp.pi*mp.sqrt(v*v+2*kappa))
    return mp.quad(f, [0, 2, 10, 40, 100])

checks = 4
assert abs(prob(mp.mpf(1), 2)-1) < mp.mpf('1e-35'); checks += 1
assert abs(prob(mp.mpf(1), 3)-(32/mp.pi**2-3)) < mp.mpf('1e-35'); checks += 1
assert abs(prob(mp.mpf(1), 4)-(81/(2*mp.pi**2)-4)) < mp.mpf('1e-35'); checks += 1
for n in [300, 1000, 3000]:
    scale = prob(mp.mpf(1), n) * n**3 / (mp.pi**4/8)
    assert abs(scale-1) < mp.mpf(20)/n
    checks += 1
for radius in ['1.1', '1.5', '2.0', '4.0']:
    R = mp.mpf(radius)
    coefficient, q = fixed_radius_coefficient(R)
    assert 0 < q < 1
    for n in [100, 500, 2000]:
        ratio = prob(R,n) / (coefficient * n**(-mp.mpf('0.5')) * q**n)
        assert abs(ratio-1) < mp.mpf(15)/n, (radius,n,ratio)
        checks += 1
for kap in [mp.mpf(0),mp.mpf(1),mp.mpf(10)]:
    target = critical_profile(kap)
    for n in [200, 1000]:
        scaled = n**3 * prob(1+kap/n**2, n)
        assert abs(scaled/target-1) < mp.mpf(15)/n
        checks += 1
assert abs(critical_profile(mp.mpf(0))-mp.pi**4/8) < mp.mpf('1e-35'); checks += 1
# Independent endpoint constants, using gamma integral rather than fitting.
g0 = 64*mp.sqrt(2)/(3*mp.pi)
for R in [mp.mpf('1.1'),mp.mpf('1.5'),mp.mpf(2)]:
    beta = 4/(mp.pi*mp.sqrt(R*R-1))
    C,q = fixed_radius_coefficient(R)
    alternate = g0*mp.gamma(mp.mpf('2.5'))*(q/beta)**mp.mpf('2.5')/(2*q**2)
    assert abs(C-alternate) < mp.mpf('1e-38')
    checks += 1
print('VERIFY_OK:', checks, 'symbolic identities / integral checks; fixed-radial and critical-window comparisons')
