#!/usr/bin/env python3
"""Finite tests for a graph-edge lattice norm; analytical proof is separate.

Run: python3 verify.py
Requires sympy, numpy and scipy.
"""
from fractions import Fraction
from math import sqrt
import numpy as np
import sympy as sp
from scipy.linalg import null_space
from scipy.optimize import minimize, minimize_scalar


def graph_edges(a,b):
    groups=(range(0,a),range(a,2*a),range(2*a,2*a+b))
    E=[]; kind=[]
    for i in range(3):
        for j in range(i+1,3):
            for u in groups[i]:
                for v in groups[j]:
                    E.append((u,v)); kind.append(0 if (i,j)==(0,1) else 1)
    return E,np.array(kind)


def formula(a,b,s):
    B=(b-1)/sqrt(b)+sqrt(1/b+1/(2*a))
    return (2*(a-1)*sqrt(1+s)+sqrt(1+3*s))/sqrt(2*a)+B*sqrt(1-s)


def optimal(a,b):
    if b>=2*a+2:
        return 0.,formula(a,b,0.)
    r=minimize_scalar(lambda x:-formula(a,b,x),bounds=(0,1),method='bounded',options={'xatol':1e-14})
    return r.x,-r.fun


def weighted_laplacian(E,kind,a,b,s,exact=False):
    n=2*a+b
    if exact:
        x=sp.Rational(s,a*a); y=sp.Rational(1-s,2*a*b)
        M=sp.zeros(n)
    else:
        x=s/(a*a); y=(1-s)/(2*a*b)
        M=np.zeros((n,n))
    for (u,v),k in zip(E,kind):
        w=x if k==0 else y
        M[u,u]+=w; M[v,v]+=w; M[u,v]-=w; M[v,u]-=w
    return M


def exact_checks():
    count=0
    for a in (2,3,4):
        for b in (1,2,3,4):
            E,kind=graph_edges(a,b)
            for s in (sp.Rational(0),sp.Rational(1,5),sp.Rational(2,3)):
                M=weighted_laplacian(E,kind,a,b,s,exact=True)
                x=(1+s)/(2*a)
                y=(1-s)/b
                z=(1+3*s)/(2*a)
                w=(2*a+b)*(1-s)/(2*a*b)
                expected={sp.Rational(0):1}
                for eig,mult in ((x,2*(a-1)),(y,b-1),(z,1),(w,1)):
                    if mult:
                        eig=sp.factor(eig)
                        expected[eig]=expected.get(eig,0)+mult
                actual=M.eigenvals()
                assert actual==expected,(a,b,s,actual,expected)
                count+=1
    return count


def spectral_and_gradient(Z,weight):
    M=np.einsum('e,ei,ej->ij',weight,Z,Z)
    lam,U=np.linalg.eigh(M)
    assert min(lam)>1e-12,min(lam)
    value=float(np.sqrt(lam).sum())
    inverse=(U/np.sqrt(lam))@U.T
    gradient=.5*np.einsum('ei,ij,ej->e',Z,inverse,Z)
    return value,gradient


def numerical_checks():
    checked=0; witness=0
    for a,b in ((2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),
                (3,4),(3,7),(3,8),(4,3),(4,9),(4,10),(5,11),(5,12)):
        E,kind=graph_edges(a,b)
        n=2*a+b; dim=n-1
        V=np.zeros((len(E),n))
        for j,(u,v) in enumerate(E): V[j,u]=1;V[j,v]=-1
        Q=null_space(np.ones((1,n)))
        Z=V@Q
        s,claimed=optimal(a,b)
        weight=np.where(kind==0,s/(a*a),(1-s)/(2*a*b))
        vv,_=spectral_and_gradient(Z,weight)
        assert abs(vv-claimed)<1e-8,(a,b,vv,claimed)
        # Unrestricted non-orbit-constrained optimization in the edge simplex.
        if len(E)<=120:
            opt=minimize(lambda z:tuple(-u for u in spectral_and_gradient(Z,z)),weight,
                jac=True,method='SLSQP',bounds=[(0,1)]*len(E),
                constraints={'type':'eq','fun':lambda z:sum(z)-1,'jac':lambda z:np.ones(len(z))},
                options={'ftol':2e-11,'maxiter':240})
            assert opt.success,(a,b,opt.message)
            assert abs(-opt.fun-claimed)<2e-7,(a,b,opt.fun,claimed)
            checked+=1
        # A witness in the original finite weak-two-summable family:
        # Z_witness has columns of a polar factor of C=[sqrt(mu_e) b_e].
        C=(np.sqrt(weight)[:,None]*Z).T
        U,svals,VT=np.linalg.svd(C,full_matrices=False)
        P=U@VT
        assert np.linalg.norm(P@P.T,ord=2)<1+1e-9
        score=sqrt(sum(np.max(np.abs(Z@P[:,j]))**2 for j in range(len(E))))
        assert score>=claimed-2e-7,(a,b,score,claimed)
        assert score<=claimed+2e-7,(a,b,score,claimed)
        witness+=1
    return checked,witness

if __name__=='__main__':
    n=exact_checks()
    p,w=numerical_checks()
    print(f'PASS: {n} exact rational Laplacian-spectrum tests')
    print(f'PASS: {p} unrestricted edge-design optimizations')
    print(f'PASS: {w} norm-attaining polar-factor witnesses in the defining inequality')
