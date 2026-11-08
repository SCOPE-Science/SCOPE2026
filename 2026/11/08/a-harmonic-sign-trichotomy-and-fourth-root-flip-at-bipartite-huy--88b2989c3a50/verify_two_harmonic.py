#!/usr/bin/env python3
"""Reproducible numerical stress tests for a two-harmonic phase-network flip.

This is a finite smoke test, not a proof of the universal theorem. Uses NumPy/SciPy.
"""
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import root


def laplacian(n, edges):
    L = np.zeros((n,n))
    for i,j,a in edges:
        L[i,i] += a; L[j,j] += a
        L[i,j] -= a; L[j,i] -= a
    return L


def coupling(u, edges, kappa):
    z = np.zeros_like(u)
    for i,j,a in edges:
        d = u[i]-u[j]
        t = a*(np.sin(d)+kappa*np.sin(3*d))
        z[i] += t; z[j] -= t
    return z


def jacobian(u, h, edges, kappa):
    n = len(u)
    J = np.eye(n)
    for i,j,a in edges:
        d = u[i]-u[j]
        t=h*a*(np.cos(d)+3*kappa*np.cos(3*d))
        J[i,i]-=t; J[j,j]-=t
        J[i,j]+=t; J[j,i]+=t
    return J


def case(n, edges, kappa, epsilon):
    vals,vecs=eigh(laplacian(n,edges))
    lam=vals[-1]; v=vecs[:,-1]
    Q=sum(a*(v[i]-v[j])**4 for i,j,a in edges)
    R=sum(a*(v[i]-v[j])**6 for i,j,a in edges)
    alpha=1+3*kappa; beta=1+27*kappa
    assert alpha>0 and Q>0 and R>0
    h=2/(alpha*lam)+epsilon
    if abs(beta)>1e-9:
        s=np.sqrt(3*alpha**2*lam**2*epsilon/(beta*Q))
    else:
        s=(60*alpha**2*lam**2*epsilon/(8*R))**.25
    def residual(x):return 2*x-h*coupling(x,edges,kappa)
    result=root(residual,s*v,tol=1e-12)
    assert np.linalg.norm(result.fun,np.inf)<2e-10, (result.message, kappa, epsilon)
    u=result.x-result.x.mean()
    assert np.linalg.norm(u)>1e-4, (kappa, epsilon)
    assert np.linalg.norm(residual(-u),np.inf)<2e-10
    amp=abs(u@v)
    assert abs(amp/s-1)<.04, (kappa,epsilon,amp,s)
    eig=np.linalg.eigvalsh(jacobian(u,h,edges,kappa))
    neutral=eig[np.abs(eig-1)<1e-7]
    assert len(neutral)==1
    e=eig[np.abs(eig-1)>=1e-7]
    assert len(e)==n-1
    if epsilon>0:assert np.max(np.abs(e))<1, (kappa,epsilon,e)
    else:assert np.min(e)<-1, (kappa,epsilon,e)
    return amp/s, e[0], Q, R


def main():
    graphs=[(2,[(0,1,1.)],'edge'),
            (4,[(0,1,1.),(1,2,1.3),(2,3,.8)],'weighted_path'),
            (5,[(0,j,1+.1*j) for j in range(1,5)],'weighted_star')]
    tests=[(-.08,-.00001), (-1/27,+.000002),(.02,+.00001)]
    total=0
    for n,edges,name in graphs:
        for kappa,eps in tests:
            amp,crit,Q,R=case(n,edges,kappa,eps)
            print(f'{name} kappa={kappa:+.9f} epsilon={eps:+.7f} amplitude_ratio={amp:.6f} eigen_min={crit:.8f}')
            total+=8
    print(f'VERIFY_OK graphs={len(graphs)} regimes={len(tests)} checks={total}')

if __name__=='__main__':main()
