"""Exact and numerical checks for a PolyCDwA simplex local-spectrum theorem.

Requires sympy and numpy. This checks finite sizes and local differentiability;
the all-dimensional spectral and asymptotic assertions are proved analytically.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp


def differential_sweep(n):
    eye=sp.eye(n)
    one=sp.ones(n,1)
    u=one/n
    t=eye
    for j in range(n):
        w=eye[:,j]-u
        p=eye-sp.Rational(n,n-1)*(w*w.T)
        t=p*t
    basis=eye[:,:n-1]-eye[:,n-1]*sp.ones(1,n-1)
    return sp.simplify((t*basis)[:n-1,:])


def poly(n,z):
    return sp.cancel(((1+(n-1)*z)**n-n**n*z**(n-1))/(z-1)**2)

z=sp.Symbol('z')
for n in range(3,9):
    t=differential_sweep(n)
    p=sp.Poly(poly(n,z),z)
    assert sp.expand(t.charpoly(z).as_expr()-z*p.as_expr()/(n-1)**n)==0
    assert p.degree()==n-2
    assert p.eval(1)!=0 and p.eval(0)!=0

assert sp.factor(poly(3,z))==8*z+1
assert sp.factor(poly(4,z))==81*z*z+14*z+1


def actual_sweep(x):
    x=np.array(x,dtype=float)
    n=x.size
    u=np.ones(n)/n
    for j in range(n):
        d=np.eye(n)[j]-x
        a=-np.dot(x-u,d)/np.dot(d,d)
        assert -x[j]/(1-x[j]) < a < 1
        x=x+a*d
    return x

rng=np.random.default_rng(314159)
for n in range(3,10):
    t=np.array(differential_sweep(n),dtype=float)
    u=np.ones(n)/n
    for _ in range(10):
        raw=rng.normal(size=n);raw-=raw.mean();raw/=np.linalg.norm(raw)
        h=1e-5
        f=actual_sweep(u+h*raw)-u
        jac=t@raw[:n-1]
        assert np.linalg.norm(f[:n-1]/h-jac) < 1e-3

for n in (3,4,6,10,20,40):
    eye=np.eye(n)
    u=np.ones(n)/n
    t=eye-np.ones((n,n))/n
    for j in range(n):
        w=eye[:,j]-u
        t=(eye-n/(n-1)*np.outer(w,w))@t
    ev=np.linalg.eigvals(t)
    if n==3: assert np.isclose(max(abs(ev)),1/8,atol=1e-9)
    if n==4: assert np.isclose(max(abs(ev)),1/9,atol=1e-9)
    print('n',n,'rho',round(float(max(abs(ev))),12))
print('VERIFY_OK exact characteristic polynomials n=3..8 and 70 nonlinear differential checks')
