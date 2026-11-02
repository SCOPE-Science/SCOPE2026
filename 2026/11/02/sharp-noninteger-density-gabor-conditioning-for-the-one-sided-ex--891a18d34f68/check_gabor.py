#!/usr/bin/env python3
"""Reproduce algebraic identities and independent fiber checks for rational Gabor bounds.
Public mathematical verification; exact derivation is in RESULT.md.
"""
import math
import cmath
import random
import numpy as np
import sympy as sp

u, t, z = sp.symbols('u t z', positive=True)
T = sum(u**j for j in range(6))
c = u*(1+u**2)
y = (1-u**3)**2
h = 4*u*(1+u**2)*(1-u)**2/(1+u**3)**2
assert sp.factor(4*c*y/T**2-h)==0
E = sp.factor(-u*sp.diff(h,u)/h)
q2 = 1-h
num = u**8-3*u**6-12*u**4-3*u**2+1
assert sp.factor(E**2-q2 + 4*u**2*num / ((u-1)**2*(u+1)**2*(u**2+1)**2*(u**2-u+1)**2))==0
v=sp.symbols('v')
s=sp.symbols('s')
assert sp.expand((v**4-3*v**3-12*v**2-3*v+1)/v**2 - (s**2-3*s-14)).subs(s,v+1/v).simplify()==0
assert sp.factor((1+t**4)*(t-t**7*z)*(t-t**7/z) - (1+t**4)*t**2*(1-t**6*z)*(1-t**6/z))==0
# Fiber determinant and trace using the explicitly summed columns.
v0=sp.Matrix([1,t**3]);v1=sp.Matrix([t**4*z,t]);
M=(1+t**4)*v0*v0.T+v1*sp.Matrix([[t**4/z,t]])
assert sp.factor(sp.trace(M)-sum(t**(2*j) for j in range(6)))==0
assert sp.factor(sp.det(M)-(1+t**4)*t**2*(1-t**6*z)*(1-t**6/z))==0

sval=(3+math.sqrt(65))/2
vstar=(sval-math.sqrt(sval*sval-4))/2
ustar=math.sqrt(vstar)
etastar=-.75*math.log(vstar)

def bounds(eta):
    u=math.exp(-2*eta/3)
    h=4*u*(1+u*u)*(1-u)**2/(1+u**3)**2
    q=math.sqrt(1-h)
    f=eta*(1+u**3)/((1-u)*(1-u**3))
    return f*u*(1-q), f*(1+q)

def fiber(eta,x,xi):
    zz=cmath.exp(-2j*math.pi*xi)
    vecs=[]
    for r in range(3):
        col=[]
        for k in range(2):
            q0=math.ceil((2*r/3 - x-k)/2 - 1e-12)
            val=math.sqrt(2*eta)*math.exp(-eta*(x+k-2*r/3+2*q0))*(zz**q0)/(1-math.exp(-2*eta)*zz)
            col.append(val)
        vecs.append(col)
    V=np.asarray(vecs,dtype=np.complex128).T
    return np.linalg.eigvalsh(V@V.conj().T)

# Check exact formula for all three equivalent x-thirds and many phases.
checks=0
rng=random.Random(20261029)
for eta in [.16,.4,.8,etastar,2.6,5.5]:
    for _ in range(100):
        x=rng.uniform(.00001,.33332)
        xi=rng.random()
        eigen0=fiber(eta,x,xi)
        for j in [1,2]:
            eigenj=fiber(eta,x+j/3,xi)
            assert np.allclose(eigenj,eigen0,rtol=2e-10,atol=3e-11)
            checks+=2
        # Independent trace and determinant from the direct infinite geometric sums.
        u=math.exp(-2*eta/3)
        tr=2*eta*math.exp(-2*eta*x)*sum(u**j for j in range(6))/abs(1-u**3*cmath.exp(-2j*math.pi*xi))**2
        det=(2*eta*math.exp(-2*eta*x))**2 *u*(1+u*u)/abs(1-u**3*cmath.exp(-2j*math.pi*xi))**2
        assert abs(sum(eigen0)-tr)<3e-9*max(1,tr)
        assert abs(np.prod(eigen0)-det)<3e-9*max(1,det)
        checks+=2
    A,B=bounds(eta)
    tiny=1e-8
    assert abs(fiber(eta,tiny,tiny)[1]/B-1)<2e-7
    assert abs(fiber(eta,1/3-tiny,tiny)[0]/A-1)<2e-7
    checks+=2

A,B=bounds(etastar)
assert abs(etastar-1.25698)<.00001
assert abs(B/A-11.237951670)<1e-8
assert 0<ustar<1
for eta in np.linspace(.08,7,1001):
    a,b=bounds(float(eta))
    assert b/a>=B/A-1e-9
    checks+=1

# Completely independent finite-sum Gram matrix tests on a cyclic truncation.
# Compare the spectral endpoints of the 2-by-2 frame fiber over a dense grid.
for eta in [.35,.8,etastar,2.1]:
    A,B=bounds(eta)
    emin,emax=1e100,0
    for j in range(35):
        for k in range(71):
            lam=fiber(eta,(j+.5)/105,k/71)
            emin=min(emin,lam[0]);emax=max(emax,lam[1])
    assert emin>A*(1-1e-9) and emax<B*(1+1e-9)
    assert (emin/A)<1.1 and (B/emax)<1.1
    checks+=1
A,B=bounds(etastar)
print('PASS',checks,'supplementary numerical and exact-symbolic checks')
print('u*',repr(ustar),'eta*',repr(etastar),'A*',repr(A),'B*',repr(B),'K*',repr(B/A))
