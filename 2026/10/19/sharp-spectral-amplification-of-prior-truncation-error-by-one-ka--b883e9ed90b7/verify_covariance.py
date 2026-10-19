#!/usr/bin/env python3
"""Exact identities and numerical checks for low-rank Kalman covariance updates.

Run with: python verify_covariance.py
Dependencies: Python 3, sympy, numpy.
"""
import itertools
import numpy as np
import sympy as sp

L, e, a, b = sp.symbols('L e a b', positive=True)
P = sp.diag(L, e)
Q = sp.diag(L, 0)
h = sp.Matrix([[a, b]])

def posterior_exact(M):
    return M - M*h.T * (h*M*h.T + sp.ones(1,1)).inv() * h*M

D = sp.simplify(posterior_exact(P)-posterior_exact(Q))
d = 1+L*a*a
v = sp.Matrix([[-L*a*b/d], [1]])
assert all(sp.simplify(z)==0 for z in D - e*d/(d+e*b*b)*v*v.T)
assert sp.simplify(D.det()) == 0
assert sp.simplify(sp.trace(D) - e*(d*d+L*L*a*a*b*b)/(d*(d+e*b*b))) == 0
x,y,k = sp.symbols('x y k', positive=True)
F = ((1+x)**2+k*x*y)/((1+x)*(1+x+y))
assert sp.simplify(F-1 - y*((k-1)*x-1)/((1+x)*(1+x+y))) == 0
assert sp.simplify(k-F - ((k-1)*(1+x)**2+k*y)/((1+x)*(1+x+y))) == 0

# Exact nontrivial witness; P=diag(1,1/100), h=(10,100), R=1.
W = D.subs({L:1,e:sp.Rational(1,100),a:10,b:100})
assert all(sp.denom(entry)>0 for entry in W)
assert sp.simplify(W.det()) == 0
assert sp.simplify(sp.trace(W)-sp.Rational(1010201,2030100)) == 0
assert sp.simplify(sp.trace(W)/sp.Rational(1,100)-sp.Rational(1010201,20301)) == 0
assert sp.trace(W)>sp.Rational(49,100)

# Test the n-dimensional sharp construction against all spectral truncations.
checks = 7
for n in range(2,8):
    lam = np.array([1/(i+1) for i in range(n)], dtype=float)
    Pn = np.diag(lam)
    for r in range(1,n):
        Qn = np.diag(np.r_[lam[:r],np.zeros(n-r)])
        gap = lam[r]
        def update(M, h):
            Mh=M@h
            return M-np.outer(Mh,Mh)/(1+h@Mh)
        for t in [3.0, 10.0, 50.0, 300.0]:
            h = np.zeros(n);h[0]=t;h[r]=t*t
            diff=update(Pn,h)-update(Qn,h)
            ev=np.linalg.eigvalsh(diff)
            assert ev.min() > -1e-10
            assert np.linalg.eigvalsh(Pn-diff).min()>-1e-10
            rho=np.linalg.norm(diff,2)/gap
            assert rho<=lam[0]/gap+1e-9
            checks+=3
        # High-signal, almost omitted-only measurement approaches sharp ratio.
        t=3000.0
        h=np.zeros(n);h[0]=t;h[r]=t*t
        diff=update(Pn,h)-update(Qn,h)
        assert abs(np.linalg.norm(diff,2)-lam[0])<0.002
        checks+=1
        # An aligned observation leaves the discarded coordinates untouched.
        h=np.zeros(n);h[0]=7.0
        diff=update(Pn,h)-update(Qn,h)
        assert abs(np.linalg.norm(diff,2)-gap)<1e-12
        checks+=1
        # Commuting information: diagonal sensors cannot amplify omitted spectrum.
        for scale in [0.01,0.5,3,30]:
            H=np.diag(np.linspace(0.1,1,n)*scale)
            def upd(M):
                W=H@M@H.T+np.eye(n)
                return M-M@H.T@np.linalg.solve(W,H@M)
            diff=upd(Pn)-upd(Qn)
            assert np.linalg.norm(diff,2)<=gap+1e-10
            checks+=1

print('PASS: exact rank-one formula, sharp ratio algebra, amplification threshold,')
print('rational witness, high-dimensional sharpness, and aligned measurements.')
print('assertions:', checks)
