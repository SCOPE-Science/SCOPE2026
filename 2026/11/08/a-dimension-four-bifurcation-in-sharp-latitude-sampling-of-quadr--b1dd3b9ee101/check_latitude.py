#!/usr/bin/env python3
"""Independent fourth-moment Gram tests and design-branch checks.
Requires numpy and scipy. All measurements use probability normalizations.
"""
from fractions import Fraction as F
import math
import numpy as np
from scipy.linalg import eigh


def coordinates(d):
    mats=[]
    for i in range(d-1):
        M=np.zeros((d,d),dtype=float);M[i,i]=1;M[-1,-1]=-1;mats.append(M)
    for i in range(d):
        for j in range(i+1,d):
            M=np.zeros((d,d),dtype=float);M[i,j]=M[j,i]=.5;mats.append(M)
    return mats


def moments(d, z=None):
    r=[]
    for i in range(d):
        t=[]
        for j in range(d):
            if z is None:
                m=(F(3) if i==j else F(1))/F(d*(d+2))
            elif i==j==0:m=z*z
            elif i==0 or j==0:m=z*(1-z)/F(d-1)
            elif i==j:m=F(3)*(1-z)*(1-z)/F((d-1)*(d+1))
            else:m=(1-z)*(1-z)/F((d-1)*(d+1))
            t.append(float(m))
        r.append(t)
    return np.array(r)


def gram(d,z=None):
    mats=coordinates(d);mm=moments(d,z);n=len(mats)
    G=np.zeros((n,n))
    for a,A in enumerate(mats):
        for b,B in enumerate(mats[:a+1]):
            v=0.0
            for i in range(d):
                for j in range(d):v+=A[i,i]*B[j,j]*mm[i,j]
            for i in range(d):
                for j in range(i+1,d):v+=4*A[i,j]*B[i,j]*mm[i,j]
            G[a,b]=G[b,a]=v
    return G


def bands(d,z):
    return ((d+2)*(d*z-1)**2/(2*(d-1)),
            d*(d+2)*z*(1-z)/(d-1),
            d*(d+2)*(1-z)**2/((d-1)*(d+1)))


def designs(d):
    zlo=(2*d-math.sqrt(d*(3*d-2)))/(d*(d+2))
    t=math.sqrt(2*d/(d+1));zhi=(1+t)/(d+t)
    return zlo,zhi

checks=0
for d in range(3,13):
    for k in (1,2,3,6,8):
        z=F(k,11)
        if z>=1:continue
        F0=gram(d);F1=gram(d,z); vals=np.sort(eigh(F1,F0,eigvals_only=True))
        predicted=[bands(d,float(z))[0]]+[bands(d,float(z))[1]]*(d-1)+[bands(d,float(z))[2]]*((d-2)*(d+1)//2)
        assert np.allclose(vals,np.sort(predicted),rtol=3e-11,atol=3e-11),(d,z,vals,predicted)
        checks+=1
for d in range(3,101):
    zlo,zhi=designs(d)
    l=bands(d,zlo)[0];r=bands(d,zhi)[0]
    assert 0<zlo<1/d<zhi<1
    assert abs(bands(d,zlo)[1]-l)<1e-10
    assert abs(bands(d,zhi)[2]-r)<1e-10
    assert bands(d,zlo)[2]>l and bands(d,zhi)[1]>r
    if d==3:assert l>r
    elif d==4:assert abs(l-r)<1e-12
    else:assert r>l
    Z=np.linspace(.00001,.99999,5003)
    vals=np.array([min(bands(d,z)) for z in Z]);want=max(l,r)
    assert float(vals.max())<=want+1e-9,(d,vals.max(),want)
    checks+=7
for d in range(3,101):
    e=1/d
    a,b,c=bands(d,e)
    assert abs(a)<1e-27 and b>0 and c>0
    checks+=1
print('LATITUDE_CHECKS_PASS',checks)
