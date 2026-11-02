#!/usr/bin/env python3
"""Reproducible checks for stationary on/off harmonic-trap covariance duality.
Scientific checks only; numerical comparisons do not replace the proof.
"""
import math
import numpy as np
from scipy.linalg import expm
import sympy as sp

q,k,D=sp.symbols('q k D', positive=True)
Q=sp.Matrix([[-q,q],[q,-q]])
Pvec=sp.Matrix([sp.Rational(1,2),sp.Rational(1,2)])
K=sp.diag(0,k)
m2=(2*K-Q.T).inv()*(2*D*Pvec)
m4=(4*K-Q.T).inv()*(12*D*m2)
C0=sp.factor(sum(m2))
K4=sp.factor(sum(m4)-3*C0**2)
assert sp.simplify(C0-D*(2/k+1/q))==0
assert sp.simplify(K4-D**2*(9/q**2+6/(k*q)))==0
M=Q-K
C1=sp.factor((m2.T*M*sp.ones(2,1))[0]);C2=sp.factor((m2.T*M**2*sp.ones(2,1))[0]);C3=sp.factor((m2.T*M**3*sp.ones(2,1))[0]);C4=sp.factor((m2.T*M**4*sp.ones(2,1))[0]);
L=k+2*q;P=k*q
assert all(sp.simplify(a-b)==0 for a,b in [(C1,-D),(C2,0),(C3,D*P),(C4,-D*P*L)])
assert sp.simplify(K4-K4.subs({q:k/2,k:2*q},simultaneous=True)-9*D**2*(1/q**2-4/k**2))==0
print('SYMBOLIC identities: PASS (stationary second/fourth moments, cumulant, four lag derivatives, involution difference)')

def covariance(q,k,D,t):
    a=k+2*q
    b=q*k
    discr=math.sqrt(k*k+4*q*q)
    low=(a-discr)/2
    high=(a+discr)/2
    c0=D*a/b
    return ((high*c0-D)*math.exp(-low*t)+(D-low*c0)*math.exp(-high*t))/(high-low)

def direct(q,k,D,t):
    Q=np.array([[-q,q],[q,-q]],float)
    B=Q.T-np.diag([0,2*k])
    m2=np.linalg.solve(-B, D*np.ones(2))
    H=Q-np.diag([0,k])
    cov=m2 @ expm(t*H) @ np.ones(2)
    m4=np.linalg.solve(-(Q.T-np.diag([0,4*k])),12*D*m2)
    cum4=m4.sum()-3*m2.sum()**2
    return cov,cum4

rng=np.random.default_rng(58021)
checks=0
for _ in range(50):
    q=float(np.exp(rng.uniform(-2,2)))
    k=float(np.exp(rng.uniform(-2,2)))
    D=float(np.exp(rng.uniform(-2,2)))
    q2,k2=k/2,2*q
    for t in [0,0.03,0.4,1,3]:
        t=t/max(k,q)
        cov1,c4a=direct(q,k,D,t)
        cov2,c4b=direct(q2,k2,D,t)
        a=covariance(q,k,D,t)
        b=covariance(q2,k2,D,t)
        assert np.allclose([a,b,cov1,cov2],[cov1,cov1,cov1,cov1],rtol=2e-9,atol=3e-10)
        checks+=4
    assert np.isclose(c4a,D**2*(9/q**2+6/(k*q)),rtol=2e-9,atol=1e-9)
    assert np.isclose(c4b,D**2*(9/q2**2+6/(k2*q2)),rtol=2e-9,atol=1e-9)
    assert np.isclose(c4a-c4b,9*D*D*(1/q**2-4/k**2),rtol=3e-8,atol=1e-9)
    # Explicit inversion of the cubic/fourth lag derivatives plus kurtosis.
    a0=-D;d3=D*q*k;d4=-D*q*k*(k+2*q)
    inferredD=-a0;inferredP=d3/inferredD;inferredL=-d4/d3
    roots=np.sort(np.roots([1,-inferredL,2*inferredP]))
    assert np.allclose(roots,np.sort([k,2*q]),rtol=4e-10,atol=4e-10)
    qhat=3*inferredD/math.sqrt(c4a-6*inferredD**2/inferredP)
    khat=inferredP/qhat
    assert np.isclose(qhat,q,rtol=2e-9)
    assert np.isclose(khat,k,rtol=2e-9)
    checks+=6
print('NUMERIC matrix-exponential/stationary-moment/spectral and inversion comparisons:',checks,'PASS')
for (q,k,D) in [(1,1,1),(0.5,2,1),(1,2,1),(0.1,8,4)]:
    c4=direct(q,k,D,1)[1]
    print(f'q={q:g}, k={k:g}, D={D:g}; C(0)={D*(2/k+1/q):.9g}; K4={c4:.9g}')
