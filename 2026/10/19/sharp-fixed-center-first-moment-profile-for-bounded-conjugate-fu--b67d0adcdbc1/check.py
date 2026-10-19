#!/usr/bin/env python3
"""High-precision independent formula and conformal-boundary cross-checks."""
import mpmath as mp

mp.mp.dps = 55


def profile(x, y):
    z = mp.exp(-mp.pi*x/2 + 1j*mp.pi*y/2)
    return 1 - 4/mp.pi**2 * mp.re(mp.polylog(2, z) - mp.polylog(2, -z))


def boundary_average(x, y):
    h0 = mp.sinh(mp.pi*(x + 1j*y)/2)
    a, b = mp.re(h0), mp.im(h0)
    assert a > 0
    left, zero, right = (-1-b)/a, -b/a, (1-b)/a
    def density(s):
        v = min(mp.mpf(1), abs(a*s+b))
        return (2/mp.pi)*mp.asin(v)/(mp.pi*(1+s*s))
    return mp.quad(density, [-mp.inf, left, zero, right, mp.inf])


def derivative(x, y):
    return mp.log((mp.cosh(mp.pi*x/2)+mp.cos(mp.pi*y/2)) /
                  (mp.cosh(mp.pi*x/2)-mp.cos(mp.pi*y/2)))/mp.pi


def corner(x, y):
    correction = (abs(y)*mp.atan(x/abs(y))) if y else mp.mpf(0)
    return abs(y) + 2/mp.pi * (x*(1+mp.log(4/(mp.pi*mp.sqrt(x*x+y*y))))-correction)


for xs in ('0.02','0.1','0.5','1','3'):
    for ys in ('0','0.2','-0.7'):
        x, y = mp.mpf(xs), mp.mpf(ys)
        actual, independent = profile(x,y), boundary_average(x,y)
        assert abs(actual-independent) < mp.mpf('2e-12'), (x,y,actual,independent)
        assert abs(mp.diff(lambda z: profile(z,y),x)-derivative(x,y)) < mp.mpf('1e-45')
        assert abs(mp.im(mp.sinh(mp.pi*(x+1j*y)/2))) < mp.inf
        assert abs(y) < actual < 1
for xs,ys in [('0.01','0'),('0.01','0.01'),('0.002','0.003')]:
    x, y = mp.mpf(xs), mp.mpf(ys)
    assert abs(profile(x,y)-corner(x,y)) < mp.mpf('0.2')*x*(x*x+y*y)
print('PASS: profile, conformal-boundary integral, derivative and corner checks')
