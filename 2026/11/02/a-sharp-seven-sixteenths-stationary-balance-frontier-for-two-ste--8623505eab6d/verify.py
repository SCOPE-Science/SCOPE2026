#!/usr/bin/env python3
"""Exact-arithmetic checks for the two-state L(kappa) simplex theorem.
This program tests finite samples and identities; universal quantifiers are proved
algebraically in RESULT.md, not by these finite tests.
"""
from fractions import Fraction as F
from itertools import product

Z, O = F(0), F(1)

def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), Z)
             for j in range(len(B[0]))] for i in range(len(A))]

def inv2(A):
    d = A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert d != 0
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]

def coeff(k):
    D=(3-k)*(1+k)
    return ( (3*k-1)/(3-k), 4*(1-k)/(3-k),
             2*k*k/D, 4*k/D, 2/D ) # c0, c1, beta0, beta1, beta2

def exact_update(k,m,t,u,v):
    c0,c1,b0,b1,b2=coeff(k)
    Q=[[m-1,1-m],[m,-m]]
    B=inv2([[O-t*b2*Q[0][0],-t*b2*Q[0][1]],
            [-t*b2*Q[1][0],O-t*b2*Q[1][1]]])
    P=mm(B,[[c1+t*b1*Q[0][0],t*b1*Q[0][1]],
            [t*b1*Q[1][0],c1+t*b1*Q[1][1]]])
    R=mm(B,[[c0+t*b0*Q[0][0],t*b0*Q[0][1]],
            [t*b0*Q[1][0],c0+t*b0*Q[1][1]]])
    a=mm([[u,O-u]],P)[0]
    b=mm([[v,O-v]],R)[0]
    return [a[j]+b[j] for j in range(2)]

def predicted(k,m,t,u,v):
    c0,c1,b0,b1,b2=coeff(k)
    x0=c1*u+c0*v
    xinf=(1+k)**2*m-2*k*u-k*k*v
    x=(x0+t*b2*xinf)/(1+t*b2)
    return [x,O-x]

checks=0
ks=[F(0),F(1,5),F(1,3),F(7,20),F(3,8),F(2,5),F(5,12),F(1,2),F(3,4),F(9,10)]
ms=[F(1,50),F(1,5),F(2,5),F(7,16),F(9,20),F(49,100),F(1,2)]
ts=[F(0),F(1,100),F(1,4),F(1),F(3),F(15),F(100),F(10000)]
for k,m,t,u,v in product(ks,ms,ts,[Z,O],[Z,O]):
    y=exact_update(k,m,t,u,v)
    z=predicted(k,m,t,u,v)
    assert y==z,(k,m,t,u,v,y,z)
    assert sum(y)==O
    checks+=1

# The convex interpolation proves all finite positive times reduce to two endpoints.
# We sample the entire simplex extreme-point set on rational boundary pairs.
for k in [F(1,3),F(7,20),F(3,8),F(2,5)]:
    mcrit=O-O/(O+k)**2
    if mcrit<=F(1,2):
        for m in [mcrit,(mcrit+F(1,2))/2,F(1,2)]:
            for t,u,v in product(ts,[Z,O],[Z,O]):
                y=exact_update(k,m,t,u,v)
                assert Z<=y[0]<=O,(k,m,t,u,v,y)
                checks+=1
        # An inadmissible smaller stationary probability gives a true finite-step failure.
        m=mcrit-F(1,1000)
        if m>0:
            _,_,_,_,b2=coeff(k)
            xinf=(O+k)**2*m-2*k-k*k
            assert xinf<0
            t=F(2)/(-b2*xinf)
            assert exact_update(k,m,t,O,O)[0]<0
            checks+=1

# Below the lower kappa endpoint, zero-step arbitrary-history positivity already fails.
for k in [F(0),F(1,10),F(1,4),F(3,10)]:
    assert exact_update(k,F(1,2),Z,Z,O)[0]<0
    checks+=1

# Above the upper bound on kappa, even the balanced chain fails for a finite step.
for k in [F(5,12),F(1,2),F(2,3),F(9,10)]:
    _,_,_,_,b2=coeff(k)
    m=F(1,2)
    xinf=(O+k)**2*m-2*k-k*k
    assert xinf<0
    t=F(2)/(-b2*xinf)
    assert exact_update(k,m,t,O,O)[0]<0
    checks+=1

# The rational equality kappa=1/3, m=7/16 is exactly sharp.
k,m=F(1,3),F(7,16)
assert (O+k)**2*(O-m)==O
assert predicted(k,m,F(10**9),O,O)[0]>0
checks+=1

print('PASS:',checks,'exact-rational identities, boundary and matrix checks')
