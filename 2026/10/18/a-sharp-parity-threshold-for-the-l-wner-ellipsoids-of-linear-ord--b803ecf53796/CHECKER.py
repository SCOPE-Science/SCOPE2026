#!/usr/bin/env python3
"""Exact covariance and contact checks for parity-restricted ordering polytopes.
Run: python3 CHECKER.py  (requires only Python and SymPy).
"""
from itertools import permutations, combinations
from math import factorial
import sympy as S

def objects(n):
    edges = list(combinations(range(n), 2))
    M=len(edges)
    B=S.zeros(n,M)
    for j,(a,b) in enumerate(edges):
        B[a,j]=1; B[b,j]=-1
    T=(S.eye(M)+B.T*B)/3
    H=S.zeros(M)
    if n in (4,5):
        for j,e in enumerate(edges):
            for k,f in enumerate(edges):
                if len(set(e+f)) != 4: continue
                w=e+f
                sg=(-1)**sum(w[a]>w[b] for a in range(4) for b in range(a+1,4))
                if n==5:
                    h=(set(range(n))-set(w)).pop()
                    sg *= (-1)**h
                H[j,k]=sg
    c={4:S.Rational(1,3), 5:S.Rational(1,15)}.get(n,S.Integer(0))
    return edges,B,T,H,T+c*H

def exact_moments(n,even_only):
    edges,B,T,H,C=objects(n)
    M=len(edges)
    W=[]
    for p in permutations(range(n)):
        parity=sum(p[i]>p[j] for i,j in edges)%2
        if even_only and parity: continue
        W.append(S.Matrix([1 if p[i]<p[j] else -1 for i,j in edges]))
    mean=sum(W,S.zeros(M,1))/len(W)
    cov=sum(((v-mean)*(v-mean).T for v in W), S.zeros(M,M))/len(W)
    return W,mean,cov

def main():
    for n in range(4,7):
        E,B,T,H,C=objects(n)
        W,mean,cov=exact_moments(n,True)
        assert mean==S.zeros(len(E),1)
        assert cov==C,(n,cov-C)
        Wa,mua,full=exact_moments(n,False)
        assert mua==S.zeros(len(E),1) and full==T
        assert C.det()>0
        M=len(E)
        for v in W:
            assert (v.T*C.inv()*v)[0]==M
        P=(B.T*B)/n
        if n==4:
            assert H*H==S.eye(M)
            assert P*H*P==S.zeros(M)
            assert (S.eye(M)-P)*H*(S.eye(M)-P)==S.zeros(M)
            assert C.charpoly().as_expr().expand()==((S.Symbol('lambda')**2-2*S.Symbol('lambda')+S.Rational(4,9))**3).expand()
        if n==5:
            assert H*P==S.zeros(M) and P*H==S.zeros(M)
            assert H*H==5*(S.eye(M)-P)
            assert H.trace()==0
            z=S.Symbol('lambda')
            assert S.factor(C.charpoly(z).as_expr() - (z-2)**4*(z**2-S.Rational(2,3)*z+S.Rational(4,45))**3)==0
        ratio2=S.factor(C.det()/T.det())
        assert ratio2==(S.Rational(64,125) if n in (4,5) else 1),ratio2
        print(f'n={n}: even_vertices={len(W)} full_vertices={len(Wa)} dim={M}; covariance determinant ratio={ratio2}; contact equality on all vertices')
    print('PASS: all exact covariance, spectrum, normalization, and volume-ratio checks')

if __name__=='__main__':main()
