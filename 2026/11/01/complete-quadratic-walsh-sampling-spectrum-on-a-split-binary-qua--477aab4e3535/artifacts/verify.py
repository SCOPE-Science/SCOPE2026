#!/usr/bin/env python3
"""Independent exact Gram reconstruction for quadratic-band Walsh sampling."""
from itertools import combinations
from math import comb, sqrt
import numpy as np
import sympy as sp


def forms(n):
    return [()] + [(j,) for j in range(n)] + list(combinations(range(n),2))


def phase(a):
    return -1 if any(a.count(2*j) and a.count(2*j+1) for j in range((max(a, default=-1)+2)//2)) else 1


def bphase(a,b):
    aa = set(a)
    bb = set(b)
    return -1 if sum(((2*j in aa and 2*j+1 in bb) + (2*j+1 in aa and 2*j in bb)) for j in range((max(aa|bb, default=-1)+2)//2) if aa or bb) % 2 else 1


def sample_matrix(m, ff):
    n=2*m
    z=[]
    for bits in range(1<<n):
        q=sum(((bits>>(2*j))&1)*((bits>>(2*j+1))&1) for j in range(m))%2
        if not q:
            z.append([(-1)**sum((bits>>i)&1 for i in a) for a in ff])
    return np.array(z,dtype=np.int64)


def Tmat(n):
    B=[1,n,comb(n,2)]
    K=sp.Matrix([[sum((-1)**j*comb(r,j)*comb(n-r,s-j) for j in range(max(0,s-(n-r)),min(r,s)+1)) for s in range(3)] for r in range(3)])
    return K


def check():
    counts={'gram_entries':0,'spectrum_values':0,'characteristic_polynomials':0,'rank_checks':0}
    t,n=sp.symbols('t n')
    p=t**3+(-n**2+7*n-14)*t**2/2+(-n**2+n-2)*t+8
    assert sp.factor(Tmat(n if isinstance(n,int) else 6).charpoly(t).as_expr()-p.subs(n,6))==0
    c=2*(n-3)
    assert sp.factor(-p.subs(t,-c)-2*(n-5)*(n-2)**2*(n-1))==0
    quotient,rem=sp.div(p,t*t-2*(n-3)*t-8,t)
    assert sp.factor(rem+(n-3)*((n*n-10*n+28)*t+4*n-32))==0
    for m in range(2,6):
        n=2*m
        ff=forms(n)
        X=sample_matrix(m,ff)
        assert len(X)==(1<<(2*m-1))+(1<<(m-1))
        gg=X.T@X
        # Exact integer equality after clearing Gram denominator.
        for i,a in enumerate(ff):
            for j,b in enumerate(ff):
                pred=( (2**m if i==j else 0) + phase(a)*phase(b)*bphase(a,b) )
                assert int(gg[i,j])*(2**m+1)==len(X)*pred, (m,i,j)
                counts['gram_entries']+=1
        U=(gg/len(X)).astype(float)
        observed=np.linalg.eigvalsh(U)
        roots=np.linalg.eigvals(np.array(Tmat(n)).astype(float))
        splus=-(n-3)+sqrt((n-3)**2+8)
        sminus=-(n-3)-sqrt((n-3)**2+8)
        H=list(roots)
        for sg,mult in [(1,m-1),(-1,m)]:
            for s in [splus,sminus]: H += [sg*s]*mult
        H += [4]* (m*(m-1)) + [-4]*(m*(m-2))
        predicted=np.sort(np.array([(2**m+h)/(2**m+1) for h in H]))
        assert len(predicted)==len(ff)
        assert np.max(abs(predicted-observed))<2e-12, (m,np.max(abs(predicted-observed)))
        counts['spectrum_values']+=len(ff)
        assert int(np.sum(observed<1e-9))==(1 if m==2 else 0)
        counts['rank_checks']+=1
        cp=Tmat(n).charpoly(t).as_expr()
        assert sp.expand(cp-p.subs({sp.Symbol('n'): n}))==0
        counts['characteristic_polynomials']+=1
    print('VERIFY_OK',counts)

if __name__=='__main__':check()
