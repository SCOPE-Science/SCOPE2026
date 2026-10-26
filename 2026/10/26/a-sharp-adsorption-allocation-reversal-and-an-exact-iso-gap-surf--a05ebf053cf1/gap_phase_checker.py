"""Numerical checks for the five-state reversible adsorption spectral-gap theorem.
Run: python3 gap_phase_checker.py
Requires numpy, scipy, and sympy; numerical checks supplement, not replace, the proof.
"""
import math
import numpy as np
from scipy.linalg import eigh
import sympy as sp


def balanced_gap(B, d):
    t = 2 + 2*d + B
    # stable small-root formula
    return 4*d/(t + math.sqrt(t*t-16*d))


def eigen_gap(a, b, d, M):
    assert min(a,b,d,M)>0
    conductances=np.array((a,1.,1.,b))
    K=np.zeros((5,5))
    for i,c in enumerate(conductances):
        K[i,i]+=c
        K[i+1,i+1]+=c
        K[i,i+1]-=c
        K[i+1,i]-=c
    weights=np.diag((a/d,1.,M,1.,b/d))
    vals=eigh(K,weights,eigvals_only=True,check_finite=True)
    assert abs(vals[0]) < 1e-9*max(1.,vals[1])
    return float(vals[1]),K,weights


def secular(lam,a,b,d,M):
    B=a+b
    gamma=lam/(d-lam)
    x=1-lam
    return (2-M*lam)*(x*x-gamma*B*x+gamma*gamma*a*b)-(2*x-gamma*B)


def symbolic_determinant_check():
    a,b,d,M,z=sp.symbols('a b d M z',nonzero=True)
    W=sp.diag(a/d,1,M,1,b/d)
    c=(a,sp.Integer(1),sp.Integer(1),b)
    K=sp.zeros(5)
    for i,t in enumerate(c):
        K[i,i]+=t
        K[i+1,i+1]+=t
        K[i,i+1]-=t
        K[i+1,i]-=t
    gamma=z/(d-z)
    u=1-z
    F=(2-M*z)*(u*u-gamma*(a+b)*u+gamma**2*a*b)-(2*u-gamma*(a+b))
    diff=sp.factor(sp.det(K-z*W)-(a*b*(d-z)**2/d**2)*F)
    assert diff==0, diff


def run():
    symbolic_determinant_check()
    rng=np.random.default_rng(20261023)
    n=0
    for z in range(600):
        B=float(np.exp(rng.uniform(-2.6,2.5)))
        d=float(np.exp(rng.uniform(-2.5,2.5)))
        ell=balanced_gap(B,d)
        assert 0 < ell < min(1,d)
        Mc=2/ell
        regime=z%3
        M=Mc * (0.25 if regime==0 else (4.0 if regime==1 else 1.0))
        chosen=[]
        for p in (0.,0.07,0.16,0.31,0.47):
            a=B*(0.5+p)
            b=B-a
            lam,K,weights=eigen_gap(a,b,d,M)
            assert lam>0 and lam<d
            assert abs(secular(lam,a,b,d,M)) < 5e-7*(1+abs(lam))
            chosen.append(lam)
            n+=1
        assert abs(chosen[0]-ell)<1e-8
        if regime==0:
            assert all(chosen[j+1] > chosen[j]+1e-12 for j in range(4)),(B,d,M,chosen)
        elif regime==1:
            assert all(chosen[j+1] < chosen[j]-1e-12 for j in range(4)),(B,d,M,chosen)
        else:
            assert max(abs(v-ell) for v in chosen)<1e-9,(B,d,M,chosen)
    # Distinct phase boundaries and the all-allocations plateau.
    for B,d in [(1.,3.),(5.,3.),(0.1,3.),(1.,0.1),(0.01,0.01),(100.,100.)]:
        ell=balanced_gap(B,d)
        M=2/ell
        for p in np.linspace(0.005,0.995,101):
            lam,_,_=eigen_gap(B*p,B*(1-p),d,M)
            assert abs(lam-ell)<1e-8*(1+ell)
            n+=1
    # Independent tridiagonal residual identity near arbitrary parameter values.
    for _ in range(500):
        B=float(np.exp(rng.uniform(-2.,2.)))
        d=float(np.exp(rng.uniform(-2.,2.)))
        M=float(np.exp(rng.uniform(-2.,3.)))
        a=B*float(rng.uniform(0.02,0.98))
        b=B-a
        lam,K,W=eigen_gap(a,b,d,M)
        full=np.linalg.det(K-lam*W)
        secular_reduced=(a*b*(d-lam)**2/d**2)*secular(lam,a,b,d,M)
        assert abs(full-secular_reduced)<1e-5*(1+np.max(np.abs(K)))**5
        n+=1
    print(f'PASS: one exact symbolic determinant identity; {n} numerical matrix/secular and allocation-phase comparisons; three regimes and six critical plateaus')


if __name__=='__main__':
    run()
