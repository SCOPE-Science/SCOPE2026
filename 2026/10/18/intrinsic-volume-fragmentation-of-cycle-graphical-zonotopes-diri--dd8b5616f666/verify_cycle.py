#!/usr/bin/env python3
"""Independent finite and asymptotic diagnostics for cycle graphical zonotope intrinsic volumes.
Only standard Python, numpy, scipy required; no access to external research ledgers.
"""
from math import sqrt,pi,gamma,log
from itertools import combinations
import numpy as np
from scipy.optimize import brentq

def comp_coeff(n,k):
    a=np.zeros(n+1)
    a[0]=1.0
    for _ in range(k):
        b=np.zeros(n+1)
        for s in range(1,n+1):
            b[s:]+=sqrt(s)*a[:-s]
        a=b
    return float(a[n])

def intrinsic_formula(n,k):
    return n/k*comp_coeff(n,k)

def direct_intrinsic(n,k):
    j=n-k
    roots=[]
    for v in range(n):
        z=np.zeros(n)
        z[v]=1;z[(v+1)%n]=-1
        roots.append(z)
    total=0.0
    for I in combinations(range(n),j):
        if j==0:
            det=1.0
        else:
            b=np.array([roots[t] for t in I],dtype=float).T
            det=float(np.linalg.det(b.T@b))
            if det<1.e-8: raise AssertionError(('dependent forest',n,I,det))
        total+=sqrt(det)
    return total

def tilt(n,k):
    mu=n/k
    def moments(th):
        s=np.arange(1,n+1,dtype=float)
        ww=np.sqrt(s)*np.exp(s*np.log(th))
        p=ww/ww.sum()
        return float((p*s).sum()),float((p*s*s).sum())
    theta=brentq(lambda t:moments(t)[0]-mu,0.001,0.99999)
    mean, second=moments(theta)
    return theta,second-mean*mean

def local_limit_ratio(n,k):
    th,var=tilt(n,k)
    s=np.arange(1,n+1,dtype=float)
    ww=np.sqrt(s)*np.exp(s*np.log(th))
    p=np.zeros(n+1)
    p[1:]=ww/ww.sum()
    arr=np.array([1.0]+[0.0]*n)
    for j in range(k):
        arr=np.convolve(arr,p)[:n+1]
    return th, float(arr[n]*sqrt(2*pi*k*var))

def fixed_ratio(n,k):
    C=gamma(1.5)**k/(k*gamma(1.5*k))
    return intrinsic_formula(n,k)/(C*n**(1.5*k))

def test():
    obs=0
    for n in range(3,10):
        for k in range(1,n+1):
            a=direct_intrinsic(n,k)
            b=intrinsic_formula(n,k)
            assert abs(a-b)<2.e-8*max(1,a),(n,k,a,b)
            obs+=1
    assert abs(intrinsic_formula(4,2)-(4+4*sqrt(3)))<1.e-10
    assert abs(intrinsic_formula(5,1)-5*sqrt(5))<1.e-9
    assert abs(intrinsic_formula(6,6)-1)<1.e-9
    ratio=fixed_ratio(500,2)
    assert .99<ratio<1.02,ratio
    th, r=local_limit_ratio(300,120)
    assert 0.93<r<1.07,(th,r)
    print('DIRECT_FOREST_CASES',obs)
    print('C4_SECOND_INTRINSIC_VOLUME',intrinsic_formula(4,2))
    print('FIXED_CODIM_2_RATIO_n500',ratio)
    print('LINEAR_DENSITY_RATIO_n300_k120',r,'theta',th)
    print('VERIFY_OK')
if __name__=='__main__': test()
