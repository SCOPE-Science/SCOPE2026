#!/usr/bin/env python3
"""Numerical spot checks for the two-mode Nyström spectral-preconditioner theorem."""
import math
import numpy as np
from scipy.optimize import brentq

rng=np.random.default_rng(27817)
checks=0

def qpoly(a,b,z):
    L,m=1+a,1+b
    d=a-b
    return (b*L*m+m*d*(L+1)*z-b*(L*(L+m)+m*m)*z*z-a*m*(L+m)*z**3)

def root(a,b):
    return brentq(lambda z:qpoly(a,b,z),0.,1.,xtol=5e-15)

def formulas(a,b,inform):
    zz=root(a,b)
    scale=math.sqrt(b**3*(1+b)/(a**3*(1+a))) if inform else b/a
    return zz,2/math.pi*math.atan(scale/math.sqrt(zz))

def experiment(a,b,omega):
    # Independently recompute Algorithm 3.1 (q=k=l=1) and scaled spectral LMP.
    A=np.diag([a,b]); H=np.eye(2)+A
    y=A@omega
    v=y/np.linalg.norm(y)
    W=omega@(A@omega)
    lamhat=y@y/W  # QR/Cholesky/SVD for rank one
    theta=1+b
    c=theta/(1+lamhat)
    C=np.eye(2)+(math.sqrt(c)-1)*np.outer(v,v)
    D=C@H@C
    eig=np.linalg.eigvalsh(D)
    return eig[-1]/eig[0], (1+a)/(1+b), (b*omega[1]/(a*omega[0]))**2

# Verify tr/det identity and the exact logical equivalence; each sampled point uses direct matrix eigenspectrum.
for a,b in [(1.1,1),(3,1),(9,1),(100,10),(.3,.1),(1.0001,1),(1000,.001)]:
    zs=root(a,b)
    assert 0<zs<1
    assert qpoly(a,b,0)>0 and qpoly(a,b,1)<0
    for z in np.geomspace(1e-6,1e6,110):
        om=np.array([1.,a/b*math.sqrt(z)])
        k,k0,z_direct=experiment(a,b,om)
        assert abs(z_direct-z)/z<1e-9
        # Exclude floating errors near equality.
        if abs(z-zs)>1e-7 and abs(z-1)>1e-7:
            assert (k>k0) == (z>zs),(a,b,z,zs,k,k0)
        checks+=1
    for inform in [False,True]:
        zstar,p=formulas(a,b,inform)
        assert 0<p<1
        # Event from exact ratio sample, requiring no linear algebra approximation.
        N=140000
        Z=rng.normal(size=(N,2))
        scale=math.sqrt(b**3*(1+b)/(a**3*(1+a))) if inform else b/a
        ze=scale**2*(Z[:,1]/Z[:,0])**2
        empirical=np.mean(ze>zstar)
        assert abs(empirical-p)<0.014,(a,b,inform,p,empirical)
        checks+=1

# Sharp asymptotics for fixed b.
for b in [0.1,1,10]:
    m=1+b
    zlim=(math.sqrt(b*b+4*m*m)-b)/(2*m)
    for a in [1e3,1e4,1e5]:
        zs,pstd=formulas(a,b,False)
        _,pinf=formulas(a,b,True)
        assert abs(zs-zlim)<(100*(1+b)/a)
        predstd=2*b/(math.pi*math.sqrt(zlim)*a)
        predinf=2*math.sqrt(b**3*m)/(math.pi*math.sqrt(zlim)*a*a)
        assert abs(pstd/predstd-1)<0.08
        assert abs(pinf/predinf-1)<0.08
        checks+=1

for a,b in [(9,1),(3,1),(100,10)]:
    zs,ps=formulas(a,b,False)
    _,pi=formulas(a,b,True)
    assert 0<pi<ps<1
    print('a,b,root,Pstandard,Pinformed=',a,b,zs,ps,pi)
print('PASS',checks,'independent algebra/matrix/probability/asymptotic checks')
