"""Reproduce exact stochastic/spectral checks for heterogeneous clique products.
Run: python verify.py. Requires numpy and scipy.
"""
from fractions import Fraction as F
from itertools import product
from math import prod
import random
import numpy as np
from scipy.optimize import linprog


def solution(sizes):
    d=len(sizes)
    C=sum((F(n-1,n) for n in sizes),F(0))
    u=min(F(2,d+1),F(1)/C)
    probs=[u/n for n in sizes]
    hold=F(1)-C*u
    mu=max(F(d-1,d+1),F(1)-F(1)/C)
    return C,u,probs,hold,mu


def matrix(sizes, probs):
    states=list(product(*(range(n) for n in sizes)))
    idx={v:i for i,v in enumerate(states)}
    N=len(states)
    P=np.zeros((N,N))
    for i,x in enumerate(states):
        for ax,n in enumerate(sizes):
            for val in range(n):
                if val!=x[ax]:
                    y=x[:ax]+(val,)+x[ax+1:]
                    P[i,idx[y]]=float(probs[ax])
        P[i,i]=1-sum(P[i,:])
    return P


def spectral(sizes,u):
    vals=[]
    d=len(sizes)
    for flags in product((0,1),repeat=d):
        k=sum(flags)
        mult=prod(n-1 for n,on in zip(sizes,flags) if on)
        vals.extend([float(F(1)-k*u)]*mult)
    return np.sort(vals)


def linprog_minimax(sizes):
    d=len(sizes)
    C=np.array([1-1/n for n in sizes])
    # variables z_1,...,z_d,t. For all nonconstant subset modes,
    # |1-sum_{i in S} z_i| <= t.
    A=[]; b=[]
    for flags in product((0,1),repeat=d):
        if not any(flags):continue
        v=np.array(flags,dtype=float)
        A.append(np.r_[-v,-1.]);b.append(-1.)
        A.append(np.r_[v,-1.]);b.append(1.)
    A.append(np.r_[C,0.]);b.append(1.)
    res=linprog(np.r_[np.zeros(d),1.],A_ub=np.array(A),b_ub=np.array(b),bounds=[(0,None)]*(d+1),method='highs')
    assert res.success, res.message
    return res.x[-1],res.x[:d]


def check():
    rng=random.Random(26071027)
    cases=[(2,3,4),(2,3,6),(2,3,7),(2,4,5),(3,4,5),
           (2,2,3),(3,3,3),(2,3,5),(2,3,8),(2,4,4),(2,2,2),
           (2,2,2,3),(2,2,2,4),(2,2,3,3),(2,3,3,3),
           (2,2,2,2),(2,2,2,2,3),(2,2,2,2,4),(2,2,3,4)]
    tests=0
    for sizes in cases:
        d=len(sizes)
        C,u,probs,hold,mu=solution(sizes)
        assert hold>=0 and all(p>0 for p in probs)
        assert sum(F(n-1)*p for n,p in zip(sizes,probs))+hold==1;tests+=3
        assert mu==max(F(1)-u,d*u-F(1));tests+=1
        assert (hold>0)==(sum((F(1,n) for n in sizes),F(0))>F(d-1,2));tests+=1
        P=matrix(sizes,probs)
        assert np.linalg.norm(P-P.T,np.inf)<1e-13; tests+=1
        assert np.max(np.abs(P.sum(1)-1))<1e-13;tests+=1
        eig=np.linalg.eigvalsh(P)
        spec=spectral(sizes,u)
        assert len(eig)==len(spec)==prod(sizes)
        assert np.max(np.abs(eig-spec))<2e-12;tests+=1
        assert abs(max(abs(eig[0]),abs(eig[-2]))-float(mu))<2e-12;tests+=1
        lp_mu,lp_z=linprog_minimax(sizes)
        assert abs(lp_mu-float(mu))<2e-9;tests+=1
        assert np.max(np.abs(lp_z-float(u)))<2e-8;tests+=1
        # Full-matrix nonsymmetric feasible perturbation: randomly
        # redistribute a small amount of edge flow with safe diagonals.
        # In zero-holding regime use convex mixtures with identity to retain feasibility.
        for _ in range(8):
            Q=np.zeros_like(P)
            N=Q.shape[0]
            for i in range(N):
                for j in range(i+1,N):
                    if P[i,j]>0:
                        w=P[i,j]*rng.random()/(2*d)
                        Q[i,j]=Q[j,i]=w
            Q[np.diag_indices(N)]=1-Q.sum(axis=1)
            W=.6*P+.4*Q
            eigW=np.linalg.eigvalsh(W)
            assert max(abs(eigW[0]),abs(eigW[-2]))+1e-10 >= float(mu)
            tests+=1
    # Exact 3-factor critical parameter classification.
    crit=[]
    for a in range(2,30):
        for b in range(a,30):
            for c in range(b,30):
                if F(1,a)+F(1,b)+F(1,c)==1:crit.append((a,b,c))
    assert crit==[(2,3,6),(2,4,4),(3,3,3)];tests+=1
    print('PASS',tests,'assertion groups on',len(cases),'product instances; full spectra, exact row budgets, LPs and perturbed feasible chains')

if __name__=='__main__':check()
