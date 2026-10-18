#!/usr/bin/env python3
"""Exact polynomial identities and auxiliary quadrature for a planar Gaussian thin-box formula.
Standard library only; symbolic checks prove the indicated polynomial identities.
Finite quadrature illustrates convergence but is not used as a universal proof.
"""
from fractions import Fraction
from math import exp, sin, cos, asin, sqrt

N = 7
Z = (0,) * N

class Poly:
    def __init__(self, terms=None):
        self.d = {k: v for k, v in (terms or {}).items() if v}
    @staticmethod
    def const(a):
        if isinstance(a, Poly):
            return a
        return Poly({Z: a})
    @staticmethod
    def var(i):
        k = list(Z); k[i] = 1
        return Poly({tuple(k): 1})
    def __add__(self, rhs):
        rhs = Poly.const(rhs)
        out = dict(self.d)
        for k, v in rhs.d.items(): out[k] = out.get(k, 0) + v
        return Poly(out)
    __radd__ = __add__
    def __neg__(self):
        return Poly({k: -v for k, v in self.d.items()})
    def __sub__(self, rhs):
        return self + (-Poly.const(rhs))
    def __rsub__(self, lhs):
        return Poly.const(lhs) - self
    def __mul__(self, rhs):
        rhs = Poly.const(rhs)
        out = {}
        for k, v in self.d.items():
            for j, w in rhs.d.items():
                m = tuple(k[t] + j[t] for t in range(N))
                out[m] = out.get(m, 0) + v * w
        return Poly(out)
    __rmul__ = __mul__
    def __pow__(self, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        value = Poly.const(1)
        for _ in range(exponent): value = value * self
        return value
    def __eq__(self, rhs):
        return self.d == Poly.const(rhs).d

p, q, c, a, b, x, y = [Poly.var(i) for i in range(N)]
alpha = p*x*x + 2*c*x*y + q*y*y
beta = a*p*x*x + (a+b)*c*x*y + b*q*y*y
gamma = 2*a*a*p*x*x + (a+b)**2*c*x*y + 2*b*b*q*y*y
factor = (a-b)**2*x*y*(c*p*x*x + c*q*y*y + 2*p*q*x*y)
assert alpha*gamma - 2*beta**2 == factor, 'quartic directional factorization'

r, w = Poly.var(0), Poly.var(1)
assert 4*(1-r*r)*w*(r+w) + r*r*(1+r*w)**2 == ((2-r*r)*w+r)**2, 'sharp square identity'

# Exact rational illustration corresponding to the initiating paper's 2D example.
P = Q = Fraction(1)
C = Fraction(-1, 2)
lam1, lam2 = Fraction(1), Fraction(-1)
comm_sq = 2*(lam1-lam2)**2*C*C
sharp = comm_sq/(16*(P*Q-C*C))
assert sharp == Fraction(1, 6)
rho = C / Fraction(1)
w_star = -rho/(2-rho*rho)
assert w_star == Fraction(2, 7)

# Independent, finite-width numerical quadrature illustrates the proved limit.
theta = 0.5*asin(float(w_star))
u = (cos(theta), sin(theta))
v = (-u[1], u[0])
def observed_curvature(epsilon):
    # Midpoint quadrature of the normalized truncated Gaussian moments.
    nx, nz, cutoff = 1600, 60, 10.0
    step_x, step_z = 2*cutoff/nx, 2*epsilon/nz
    total = m1 = m2 = mg = 0.0
    for i in range(nx):
        t = -cutoff + (i+.5)*step_x
        for j in range(nz):
            z = -epsilon + (j+.5)*step_z
            xx, yy = t*u[0] + z*v[0], t*u[1] + z*v[1]
            # S=[[1,-.5],[-.5,1]], A=diag(1,-1).
            density = exp(-.5*(xx*xx-xx*yy+yy*yy))
            B = xx*xx - yy*yy
            G = 2*(xx*xx+yy*yy)
            total += density
            m1 += density*B
            m2 += density*B*B
            mg += density*G
    return m2/total - (m1/total)**2 - mg/total

values = [observed_curvature(eps) for eps in (0.2, 0.1, 0.05)]
assert values[0] < values[1] < values[2] < float(sharp)
assert abs(values[2] - float(sharp)) < .004
print('PLANAR_GAUSSIAN_THIN_BOX_EXACT_IDENTITIES_OK')
print('test-case exact maximum:', sharp, 'optimal sine:', w_star)
print('auxiliary finite-width curvatures:', values)
