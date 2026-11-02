#!/usr/bin/env python3
"""Exact finite arithmetic and numerical checks for a two-habitat ratio-support theorem.
No external packages are required; analytical proof remains essential.
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random

checks = 0

def check(pred, msg=""):
    global checks
    assert pred, msg
    checks += 1

def f(t,z):
    return (z + t)/(1 + t*z)

def qdual(q,s):
    return (1-q)/(1-q+s*s*q)

def tau(q,s):
    t=q*s/(1-q)
    return min(t,1/t)

def root(a,t):
    a,t=float(a),float(t)
    return ((a-1)+sqrt((a-1)**2+4*a*t*t))/(2*a*t)

def transitions(a,s):
    k=a*a+a+1
    return a/(a+s*k), F(1)/(1+s), k/(k+a*s)

# The key rational Mobius, inversion, and dispersal duality identities.
vals=[F(1,10),F(1,3),F(2,3),F(1),F(4),F(10)]
for t in vals:
    for z in vals:
        check(f(t,1/z)==1/f(t,z),"reciprocal symmetry")
        check(f(1/t,z)==1/f(t,z),"dual Mobius branch")

for a in [F(3,2),F(2),F(3),F(7,2),F(5),F(9)]:
    for s in [F(1,5),F(1,2),F(3,4),F(1)]:
        lo,mix,hi=transitions(a,s)
        check(0<lo<mix<hi<1,"threshold order")
        critical=a/(a*a+a+1)
        check(tau(lo,s)==critical,"lower critical")
        check(tau(hi,s)==critical,"upper critical")
        check(tau(mix,s)==1,"well mixed")
        check(qdual(lo,s)==hi,"critical dual")
        for q in [lo/2,lo,(lo+mix)/2,mix,(mix+hi)/2,hi,(1+hi)/2]:
            if q in (F(0),F(1)): continue
            q2=qdual(q,s)
            check(0<q2<1 and qdual(q2,s)==q,"involution")
            check(tau(q,s)==tau(q2,s),"same reduced coupling")
            t=q*s/(1-q)
            for r in [F(1,7),F(1),F(7)]:
                for env in [a,1/a]:
                    check(f(t,env*r)*f(1/t,env*r)==1,"dual branch")
            T=tau(q,s)
            # The positive root R of P(X)=a*T*X^2+(1-a)*X-T.
            # P(a) has the same sign as (T-critical).
            P=a*T*a*a+(1-a)*a-T
            check(P==(a-1)*(T*(a*a+a+1)-a),"critical polynomial")
            R=root(a,T)
            check(isclose(float(a*T)*R*R+float(1-a)*R-float(T),0,abs_tol=1e-9),"root")
            check(isclose(f(float(T),float(a)*R),R,abs_tol=1e-9),"extremal fixed point")
            X=f(float(T),R/float(a))
            check((R>=float(a)-1e-10)==(T<=critical),"interval versus Cantor boundary")
            if T==1:
                check(isclose(X,1,abs_tol=1e-10) and isclose(R,1,abs_tol=1e-10),"well mixed collapse")
            elif T<critical:
                check(X>1+1e-10,"overlapping first images")
            elif T>critical:
                check(X<1-1e-10,"separated first images")
            else:
                check(isclose(X,1,abs_tol=1e-10),"touching first images")

# Exact, visually interpretable example (no simulations used to prove universality).
a,s=F(2),F(1)
lo,mix,hi=transitions(a,s)
check((lo,mix,hi)==(F(2,9),F(1,2),F(7,9)),"example exact thresholds")
check(qdual(F(1,6),s)==F(5,6),"interval paired migrations")
check(qdual(F(1,3),s)==F(2,3),"Cantor paired migrations")
check(tau(F(1,6),s)==F(1,5),"interval reduced coupling")
check(tau(F(1,3),s)==F(1,2),"Cantor reduced coupling")
check(isclose(root(a,F(1,5)),(5+sqrt(33))/4,abs_tol=1e-12),"interval endpoint")
check(isclose(root(a,F(1,2)),(1+sqrt(3))/2,abs_tol=1e-12),"Cantor endpoint")
print("PASS",checks,"exact rational identities and floating root consistency checks")
print("a=2, s=1: q thresholds",lo,mix,hi)
for q in [F(1,6),F(1,3),F(1,2),F(2,3),F(5,6)]:
    T=tau(q,s)
    R=root(a,T)
    X=f(float(T),R/float(a))
    state='singleton' if T==1 else ('interval' if X>=1-1e-12 else 'Cantor')
    print("q=",str(q),"support=",state,"R=",format(R,'.12g'),"inner endpoint=",format(X,'.12g'))
