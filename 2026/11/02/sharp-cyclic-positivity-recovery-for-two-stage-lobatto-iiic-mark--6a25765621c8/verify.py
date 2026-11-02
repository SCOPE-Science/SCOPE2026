#!/usr/bin/env python3
"""Standalone exact and floating-point checks for two-stage Lobatto IIIC on directed cycles.
Only Python standard-library dependencies; no stored search results or external inputs.
"""
from fractions import Fraction as F
from math import atan, cos, sin, pi, exp, sqrt, tan
from cmath import exp as cexp

CHECKS=0

def check(condition, msg):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(msg)

def inverse_first_row(n,h):
    """Solve (I-hQ+h^2 Q^2/2) X=I exactly over Q; P[i,i+1]=1."""
    A=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        A[i][i] += h + h*h/2
        A[i][(i+1)%n] -= h + h*h
        A[i][(i+2)%n] += h*h/2
    # augment with identity, invert by Gauss-Jordan
    W=[A[i]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if W[i][j])
        W[j],W[pivot]=W[pivot],W[j]
        v=W[j][j]
        W[j]=[z/v for z in W[j]]
        for i in range(n):
            if i==j:continue
            mult=W[i][j]
            if mult:
                W[i]=[x-mult*y for x,y in zip(W[i],W[j])]
    return W[0][n:]

def formula(n,h,j):
    x=float(h)
    theta=atan(1/(1+x))
    rho=cos(theta)-sin(theta)
    den=1-2*rho**n*cos(n*theta)+rho**(2*n)
    return (2*rho**(j+1)/(x*den))*(sin((j+1)*theta)+rho**n*sin((n-j-1)*theta))

def theorem_safe(n,h):
    if h==0:return True
    return n<=4 or float(h)>=1/tan(pi/n)-1

# Independent rational matrix-inverse calculations, entry signs and mass preservation.
steps=[F(1,16),F(1,8),F(1,4),F(1,2),F(3,4),F(1),F(3,2),F(2),F(3),F(4),F(8),F(16)]
for n in range(2,18):
    # n=2 has P^2=I, so accumulation in the diagonal is intentional.
    for h in steps:
        row=inverse_first_row(n,h)
        check(sum(row)==1, ('mass',n,h))
        check(all((x>=0) for x in row)==theorem_safe(n,h),('exact_sign',n,h,row))
        for j,exact in enumerate(row):
            approximate=formula(n,h,j)
            check(abs(float(exact)-approximate) <= 2e-10*max(1,abs(float(exact))),('formula',n,h,j,float(exact),approximate))
            if abs(float(exact))>1e-11:
                check((approximate>0)==(exact>0),('sign',n,h,j))

# Independently verify stability function from Butcher coefficients symbolically.
# A=[[1/2,-1/2],[1/2,1/2]], b=[1/2,1/2]. For z the determinant is 1-z+z^2/2
# and b^T adj(I-zA)1=1-z/2, so numerator is exactly 1.
for z in [F(-11,4),F(-1),F(-1,5),F(0),F(1,3),F(4)]:
    A11=1-z/2; A12=z/2; A21=-z/2; A22=1-z/2
    d=A11*A22-A12*A21
    R=1+z*((A22-A12)+(A11-A21))/(2*d)
    check(R==1/(1-z+z*z/2),('tableau',z))

# Boundary check across many dimensions: one coefficient vanishes, all others positive.
for n in range(5,201):
    theta=pi/n
    rho=cos(theta)-sin(theta)
    for j in range(n):
        term=sin((j+1)*theta)+rho**n*sin((n-j-1)*theta)
        if j==n-1:check(abs(term)<1e-12,('boundaryzero',n,j,term))
        else:check(term>0,('boundary_positive',n,j,term))

# Elementary strict obstruction bound in the late-phase range.
for n in range(9,180):
    for h in [0.0001,0.001,0.01,0.1]:
        theta=atan(1/(1+h))
        if n*theta>=2*pi:
            from math import ceil
            k=ceil(1.5*pi/theta)
            check(k<=n,('kbound',n,h))
            rho=cos(theta)-sin(theta)
            term=sin(k*theta)+rho**n*sin((n-k)*theta)
            check(term<0,('late_negative',n,h,k,term))

print('VERIFIED',CHECKS,'assertions; exact rational inverses, coefficients, signs, tableau, and endpoint checks.')
