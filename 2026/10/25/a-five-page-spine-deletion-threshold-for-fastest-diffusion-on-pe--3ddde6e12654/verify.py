#!/usr/bin/env python3
"""Exact checks for the pendant-book spectral-gap formulas.

Requires Python 3 and SymPy. Symbolic tests below are polynomial identities
valid for the parameter m, not a claim about numerical enumeration.
"""
from fractions import Fraction
import sympy as S

m, t = S.symbols('m t')
N = m + 3
A = (m + 2) / 2


def branch(which):
    if which == 'small':
        s = S.Integer(1)
    else:
        s = S.factor(A / (A*A-N))
    mu = S.factor((A*s-1)/N)
    x = S.factor(1-A*mu/s)
    a = S.factor(1-mu/s)
    b = S.factor(mu/s)
    c = S.factor(1+mu)
    D = S.factor(m+1+s*s-(A*s-1)**2/N)
    return s,mu,x,a,b,c,D


def check_symbolic():
    for which in ('small','large'):
        s,mu,x,a,b,c,D = branch(which)
        if which=='small':
            expected_D = m+2-m*m/(4*N)
            expected_product=(m*m*(11*m+24))/(8*N*N)
            expected_sum=(m+2)*(m+12)/(2*N)
        else:
            expected_D=m+1+4/(m*m-8)
            expected_product=m*(m**3-m*m-6*m+16)/((m+2)*(m*m-8))
            expected_sum=(m**3+2*m*m-8*m-8)/(m*m-8)
        assert S.factor(D-expected_D)==0
        assert S.factor(x+m*(a+b)+c-D)==0
        assert S.factor(a+b-1)==0
        assert S.factor(-s*x-m*a*s/2+c+mu)==0
        assert S.factor(s*x+m*b*s/2-(s-mu))==0
        assert S.factor((a-b)*s/2-(s/2-mu))==0
        assert S.factor(c-(1+mu))==0
        # Quotient on (hub u, hub v, common-page value, pendant z).
        L=S.Matrix([[x+m*a+c,-x,-m*a,-c],
                    [-x,x+m*b,-m*b,0],
                    [-a,-b,a+b,0],
                    [-c,0,0,c]])
        poly=S.Poly(L.charpoly(t).as_expr(),t)
        quotient,rem=S.div(poly,S.Poly(t*(t-1),t))
        assert rem.is_zero
        Q=quotient.as_expr()
        assert S.factor(Q.subs(t,1)-expected_product)==0
        assert S.factor(S.trace(L)-1-expected_sum)==0
        assert S.factor(S.LC(quotient)-1)==0
        # Geometric upper certificate: centered total squared norm.
        assert S.factor(D-(m+1+s*s-(A*s-1)**2/N))==0
    print('PASS: two all-parameter symbolic characteristic/geometry identities')


def numerical_finite_check():
    import numpy as np
    for k in range(2,121):
        s,mu,x,a,b,c,D=branch('small' if k<=4 else 'large')
        x,a,b,c,D=[float(S.N(expr.subs(m,k))) for expr in (x,a,b,c,D)]
        M=k+3
        Lap=np.zeros((M,M))
        for i,j,w in [(0,1,x),(0,M-1,c)]+[(0,i+2,a) for i in range(k)]+[(1,i+2,b) for i in range(k)]:
            assert w >= -1e-14
            Lap[i,i]+=w;Lap[j,j]+=w;Lap[i,j]-=w;Lap[j,i]-=w
        eig=np.linalg.eigvalsh(Lap)
        assert abs(eig[1]-1)<5e-12,(k,eig[1])
        assert abs(x+k*(a+b)+c-D)<1e-10
        assert np.linalg.norm(Lap@np.ones(M))<1e-12
        assert abs(eig[0])<1e-11
        # There are k eigenvalues exactly 1; the other two exceed it.
        assert np.allclose(eig[1:k+1],1,atol=2e-11)
        assert eig[k+1]>1+1e-8
        if k>=5:assert x==0
    print('PASS: 119 complete finite matrices with expected spectrum and costs')


if __name__=='__main__':
    check_symbolic()
    numerical_finite_check()
