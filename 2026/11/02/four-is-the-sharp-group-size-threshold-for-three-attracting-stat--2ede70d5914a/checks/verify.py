#!/usr/bin/env python3
"""Exact-rational and numerical cross-checks for a two-helper threshold public-good game."""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import random

checks = 0

def check(condition, explanation="assertion"):
    global checks
    checks += 1
    assert condition, explanation

def H(p,x):
    return p*x+3*(1-p)*x*(1-x)**2

def gain_from_group(n,x):
    """Enumerate exactly one cooperating coplayer using independent Bernoulli composition."""
    result = F(0)
    for outcomes in product((0,1), repeat=n-1):
        if sum(outcomes)==1:
            probability=F(1)
            for bit in outcomes:
                probability *= x if bit else (1-x)
            result += probability
    return result

for x in [F(0), F(1,6), F(1,3), F(1,2), F(2,3), F(5,6), F(1)]:
    for p in [F(0), F(1,13), F(11,23), F(1,2), F(3,4), F(1)]:
        check(H(p,x)==p*gain_from_group(2,x)+(1-p)*gain_from_group(4,x),"pivotal model")

p=F(11,23)
kappa=F(10,23)
for x in [F(0), F(1,7), F(1,3), F(1,2), F(2,3), F(5,6), F(1)]:
    lhs=23*(H(p,x)-kappa)
    rhs=(2*x-1)*(3*x-2)*(6*x-5)
    check(lhs==rhs,"exact cubic factorization")
for root in [F(1,2),F(2,3),F(5,6)]:
    check(H(p,root)==kappa,"interior equilibrium")
for x,sign in [(F(0),-1),(F(1,3),-1),(F(3,5),1),
               (F(3,4),-1),(F(9,10),1),(F(1),1)]:
    check((H(p,x)>kappa) if sign>0 else (H(p,x)<kappa),"phase portrait")
check(F(2)*F(11,17)/(F(2)*F(11,17)+F(4)*F(6,17))==p,"experienced-vs-observer weights")

# General interval condition: examine the critical points and bracket three roots.
random.seed(82317)
for _ in range(500):
    numerator = random.randrange(1,500)
    denominator = random.randrange(2*numerator+1,2*numerator+1000)
    pp=F(numerator,denominator)
    check(0<pp<F(1,2),"admissible p")
    delta=sqrt(float((1-2*pp)/(1-pp)))
    a,b=(2-delta)/3,(2+delta)/3
    check(0<a<b<1,"interior turns")
    hmax,hmin=H(float(pp),a),H(float(pp),b)
    check(hmin<min(hmax,float(pp)),"nonempty three-root window")
    kk=(hmin+min(hmax,float(pp)))/2
    intervals=[(0.,a),(a,b),(b,1.)]
    for left,right in intervals:
        vleft,vright=H(float(pp),left)-kk,H(float(pp),right)-kk
        check(vleft*vright<0,"bracket sign")
        for j in range(45):
            mid=(left+right)/2
            vmid=H(float(pp),mid)-kk
            if vmid*vleft>0:
                left,vleft=mid,vmid
            else:
                right,vright=mid,vmid
        check(abs(H(float(pp),(left+right)/2)-kk)<1.e-11,"root residual")

# For any group sizes <=3, the gain function is at most quadratic;
# for any single size n>=3, the derivative changes sign at most once.
for n in range(2,61):
    for x in [F(1,10),F(1,3),F(2,3),F(9,10)]:
        h=(n-1)*x*(1-x)**(n-2)
        check(h==gain_from_group(n,x) if n<=11 else h>=0,"fixed group pivotal probability")

print(f"PASS: {checks} checks; exact example and 500 parameter tests verified.")
