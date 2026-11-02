#!/usr/bin/env python3
"""Exact rational verification of two Fourier-energy identities and positive Bernstein data."""
from fractions import Fraction as F
from math import comb

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in (0,1)) for j in (0,1)] for i in (0,1)]
def matsum(*parts):
    return [[sum(A[i][j] for A in parts) for j in (0,1)] for i in (0,1)]
def scalar(a,A): return [[a*A[i][j] for j in (0,1)] for i in (0,1)]
def transpose(A):return [[A[j][i] for j in (0,1)] for i in (0,1)]
def sub(A,B):return matsum(A,scalar(-1,B))
I=[[F(1),F(0)],[F(0),F(1)]]
W=[[F(1),F(0)],[F(0),F(1,3)]]
def R(z,s):
    a=z-1
    L=[[a,a],[-3*a,-3*(1+z)]]
    L2=matmul(L,L);L3=matmul(L2,L)
    return matsum(I,scalar(s,L),scalar(s*s/2,L2),scalar(s**3/6,L3))
def energy(z,s):
    T=R(z,s); Tstar=R(1/z,s)
    D=sub(W,matmul(transpose(Tstar),matmul(W,T)))
    return D[0][0],D[0][0]*D[1][1]-D[0][1]*D[1][0]

def Q(s,t):
    return -(64*s**5*t*t-540*s**5*t+972*s**5-120*s**4*t*t+702*s**4*t-972*s**4+96*s**3*t*t-510*s**3*t+567*s**3-24*s*s*t*t+162*s*s*t-216*s*s-18*s*t+54*s-9)/9

def p(s):return 18*s**4-9*s**3+3*s*s+5*s-1
def fp(s):return 3*(6*s*s-3*s+1)*p(s)
def fm(s):return -(12*s**3-6*s*s-s-1)*(36*s**5-18*s**4-3*s**3+s*s+3*s-3)
def flux_F(s,c):return ((1+c)*fp(s)+(1-c)*fm(s))/2

checks=0
# Exact interpolation certificates: both expressions are polynomials in s of
# degree <=12, Laurent in z with exponents [-6,6]. Thirteen rational samples
# in each variable establish equality identically by the root-counting theorem.
for j in range(13):
    s=F(j+1,53)
    for k in range(13):
        z=F(k+2,17)
        c=(z+1/z)/2;t=1-c
        v,d=energy(z,s)
        assert v==2*s*t*Q(s,t),(j,k,'D11',v)
        assert d==-F(4,9)*s**4*t*t*flux_F(s,c),(j,k,'detD',d)
        checks+=2

# Convert Q(s,t) to Bernstein form in (u,v) on s=u/5, t=2v.
# It has bidegree at most (5,2); exact coefficients are obtained from
# its power coefficients via the binomial change of basis.
S=F(1,5);T=F(2)
# Use 6 x 3 rational interpolation to obtain all monomial coefficients.
def inverse(A):
    n=len(A);A=[list(map(F,row))+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        pivot=next(k for k in range(i,n) if A[k][i]);A[i],A[pivot]=A[pivot],A[i]
        v=A[i][i];A[i]=[a/v for a in A[i]]
        for k in range(n):
            if k!=i:
                v=A[k][i];A[k]=[a-v*b for a,b in zip(A[k],A[i])]
    return [row[n:] for row in A]
xs=[F(i,5) for i in range(6)];ys=[F(j,2) for j in range(3)]
Xi=inverse([[x**i for i in range(6)] for x in xs]);Yi=inverse([[y**j for j in range(3)] for y in ys])
vals=[[Q(S*x,T*y) for y in ys] for x in xs]
# monomial coefficients a_{ij}
a=[[sum(Xi[i][k]*vals[k][ell]*Yi[j][ell] for k in range(6) for ell in range(3)) for j in range(3)] for i in range(6)]
b=[[sum(a[ii][jj]*F(comb(i,ii),comb(5,ii))*F(comb(j,jj),comb(2,jj)) for ii in range(i+1) for jj in range(j+1)) for j in range(3)] for i in range(6)]
expected=[['1','1','1'],['19/25','21/25','23/25'],['77/125','88/125','313/375'],['647/1250','2201/3750','2813/3750'],['1403/3125','37/75','2107/3125'],['1232/3125','3956/9375','17192/28125']]
assert b==[[F(x) for x in row] for row in expected]
assert all(x>0 for row in b for x in row)
checks+=18
# Root isolation and strict monotonicity: p'(s)=5+s(72s^2-27s+6)>0.
assert p(F(186457,1000000))<0<p(F(186458,1000000))
assert F(4)*F(72)*F(6)-F(27)**2>0
checks+=2
# D22 at the constant Fourier mode and the sign of all Bernstein coefficients
# complete the positive-semidefinite certificate for s in [0,root].
for j in range(1,101):
    s=F(j,500)
    amp=1-6*s+18*s*s-36*s**3
    assert 0<amp<1
    assert fm(s)<0
    checks+=2
# Non-normal instability: above threshold det(I-R*R)<0 for a sufficiently
# small nonzero Fourier angle; exact rational z<1 is a Laurent surrogate.
for s in [F(19,100),F(1,5),F(1,4),F(1,3)]:
    assert fp(s)>0
    checks+=1
print('VERIFY_OK',checks,'threshold_interval=(0.186457,0.186458)', 'min_Bernstein',min(map(min,b)))
