#!/usr/bin/env python3
"""Independent finite checks of the marked Boolean-cube average-mixing rank law.
Requires numpy and sympy. Finite checks corroborate, rather than establish, the theorem.
"""
from math import comb, factorial, ceil
import numpy as np
import sympy as sp


def cube(d):
    N=1<<d
    A=np.zeros((N,N),dtype=int)
    for x in range(N):
        for i in range(d): A[x,x^(1<<i)]=1
    return A


def dark_exact(d):
    N=1<<d
    chars=np.array([[1 if ((x&t).bit_count()%2==0) else -1
                     for t in range(N)] for x in range(N)],dtype=int)
    K=sp.zeros(N)
    for j in range(1,d):
        ids=[t for t in range(N) if t.bit_count()==j]
        m=len(ids)
        X=sp.Matrix(chars[:,ids].tolist())
        v=X*sp.ones(m,1)
        F=(X*X.T-v*v.T/sp.Integer(m))/sp.Integer(N)
        K+=F.multiply_elementwise(F)
    rank=K.rank()
    assert rank == (N//2)-1, (d,rank)
    parity_even=[]
    for x in range(N): parity_even.append(1 if (x==0 or x==N-1) else 0)
    assert K*sp.Matrix(parity_even)==sp.zeros(N,1)
    return N*N, rank


def moment_exact(d,tau=sp.Rational(3,2)):
    A=sp.Matrix(cube(d).tolist())
    A[0,0]=tau
    N=1<<d
    H=A
    checked=0
    for j in range(d+1):
        if j: H=H*A*A
        for r in range(d+1):
            x=(1<<r)-1
            if r>j: assert H[x,x]==0,(d,j,r,H[x,x])
            if r==j: assert H[x,x]==tau*factorial(r)**2,(d,j,r,H[x,x])
            checked+=1
    return checked


def mixing_numeric(d,tau):
    H=cube(d).astype(float)
    H[0,0]=tau
    eigen,V=np.linalg.eigh(H)
    N=len(H)
    M=np.zeros((N,N))
    i=0
    while i<N:
        j=i+1
        while j<N and abs(eigen[j]-eigen[i])<1e-8: j+=1
        P=V[:,i:j]@V[:,i:j].T
        M+=P*P
        i=j
    s=np.linalg.eigvalsh(M)
    rank=np.count_nonzero(s>2e-9)
    expected=N//2 if tau==0 else N//2+ceil(d/2)
    assert rank==expected,(d,tau,rank,expected,s)
    assert abs(M.sum(axis=1).max()-1)<2e-12
    assert abs(M.sum(axis=1).min()-1)<2e-12
    return N*N


def main():
    entries=0; exact=0; moments=0; profiles=0
    for d in range(1,6):
        n2,r=dark_exact(d); exact+=1; entries+=n2
    for d in range(1,5): moments+=moment_exact(d)
    for d in range(1,7):
        for tau in [-2.0,-0.37,0.0,0.4,1.3]:
            entries+=mixing_numeric(d,tau);profiles+=1
    print(f'VERIFY_OK exact_dark_profiles={exact} moment_identities={moments} spectral_profiles={profiles} matrix_entries={entries} cube_orders=1..6')
if __name__=='__main__': main()
