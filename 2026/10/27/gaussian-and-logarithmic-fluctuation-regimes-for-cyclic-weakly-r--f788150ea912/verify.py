#!/usr/bin/env python3
"""Independent finite-dimensional checks for the cyclic WARM fluctuation theorem."""
import math
import numpy as np

checks=0

def intensity(x, a):
    x=np.asarray(x,dtype=float)
    xa=x**a
    return xa/(xa+np.roll(xa,1))+xa/(xa+np.roll(xa,-1))

def jacobian_numeric(d,a,h=1.e-6):
    out=np.zeros((d,d))
    for j in range(d):
        p=np.ones(d);m=np.ones(d)
        p[j]+=h;m[j]-=h
        out[:,j]=(intensity(p,a)-intensity(m,a))/(2*h)
    return out

def jacobian_explicit(d,a):
    eye=np.eye(d)
    return (a/2)*eye-(a/4)*(np.roll(eye,1,axis=1)+np.roll(eye,-1,axis=1))

for d in range(3,22):
    for a in [0.0, 0.1, 0.35, 0.63, 0.95]:
        J=jacobian_explicit(d,a)
        assert np.max(np.abs(jacobian_numeric(d,a)-J))<1.e-8
        checks+=1
        eig=np.linalg.eigvalsh(J)
        expected=np.sort([a*math.sin(math.pi*k/d)**2 for k in range(d)])
        assert np.max(abs(eig-expected))<2.e-13
        checks+=1
    m=max(math.sin(math.pi*k/d)**2 for k in range(d))
    mc=1 if d%2==0 else math.cos(math.pi/(2*d))**2
    assert abs(m-mc)<1.e-12
    checks+=1
    ac=1/(2*m)
    J=jacobian_explicit(d,ac)
    evals=np.linalg.eigvalsh(J)
    assert np.sum(abs(evals-0.5)<1.e-10)==(1 if d%2==0 else 2)
    checks+=1
    alpha=.6*ac
    J=jacobian_explicit(d,alpha)
    S=np.linalg.inv(np.eye(d)-2*J)
    assert np.max(abs((np.eye(d)-2*J)@S-np.eye(d)))<1.e-12
    assert np.min(np.linalg.eigvalsh(S))>0
    checks+=1
    if d<=13:
        # Fourier inversion of the proposed limiting covariance.
        D=np.zeros((d,d))
        for j in range(d):
            for k in range(d):
                D[j,k]=sum(math.cos(2*math.pi*m*(j-k)/d)/(1-2*alpha*math.sin(math.pi*m/d)**2) for m in range(d))/d
        assert np.max(abs(D-S))<1.e-12
        checks+=1

# An exact normalization check: total count is Poisson(d*t) for any reinforcement.
for d in range(3,22):
    for a in [.0,.2,.79]:
        x=np.exp(np.linspace(-1,1,d))
        assert abs(sum(intensity(x,a))-d)<1.e-12
        checks+=1

print(f'PASS {checks} independent Jacobian, Fourier, parity, covariance and conserved-rate checks')
