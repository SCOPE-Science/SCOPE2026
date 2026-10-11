#!/usr/bin/env python3
"""Exact finite-dimensional checks of the stated Hamming-shell Fourier spectrum.
Requires Python 3.10+ and SymPy. The unrestricted theorem uses the written proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from collections import Counter
from sympy import Matrix, Rational, symbols, expand


def binom(a,b):
    return comb(a,b) if 0 <= b <= a else 0


def falling(a,j):
    v=1
    for t in range(j):v*=a-t
    return v


def prediction(q,n,k,d):
    p=F(q-1,q);v=p*(1-p);out=[]
    for s in range(d+1):
        m=n-s;l=k-s;r=d-s
        for j in range(r+1):
            if not j<=min(l,m-l):continue
            M=binom(n,s)*(q-2)**s*(binom(m,j)-binom(m,j-1))
            b=F(binom(m,l))*p**l*(1-p)**(m-l)
            R=F(falling(l,j)*falling(m-l,j),falling(m,2*j))
            C=F(0)
            for a in range(j,r+1):
                t=a-j
                kap=sum((F(binom(l-j,u)*binom(m-l-j,t-u))*(1-p)**u*(-p)**(t-u)
                         for u in range(t+1)), F(0))
                C+=kap*kap/(v**a*binom(m-2*j,t))
            ev=b*R*C
            assert ev>0
            out.extend([ev]*M)
    assert len(out)==binom(n,d)*(q-1)**d
    return out


def local_basis(q):
    p=F(q-1,q)
    # 0: constant; 1: centered activity; 2..q-1: Helmert contrasts.
    rows=[[F(1) for _ in range(q)], [F(int(x!=0))-p for x in range(q)]]
    for t in range(1,q-1):
        rows.append([F(0)]+[F(int(1<=x<=t)-t*int(x==t+1)) for x in range(1,q)])
    variances=[F(1),p*(1-p)]+[F(t*(t+1),q) for t in range(1,q-1)]
    assert len(rows)==q
    for i in range(q):
        for j in range(q):
            dot=sum((rows[i][x]*rows[j][x] for x in range(q)),F(0))/q
            assert dot==(variances[i] if i==j else 0)
    return rows,variances


def direct(q,n,k,d):
    B,variances=local_basis(q)
    patterns=[u for u in product(range(q),repeat=n) if sum(bool(x) for x in u)<=d]
    sphere=[x for x in product(range(q),repeat=n) if sum(bool(t) for t in x)==k]
    N=len(patterns);values=[];g=[]
    for u in patterns:
        g.append(F(1))
        for t in u:g[-1]*=variances[t]
        values.append([F(1) for x in sphere])
        for xidx,x in enumerate(sphere):
            for i in range(n):values[-1][xidx]*=B[u[i]][x[i]]
    K=[]
    for i in range(N):
        K.append([])
        for j in range(N):
            summ=sum((values[i][x]*values[j][x] for x in range(len(sphere))),F(0))
            K[i].append(summ/F(q**n)/g[i])
    return K,N


def check(q,n,k,d):
    eigen=prediction(q,n,k,d)
    K,N=direct(q,n,k,d)
    z=symbols('z')
    C=Counter(eigen)
    C[F(0)]=N-len(eigen)
    target=1
    for lam,mul in C.items():target*= (z-Rational(lam.numerator,lam.denominator))**mul
    P=Matrix([[Rational(t.numerator,t.denominator) for t in row] for row in K])
    actual=P.charpoly(z).as_expr()
    assert expand(actual-target)==0,(q,n,k,d)
    print('PASS q=%s n=%s k=%s d=%s dim=%s rank=%s branches=%s' %
          (q,n,k,d,N,len(eigen),len(C)-1))

if __name__=='__main__':
    for case in [(3,4,2,2),(3,5,2,2),(4,4,2,2)]:check(*case)
    print('VERIFY_OK exact_rational_full_characteristic_polynomials=PASS')

# Additional non-certifying numerical check in the first genuinely higher-degree case.
def degree_three_numeric():
    import numpy as np
    q,n,k,d=3,6,3,3
    B,V=local_basis(q)
    pats=[u for u in product(range(q),repeat=n) if sum(x!=0 for x in u)<=d]
    shell=[x for x in product(range(q),repeat=n) if sum(y!=0 for y in x)==k]
    D=np.array([float(F(1)/np.prod([float(V[t]) for t in u]))**0.5 for u in pats])
    Y=np.array([[np.prod([float(B[u[i]][x[i]]) for i in range(n)]) for x in shell] for u in pats])
    K=(D[:,None]*Y)@(D[:,None]*Y).T/q**n
    actual=np.linalg.eigvalsh(K)
    target=np.array(sorted([0.]*(len(pats)-len(prediction(q,n,k,d)))+[float(x) for x in prediction(q,n,k,d)]))
    assert np.max(np.abs(actual-target))<1.e-11
    print('PASS q=3 n=6 k=3 d=3 dim=%s rank=%s numerical_spectrum=PASS' % (len(pats),len(prediction(q,n,k,d))))

if __name__=='__main__':
    degree_three_numeric()
    print('VERIFY_OK higher_degree_numerical_spectrum=PASS')
