#!/usr/bin/env python3
"""Numerical consistency checks for a one-coordinate phase perturbation of a complex Hadamard symbol."""
import numpy as np
from scipy.optimize import minimize, minimize_scalar

def closed_formula(n, z):
    h=abs(n-1+z)
    if n==2:
        return (1+h/2)**.5
    a=(n-2)*np.sqrt(n)
    d=n-1
    b=d*d-1+2*d*h
    return (a*h+np.sqrt((a*a+b)*((d+h)**2-1)))/b

def f_restricted(n,z, y):
    h=abs(n-1+z)
    return ((n-2)*np.sqrt(n)+np.sqrt(y*y+2*(n-1+h)*y+1))/(y+n-1)

def objective(H,z,x):
    n=len(H)
    p=np.exp(x[:n]-max(x[:n]));p/=sum(p)
    q=np.exp(x[n:]-max(x[n:]));q/=sum(q)
    B=H.copy(); B[0,0]=z*H[0,0]
    m=np.sqrt(p)[:,None]*B*np.sqrt(q)[None,:]
    return np.linalg.svd(m,compute_uv=False).sum()

if __name__=='__main__':
    rng=np.random.default_rng(50317)
    total=0
    for n in [2,3,4,5,6,8]:
        i,j=np.meshgrid(np.arange(n),np.arange(n),indexing='ij')
        H=np.exp(2j*np.pi*i*j/n)
        for theta in [0.0,0.22,0.81,1.7,np.pi]:
            z=np.exp(1j*theta)
            target=closed_formula(n,z)
            opt=minimize_scalar(lambda y:-f_restricted(n,z,y),bounds=(1e-7,4),method='bounded',options={'xatol':1e-12})
            assert abs(-opt.fun-target)<2e-9,(n,theta,target,-opt.fun)
            best=0
            for it in range(3):
                x=np.zeros(2*n) if it==0 else rng.normal(size=2*n)
                res=minimize(lambda x:-objective(H,z,x),x,method='L-BFGS-B',options={'maxiter':300,'ftol':1e-12})
                best=max(best,-res.fun)
                assert -res.fun<=target+4e-8,(n,theta,-res.fun,target)
            assert abs(best-target)<4e-7,(n,theta,best,target)
            total+=1
            print('PASS',n,round(theta,5), 'norm',f'{target:.12f}', 'numerical',f'{best:.12f}')
    print('PASSED_CASES',total)
    # Complex Hadamard four-by-four family (not a real equivalence class)
    for angle in [0.3,1.1,2.3]:
        v=np.exp(1j*angle)
        H=np.array([[1,1,1,1],[1,v,-1,-v],[1,-1,1,-1],[1,-v,-1,v]],dtype=complex)
        assert np.max(abs(H@H.conj().T-4*np.eye(4)))<1e-12
        for phase in [0.25,1.3,2.8]:
            z=np.exp(1j*phase);target=closed_formula(4,z)
            best=-np.inf
            for it in range(3):
                x=np.zeros(8) if it==0 else rng.normal(size=8)
                res=minimize(lambda x:-objective(H,z,x),x,method='L-BFGS-B',options={'maxiter':250,'ftol':1e-12})
                best=max(best,-res.fun)
                assert -res.fun<=target+4e-8,(angle,phase,-res.fun,target)
            assert abs(best-target)<6e-7,(angle,phase,best,target)
            print('COMPLEX_HADAMARD_PASS',angle,phase,f'{target:.12f}')
    print('ALL_CHECKS_PASS')
