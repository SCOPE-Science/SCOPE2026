#!/usr/bin/env python3
"""Exact finite consistency checks for folded asymmetric geometric laws.
The analytic statements are proved separately; finite checks are not a proof.
"""
from fractions import Fraction as F
from itertools import product

def pgf_coefficients(q,r,K):
    c=(1-q)*(1-r)/(1-q*r)
    return [c]+[c*(q**k+r**k) for k in range(1,K+1)]

def direct_coefficients(q,r,K,N=70):
    # The omitted geometric tails are bounded by q**N+r**N.
    aq=[(1-q)*q**i for i in range(N+1)]
    ar=[(1-r)*r**j for j in range(N+1)]
    return [sum(aq[i]*ar[j] for i in range(N+1) for j in range(N+1) if abs(i-j)==k) for k in range(K+1)]

def levy(k,q,r):
    if k%2:
        return (q**k+r**k)/k
    m=k//2
    return (q**m-r**m)**2/k

samples=0
for i,j in product(range(1,10),repeat=2):
    q=F(i,11);r=F(j,11)
    p=pgf_coefficients(q,r,16)
    c=(1-q)*(1-r)/(1-q*r)
    assert sum(p)+(c*(q**17/(1-q)+r**17/(1-r)))==1
    # check rational-power-series logarithmic derivatives coefficientwise
    lev=[F(0)]+[levy(k,q,r) for k in range(1,17)]
    for k in range(1,17):
        assert k*p[k]==sum(j*lev[j]*p[k-j] for j in range(1,k+1))
        assert lev[k]>=0
        samples+=2
    # sharp all-index canonical monotonicity reduces to one comparison
    cond=(q-r)**2 >=q**3+r**3
    a=[F(0)]+[k*lev[k] for k in range(1,17)]
    all_adjacent=all(a[k]>=a[k+1] for k in range(1,16))
    assert all_adjacent==cond
    for k in range(2,16):
        diff=p[k-1]*p[k+1]-p[k]**2
        assert diff==c*c*q**(k-1)*r**(k-1)*(q-r)**2
        samples+=1
    assert (p[1]**2>=p[0]*p[2])
    samples+=2

# Direct double sums at moderate truncation with an exact (positive) residual.
for q,r in [(F(1,2),F(2,3)),(F(1,4),F(3,4)),(F(7,9),F(1,9))]:
    c=(1-q)*(1-r)/(1-q*r)
    # exact infinite double sums by conditioning on the sign of i-j
    for k in range(1,12):
        plus=sum((1-q)*q**(j+k)*(1-r)*r**j for j in range(70))
        rem_plus=(1-q)*(1-r)*q**k*(q*r)**70/(1-q*r)
        minus=sum((1-q)*q**j*(1-r)*r**(j+k) for j in range(70))
        rem_minus=(1-q)*(1-r)*r**k*(q*r)**70/(1-q*r)
        assert plus+rem_plus+minus+rem_minus == c*(q**k+r**k)
        samples+=1
print('PASS exact rational checks:',samples)
