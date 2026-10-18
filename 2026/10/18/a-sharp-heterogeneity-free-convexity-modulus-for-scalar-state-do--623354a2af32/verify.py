#!/usr/bin/env python3
"""Standalone symbolic checks and finite tests for the stated LQR curvature identity.
This program cannot certify the universal theorem or its bibliographic originality.
Requires sympy and numpy.
"""
import math
import numpy as np
import sympy as sp

checks = 0
x, a, k, q, y = sp.symbols('x a k q y', real=True)
f = 1/(1-x*x)
fp, fpp = sp.diff(f,x), sp.diff(f,x,2)
assert sp.simplify(2*f-4*fp**2/fpp-2/(1+3*x*x)) == 0
checks += 1
assert sp.simplify(fpp-2*(1+3*x*x)/(1-x*x)**3) == 0
checks += 1
cost = (q+k*k)/(1-(a+k)**2)
a_y = y*(3+y*y)/(1+3*y*y)
k_y = y-a_y
q_y = (1-y)**4
sharp_hess = sp.factor(sp.diff(cost,k,2).subs({a:a_y,k:k_y,q:q_y}))
sharp_exp = 2/(1+3*y*y)+2*q_y*(1+3*y*y)/(1-y*y)**3
assert sp.simplify(sharp_hess-sharp_exp) == 0
checks += 1
assert sp.limit(sharp_hess,y,1,dir='-') == sp.Rational(1,2)
checks += 1

rng = np.random.default_rng(802431)
for d in range(1,8):
    for _ in range(200):
        C = rng.normal(size=(d,d))
        R = C.T@C+np.eye(d)/4
        b = rng.normal(size=d)
        v = rng.normal(size=d)
        av = rng.uniform(-2,2)
        yy = rng.uniform(-0.96,0.96)
        base = b*(yy-av)/np.dot(b,b)
        other = rng.normal(size=d)
        other -= b*(np.dot(other,b)/np.dot(b,b))
        kv = base + other
        assert abs(av+np.dot(b,kv)-yy)<3e-13
        Q = rng.uniform(1e-5,3)+kv@R@kv
        z = v@R@v
        u = kv@R@v
        h = b@v
        F = 1/(1-yy*yy)
        Fp = 2*yy/(1-yy*yy)**2
        Fpp = 2*(1+3*yy*yy)/(1-yy*yy)**3
        d2 = 2*z*F+4*u*Fp*h+Q*Fpp*h*h
        bound=2*z/(1+3*yy*yy)
        assert d2 + 5e-10*max(1,abs(d2)) >= bound
        checks += 1
        assert d2 + 5e-10*max(1,abs(d2)) >= z/2
        checks += 1
        hh=1e-4/(1+np.linalg.norm(v))
        def J(tt):
            kk=kv+tt*v
            yy2=av+b@kk
            return (Q-(kv@R@kv)+kk@R@kk)/(1-yy2*yy2)
        fd = (J(hh)-2*J(0)+J(-hh))/(hh*hh)
        assert abs(fd-d2)<0.04*max(1,abs(d2))
        checks += 1
for yy in [0.80,0.90,0.95,0.99,0.999,0.9999]:
    H=float(sharp_exp.subs(y,yy))
    assert H>0.5
    checks += 1
assert float(sharp_exp.subs(y,sp.Rational(9999,10000)))<0.502
checks+=1
print('PASS:',checks,'symbolic, exact-limit, numerical curvature, and sharpness checks')
