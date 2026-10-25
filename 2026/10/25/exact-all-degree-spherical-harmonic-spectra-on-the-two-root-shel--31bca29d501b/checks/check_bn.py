"""Reproduce the exact spherical-kernel spectral identities using Python, NumPy, SymPy.
Run: python checks/check_bn.py
"""
from itertools import combinations, product
from math import comb, sqrt
import numpy as np
import sympy as sp

u = sp.symbols('u')
N = sp.symbols('N', integer=True, positive=True)

def zonal_polynomial(n, ell):
    return sp.expand(sp.gegenbauer(ell, sp.Rational(n-2,2), u)
                     /sp.gegenbauer(ell, sp.Rational(n-2,2), 1))

def nodes(n):
    rows=[]
    for i in range(n):
        for sign in (-1,1):
            x=np.zeros(n)
            x[i]=sign
            rows.append(x)
    for i,j in combinations(range(n),2):
        for a,b in product((-1,1),repeat=2):
            x=np.zeros(n)
            x[i]=a/sqrt(2)
            x[j]=b/sqrt(2)
            rows.append(x)
    return np.asarray(rows)

def eigen_pair(a,b,d):
    delta=sqrt(max(0,(a-d)**2+4*b*b))
    return [(a+d+delta)/2,(a+d-delta)/2]

def predicted(n,ell,p0,ph,pq):
    E=comb(n,2)
    zeros=[0.]*(n*n)
    if ell%2:
        B=2*sqrt(2*(n-1))*pq
        return sorted(zeros+[2-4*ph]*(n*(n-2))
                  +eigen_pair(2,B,2+4*(n-2)*ph)*n)
    A0=2*(1+(n-1)*p0)
    B0=4*sqrt(n-1)*(pq+(n-2)*p0/2)
    D0=2*(1+p0)+8*(n-2)*ph+2*(n-2)*(n-3)*p0
    As=2*(1-p0)
    Bs=2*sqrt(2*(n-2))*(pq-p0)
    Ds=2+(14-4*n)*p0+4*(n-4)*ph
    edge=2+6*p0-8*ph
    pair=2*(1-p0)
    return sorted(zeros+eigen_pair(A0,B0,D0)
                  +eigen_pair(As,Bs,Ds)*(n-1)
                  +[edge]*(E-n)+[pair]*E)

def exact_phase_checks():
    p5=sp.factor(sp.gegenbauer(5,(N-2)/2,u)/sp.gegenbauer(5,(N-2)/2,1))
    h5=sp.factor(p5.subs(u,sp.Rational(1,2)))
    q5=sp.factor(p5.subs(u,1/sp.sqrt(2)))
    perp5=sp.factor(2-4*h5)
    det5=sp.factor(2*(2+4*(N-2)*h5)-8*(N-1)*q5**2)
    assert sp.simplify(perp5-15*(N-2)*(N+4)/(8*(N-1)*(N+1)))==0
    assert sp.simplify(det5-5*(N-2)*(N+4)*(N+6)/(4*(N-1)*(N+1)**2))==0

    p6=sp.factor(sp.gegenbauer(6,(N-2)/2,u)/sp.gegenbauer(6,(N-2)/2,1))
    o=sp.factor(p6.subs(u,0));h=sp.factor(p6.subs(u,sp.Rational(1,2)))
    q=sp.factor(p6.subs(u,1/sp.sqrt(2)))
    E=sp.factor(2+6*o-8*h)
    assert sp.simplify(E-15*(N-4)*(N+4)*(N+6)/(8*(N-1)*(N+1)*(N+3)))==0
    a=2*(1+(N-1)*o)
    b=4*sp.sqrt(N-1)*(q+(N-2)*o/2)
    d=2*(1+o)+8*(N-2)*h+2*(N-2)*(N-3)*o
    assert sp.simplify(a*d-b**2)==0
    assert sp.simplify((a+d)-(N-2)*(N+6)*(N**2-16*N+240)/(8*(N-1)*(N+1)*(N+3)))==0
    aa=2*(1-o)
    bb=2*sp.sqrt(2*(N-2))*(q-o)
    dd=2+(14-4*N)*o+4*(N-4)*h
    assert sp.simplify(aa*dd-bb**2-15*N*(N-3)*(N+4)**2*(N+6)*(N+8)/(8*(N-1)**2*(N+1)**2*(N+3)**2))==0
    print('symbolic: degree-five positive minors and degree-six defect identities PASS')

def finite_checks():
    tested=0
    worst=0.
    for n in range(3,8):
        X=nodes(n)
        dot=X@X.T
        assert len(X)==2*n*n
        for ell in range(13):
            p=zonal_polynomial(n,ell)
            vals={}
            for x in (-1,-1/sqrt(2),-1/2,0,1/2,1/sqrt(2),1):
                exact_x=sp.nsimplify(x,[sp.sqrt(2)])
                vals[x]=float(p.subs(u,exact_x))
            G=np.zeros_like(dot)
            for t,f in vals.items():G[np.isclose(dot,t,atol=1e-10)]=f
            actual=np.linalg.eigvalsh(G)
            expected=np.asarray(predicted(n,ell,vals[0],vals[.5],vals[1/sqrt(2)]))
            discrepancy=float(np.max(np.abs(actual-expected)))
            assert discrepancy<1e-9,(n,ell,discrepancy)
            assert actual[0]>-1e-9
            tested+=1
            worst=max(worst,discrepancy)
    print(f'independent direct Gram eigenspectra: {tested} cases PASS; maximum absolute discrepancy {worst:.3e}')

if __name__=='__main__':
    exact_phase_checks()
    finite_checks()
    print('ALL CHECKS PASS')
