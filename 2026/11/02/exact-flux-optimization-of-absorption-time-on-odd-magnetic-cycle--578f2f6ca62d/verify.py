#!/usr/bin/env python3
"""Numerically reproduce an exact mean-absorption identity on odd quantum cycles."""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov

def direct(n, j, phi, kappa, J):
    H=np.zeros((n,n),dtype=complex)
    for r in range(n):
        s=(r+1)%n
        H[r,s] += J*np.exp(1j*phi/n)
        H[s,r] += J*np.exp(-1j*phi/n)
    A=-1j*H
    A[0,0]-=kappa/2
    initial=np.zeros((n,n),dtype=complex)
    initial[j,j]=1
    X=solve_continuous_lyapunov(A,-initial)
    assert np.linalg.norm(A@X+X@A.conj().T+initial)<1e-8
    return X.trace().real

def formula(n,j,phi,kappa,J):
    sigma=j if j<=n//2 else j-n
    return n/kappa + sigma/(2*J*np.sin(phi)) + kappa*j*(n-j)/(8*J*J*np.sin(phi)**2)

def check():
    checks=0
    for n in (3,5,7,9,11):
        for phi,kappa,J in ((.41,.6,1.1),(-1.27,3.2,.8),(2.1,1.9,1.3),(-.8,.25,1.5)):
            for j in range(n):
                a=direct(n,j,phi,kappa,J)
                b=formula(n,j,phi,kappa,J)
                assert np.isclose(a,b,rtol=1e-8,atol=1e-8),(n,j,phi,a,b)
                checks+=1
        for j in range(1,n):
            val=sum((np.sin(np.pi*j*q/n)/np.sin(np.pi*q/n))**2 for q in range(1,n))
            assert abs(val-j*(n-j))<1e-8
            checks+=1
        J=1.2
        for j in (1,n//2,n-1):
            d=min(j,n-j);L=max(j,n-j)
            for kappa in (J/L,2*J/L,4*J/L):
                sign=-1 if j<=n//2 else 1
                optimal_s=min(1,kappa*L/(2*J))
                opt=sign*np.arcsin(optimal_s)
                b=formula(n,j,opt,kappa,J)
                x=min(2*J/(kappa*L),1e8)
                target= n/kappa-d/(2*J)*x+kappa*d*L/(8*J*J)*x*x if x>=1 else n/kappa-d/(2*J)+kappa*d*L/(8*J*J)
                # At weak absorption optimal_s corresponds to x>=1; at strong absorption x=1.
                x=max(1,2*J/(kappa*L))
                target=n/kappa-d*x/(2*J)+kappa*d*L*x*x/(8*J*J)
                assert abs(b-target)<1e-8
                grid=np.linspace(-np.pi+0.02,np.pi-0.02,2000)
                for phi in grid[::71]:
                    if abs(np.sin(phi))>.03:
                        assert formula(n,j,phi,kappa,J)>=b-1e-7
                checks+=1
    print(f"PASS: {checks} independently computed cases and identities")

if __name__=='__main__':
    check()
