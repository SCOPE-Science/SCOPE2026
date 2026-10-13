#!/usr/bin/env python3
"""Reproduce exact finite-horizon covariance identities and illustrative parameter checks.

All arithmetic used in covariance identities and the counterexample is exact
(Fraction). Floating-point sweeps are diagnostics, not exhaustive proof.
Run: python3 verify.py
"""
from fractions import Fraction as F
from math import comb, sqrt

checks = 0

def check(assertion, message):
    global checks
    if not assertion:
        raise AssertionError(message)
    checks += 1

def block(c, q, a):
    p = (1+c)/2
    r = (1-c)/2
    u = p*r
    return ((1-a*p)**2, a*a*u/q, (1-a*r)**2)

def covariance_branches(c, q, a):
    p, r = (1+c)/2, (1-c)/2
    # Tested rational cosines permit rational sqrt(p*r).
    sq = {F(0):F(1,2), F(3,5):F(2,5), F(5,13):F(6,13), F(15,17):F(4,17)}[c]
    for j in range(q+1):
        xi = F(2*j-q,q)
        yield F(comb(q,j),2**q), 1-a*p, -a*sq*xi, 1-a*r

def step_cov(cov, branches):
    x,z,y=cov
    X=Y=Z=F(0)
    for prob,A,B,D in branches:
        X+=prob*(A*A*x+2*A*B*z+B*B*y)
        Z+=prob*(A*B*x+(A*D+B*B)*z+B*D*y)
        Y+=prob*(B*B*x+2*B*D*z+D*D*y)
    return X,Z,Y

for c in (F(0),F(3,5),F(5,13),F(15,17)):
    for q in range(1,7):
        for a in (F(1,2),F(1),F(7,4),F(9,4),F(3)):
            a11,b,a22=block(c,q,a)
            p,r=(1+c)/2,(1-c)/2
            u=p*r
            first=step_cov((F(2,3),F(1,7),F(5,4)),list(covariance_branches(c,q,a)))
            check(first[0]==a11*F(2,3)+b*F(5,4),'first diagonal')
            check(first[2]==b*F(2,3)+a22*F(5,4),'second diagonal')
            # Exact symbolic (at rational arguments) factorization of the
            # determinant used to identify the stability boundary.
            determinant=(1-a11)*(1-a22)-b*b
            factor=a*a*u*(4-2*a+a*a*u*(1-F(1,q*q)))
            check(determinant==factor,'determinant identity')
            x0,y0=F(4,7),F(11,13)
            x,z,y=x0*x0,x0*y0,y0*y0
            ex,ey=x,y
            branches=list(covariance_branches(c,q,a))
            for t in range(1,5):
                x,z,y=step_cov((x,z,y),branches)
                ex,ey=a11*ex+b*ey,b*ex+a22*ey
                check(x==ex and y==ey,f'finite-horizon exact moment t={t}')

# Nonmonotonic expected error but geometrically decaying moments.
c,q,a=F(3,5),2,F(9,4)
x,b,y=block(c,q,a)
check((x,b,y)==(F(16,25),F(81,200),F(121,400)),'witness T')
check(x+b==F(209,200),'witness expanding first iteration')
check((1-x)*(1-y)-b*b==F(3483,40000),'witness positive definite I-T')
check(1-x>0 and 1-y>0,'witness stable')

for q in range(1,11):
    for c in (0.02,0.1,0.3,0.6,0.9,0.99):
        limit=4/(1+sqrt(c*c+(1-c*c)/q**2))
        one=4/(1+c+(1-c)/q)
        if q>1:
            check(one<limit and 2<limit,'strict window')
        else:
            check(abs(limit-2)<1e-12,'single sample threshold')
        for ratio in (0.4,0.99,1.,1.01,1.4):
            a=ratio*limit
            t11,b,t22=block(c,q,a)
            radius=((t11+t22)/2+sqrt((t11-t22)**2/4+b*b))
            check((radius<1)==(ratio<1) or abs(radius-1)<1e-12,'sharp boundary')

# Near-coincident-row asymptotics, numerical diagnostics only.
for q in (1,2,3,5):
    for delta in (1e-4,1e-5):
        c=1-delta
        def rate(a):
            x,b,y=block(c,q,a)
            return (x+y)/2+sqrt((x-y)**2/4+b*b)
        # golden section on [1,2], no non-stdlib packages
        lo,hi=1.,2.
        phi=(sqrt(5)-1)/2
        u=hi-phi*(hi-lo);v=lo+phi*(hi-lo)
        for _ in range(150):
            if rate(u)>rate(v):
                lo=u;u=v;v=lo+phi*(hi-lo)
            else:
                hi=v;v=u;u=hi-phi*(hi-lo)
        star=(lo+hi)/2
        check(abs((2-star)/sqrt(delta)-sqrt(2)/q)<0.02,'near-coherent optimizer asymptotic')
        check(abs((rate(star)-(1-2*delta))/delta**1.5-2*sqrt(2)/q)<0.16,'near-coherent rate asymptotic')

print('VERIFY_OK',checks,'checks')
