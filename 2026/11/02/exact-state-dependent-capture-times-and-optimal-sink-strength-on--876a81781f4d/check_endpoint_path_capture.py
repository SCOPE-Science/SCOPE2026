#!/usr/bin/env python3
"""Independent finite-dimensional checks of endpoint capture on a uniform quantum path.

Requires numpy and scipy. No downloaded data are used.
"""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov


def kernels(n):
    f=np.zeros((n,n),float)
    g=np.zeros((n,n),float)
    c=np.zeros((n,n),complex)
    for a in range(n):
        for b in range(n):
            i=min(a,b)+1
            j=max(a,b)+1
            if (j-i)%2 == 0:
                f[a,b]=i*(n+1-j)
                g[a,b]=i*(n-j)
            elif a<b:
                c[a,b]=-0.5j*i
            else:
                c[a,b]=0.5j*i
    return f,g,c


def claimed(n,J,kappa):
    f,g,c=kernels(n)
    return f/kappa+kappa*g/(4*J**2)+c/J


def generator(n,J,kappa):
    h=np.diag(np.full(n-1,J),1)+np.diag(np.full(n-1,J),-1)
    a=-1j*h.astype(complex)
    a[-1,-1]-=kappa/2
    return a


def exact_structural_check(n):
    f,g,c=kernels(n)
    s=np.diag(np.ones(n-1),1)+np.diag(np.ones(n-1),-1)
    q=np.zeros((n,n));q[-1,-1]=1
    assert np.max(np.abs(s@f-f@s))<1e-12
    assert np.max(np.abs(1j*(s@c-c@s)-(q@f+f@q)/2+np.eye(n)))<1e-12
    assert np.max(np.abs(1j*(s@g-g@s)-2*(q@c+c@q)))<1e-12
    assert np.max(np.abs(q@g+g@q))<1e-12
    eig_b=np.linalg.eigvalsh(g)
    assert abs(eig_b[0])<1e-9 and np.min(eig_b[1:])>1e-8
    assert np.min(np.linalg.eigvalsh(f))>1e-8


def main():
    for n in range(2,31):
        exact_structural_check(n)
    rng=np.random.default_rng(20261026)
    tests=0
    maxerr=0.0
    for n in range(2,14):
        for J in (0.37, 1.0, 2.3):
            for kappa in (0.2,0.75,1.35,4.0,9.0):
                A=generator(n,J,kappa)
                M=claimed(n,J,kappa)
                num=solve_continuous_lyapunov(A.conj().T,-np.eye(n))
                resid=np.max(np.abs(A.conj().T@M+M@A+np.eye(n)))
                err=np.max(np.abs(num-M))
                maxerr=max(maxerr,err,resid)
                assert err<2e-8 and resid<2e-10
                assert np.max(np.real(np.linalg.eigvals(A)))<-1e-10
                for _ in range(5):
                    v=rng.normal(size=n)+1j*rng.normal(size=n)
                    v/=np.linalg.norm(v)
                    tq=np.vdot(v,M@v).real
                    assert tq>0
                    assert abs(tq-np.vdot(v,num@v).real)<2e-8
                    tests+=1
    print('STRUCTURAL_DIMENSIONS=29')
    print('NUMERIC_N_J_K_SETS=180')
    print('COHERENT_STATE_COMPARISONS='+str(tests))
    print('MAX_ABSOLUTE_MATRIX_OR_EQUATION_ERROR='+format(maxerr,'.4g'))
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
