"""Exact and numerical checks for the optimal symmetric stochastic kernel on K_(1,m,m).
Run with python verify.py; requires SymPy and NumPy.
"""
from random import Random
import sympy as sp
import numpy as np

def kernel(m, a, b):
    N=2*m+1
    P=sp.zeros(N)
    for i in range(1,N):
        P[0,i]=P[i,0]=a
    for i in range(1,m+1):
        for j in range(m+1,2*m+1):
            P[i,j]=P[j,i]=b
    for i in range(N):
        P[i,i]=1-sum(P[i,j] for j in range(N) if j!=i)
    return P

def exact():
    count=0
    for m in range(2,10):
        a=sp.Rational(1,2*m)
        b=sp.Rational(2*m-1,3*m*m)
        mu=sp.Rational(2*m-1,6*m)
        P=kernel(m,a,b)
        assert all(P[i,j]>=0 for i in range(P.rows) for j in range(P.cols))
        assert P==P.T and P*sp.ones(P.rows,1)==sp.ones(P.rows,1)
        lam=P.eigenvals()
        pred={sp.Integer(1):1,mu:2*m-2, -mu:1, -sp.Rational(1,2*m):1}
        if m==2:
            pred[-mu]=2
        # Merge repeated eigenvalues in multiplicity map (m=2 only)
        actual={v:int(k) for v,k in lam.items()}
        assert actual==pred,(m, actual, pred)
        count+=len(actual)
    return count

def stress():
    rng=Random(124981)
    count=0
    for m in range(2,13):
        a=1/(2*m)
        b=(2*m-1)/(3*m*m)
        opt=(2*m-1)/(6*m)
        Pstar=np.array(kernel(m,sp.Rational(1,2*m),sp.Rational(2*m-1,3*m*m)), dtype=float)
        eig=np.linalg.eigvalsh(Pstar)
        assert abs(max(abs(eig[:-1]))-opt)<1e-10
        count+=1
        for k in range(120):
            n=2*m+1
            M=np.zeros((n,n))
            for i in range(n):
                for j in range(i+1,n):
                    if (i==0 or j==0) or (1<=i<=m and m+1<=j<=2*m):
                        M[i,j]=M[j,i]=rng.random()
            # guarantee symmetric stochastic with nonnegative diagonal after safe row scaling
            M*=1.0/max(1.,max(np.sum(M,axis=1)))
            np.fill_diagonal(M,1-M.sum(axis=1))
            e=np.linalg.eigvalsh(M)
            assert max(abs(e[:-1]))>=opt-1.e-10,(m,k,max(abs(e[:-1])),opt)
            count+=1
    return count

if __name__=='__main__':
    print('exact distinct-eigenvalue counts:',exact())
    print('full-matrix checks:',stress())
    print('PASS')
