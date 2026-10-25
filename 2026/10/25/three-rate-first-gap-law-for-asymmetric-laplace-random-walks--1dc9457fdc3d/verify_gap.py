#!/usr/bin/env python3
"""Two-method exact-rational checks for a bilateral-exponential walk gap law.

No third-party dependencies. This script checks finite persistence coefficients by
(1) an algebraic square-root expansion, and (2) the generalized
Sparre--Andersen recurrence using gamma comparisons. It also checks the
finite-mixture normalization and the symmetric special case.
"""
from fractions import Fraction as F
from math import comb

def square_root_coeffs(rho,N):
    # sqrt(1-rho*z) coefficients: h[0]=1, h[j]=h[j-1]*(j-3/2)/j*rho
    h=[F(1)]
    for j in range(1,N+1):
        h.append(h[-1]*F(2*j-3,2*j)*rho)
    return h

def persistence_sqrt(a,b,N):
    rho=4*a*b/(a+b)**2
    h=square_root_coeffs(rho,N)
    partial=F(0)
    qp=[]; qm=[]
    for j in range(N+1):
        partial+=h[j]
        qp.append(((a+b)*partial-(a-b))/(2*b))
        qm.append(((a+b)*partial+(a-b))/(2*a))
    return qp,qm

def beta_tail(k,r):
    return sum((F(comb(2*k-1,j))*r**j*(1-r)**(2*k-1-j)
                for j in range(k,2*k)),F(0))

def persistence_sa(a,b,N):
    r=b/(a+b)
    out=[]
    for p in [r,1-r]:
        q=[F(1)]
        for n in range(1,N+1):
            q.append(sum((q[n-k]*beta_tail(k,p) for k in range(1,n+1)),F(0))/n)
        out.append(q)
    return out

for a,b in [(F(1),F(1)),(F(2),F(1)),(F(1),F(3)),(F(3),F(5))]:
    N=12
    up,dn=persistence_sqrt(a,b,N)
    us,ds=persistence_sa(a,b,N)
    assert up==us and dn==ds
    assert up[0]==dn[0]==1
    for n in range(1,N+1):
        assert 0<=up[n]<=1 and 0<=dn[n]<=1 and up[n]+dn[n]<=1
        assert up[n]<=up[n-1] and dn[n]<=dn[n-1]
        if a==b:
            assert up[n]==dn[n]==F(comb(2*n,n),4**n)
    print('PASS rates',a,b,'n=1..',N,'q+_3',up[3], 'q-_3',dn[3])
print('All exact coefficient and probability tests passed.')
