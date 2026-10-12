"""Standalone finite-dimensional checks of odd SSH dark-mode arithmetic.
Run: python artifacts/verify.py. Numerical tests corroborate; the general proof is analytic.
"""
import itertools
import math
import numpy as np
from scipy.linalg import expm


def construct(M, a, b, losses):
    L=2*M+1
    H=np.zeros((L,L),dtype=float)
    for u in range(M):
        H[2*u,2*u+1]=H[2*u+1,2*u]=a
        H[2*u+1,2*u+2]=H[2*u+2,2*u+1]=b
    Gamma=np.zeros((L,L),dtype=float)
    for k,rate in losses.items(): Gamma[2*k-1,2*k-1]=rate
    G=-1j*H-0.5*Gamma
    return H,G


def predicted_projector(M,a,b,sites):
    H,_=construct(M,a,b,{k:1. for k in sites})
    w,v=np.linalg.eigh(H)
    dim=2*M+1
    P=np.zeros((dim,dim),dtype=complex)
    for j in range(dim):
        if max(abs(v[2*k-1,j]) for k in sites)<1e-8:
            P += np.outer(v[:,j],v[:,j].conj())
    return P

cases=0
for M in range(1,12):
    S0=list(range(1,M+1))
    groups=[c for q in range(1,min(3,M)+1) for c in itertools.combinations(S0,q)]
    for ks in groups:
        g=math.gcd(M+1,*ks)
        for a,b in [(1.,1.),(0.7,1.3),(2.2,0.6)]:
            H,G=construct(M,a,b,{k:0.3+0.23*k for k in ks})
            w,v=np.linalg.eigh(H)
            mask=np.array([max(abs(v[2*k-1,j]) for k in ks)<1e-8 for j in range(2*M+1)])
            assert int(np.sum(mask))==2*g-1,(M,ks,a,b,mask,g)
            E=np.sort(w[mask]); predicted=[0.0]
            for j in range(1,g):
                r=(M+1)//g*j
                val=math.sqrt(a*a+b*b+2*a*b*math.cos(math.pi*r/(M+1)))
                predicted.extend([-val,val])
            assert np.allclose(E,sorted(predicted),atol=1e-8),(M,ks,E,predicted)
            P=v[:,mask]@v[:,mask].conj().T
            for ell in range(1,M+1):
                plateau=float(P[2*ell-1,2*ell-1].real)
                expected=0 if ell%g==0 else g/(M+1)
                assert abs(plateau-expected)<3e-10,(M,ks,ell,plateau,expected)
            # Contraction property and no additional undamped non-Hermitian eigenvalues.
            z=np.linalg.eigvals(G)
            assert np.sum(abs(z.real)<1e-8)==2*g-1,(M,ks,a,b,z)
            assert np.max(z.real)<1e-7
            cases+=1

# Dynamical plateau at long time for two nontrivial commensurate traps.
for M,ks,ell in [(5,(2,),1),(11,(3,6),1),(11,(3,6),3),(9,(2,4),5)]:
    H,G=construct(M,0.9,1.2,{k:1.5 for k in ks})
    g=math.gcd(M+1,*ks)
    v=np.zeros(2*M+1,dtype=complex); v[2*ell-1]=1
    t=20000.0
    out=expm(t*G)@v
    observed=np.vdot(out,out).real
    expected=0.0 if ell%g==0 else g/(M+1)
    assert abs(observed-expected)<3e-5,(M,ks,ell,observed,expected)
print('VERIFY_OK', cases, 'clean-spectrum, dark-space, survival, and non-Hermitian checks')
