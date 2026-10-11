#!/usr/bin/env python3
"""Finite algebraic sanity checks for the Chazy energy/contraction theorem.

These checks do not establish the all-parameter uniqueness or convergence proof.
"""
import sympy as s

x,y,z,t,L=s.symbols('x y z t L',real=True,positive=True)
X,Y,Z=s.symbols('X Y Z', real=True)
for q in range(2,10):
    # On x=sign*u, u>0, |x|^q=u^q and |x|^q/x=sign*u^(q-1).
    for sign in (-1,1):
        u,v,w=s.symbols('u v w',real=True,positive=True)
        # Direct H definition on this half-line; physical Cartesian x = sign*u.
        xx=sign*u
        f=u**q
        aa=sign*u**(q-1)
        H=xx*w-v*v/s.Integer(2)+xx*f*v
        xd=v; yd=w; zd=-f*w-(q+1)*aa*v*v
        # d/dt u = sign*dx/dt
        Hdot=s.expand(s.diff(H,u)*sign*xd+s.diff(H,v)*yd+s.diff(H,w)*zd)
        assert Hdot==0, (q,sign,Hdot)
        div=s.diff(zd,w)
        assert div==-f
        # The anisotropic transformation preserves the time-rescaled equations:
        # xbar=L*x(L^q t), ybar=L^(q+1)*y(L^q t), etc.
        lbx=L*xx; lby=L**(q+1)*v; lbz=L**(2*q+1)*w
        Hscaled=s.expand(lbx*lbz-lby*lby/s.Integer(2)+lbx*(L**q*f)*lby)
        assert s.simplify(Hscaled-L**(2*q+2)*H)==0
        Fscaled=-L**q*f*lbz-(q+1)*(sign*L**(q-1)*u**(q-1))*lby*lby
        assert s.simplify(Fscaled-L**(3*q+1)*zd)==0
    # The amplitude exponent remains strictly positive.
    assert s.Rational(q,2*(q+1))>0
print('CHECK_OK')
