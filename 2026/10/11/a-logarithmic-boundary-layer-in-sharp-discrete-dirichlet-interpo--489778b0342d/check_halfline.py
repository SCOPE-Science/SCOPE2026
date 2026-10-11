"""Numerical corroboration of exact boundary point-evaluation interpolation constants.
Run with Python 3 and the standard scientific packages scipy, numpy, sympy.
"""
import math
from scipy.optimize import brentq
import numpy as np
import sympy as sp

def rho_at(m):
    assert m >= 1
    def f(r):
        return (1.0-r)*(-math.expm1(2*m*math.log(r)))-4*m*(r**(2*m))*(1.0+r)
    return brentq(f,0.01, 1.0-1e-13,xtol=1e-14,rtol=1e-14)

def K(m, r):
    return (2*math.sqrt(r)/(1+r))*(-math.expm1(2*m*math.log(r)))

def extremizer(m,r,jmax):
    idx=np.arange(1,jmax+1, dtype=np.float64)
    return np.power(r,np.abs(idx-m))-np.power(r,idx+m)

def ratio(u,m):
    l2 = np.linalg.norm(u)
    gradient = np.diff(np.r_[0.0,u,0.0])
    return u[m-1]**2/(l2*np.linalg.norm(gradient))

r=sp.symbols('r',positive=True)
f1=2*sp.sqrt(r)*(1-r)
assert sp.simplify(sp.diff(f1,r).subs(r,sp.Rational(1,3)))==0
assert sp.simplify(f1.subs(r,sp.Rational(1,3))-4/(3*sp.sqrt(3)))==0
checks=2
rng=np.random.default_rng(307)
for m in [1,2,3,4,5,8,12,20,30,50]:
    root=rho_at(m);val=K(m,root)
    assert 0 < root < 1 and 0 < val < 1
    if m>1:assert val>K(m-1,rho_at(m-1))
    J=max(800,m+800)
    u=extremizer(m,root,J)
    approx=ratio(u,m)
    assert abs(val-approx)<1e-8,(m,val,approx)
    checks+=4
    print(f'm={m:4d} r={root:.12f} K={val:.12f} attained-ratio={approx:.12f}')
for m in [1,2,3,5,10,20]:
    val=K(m,rho_at(m))
    for k in range(160):
        u=rng.normal(size=160)
        x=ratio(u,m)
        assert x<=val+1e-12, (m,k,x,val)
        checks+=1
for m in [100,500,1000,5000,10000]:
    root=rho_at(m);val=K(m,root)
    c=(1-val)*m*m/(math.log(m)**2)
    print(f'asympt m={m:5d} K={val:.14f} normalized={c:.10f}')
    assert c>0.02 and c<0.22
    checks+=1
print(f'PASS {checks} checks')
