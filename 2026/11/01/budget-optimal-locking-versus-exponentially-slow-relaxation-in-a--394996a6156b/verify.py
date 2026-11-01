#!/usr/bin/env python3
"""Reproducible symbolic and numerical checks for the three-frequency Kuramoto triad.

Uses sympy, scipy, and NumPy for finite checks. The universal theorem follows
from the mathematical proof, not from any finite grid of test parameters.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq

# Algebraic Jacobian checks; the displayed matrix is the positive Laplacian
# and the dynamical Jacobian is its negative.
a, b, c, d = sp.symbols('a b c d', real=True)
L = sp.Matrix([[a*c+b*d, -a*c, -b*d],
               [-a*c, 2*a*c, -a*c],
               [-b*d, -a*c, a*c+b*d]])
assert sp.simplify(L*sp.Matrix([1, 1, 1])) == sp.zeros(3,1)
assert sp.simplify(L*sp.Matrix([1,-2,1]) - 3*a*c*sp.Matrix([1,-2,1])) == sp.zeros(3,1)
assert sp.simplify(L*sp.Matrix([-1,0,1]) - (a*c+2*b*d)*sp.Matrix([-1,0,1])) == sp.zeros(3,1)

# The alternative sine-equality branch has opposite neighbor cosines
# and far-edge cosine -1; its Laplacian has negative trace.
t = sp.symbols('t', real=True)
Lalt = sp.Matrix([[a*t-b, -a*t, b],
                  [-a*t, 0, a*t],
                  [b, a*t, -a*t-b]])
assert sp.simplify(sp.trace(Lalt)+2*b)==0
assert sp.simplify(Lalt*sp.ones(3,1))==sp.zeros(3,1)


def fold(q):
    c=(math.sqrt(1+32*q*q)-1)/(8*q)
    angle=math.acos(c)
    g=math.sin(angle)*(1+2*q*c)
    k=2*(q+2)/(3*g)
    return c,angle,k


def stable_phase(q,K,omega=1.0):
    c, phstar, Kcritnorm=fold(q)
    if K<=Kcritnorm*omega:
        return None
    a=3*K/(2*(q+2))
    fun=lambda phi:a*(math.sin(phi)+q*math.sin(2*phi))-omega
    phi=brentq(fun,0,phstar,xtol=1e-14)
    lap1=3*a*math.cos(phi)
    lap2=a*(math.cos(phi)+2*q*math.cos(2*phi))
    return phi,lap1,lap2

# All identities used in the proof, tested over a finite range of q and K.
for q in np.geomspace(1,4096,100):
    c,phi,kcrit=fold(q)
    assert 0.5<c<1/math.sqrt(2)
    assert abs(4*q*c*c+c-2*q)<1e-10
    assert abs(math.cos(phi)+2*q*math.cos(2*phi))<1e-10
    for ratio in (1.01,1.3,3,12):
        K=ratio*kcrit
        phase=stable_phase(q,K)
        assert phase is not None
        z,lam1,lam2=phase
        assert 0<z<phi and lam1>0 and lam2>0
        theta=np.array([-z,0,z])
        a=3*K/(2*(q+2)); b=q*a
        W=np.array([[0,a,b],[a,0,a],[b,a,0]])
        freq=np.array([-1.,0.,1.])
        velocity=freq + np.sum(W*np.sin(theta[None,:]-theta[:,None]),axis=1)
        assert np.max(np.abs(velocity))<2e-11
        J=W*np.cos(theta[None,:]-theta[:,None]); np.fill_diagonal(J,0)
        J=J-np.diag(np.sum(J,axis=1))
        ev=np.linalg.eigvalsh(J)
        assert np.max(np.abs(np.sort(ev)-np.sort(np.array([-lam1,-lam2,0]))))<2e-10

# Onset monotonicity on a dense parameter sample (supplementary only).
qvalues=np.geomspace(1,10**6,180)
thresholds=[fold(float(q))[2] for q in qvalues]
assert np.all(np.diff(thresholds)<0)
assert abs(fold(1)[2]-1.1362522106646809)<5e-15

# Fixed budget: improved locking yet arbitrarily slow convergence.
K=1.0; omega=1.0
assert stable_phase(1,K,omega) is None
assert stable_phase(2,K,omega) is not None
phi_inf=0.5*math.asin(2*omega/(3*K))
for q in (64,256,1024,4096,16384):
    z,lam1,lam2=stable_phase(q,K,omega)
    pred=9*K*math.cos(phi_inf)/(2*q)
    assert lam2>0
    if q>=4096:
        assert abs(lam1/pred-1)<0.001

# First asymptotic correction at the onset.
for q in (10**4,10**5,10**6):
    lhs=q*(fold(q)[2]/(2/3)-1)
    assert abs(lhs-(2-1/math.sqrt(2)))<0.002

print('PASS symbolic Laplacian/eigenbranch identities')
print('PASS 400 stable phases and direct 3x3 Jacobian cross-checks')
print('PASS 180 monotone threshold samples and asymptotic diagnostics')
print('Kcrit(p=0)/omega =',repr(fold(1)[2]))
print('Kcrit(p=1)/omega =',repr(fold(2)[2]))
print('sample K=omega: no stable state at p=0; stable at p=1')
