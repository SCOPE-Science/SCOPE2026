#!/usr/bin/env python3
"""Checks finite algebraic identities and samples of a boundary-pole calculation.

The universal theorem follows from its analytic proof, not finite checks.
"""
import cmath
import math

W0 = 1j / math.sqrt(3)
q = 1 / math.sqrt(2 * math.sqrt(3))
A0 = (1 + W0) * (1 + cmath.sqrt(W0)) / (4 * cmath.sqrt(W0))
u = (1 + (1 + 1 / math.sqrt(3)) / (2 * q)) / 4
v = (2 * q + 1 - math.sqrt(3)) / (8 * q * math.sqrt(3))
assert 0.5 < q < 0.6
assert u > 9/16 and v > 0
assert abs(A0 - (u + 1j * v)) < 1e-12


def components(alpha, w):
    t = cmath.sqrt(w)
    a = (1 + w) * (1 + t) / (4 * t)
    p = (1 + 3 * w*w) / (4 * w)
    d = 1-alpha + alpha*a
    c = alpha*((1-alpha)*(a*a+1)+(2*alpha-1)*a)/d
    h = ((alpha*(1-alpha)*a*a + (2*alpha*alpha-alpha)*a
          + (1-alpha)*(alpha+p)) / (p*d))
    separate = (1-alpha)/d + c/p
    assert abs(h - separate) < 1e-7 * max(1, abs(h))
    return h, a, p, c


def im_certificate(alpha):
    c = alpha*((1-alpha)*(A0*A0+1)+(2*alpha-1)*A0)/(1-alpha+alpha*A0)
    d = (1-alpha + alpha*u)**2 + (alpha*v)**2
    rhs = alpha*(1-alpha)*v*(alpha*((u-1)**2+v*v)+2*u-1)/d
    assert abs(c.imag-rhs) < 1e-12
    assert rhs > 0

for a in (0.001, 0.01, 0.05, 0.2, 0.5, 0.8, 0.95, 0.99, 0.999):
    im_certificate(a)
    values = []
    for delta in (1e-5, 1e-7, 1e-9):
        # Re(w)>0 ensures |z(w)|<1. The imaginary line itself is boundary.
        w = delta**1.5 + 1j*(1/math.sqrt(3)-delta)
        z = (w-1)/(w+1)
        assert abs(z) < 1
        h,_,p,_ = components(a,w)
        values.append(h.real)
    assert values[2] < -1, (a,values)
for w in (0.3+0.2j, 0.8+0.1j, 1.3-0.4j):
    z = (w-1)/(w+1)
    assert abs(z)<1
    # Holomorphic differentiation formula for the square-root map.
    t=cmath.sqrt(w)
    fp=(w+1)**2/(4*t)
    dw_dz=(w+1)**2/2
    analytic_A=z*fp/(t-1)
    analytic_B=z*dw_dz*(2/(w+1)-1/(2*w))
    h,A,P,C=components(0.37,w)
    assert abs(A-analytic_A) < 1e-11
    assert abs(P-(1+analytic_B)) < 1e-11
print('PASS: pole, residue-sign, component identities, interior approach, and normalization checks')
