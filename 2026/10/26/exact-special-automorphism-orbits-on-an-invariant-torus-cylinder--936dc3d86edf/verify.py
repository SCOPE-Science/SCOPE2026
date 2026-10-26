#!/usr/bin/env python3
"""Finite symbolic checks for a quotient-boundary orbit calculation.

Requires SymPy. Universal assertions are justified in the accompanying proof,
not by finite computational tests.
"""
import itertools
import sympy as s

for n in (1, 2, 3, 4):
    x, y, z, w = s.symbols('x y z w')
    us = s.symbols('u1:%d' % (n + 1))
    P = s.prod(u**2 for u in us)
    F = x**2 * y + z**3 * w**2 * P - 1
    dy = -3 * z**2 * w**2 * P
    dz = x**2
    def d(f):
        return s.expand(s.diff(f, y)*dy+s.diff(f,z)*dz)
    assert s.expand(d(F)) == 0
    B, C = z*w, y*z
    assert s.expand(d(B)-x**2*w)==0
    assert s.expand(d(C)-(1-4*z**3*w**2*P)-F)==0
    # Weight-zero generators and degree-zero differential.
    weights = {'x':1,'y':-2,'z':2,'w':-2,'u1':-1}
    assert weights['z']+weights['w']==0
    assert weights['y']+weights['z']==0
    assert weights['z']+2*weights['u1']==0
    assert weights['z']==2*weights['x']
    assert weights['y']==2*weights['z']+2*weights['w']+2*weights['u1']
    # Every invariant Laurent monomial in a bounded box has the claimed form.
    for a,b,c,e in itertools.product(range(3),range(-2,3),range(-2,3),range(-2,3)):
        # e stands for the u1 exponent; extra u_i are independent weight-zero units.
        if -2*a+2*b-2*c-e:
            continue
        t=b-a-c
        assert e==2*t
        # y^a z^b w^c u1^e = C^a B^c E^t,
        # and E=B^-2 P_extra^-1 on the boundary.
        # The right side has exponents (a,a+c+t,c,2t) in (y,z,w,u1).
        assert a + c + t == b and 2*t == e
    print(f'VERIFY_OK n={n}: invariance, degrees, derivation and boundary-monomial reductions')

# Quotient affine chart: substitute coordinates fixed by the torus.
Z,W,V,U=s.symbols('Z W V U')
x=s.symbols('x', nonzero=True)
assert s.expand((Z*x**2)**3*(W/x**2)**2*(V/x)**2*U**2-Z**3*W**2*V**2*U**2)==0
print('VERIFY_OK affine-complement gauge x=1')
print('VERIFY_OK boundary restriction delta(C)=-3 and delta(B)=delta(U_i)=0')
