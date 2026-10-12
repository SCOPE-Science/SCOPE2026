#!/usr/bin/env python3
"""Reproducible checks for the clique-core heterogeneous windmill theorem.
No external data, network access, or publication assumptions are used.
"""
import itertools
from fractions import Fraction
import numpy as np
import sympy as sp


def cells(a, blades):
    out=[tuple(range(a))]; start=a
    for t in blades:
        out.append(tuple(range(start,start+t)));start+=t
    return out


def matrix(a, blades, dtype=float):
    cls=cells(a,blades); n=sum(map(len,cls)); A=np.zeros((n,n),dtype=dtype)
    for C in cls:
        for x in C:
            for y in C:
                if x!=y:A[x,y]=1
    for x in cls[0]:
        for C in cls[1:]:
            for y in C:A[x,y]=A[y,x]=1
    return A


def es_minus(a,blades,exact=False):
    cls=cells(a,blades);n=sum(map(len,cls))
    E=sp.zeros(n) if exact else np.zeros((n,n))
    for C in cls:
        t=len(C)
        for x in C:
            for y in C:
                v= (int(x==y)-sp.Rational(1,t)) if exact else (float(x==y)-1/t)
                E[x,y]=v
    return E


def mixing(A):
    w,Q=np.linalg.eigh(A); clusters=[]
    for i in range(len(w)):
        if not clusters or abs(w[i]-w[clusters[-1][-1]])>2e-8:clusters.append([i])
        else:clusters[-1].append(i)
    M=np.zeros_like(A)
    for I in clusters:
        P=Q[:,I]@Q[:,I].T
        M+=P*P
    return (M+M.T)/2


def theoretical_kernel(a, blades):
    cls=cells(a,blades); n=sum(map(len,cls)); ans=[]
    for C in cls:
        if len(C)==2:
            z=np.zeros(n);z[C[0]]=1;z[C[1]]=-1;ans.append(z)
    return np.column_stack(ans) if ans else np.zeros((n,0))


def numeric_checks():
    cases=0; mins=[]; worst_k=0.; worst_proj=0.; worst_orth=0.;
    for a in range(1,6):
        for blades in itertools.product(range(2,6),repeat=2):
            if a==5 and sum(blades)>8:continue
            A=matrix(a,blades);n=len(A)
            M=mixing(A); E=es_minus(a,blades)
            Z=theoretical_kernel(a,blades); nullity=Z.shape[1]
            ev=np.linalg.eigvalsh(M)
            got=np.sum(ev<1e-7)
            assert got==nullity, ('rank',a,blades,got,nullity,ev)
            assert ev[nullity]>0.0
            if a>=2:assert ev[nullity]>=1/3-1e-8,(a,blades,ev)
            worst_k=max(worst_k,np.max(np.abs(M@Z)) if nullity else 0.)
            worst_proj=max(worst_proj,np.max(np.abs(E@E-E)),np.max(np.abs(A@E+E)))
            # Differences inside a 3-clique are EXACT 1/3 modes.
            for C in cells(a,blades):
                if len(C)==3:
                    z=np.zeros(n);z[C[0]]=1;z[C[1]]=-1
                    worst_orth=max(worst_orth,np.max(np.abs(M@z-z/3)))
            cases+=1
    return cases,worst_k,worst_proj,worst_orth


def exact_checks():
    examples=[(1,[2,2]),(1,[3,4]),(2,[2,3]),(3,[2,3]),(4,[3,4]),(2,[2,2,3])]
    tested=0
    for a,blades in examples:
        n=a+sum(blades);A=sp.Matrix(matrix(a,blades,dtype=int));E=es_minus(a,blades,True)
        assert E*E==E
        assert A*E==-E
        assert E.rank()==sum(t-1 for t in [a]+blades)
        assert (A+sp.eye(n)).rank()==n-E.rank()
        # Exact spectral profile of E∘E on each individual clique.
        F=E.multiply_elementwise(E)
        for C in cells(a,blades):
            t=len(C)
            ones=sp.zeros(n,1)
            for i in C:ones[i]=1
            if t>=2:assert F*ones==sp.Rational(t-1,t)*ones
            for x,y in zip(C[:-1],C[1:]):
                z=sp.zeros(n,1);z[x]=1;z[y]=-1
                assert F*z==sp.Rational(t-2,t)*z
        tested+=1
    return tested

if __name__=='__main__':
    ec=exact_checks()
    nc,k,p,o=numeric_checks()
    print(f'VERIFY_OK exact_projectors={ec} independent_graphs={nc} '
          f'max_null_residual={k:.3e} max_projector_residual={p:.3e} '
          f'max_three_clique_mode_residual={o:.3e}')
