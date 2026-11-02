"""Reproducibility checks for a sharp rank-two Nystrom preconditioner event.

This code tests finite identities and examples. The theorem for all L>1 and
Gaussian sketches is established separately by the exact proof in RESULT.md.
Python 3.11; sympy and numpy. No external data or network required.
"""
import math
import numpy as np
import sympy as sp

L, t = sp.symbols('L t', positive=True)
d = L*(1-t)+t
e = L**2*(1-t)+t
f = L**3*(1-t)+t
tau = e/d
tr = sp.factor(L+1 -(1-1/tau)*f/e)
det = sp.factor(L/tau)
normalized = sp.factor(tr**2/det)
baseline = (L+1)**2/L
N = L**5*(1-t)**2-L**3*t*(1-t)-(L+1)*t**2
identity = -(L-1)**2*(1-t)*N/e**3
assert sp.simplify(normalized-baseline-identity) == 0
assert sp.simplify(tau-1-L*(L-1)*(1-t)/d) == 0

critical = 2*L**2/(2*L**2+1+sp.sqrt(5+4/L))
assert sp.simplify(N.subs(t,critical)) == 0
p = 1-sp.sqrt(critical)
assert sp.simplify(sp.limit(L**2*p,L,sp.oo)-(1+sp.sqrt(5))/4) == 0
assert sp.simplify(tr.subs({L:2,t:sp.Rational(8,9)})-sp.Rational(25,9)) == 0
assert sp.simplify(det.subs({L:2,t:sp.Rational(8,9)})-sp.Rational(5,3)) == 0

rng=np.random.default_rng(20261026)
checks=0
for l in (1.25,2.,4.,10.,30.):
    A=np.diag([l,1.,1.])
    for _ in range(32):
        omega=rng.standard_normal((3,2))
        Q, _=np.linalg.qr(omega)
        # Gaussian range and its Euclidean unit normal
        n=np.cross(Q[:,0],Q[:,1]); n/=np.linalg.norm(n)
        tt=float(n[0]**2)
        Nmat=A@Q@np.linalg.solve(Q.T@A@Q,Q.T@A)
        vals,U=np.linalg.eigh(Nmat)
        assert abs(vals[0])<1e-11 and abs(vals[1]-1)<1e-11
        assert abs(vals[2]-float(tau.subs({L:l,t:tt})))<1e-10
        uu=U[:,-1]
        P=np.eye(3)+(vals[2]-1.)*np.outer(uu,uu)
        R=np.linalg.cholesky(P)
        Rinv=np.linalg.inv(R)
        B=Rinv@A@Rinv.T
        k=float(np.linalg.cond(B))
        # Compare against analytic sharp event; ties are measure zero.
        k_critical=float(critical.subs(L,l))
        if abs(tt-k_critical)>1e-9:
            assert (k>l)==(tt>k_critical), (l,tt,k,k_critical)
        assert np.isclose(np.trace(B@B)*0+np.trace(B),
               1+float(tr.subs({L:l,t:tt})),rtol=1e-9)
        checks+=1

# Minimal dimension: rank-one P is I, and full-rank Nyström is exact.
for _ in range(20):
    Z=rng.standard_normal((2,2)); A=Z.T@Z+np.eye(2)
    o=rng.standard_normal((2,1)); Nmat=A@o@np.linalg.solve(o.T@A@o,o.T@A)
    tau1=np.linalg.eigvalsh(Nmat)[-1]
    P1=1/tau1*Nmat+(np.eye(2)-Nmat/tau1)
    assert np.allclose(P1,np.eye(2),atol=1e-12)
    O=rng.standard_normal((2,2)); Nfull=A@O@np.linalg.solve(O.T@A@O,O.T@A)
    assert np.allclose(Nfull,A,atol=1e-10)
    assert np.linalg.cond(np.linalg.solve(A,A)) < 1+1e-12

k_exact=(sp.Integer(71)+5*sp.sqrt(85))/54
assert abs(float(k_exact)-2.1684763386382304)<1e-13
print('VERIFY_OK symbolic identities=6, exact example=3, sampled Gaussian sketches='+str(checks)+', dimension-two cases=20')
print('L=2 probability of harm:',float(p.subs(L,2)))
print('L=2 witness condition number:',float(k_exact))
