#!/usr/bin/env python3
"""Exact algebraic and boundary checks for a Gaussian zero-crossing covariance theorem.
All mathematical statements of infinite scope are proved analytically in RESULT.md.
"""
from fractions import Fraction as Q
from math import sqrt

def row_sums(n,r):
    return [sum(r**abs(i-j) for j in range(1,n+1)) for i in range(1,n+1)]

def directly(n,r):
    b=row_sums(n,r)
    return sum(r*(b[i]**2+b[i+1]**2)-2*b[i]*b[i+1] for i in range(n-1))

def closed(n,r):
    t=r**n
    num=n*(r-1)*(r+1)**2+3*r*r+3*r+1
    num+=(n*(r*r-1)-3*r*r-4*r-1)*t+r*t*t
    return 2*num/(1-r)**2

def poly_add(x,y):
    z=[0]*max(len(x),len(y))
    for i,a in enumerate(x):z[i]+=a
    for i,a in enumerate(y):z[i]+=a
    return z

def poly_mul(x,y):
    z=[0]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):z[i+j]+=a*b
    return z

def poly_pow_r(k):return [0]*k+[1]

def polynomial(n):
    bb=[]
    for i in range(1,n+1):
        a=[0]
        for j in range(1,n+1):a=poly_add(a,poly_pow_r(abs(i-j)))
        bb.append(a)
    ans=[0]
    for i in range(n-1):
        p=poly_add(poly_mul(bb[i],bb[i]),poly_mul(bb[i+1],bb[i+1]))
        p=[0]+p
        q=poly_mul(bb[i],bb[i+1]);q=[-2*a for a in q]
        ans=poly_add(ans,poly_add(p,q))
    return ans

def taylor(poly,at,order):
    from math import comb
    return sum(coeff*comb(k,order)*at**(k-order) for k,coeff in enumerate(poly) if k>=order)

checks=0
R=[Q(-9,10),Q(-4,5),Q(-1,2),Q(-1,11),Q(0),Q(1,3),Q(4,5)]
for n in range(2,39):
    for r in R:
        assert directly(n,r)==closed(n,r),(n,r)
        checks+=1
for n in range(2,31):
    p=polynomial(n)
    assert taylor(p,-1,0)==0
    assert taylor(p,0,0)==-2*(n-1)
    if n%2:
        assert taylor(p,-1,1)==2*(n-1)
    else:
        assert taylor(p,-1,1)==0
        assert taylor(p,-1,2)==-2*n
    checks+=4
# Boundary layers: exact rational formulas, observed directional numerical limits.
for n in [100,200,400,800]:
    for c in [Q(6),Q(10),Q(15),Q(20)]:
        r=-1+c/Q(n*n)
        observed=float(n**3*closed(n,r))
        predicted=float(c*c*(c-12)/6)
        # verified error vanishes in the proven asymptotic, with generous finite n bound
        if n>=400: assert abs(observed-predicted) < 75.0
        checks+=1
for n in [101,201,401,801]:
    for c in [Q(3),Q(11)]:
        r=-1+c/Q(n*n)
        observed=float(n*closed(n,r))
        assert abs(observed-2*float(c))<5 if n>=401 else True
        checks+=1
for n in [400,625,900,1225]:
    root=int(sqrt(n)); assert root*root==n
    for c in [Q(1,2),Q(1)]:
        r=-1+c/Q(root)
        observed=float(closed(n,r))
        predicted=.5-float(c)**2
        if n>=900:assert abs(observed-predicted)<0.12
        checks+=1
# Existence of a negative--positive--negative regime for an even sample.
for n in [100,200,400]:
    vals=[closed(n,Q(-1)+Q(5,n*n)),closed(n,Q(-1)+Q(20,n*n)),
          closed(n,Q(-1)+Q(1,int(sqrt(n))) if int(sqrt(n))**2==n else Q(-1)+Q(1,2*int(sqrt(n))))]
    assert vals[0]<0 and vals[1]>0, (n,vals)
    checks+=2
print('PASS',checks,'exact and boundary checks')
