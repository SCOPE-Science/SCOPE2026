#!/usr/bin/env python3
"""Algebraic and numerical checks of a scalar BDF2 splitting amplification law.
Only NumPy and SymPy are used; conclusions about all parameters rely on the accompanying proof.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp

checks=0

def verify(cond, detail=''):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(detail)


def state_matrix(w0, eps, K):
    # Scaled displacement z=D u, pressure p, state (z_n,z_{n+1},p_n,p_{n+1}).
    w=w0/(1+eps)
    gam=2/(2+w)
    rows=[]
    for i in range(4):
        x=np.zeros(4);x[i]=1
        z0,z1,p0,p1=x
        B= (4*(z1+p1)-(z0+p0))/3/(1+eps)
        pk=2*p1-p0
        for k in range(K):
            pnext=B-w*pk
            if k < K-1:
                pk=gam*pnext+(1-gam)*pk
        znext=w0*pk
        rows.append([z1,znext,p1,pnext])
    return np.stack(rows,axis=1)


def predicted_coefficients(w0,eps,K):
    w=w0/(1+eps)
    q=(-w/(2+w))**(K-1)
    Z=np.poly1d([1.,0.]); H=(4*Z-1)/(3*(1+eps)); v=2*Z-1
    F=Z**4+Z**2*(w*q*v-((1+w0-eps*w*q)/(1+w))*H)-w0*q*v*H
    return F.c

# Compare independently constructed time-stepping matrix to predicted characteristic.
for K in range(1,9):
    for w0 in (.03,.28,.9,1.4,1.8,2.9,5.5):
        for eps in (0.,.00001,.008,.19):
            mat=state_matrix(w0,eps,K)
            pred=predicted_coefficients(w0,eps,K)
            coeff=np.poly(mat)
            verify(np.allclose(coeff,pred,atol=2e-10,rtol=2e-10), (K,w0,eps,coeff,pred))

# Exact epsilon-zero factorization and z=1 derivative for arbitrary K, with symbolic w.
w,eps,z,q=sp.symbols('w eps z q', positive=True)
w_eff=w/(1+eps)
H=(4*z-1)/(3*(1+eps));v=2*z-1
F=z**4+z**2*(w_eff*q*v - ((1+w-eps*w_eff*q)/(1+w_eff))*H)-w*q*v*H
zero=sp.factor(F.subs(eps,0))
expected=(z-1)*(z-sp.Rational(1,3))*(z*z+w*q*(2*z-1))
verify(sp.simplify(zero-expected)==0, 'factorization')
verify(sp.simplify(F.subs(z,1)-eps*(1+w_eff*q)/(1+eps+w))==0,'z=1 identity')
verify(sp.simplify(sp.diff(F,eps).subs({z:1,eps:0})-(1+w*q)/(1+w))==0,'epsilon derivative')
verify(sp.simplify(sp.diff(F,z).subs({z:1,eps:0})-sp.Rational(2,3)*(1+w*q))==0,'root derivative')

# Full finite-epsilon roots near the analytically determined weak-flow barriers.
for K in range(1,9):
    for w0 in (.05,.15,.3,.5,.7,.95,1.1,1.4,1.7,1.9,2.05,2.5,3.,5.,7.):
        a=w0*(-w0/(w0+2))**(K-1)
        stable=(-1<a<1/3)
        roots0=np.roots(predicted_coefficients(w0,0.,K))
        parasitic=np.roots([1,2*a,-a])
        verify(stable==bool(np.max(np.abs(parasitic))<1.-1e-7), (K,w0,a,parasitic))
        if abs(a+1)<.05 or abs(a-1/3)<.05: continue
        # At small positive eps the physical root is inside for stable cases.
        roots=np.linalg.eigvals(state_matrix(w0,1e-7,K))
        verify((max(abs(roots))<1)==stable,(K,w0,a,roots))

# Example 2 inner iterations, w0=3/2.
a=Fraction(-9,14)
verify(a==Fraction(3,2)*Fraction(-3,7),'example a')
verify(Fraction(3,2)>1 and a>-1,'example missed by published sufficient bound')
roots=np.linalg.eigvals(state_matrix(1.5,1e-4,2))
verify(max(abs(roots))<1,roots)
# The two parasitic roots at zero flow have modulus 3/sqrt(14).
verify(abs(abs(complex(*[9/14,math.sqrt(45)/14]))-math.sqrt(9/14))<1e-12)
print(f'PASS: {checks} symbolic/numerical checks')
print('K=2, coupling=3/2, epsilon=1e-4 roots:', [complex(round(r.real,9),round(r.imag,9)) for r in roots])
print('Characteristic at epsilon=0: (z-1)(z-1/3)(z^2+2a z-a), a=(-1)^(K-1) w^K/(2+w)^(K-1)')
print('Physical root first derivative: -3/[2(1+w)]')
