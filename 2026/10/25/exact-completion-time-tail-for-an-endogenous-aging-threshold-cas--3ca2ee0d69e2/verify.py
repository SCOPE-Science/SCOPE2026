#!/usr/bin/env python3
"""Exact verification of finite-time laws for an aging threshold cascade on cycles."""
from fractions import Fraction as F
from math import factorial

def matmult(A, B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)), F(0)) for j in range(n)] for i in range(n)]

def exact_survival(m, t):
    N=m+2
    p=[F(int(i==m)) for i in range(m+1)]
    for s in range(t):
        a=F(1, N*(s+2))
        for _ in range(N):
            pnew=[F(0)]*(m+1)
            for k,x in enumerate(p):
                r=1 if k==1 else (2 if k>=2 else 0)
                pnew[k] += x*(1-a*r)
                if k>0:
                    pnew[k-1] += x*a*r
            p=pnew
    assert sum(p)==1
    return sum(p[1:],F(0))

def Fval(N,t,degree):
    out=F(1)
    for s in range(t):
        out*= (F(1)+F(degree,N*(s+2)))**N
    return out

def Fderiv(N,t,degree):
    value=Fval(N,t,degree)
    # log derivative sum over N repeated simple factors
    return value*sum((F(N,N*(s+2)+degree) for s in range(t)),F(0))

for m in range(1,8):
    for t in range(0,9):
        s=exact_survival(m,t)
        assert F(0)<=s<=F(1)
        if m==1: assert s==Fval(m+2,t,-1)
        if m==2: assert s==2*Fval(m+2,t,-1)-Fval(m+2,t,-2)
        if m==3: assert s==4*Fval(m+2,t,-1)-3*Fval(m+2,t,-2)-2*Fderiv(m+2,t,-2)
    assert exact_survival(m,8)<exact_survival(m,7)
print('PASS: 63 exact-rational survival chains; closed forms for m=1,2,3 verified.')
print('N=4, t=1:',exact_survival(2,1))
print('N=5, t=1:',exact_survival(3,1))
