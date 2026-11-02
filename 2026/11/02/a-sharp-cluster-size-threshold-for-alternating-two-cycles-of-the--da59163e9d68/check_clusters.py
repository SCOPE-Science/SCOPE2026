#!/usr/bin/env python3
"""Standalone numerical cross-check of exact alternating two-cluster spectrum.
No external data or previous computations are required.
"""
import math
import numpy as np
from scipy.optimize import brentq

def model(t,k):
    return t+(k/len(t))*np.sin(t[None,:]-t[:,None]).sum(axis=1)

def derivative(t,k):
    n=len(t)
    c=np.cos(t[None,:]-t[:,None]); j=(k/n)*c
    np.fill_diagonal(j,0.)
    j[np.diag_indices(n)]=1-j.sum(axis=1)
    return j

def check(n,m,k):
    u=brentq(lambda u: 2*u/math.sin(u)-k,1e-6,math.pi/2-1e-9)
    p=m/n; q=1-p
    x=np.array([q*u]*m+[-p*u]*(n-m),dtype=float)
    y=np.array([-q*u]*m+[p*u]*(n-m),dtype=float)
    assert np.linalg.norm(model(x,k)-y)<1e-11
    assert np.linalg.norm(model(y,k)-x)<1e-11
    vals=np.sort(np.linalg.eigvalsh(derivative(y,k)@derivative(x,k)))
    expected=[1.,(1-k*math.cos(u))**2]
    expected +=[(1-k*(p+q*math.cos(u)))**2]*(m-1)
    expected +=[(1-k*(q+p*math.cos(u)))**2]*(n-m-1)
    assert np.allclose(vals,sorted(expected),atol=1e-12)
    pc=(math.sin(u)-u*math.cos(u))/(u*(1-math.cos(u)))
    is_stable=max(p,q)<pc
    transverse=[(1-k*math.cos(u))**2] + [ (1-k*(p+q*math.cos(u)))**2]*(m-1) +[(1-k*(q+p*math.cos(u)))**2]*(n-m-1)
    assert is_stable==(max(transverse)<1-1e-11)
    return (n,m,k,u,pc,is_stable,max(transverse))

if __name__=='__main__':
    for n,m in [(2,1),(3,1),(4,1),(4,2),(5,2),(6,2),(6,3),(7,2),(7,3),(8,3),(9,4)]:
        for k in [2.01,2.5,3.1]:
            print(check(n,m,k))
    print('All direct-map, direct-Jacobian and exact-spectrum checks passed.')
