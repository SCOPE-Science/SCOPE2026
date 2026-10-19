#!/usr/bin/env python3
"""Exact rational checks for logistic-map boundary moments and small compression.

Requires only Python 3 standard library. Every check is finite; the accompanying
analytical proof establishes assertions for all fixed degrees and iterations.
"""
from fractions import Fraction as F
from math import comb

CHECKS = 0

def check(test):
    global CHECKS
    assert test
    CHECKS += 1

def cosine_sin_integral(k):
    # Integral_0^pi sin(theta) cos(k theta) dtheta for integer k.
    return F(0) if k % 2 else F(2, 1-k*k)

def cosine_moment(r, m):
    # Integral_0^pi sin(theta) cos(theta)^r cos(m theta) dtheta.
    return sum((F(comb(r,j), 2**(r+1)) *
                (cosine_sin_integral(m+r-2*j) +
                 cosine_sin_integral(m-r+2*j))
                for j in range(r+1)), F(0))

def logistic_delta(coeff, m):
    # Delta for g(x)=sum_j coeff[j]*x^j, m an even power of two.
    poly = [F(0)] * len(coeff)
    for j, c in enumerate(coeff):
        for k in range(j+1):
            poly[k] += F(c) * F(comb(j,k)*(-1)**k, 2**j)
    return -sum((c*cosine_moment(k,m)
                 for k,c in enumerate(poly)), F(0))/4

def multiply(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            out[i+j]+=F(ai)*F(bj)
    return out

def cheb_recursion(m):
    # Independent Chebyshev expansion by T_{k+1}=2tT_k-T_{k-1}.
    p,q=[F(1)],[F(0),F(1)]
    if m == 0: return p
    if m == 1: return q
    for _ in range(1,m):
        nxt=[F(0)]*(len(q)+1)
        for j,a in enumerate(q):nxt[j+1]+=2*a
        for j,a in enumerate(p):nxt[j]-=a
        p,q=q,nxt
    return q

def cheb_delta(coeff,m):
    # Integrate -g((1-t)/2)T_m(t)/4 over t in [-1,1].
    g=[F(0)]*len(coeff)
    for j,c in enumerate(coeff):
        for k in range(j+1):g[k]+=F(c)*F(comb(j,k)*(-1)**k,2**j)
    poly=multiply(g,cheb_recursion(m))
    return -sum((a*F(2,k+1) for k,a in enumerate(poly) if k%2==0),F(0))/4

def asymp_two(coeff,m):
    g0=F(coeff[0]);g1=sum(map(F,coeff))
    dg0=F(coeff[1]) if len(coeff)>1 else F(0)
    dg1=sum((j*F(c) for j,c in enumerate(coeff)),F(0))
    return (g0+g1)/F(4*m*m)+(g0+g1+F(3,2)*(dg1-dg0))/F(4*m**4)

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

# Exact finite polynomial integrations by two independent constructions.
for n in range(1,7):
    m=2**n
    for coeff in ([1],[0,1],[0,1,-1],[F(1,3),-2,3],
                  [2,0,-5,1,2],[-1,3,-2,4,-1,1]):
        check(logistic_delta(coeff,m)==cheb_delta(coeff,m))
    check(logistic_delta([1],m)==F(1,2*(m*m-1)))
    check(logistic_delta([0,1],m)==F(1,4*(m*m-1)))
    check(logistic_delta([F(-1,2),1],m)==0)
    if m>=4:
        check(logistic_delta([0,1,-1],m)==F(-3,4*(m*m-1)*(m*m-9)))

# Check exact finite-rational asymptotic coefficient and block determinant.
shifted_legendre=[[1],[-1,2],[1,-6,6]]
for n in range(4,11):
    m=2**n
    for coeff in ([1],[0,1],[0,1,-1],[0,0,1,-2,1],[2,-1,3]):
        residual=(logistic_delta(coeff,m)-asymp_two(coeff,m))*m**6
        check(abs(residual)<100000)
    H=[[logistic_delta(multiply(p,q),m)
        for q in shifted_legendre] for p in shifted_legendre]
    # In the orthonormal basis, determinant is 15 times this determinant.
    scaled_det=F(15)*det3(H)*m**10
    check(abs(scaled_det-F(2835,8))<F(300000,m*m))
    check(H[0][1]==0 and H[1][2]==0)
    # A function vanishing at both endpoints, q=x(1-x), has m^-6 energy.
    check(abs(logistic_delta([0,0,1,-2,1],m)*m**6-F(15,4))<F(20000,m*m))
print('VERIFY_OK: independent exact integrations and finite asymptotic checks:', CHECKS)
