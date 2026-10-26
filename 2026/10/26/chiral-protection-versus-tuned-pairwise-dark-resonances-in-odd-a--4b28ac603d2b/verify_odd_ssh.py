"""Finite checks of the odd alternating-chain one-sink spectral classification.
Run: python verify_odd_ssh.py (requires numpy and sympy).
"""
import math
import numpy as np
import sympy as sp


def hamiltonian(m, a, b):
    n = 2*m+1
    h = np.zeros((n,n), dtype=float)
    for i in range(n-1):
        h[i,i+1] = h[i+1,i] = a if i%2==0 else b
    return h


def sink_dark(h, site, tol=1e-9):
    eig,vec = np.linalg.eigh(h)
    dark = np.where(np.abs(vec[site-1,:]) < tol)[0]
    return eig,vec,dark

checks=0
for m in range(2,12):
    for a,b in [(1.,1.),(0.7,1.31),(1.1,0.9)]:
        h=hamiltonian(m,a,b)
        for site in (1,2):
            eig,vec,dark=sink_dark(h,site)
            expected=0 if site==1 else 1
            assert len(dark)==expected,(m,a,b,site,dark)
            if site==2:
                assert abs(eig[dark[0]]) < 1e-10
                ratio=a/b
                exact=1/sum(ratio**(2*j) for j in range(m+1))
                measured=float(np.sum(vec[0,dark]**2))
                assert abs(measured-exact) < 2e-10,(m,a,b,exact,measured)
            checks+=1
    for k in range(1,m//2+1):
        theta=k*math.pi/(m+1)
        r=2*math.cos(theta)
        a=1.
        eig,vec,dark=sink_dark(hamiltonian(m,a,r),3)
        assert len(dark)==2,(m,k,r,len(dark))
        assert sorted(np.round(eig[dark],9).tolist())==[-1.,1.],(m,k,eig[dark])
        exact=2*math.sin(theta)**2/(m+1)
        measured=float(np.sum(vec[0,dark]**2))
        assert abs(measured-exact)<2e-10,(m,k,exact,measured)
        # Off resonance the entire chain is bright.
        r2=r+0.000713
        eig2,vec2,dark2=sink_dark(hamiltonian(m,a,r2),3)
        assert len(dark2)==0,(m,k,r2,dark2)
        checks+=1

r=sp.Symbol('r')
for t in range(1,22):
    x0,x1=-r,r*r-1
    for _ in range(1,t):
        x0,x1=x1,sp.expand(-r*x1-x0)
    assert sp.expand(x1-(-1)**(t+1)*sp.chebyshevu(t+1,r/2))==0
    checks+=1

print(f'PASS: {checks} checks of spectral dark ranks, overlap probabilities, off-resonance absence, and exact Chebyshev identities')
