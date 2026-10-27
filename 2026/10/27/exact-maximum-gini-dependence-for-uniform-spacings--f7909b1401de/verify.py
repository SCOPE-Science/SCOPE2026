"""Reproduce exact moment identities for uniform Dirichlet spacings.
Python 3, standard library.  All polynomial checks use fractions.Fraction.
Numerical simulations are independent diagnostic checks, not proof.
"""
from fractions import Fraction as F
import math
import random


def direct_exponential_gap_moments(m):
    # Descending ordered iid Exp(1) variables have independent E_r/r gaps.
    weights_a = [F(1,r) for r in range(1,m+1)]
    weights_b = [F(m-r,m) if r<m else F(0) for r in range(1,m+1)]
    mean_a=sum(weights_a)
    mean_b=sum(weights_b)
    covariance_ab=sum(a*b for a,b in zip(weights_a,weights_b))
    var_a=sum(a*a for a in weights_a)
    var_b=sum(b*b for b in weights_b)
    e_ab=mean_a*mean_b+covariance_ab
    e_a2=mean_a*mean_a+var_a
    e_b2=mean_b*mean_b+var_b
    # T is Gamma(m,1) and independent of normalized vector.
    em=mean_a/m
    eg=mean_b/m
    emg=e_ab/F(m*(m+1))
    em2=e_a2/F(m*(m+1))
    eg2=e_b2/F(m*(m+1))
    return em,eg,emg-em*eg,em2-em*em,eg2-eg*eg


def claimed_moments(m):
    h=sum((F(1,j) for j in range(1,m+1)),F())
    h2=sum((F(1,j*j) for j in range(1,m+1)),F())
    em=h/m
    eg=F(m-1,2*m)
    cov=((m+1)*h-2*m)/F(2*m*m*(m+1))
    vm=(m*h2-h*h)/F(m*m*(m+1))
    vg=F(m-1,12*m*m)
    return em,eg,cov,vm,vg

for m in range(2,501):
    actual=direct_exponential_gap_moments(m)
    expected=claimed_moments(m)
    assert actual==expected,(m,actual,expected)
    assert actual[2]>0 and actual[3]>0 and actual[4]>0
assert claimed_moments(2)[2]==F(1,48)
assert claimed_moments(3)[2]==F(1,54)
print('EXACT PASS: 499 full-five-moment rational identities, m=2..500')

random.seed(330409)
for m in (2,3,5,10):
    n=60000
    sm=sg=smg=0.
    for _ in range(n):
        y=[random.expovariate(1) for _ in range(m)]
        s=sum(y);x=[v/s for v in y]
        mx=max(x)
        g=sum(abs(x[i]-x[j]) for i in range(m) for j in range(i+1,m))/m
        sm+=mx;sg+=g;smg+=mx*g
    cv=smg/n-(sm/n)*(sg/n)
    target=float(claimed_moments(m)[2])
    print(f'MC diagnostic m={m}: covariance={cv:.8f}; theory={target:.8f}; abs_err={abs(cv-target):.8f}')
    assert abs(cv-target)<0.003
print('PASS: exact moments and independent Monte Carlo diagnostics')
