#!/usr/bin/env python3
"""Reproducible finite checks of the three-channel two-tap Gabor theorem.
The analytical inequalities in RESULT.md are required for the all-order proof.
"""
from itertools import combinations
from math import pi, cos, isclose
import cmath
import numpy as np

assertions=0
for N in range(4, 41):
    zeta=np.exp(2j*pi*np.arange(N)/N)
    q=N//3
    if N%3==0:
        prototype={0,q,2*q}
        radius=0.0
    elif N%3==1:
        prototype={0,q,2*q}
        radius=1+2*cos(2*pi*q/N)
    else:
        prototype={0,q+1,2*(q+1)}
        radius=-(1+2*cos(2*pi*(q+1)/N))
    expected={frozenset((k+t)%N for k in prototype) for t in range(N)}
    alltrios=list(combinations(range(N),3))
    minratio=1e99
    minframe=1e99
    best=set(); bestfp=set()
    for tri in alltrios:
        Z=sum(zeta[-k] for k in tri)
        eigenvalues=3+(zeta*Z).real
        ratio=float(eigenvalues.max()/eigenvalues.min())
        fp=float(np.dot(eigenvalues-3,eigenvalues-3))
        assert abs(fp-N/2*abs(Z)**2)<2e-11
        assertions+=1
        key=frozenset(tri)
        if ratio<minratio-1e-10:
            minratio=ratio;best={key}
        elif abs(ratio-minratio)<1e-10:
            best.add(key)
        if fp<minframe-1e-10:
            minframe=fp;bestfp={key}
        elif abs(fp-minframe)<1e-10:
            bestfp.add(key)
    assert best==expected,(N,'condition',len(best),len(expected),best^expected)
    assert bestfp==expected,(N,'potential',len(bestfp),len(expected),bestfp^expected)
    assert isclose(minframe,N/2*radius**2,abs_tol=2e-11)
    assertions+=3
    r=radius
    if N%3==0: target=1.0
    elif N%2==0: target=(3+r)/(3-r)
    elif N%3==1: target=(3+r)/(3-r*cos(pi/N))
    else: target=(3+r*cos(pi/N))/(3-r)
    assert isclose(minratio,target,abs_tol=2e-11),(N,minratio,target)
    assertions+=1

# Independent direct frame construction with a nontrivial coprime window shift.
for N in range(4,12):
    zeta=np.exp(2j*pi*np.arange(N)/N)
    for s in range(1,N):
        if np.gcd(N,s)!=1: continue
        g=np.zeros(N,complex)
        g[0]=g[s]=2**-0.5
        for tri in combinations(range(N),3):
            if N>8 and tri[0]>0:continue
            S=np.zeros((N,N),complex)
            for k in range(N):
                shifted=np.roll(g,k)
                for l in tri:
                    v=zeta**l * shifted
                    S+=np.outer(v,v.conjugate())
            eig=np.linalg.eigvalsh(S)
            Z=sum(cmath.exp(-2j*pi*s*l/N) for l in tri)
            claimed=np.sort([3+(cmath.exp(2j*pi*s*j/N)*Z).real for j in range(N)])
            assert np.max(np.abs(eig-claimed)) < 1e-10
            assertions+=1

print('CHECK_OK', assertions, 'N=4..40 exhaustive optimizers; direct spectral checks N=4..11')
