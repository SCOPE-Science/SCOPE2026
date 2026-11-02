#!/usr/bin/env python3
"""Algebraic checks for the viscoelastic-probe Gaussian kernel and tail cost.

This is a finite symbolic consistency checker, not an infinite-distance proof.
"""
import sympy as sp

x,q,g,r,a,c = sp.symbols('x q g r a c', positive=True, finite=True)
s = sp.symbols('s', real=True)
lam = (g+1)/g
b = g/(g+1)*(1-sp.exp(-lam*a))
var = 2*a/(g+1)+g**2/(g+1)**2*(1-sp.exp(-2*lam*a))

# The stationary Lyapunov identity for the full jump-diffusion generator.
V = x**2+g*q**2
LV = ((q-x)*sp.diff(V,x)+(x-q)/g*sp.diff(V,q)
      +sp.diff(V,x,2)+sp.diff(V,q,2)/g
      +r*(V.subs(x,0)-V))
assert sp.simplify(LV-(4-2*(x-q)**2-r*x**2)) == 0

# Exact reset-free evolution of the two deterministic initial coordinates.
A = sp.Matrix([[-1,1],[1/g,-1/g]])
prop = sp.Matrix([[1+g*sp.exp(-lam*a),g*(1-sp.exp(-lam*a))],
                  [1-sp.exp(-lam*a),g+sp.exp(-lam*a)]])/(g+1)
assert sp.simplify(prop.subs(a,0)-sp.eye(2)) == sp.zeros(2)
assert sp.simplify(sp.diff(prop,a)-A*prop) == sp.zeros(2)
assert sp.simplify(prop[0,1]-b) == 0

# Itô isometry: the variance derivative is instantaneous noise variance.
kx=(1+g*sp.exp(-lam*a))/(g+1)
kq=g*(1-sp.exp(-lam*a))/(g+1)
assert sp.simplify(sp.diff(var,a)-2*(kx**2+kq**2/g)) == 0
assert sp.simplify(var.subs(a,0)) == 0

# Positive-definite quadratic control and Gaussian-age saddle cost.
Q=sp.Matrix([[2+r,-2],[-2,2]])
assert sp.simplify(Q.det()-2*r) == 0
cost=r*c+(g+1)/(4*c)
cstar=sp.sqrt((g+1)/r)/2
assert sp.simplify(sp.diff(cost,c).subs(c,cstar)) == 0
assert sp.simplify(cost.subs(c,cstar)-sp.sqrt(r*(g+1))) == 0
assert sp.simplify(sp.diff(cost,c,2)) == (g+1)/(2*c**3)

# The distinct bath-frozen comparator has bounded increasing variance.
sigma=1-sp.exp(-2*a)+(1+r)/r*(1-sp.exp(-a))**2
sigmax=(2*r+1)/r
assert sp.simplify(sp.limit(sigma,a,sp.oo)-sigmax)==0
assert sp.simplify(1/(2*sigmax)-r/(2*(2*r+1)))==0

# A handful of finite-parameter checks, not tail certification.
for gv in [sp.Rational(1,4), sp.Integer(1), sp.Integer(5), sp.Integer(30)]:
    for rv in [sp.Rational(1,3), sp.Integer(2), sp.Integer(7)]:
        assert float(cstar.subs({g:gv,r:rv})) > 0
        assert float(cost.subs({g:gv,r:rv,c:cstar.subs({g:gv,r:rv})})) > 0
        for av in [sp.Rational(1,5),sp.Integer(1),sp.Integer(4)]:
            assert float(var.subs({g:gv,a:av}))>0
            assert 0<float(b.subs({g:gv,a:av}))<1
print('PASS: exact generator, propagator, variance, saddle, quasistatic comparison; 48 finite kernel points')
