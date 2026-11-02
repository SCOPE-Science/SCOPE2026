"""Reproduce finite-dimensional Gaussian trace-variance benchmark identities.

Run: python verify.py
Requires SymPy and NumPy. Symbolic identities supply the exact certificate;
Monte Carlo is an independent finite-sample sanity check, not a proof.
"""
import math
import numpy as np
import sympy as sp

L, b, c = sp.symbols('L b c', positive=True)
# J(b,c) = integral_0^infty dt/[(t^2+b^2)(t^2+c^2)].
J = sp.pi/(2*b*c*(b+c))
J_b = -sp.diff(J,b)/(2*b)
J_bc = -sp.diff(J_b,c)/(2*c)
EU = sp.factor((4/sp.pi)*J_b.subs({b:1,c:1/L})/L**2)
EU2 = sp.factor((4/sp.pi)*J_bc.subs({b:1,c:1/L})/L**4)
assert sp.simplify(EU-(2*L+1)/(L+1)**2)==0
assert sp.simplify(EU2-(L**2+3*L+1)/(L+1)**3)==0

Eres = sp.factor(3 + 2*(L-1)*EU + (L-1)**2*EU2)
assert sp.simplify(Eres-(L**4+8*L**3+7*L**2+6*L+2)/(L+1)**3)==0
Vpp = sp.factor(2*Eres)
Vgh = sp.Rational(2,3)*(L**2+3)
p = L**5-18*L**3-11*L**2-9*L-3
assert sp.simplify((Vpp-Vgh)+2*p/(3*(L+1)**3))==0
R = sp.factor(Vpp/Vgh)
assert sp.simplify(sp.diff(R,L) + 3*L*(L-1)*(L**4+15*L**3+25*L**2+37*L+2)/((L+1)**4*(L**2+3)**2))==0
assert p.subs(L,4)<0 and p.subs(L,5)>0
positive_roots=[complex(z) for z in sp.nroots(p,maxsteps=200) if abs(sp.im(z))<1e-10 and sp.re(z)>0]
assert len(positive_roots)==1
root=positive_roots[0].real
assert 4.56 <root<4.58
assert sp.limit(R,L,sp.oo)==0
assert R.subs(L,1)==sp.Rational(9,4)

# Independent exact 4x4 matrix verification of projector algebra.
for ell in (1,2,3,5,9):
    A=sp.diag(ell,1,1,1)
    for gg in ((1,2,3,4),(2,0,1,1),(0,2,1,1),(3,4,2,1),(1,-1,1,-1)):
        y=A*sp.Matrix(gg)
        proj=y*y.T/(y.dot(y))
        B=(sp.eye(4)-proj)*A*(sp.eye(4)-proj)
        u=sp.Rational(sum(g*g for g in gg[1:]),ell**2*gg[0]**2+sum(g*g for g in gg[1:]))
        expected=3+2*(ell-1)*u+(ell-1)**2*u*u
        assert sp.factor(sp.trace(B*B)-expected)==0
        assert sp.factor(sp.trace(proj*A)+sp.trace(B)-sp.trace(A))==0

# Independent quadrature of the actual polar density, not the derivative trick.
import mpmath as mp
mp.mp.dps=35
for ell in (1,sp.Rational(3,2),2,5,10):
    a=mp.mpf(str(ell)) if ell!=sp.Rational(3,2) else mp.mpf('1.5')
    for k,f in ((1,EU),(2,EU2)):
        actual=4/mp.pi*mp.quad(lambda t: 1/((1+t*t)**2*(1+a*a*t*t)**k),[0,1,mp.inf])
        predicted=sp.N(f.subs(L,ell),32)
        assert abs(actual-mp.mpf(str(predicted)))<mp.mpf('1e-28')

# Finite sample test with independent normal sketches and residual probes.
rng=np.random.default_rng(20261025)
for ell in (1.,2.,4.,5.,10.):
    S=rng.standard_normal((160000,4))
    H=rng.standard_normal((160000,4))
    Y=S*np.array([ell,1,1,1])[None,:]
    Q=Y/np.linalg.norm(Y,axis=1)[:,None]
    Ptrace=1+(ell-1)*Q[:,0]**2
    GH=H-Q*np.sum(Q*H,axis=1)[:,None]
    Z=Ptrace+np.sum((GH**2)*np.array([ell,1,1,1])[None,:],axis=1)
    var=float(np.var(Z,ddof=1))
    target=float(Vpp.subs(L,ell))
    assert abs(var/target-1)<0.065, (ell,var,target)

print('VERIFY_OK: 25 exact projection cases, symbolic integrals and variance polynomial,')
print('derivative sign certificate, 10 independent quadratures and 5 finite-sample checks')
print('unique crossover lambda =',format(root,'.12f'))
print('E_residual_Frobenius_squared =',Eres)
print('three-query Gaussian variance ratio =',R)
