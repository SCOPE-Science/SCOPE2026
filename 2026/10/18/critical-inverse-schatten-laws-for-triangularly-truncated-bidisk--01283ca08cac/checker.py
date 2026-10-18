#!/usr/bin/env python3
"""Reproduce finite-section spectra and inverse-Schatten scaling checks."""
import math
import numpy as np

PI=math.pi
checks=0

def theoretical(N,a,b):
    A,B=abs(a),abs(b)
    return np.sort(np.array([math.sqrt(max(0., A*A+B*B+2*A*B*math.cos(PI*r/j))) for j in range(2,N+2) for r in range(1,j)],dtype=float))

def matrix(N,a,b):
    basis=[(i,k-i) for k in range(N+1) for i in range(k+1)]
    ind={t:i for i,t in enumerate(basis)}
    M=np.zeros((len(basis),len(basis)),dtype=complex)
    for (i,j),col in ind.items():
        if (i+1,j) in ind:M[ind[i+1,j],col]+=a
        if (i,j+1) in ind:M[ind[i,j+1],col]+=b
    return M

for N in range(1,14):
    for a,b in [(1.,1.),(2.,1.),(0.,2.),(1j,3-4j),(0.6-0.7j,-1.8+0.1j)]:
        M=matrix(N,a,b)
        sv=np.linalg.svd(M,compute_uv=False)
        rank=N*(N+1)//2
        s=theoretical(N,a,b)
        assert len(s)==rank
        assert np.allclose(s, np.sort(sv)[-rank:], atol=1e-12)
        assert np.sum(sv>1e-10)==rank
        checks+=3

for N in range(1,151):
    s=theoretical(N,1.,1.)
    exactly=N*(N+1)*(2*N+7)/36
    assert abs(float(np.sum(s**(-2)))/exactly-1)<2e-12
    assert abs(s[0] - 2*math.sin(PI/(2*(N+1))))<1e-12
    checks+=2

for a,b in [(1.,1.),(2.,1.),(0.,1.),(3.,4.)]:
    for N in [1,2,3,5,15,50]:
        s=theoretical(N,a,b)
        z=PI/(N+1)
        aa,bb=abs(a),abs(b)
        maxv=math.sqrt(aa*aa+bb*bb+2*aa*bb*math.cos(z))
        minv=math.sqrt(aa*aa+bb*bb-2*aa*bb*math.cos(z))
        assert abs(s[0]-minv)<1e-10
        assert abs(s[-1]-maxv)<1e-10
        checks+=2

for tau in [0.,2.,10.]:
    # Integral with midpoint Riemann sums of (tau*u*coth(tau*u)-1)/(2*tau^2).
    # At tau=0 the expression is u^2/6.
    nquad=20000
    if tau==0: L=1/18
    else: L=sum((((tau*(k+0.5)/nquad)/math.tanh(tau*(k+0.5)/nquad)-1)/(2*tau*tau)) for k in range(nquad))/nquad
    for N in [150,400]:
        a=1+tau/(2*N);b=1-tau/(2*N)
        moment=float(np.sum(theoretical(N,a,b)**(-2)))/N**3
        assert abs(moment/L-1)<0.1,(tau,N,moment,L)
        checks+=1

print('PASS',checks,'finite-matrix/moment/endpoint/crossover assertions')
