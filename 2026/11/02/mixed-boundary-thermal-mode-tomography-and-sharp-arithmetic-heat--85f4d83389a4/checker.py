#!/usr/bin/env python3
"""Standalone numerical cross-checks for mixed-boundary modal-temperature tomography.
Run: python checker.py (requires NumPy and SciPy). Numerical checks supplement the proof.
"""
import math
import numpy as np
from scipy.linalg import solve_continuous_lyapunov


def transfer(n):
    M = 2*n + 1
    k = np.arange(n)[:, None]
    j = np.arange(n)[None, :]
    return (2/M)*(1+np.cos(np.pi*(2*k+1)*(2*j+1)/M))


def stiffness(n):
    H = 2*np.eye(n)
    H[0,0]=1
    for j in range(n-1):
        H[j,j+1]=H[j+1,j]=-1
    return H


def test():
    rng=np.random.default_rng(310501)
    matrix_checks=0
    arith_checks=0
    dyn_checks=0
    for n in range(2,151):
        M=2*n+1
        q=transfer(n)
        j=np.ones((n,n))
        np.testing.assert_allclose(q,q.T,rtol=0,atol=3e-14)
        np.testing.assert_allclose(q@q,(np.eye(n)+2*j)/M,rtol=0,atol=4e-12)
        np.testing.assert_allclose(q.sum(axis=0),np.ones(n),rtol=0,atol=1e-12)
        t=rng.uniform(0.1,4,size=n)
        theta=q@t
        rec=M*(q@theta)-2*theta.sum()
        np.testing.assert_allclose(rec,t,rtol=0,atol=6e-11)
        delta=rng.standard_normal(n);delta-=delta.mean()
        np.testing.assert_allclose(np.linalg.norm(q@delta)*np.sqrt(M),np.linalg.norm(delta),rtol=5e-11,atol=1e-12)
        matrix_checks+=5
        for k in range(n):
            g=math.gcd(2*k+1,M)
            hi=2/M*(1+math.cos(math.pi*g/M))
            lo=(0 if g>1 else 2/M*(1-math.cos(2*math.pi/M)))
            np.testing.assert_allclose(q[k].max(),hi,atol=5e-14,rtol=0)
            np.testing.assert_allclose(q[k].min(),lo,atol=5e-14,rtol=0)
            assert int(np.sum(np.abs(q[k]-hi)<2e-13))==g
            if g>1:
                assert int(np.sum(np.abs(q[k])<2e-13))==(g-1)//2
            arith_checks+=4 if g>1 else 3
    for n in range(2,13):
        q=transfer(n)
        lam,U=np.linalg.eigh(stiffness(n))
        assert np.all(lam>0)
        np.testing.assert_allclose(U.T**2,q,rtol=0,atol=1e-12)
        for _ in range(4):
            t=rng.uniform(0.2,4,size=n)
            friction=float(rng.uniform(0.2,3))
            kap=float(rng.uniform(0.2,3))
            A=np.block([[np.zeros((n,n)),np.eye(n)],[-kap*stiffness(n),-friction*np.eye(n)]])
            cov_noise=np.zeros((2*n,2*n))
            cov_noise[n:,n:]=2*friction*np.diag(t)
            cov=solve_continuous_lyapunov(A,-cov_noise)
            modal_var=np.diag(U.T@cov[n:,n:]@U)
            np.testing.assert_allclose(modal_var,q@t,atol=1e-10,rtol=2e-10)
            dyn_checks+=1
    print('PASS: %s transfer/reconstruction/norm checks; %s modular-extrema/count checks; %s independent Lyapunov checks.'%(matrix_checks,arith_checks,dyn_checks))

if __name__=='__main__':test()
