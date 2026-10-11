#!/usr/bin/env python3
"""Exact polynomial identity and original-time period cross-checks.

Requires Python 3 standard library only. Numeric quadrature is not used
as a proof of limiting behavior.
"""
from fractions import Fraction
from math import acos, cos, pi, sin, sqrt

NVAR = 5  # a, b, c, x, y
ZEROEXP = (0,) * NVAR

class Poly:
    def __init__(self, terms):
        self.d = {k: Fraction(v) for k, v in terms.items() if v}

    @staticmethod
    def constant(n):
        return Poly({ZEROEXP: Fraction(n)})

    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly.constant(other)
        d = self.d.copy()
        for k, v in other.d.items():
            d[k] = d.get(k, 0) + v
            if d[k] == 0:
                del d[k]
        return Poly(d)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.d.items()})

    def __sub__(self, other):
        return self + - (other if isinstance(other, Poly) else Poly.constant(other))

    def __rsub__(self, other):
        return other + -self

    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly.constant(other)
        d = {}
        for i, vi in self.d.items():
            for j, vj in other.d.items():
                k = tuple(e + f for e, f in zip(i, j))
                d[k] = d.get(k, 0) + vi * vj
        return Poly(d)

    __rmul__ = __mul__

    def __pow__(self, power):
        assert isinstance(power, int) and power >= 0
        res = Poly.constant(1)
        for _ in range(power):
            res = res * self
        return res

    def derivative(self, idx):
        d = {}
        for exp, val in self.d.items():
            if exp[idx]:
                j = list(exp)
                j[idx] -= 1
                j = tuple(j)
                d[j] = d.get(j, 0) + exp[idx] * val
        return Poly(d)

    def __eq__(self, other):
        return self.d == other.d

V = []
for i in range(NVAR):
    e = [0] * NVAR
    e[i] = 1
    V.append(Poly({tuple(e): 1}))
a, b, c, x, y = V
s = a + b
p = -4*a*b*c*x - s*y + 3*s*c*x**2 + 4*x*y
q = s*a*b*x - 4*a*b*c*y + (4*a*b*c**2 - Fraction(3, 2)*s**2 + 4*a*b)*x**2 + 8*s*c*x*y + 8*y**2
f = (y+c*x**2)**2 + x**2*(x-a)*(x-b)
k = 4*(-2*a*b*c + 3*c*s*x + 4*y)
assert f.derivative(3)*p + f.derivative(4)*q == k*f, 'Polynomial invariance identity failed'


def simpson(fun, left, right, n=32768):
    assert n % 2 == 0
    h = (right-left) / n
    out = fun(left) + fun(right)
    for i in range(1, n):
        out += (4 if i % 2 else 2) * fun(left+i*h)
    return out * h/3


def period(aa, bb, cc):
    delta = bb-aa
    ss = aa+bb
    def integrand(th):
        xx = aa + delta*(1-cos(th))/2
        rr = delta*sin(th)/2
        mm = 4*xx-ss
        return 1/(xx*(mm+4*cc*rr)) + 1/(xx*(mm-4*cc*rr))
    return simpson(integrand, 0.0, pi)


def lower_mass(aa, bb, cc, leftx, rightx):
    delta = bb-aa
    ss = aa+bb
    def integrand(th):
        xx = aa+delta*(1-cos(th))/2
        rr = delta*sin(th)/2
        mm = 4*xx-ss
        return 1/(xx*(mm-4*cc*rr))
    leftth = acos(1-2*(leftx-aa)/delta)
    rightth = acos(1-2*(rightx-aa)/delta)
    return simpson(integrand, leftth, rightth, n=16384)


def test_periods():
    aa, bb = 1.0, 2.0
    dd, ss = bb-aa, aa+bb
    hh, HH = 3*aa-bb, 3*bb-aa
    ccrit = sqrt(hh*HH)/(2*dd)
    xcrit = (6*aa*bb-aa*aa-bb*bb)/(2*ss)
    K = pi/(xcrit*sqrt(dd)*(hh*HH)**0.25)
    tzero = (2*pi/ss)*(4/sqrt(hh*HH)-1/sqrt(aa*bb))
    assert abs(period(aa,bb,0)-tzero) < 1e-9
    ts = [period(aa,bb,ccrit*p) for p in (.1,.3,.6,.9)]
    assert all(t1 < t2 for t1,t2 in zip(ts,ts[1:]))
    delta = 1e-5
    cvalue = ccrit-delta
    tvalue = period(aa,bb,cvalue)
    assert abs(sqrt(delta)*tvalue/K - 1)<0.005
    rrcrit2 = (xcrit-aa)*(bb-xcrit)
    fpp = ss/(4*rrcrit2**1.5)
    ell = sqrt(2*delta/fpp)
    mass = lower_mass(aa,bb,cvalue,xcrit-ell,xcrit+ell)/tvalue
    assert abs(mass-0.5)<0.025, ('localized mass',mass)
    print('EXACT_POLYNOMIAL_IDENTITY_OK')
    print('PERIOD_QUADRATURE_OK')
    print('MONOTONIC_SAMPLES_OK')
    print('ENDPOINT_ASYMPTOTIC_SAMPLE', f'{sqrt(delta)*tvalue:.12f}',f'{K:.12f}')
    print('SCALED_CAUCHY_UNIT_WINDOW_SAMPLE',f'{mass:.8f}', '(limiting 0.50000000)')
    print('CHECK_OK')

if __name__ == '__main__':
    test_periods()
