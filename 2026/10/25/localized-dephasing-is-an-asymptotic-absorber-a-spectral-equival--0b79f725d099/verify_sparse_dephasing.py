"""Finite-dimensional cross-checks for a site-dephasing/sink theorem.
Requires Python 3.10+, numpy and scipy. Run: python verify_sparse_dephasing.py
All mathematical conclusions for arbitrary size rely on the written proof.
"""
import math
import numpy as np
from scipy.linalg import eig, null_space

I_COUNT = 0
MAX_ERR = 0.

def check(H, absorbers, dephasers, initial_sites, kappa=0.87, gamma=1.31):
    global I_COUNT, MAX_ERR
    n = H.shape[0]
    I = np.eye(n)
    F = np.zeros((n, n))
    for s in absorbers: F[s, s] = gamma
    deph = []
    for s in dephasers:
        P = np.zeros((n,n));P[s,s] = 1
        deph.append(P)
    L = -1j * (np.kron(I,H)-np.kron(H.T,I)) - (np.kron(I,F)+np.kron(F.T,I))
    for P in deph:
        L += kappa*(np.kron(P.T,P)-.5*np.kron(I,P)-.5*np.kron(P.T,I))
    # The joint H-cyclic annihilator is the predicted protected sector.
    cols=[]
    for site in set(absorbers)|set(dephasers):
        x = I[:,site].copy()
        for _ in range(n):
            cols.append(x.copy());x=H@x
    B=np.stack(cols,axis=1)
    U=null_space(B.conj().T, rcond=1e-10)
    dark=U@U.conj().T
    eigenvalues, left, right = eig(L, left=True, right=True)
    neutral=np.flatnonzero(abs(eigenvalues.real)<1e-8)
    # Peripheral operator dimension includes coherences between protected eigenmodes.
    assert len(neutral)==U.shape[1]**2, (n,absorbers,dephasers,len(neutral), U.shape[1]**2)
    if neutral.size:
        R=right[:,neutral]; LL=left[:,neutral]
        P=R@np.linalg.inv(LL.conj().T@R)@LL.conj().T
    else:
        P=np.zeros_like(L)
    for site in initial_sites:
        rho=np.zeros((n,n),complex);rho[site,site]=1
        infstate=(P@rho.reshape(-1,order='F')).reshape(n,n,order='F')
        measured=np.trace(infstate).real
        expected=np.trace(dark@rho).real
        err=abs(measured-expected)
        assert err<1e-7,(n,absorbers,dephasers,site,measured,expected)
        I_COUNT+=1;MAX_ERR=max(MAX_ERR,err)
    return dark

for n in range(3,12):
    H=np.zeros((n,n))
    for j in range(n): H[j,(j+1)%n]=H[(j+1)%n,j]=1
    for s in range(1,n):
        U=check(H,[0],[s],range(n))
        g=math.gcd(n,2*s)
        assert abs(np.trace(U).real-(g-1)//2)<1e-7
        for a in range(n):
            expected=g/(2*n) if (2*a)%g else 0
            err=abs(U[a,a].real-expected)
            assert err<1e-7,(n,s,a,U[a,a].real,expected)
            I_COUNT+=1;MAX_ERR=max(MAX_ERR,err)

# Asymmetric connected positive-weight trees with several dephasing vertices.
for n in range(3,9):
    H=np.zeros((n,n))
    for j in range(n-1): H[j,j+1]=H[j+1,j]=(1+j%3)/2.
    for site in range(1,n):
        check(H,[0],[site],range(n))

# Star graph: surviving noiseless sectors are nontrivial but not symmetric
# around the initial state when the dephasing site changes.
for n in range(5,9):
    H=np.zeros((n,n))
    for j in range(1,n): H[0,j]=H[j,0]=1.+j/20.
    for f in [0,1]:
        for noisy in [[2],[3],[2,3]]:
            if f in noisy: continue
            check(H,[f],noisy,range(n))
print('PASS:',I_COUNT,'finite predictions, maximum absolute error:',format(MAX_ERR,'.3e'))
