"""Standalone arithmetic and numerical cross-checks for a two-cycle theorem.

Exact proof is in RESULT.md. No third-party dependencies are required.
"""
from cmath import exp
from math import acosh, asinh, cos, isclose, pi, sin, sqrt


def base(p):
    t, s = p
    return ((2*t+s) % 5, (t+s) % 5)


pairs = []
fixed2 = [p for t in range(5) for s in range(5)
          if (p := (t, s)) == base(base(p))]
assert set(fixed2) == {(0, 0), (1, 2), (4, 3), (2, 4), (3, 1)}
assert base((1, 2)) == (4, 3) and base((4, 3)) == (1, 2)
assert base((2, 4)) == (3, 1) and base((3, 1)) == (2, 4)


def compose2(z, eps, delta):
    def f(w, d):
        return exp(2j*pi*d)*(w+eps)/(1+eps*w)
    return f(f(z, delta), -delta)


def mul(a, b):
    return ((a[0][0]*b[0][0]+a[0][1]*b[1][0],
             a[0][0]*b[0][1]+a[0][1]*b[1][1]),
            (a[1][0]*b[0][0]+a[1][1]*b[1][0],
             a[1][0]*b[0][1]+a[1][1]*b[1][1]))


def matrix(eps, delta):
    den = sqrt(1-eps*eps)
    b = ((1/den, eps/den), (eps/den, 1/den))
    def u(q):
        return ((exp(1j*pi*q), 0j), (0j, exp(-1j*pi*q)))
    return mul(mul(mul(u(-delta), b), u(delta)), b)


for eps in (0.1, 0.4, 0.7):
    for delta in (0., 0.23, .5, 1.5, 2.31):
        m = matrix(eps, delta)
        actual_halftrace = (m[0][0]+m[1][1])/2
        target_halftrace = (1+eps**2*cos(2*pi*delta))/(1-eps**2)
        assert abs(actual_halftrace-target_halftrace) < 1e-12
        chi = acosh(max(1., target_halftrace))
        closed = 2*asinh(eps*abs(cos(pi*delta))/sqrt(1-eps**2))
        assert abs(chi-closed) < 1e-7
        if abs(delta - (round(delta-.5)+.5)) < 1e-12:
            assert abs(m[0][0]-1) < 1e-12 and abs(m[1][1]-1) < 1e-12
            assert abs(m[0][1]) < 1e-12 and abs(m[1][0]) < 1e-12
        z = exp(2j*pi*0.137)
        if delta in (.5, 1.5):
            assert abs(compose2(z,eps,delta)-z) < 1e-12

s1, s2 = sin(2*pi/5), sin(4*pi/5)
phi = (1+sqrt(5))/2
assert isclose(s1/s2,phi,rel_tol=1e-14)
for k in range(5):
    mu = (k+.5)/s1
    assert abs(compose2(exp(2j*pi*.37), .4, mu*s1) - exp(2j*pi*.37)) < 1e-12
    assert abs(cos(pi*mu*s2)) > 1e-6  # sample only; irrationality proves all k

print('CHECK_OK')
