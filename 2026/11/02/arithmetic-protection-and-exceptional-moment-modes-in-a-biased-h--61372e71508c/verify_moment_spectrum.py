#!/usr/bin/env python3
"""Exact finite-degree checks for a two-orientation harmonic filter."""
from fractions import Fraction as F
from math import factorial

def rank(A):
    A=[list(map(F,row)) for row in A]
    if not A: return 0
    n=len(A); p=len(A[0]); r=0
    for j in range(p):
        pivot=next((i for i in range(r,n) if A[i][j]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        c=A[r][j]; A[r]=[x/c for x in A[r]]
        for i in range(n):
            if i==r or not A[i][j]: continue
            v=A[i][j]; A[i]=[x-v*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==n:break
    return r

def matrix(N,a,b):
    # In each degree j: p_j=z^j, q_j=(sigma-h)z^j, generator kappa=1.
    h=(b-a)/(a+b); lam=a+b
    size=2*(N+1); M=[[F(0) for _ in range(size)] for _ in range(size)]
    for j in range(N+1):
        M[2*j][2*j]=-j
        M[2*j+1][2*j+1]=-j-lam
        if j:
            M[2*(j-1)][2*j]=j*h
            M[2*(j-1)+1][2*j]=j
            M[2*(j-1)][2*j+1]=j*(1-h*h)
            M[2*(j-1)+1][2*j+1]=-j*h
    return M

def kernel_dimension_shift(M,eig):
    n=len(M)
    return n-rank([[M[i][j]+(eig if i==j else 0) for j in range(n)] for i in range(n)])

def defect_expected(a,b,N):
    lam=a+b
    if lam.denominator!=1:return {}
    m=int(lam)
    if not 1<=m<=N:return {}
    protect=a.denominator==1 and b.denominator==1
    return {n:(0 if protect else 1) for n in range(m,N+1)}

def transfer_m(m,a):
    """Second-pole coefficient in E[z(t)^m] along q_0 at total rate m."""
    b=F(m)-a; h=(b-a)/F(m)
    B=[[h,1-h*h],[F(1),-h]]
    def mul(v): return [B[0][0]*v[0]+B[0][1]*v[1],B[1][0]*v[0]+B[1][1]*v[1]]
    v=mul([F(1),F(0)])
    for j in range(m-1,0,-1):
        v=mul([v[0]/F(j-m),v[1]/F(j)])
    return factorial(m)*v[1]

def closed_coeff(m,a):
    v=F(m*2**(m-1),factorial(m-1))
    for j in range(1,m):v*=a-j
    return v

count=0
# Degree-filtration matrices are assembled directly from both physical-state generators.
for N in range(1,11):
    for a,b in [(F(1,2),F(1,2)),(F(1),F(1)),(F(3,2),F(3,2)),(F(1),F(2)),(F(2),F(3)),(F(3,4),F(5,4)),(F(3,5),F(7,5)),(F(2,5),F(8,5)),(F(3,5),F(12,5)),(F(1,3),F(7,6))]:
        M=matrix(N,a,b)
        for j in range(N+1):
            assert kernel_dimension_shift(M,F(j))>=1
            count+=1
        expected=defect_expected(a,b,N)
        for j in range(N+1):
            if F(j)-(a+b) in range(N+1):
                geom=kernel_dimension_shift(M,F(j))
                assert geom==(2-expected.get(j,0)), (N,a,b,j,geom)
                count+=1
# Direct independent rational-resolvent coefficient multiplication.
for m in range(1,11):
    for k in range(1,16):
        a=F(m*k,16)
        b=F(m)-a
        assert b>0
        got=transfer_m(m,a)
        assert got==closed_coeff(m,a),(m,a,got,closed_coeff(m,a))
        count+=1
# Explicit symmetric and asymmetric witnesses.
assert transfer_m(2,F(4,5))==F(-4,5)  # h=1/5, -4h
assert transfer_m(2,F(1))==0
assert transfer_m(3,F(3,2))==F(-3,2)
assert transfer_m(3,F(1))==0
count+=4
print('VERIFY_OK',count,'exact-rational assertions')
