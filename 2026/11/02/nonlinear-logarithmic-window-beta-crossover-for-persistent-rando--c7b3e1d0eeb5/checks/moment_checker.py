#!/usr/bin/env python3
"""Finite verification of the critical-window coin-turning moment identities.
The analytic functional limit is proven separately; finite checks are not a proof.
"""
from fractions import Fraction
from itertools import product
from math import exp, log, isclose

COUNT=0

def check(condition, message):
    global COUNT
    assert condition, message
    COUNT+=1

def exact_moments(n, c):
    # Critical exponent alpha=1, p_k=c/k.  Only c=1 used here.
    law={(1,1): Fraction(1,2),(-1,-1): Fraction(1,2)}
    for k in range(2,n+1):
        p=Fraction(c,k)
        next_law={}
        for (s,v),w in law.items():
            for flip,prob in [(False,1-p),(True,p)]:
                vv=-v if flip else v
                key=(s+vv,vv)
                next_law[key]=next_law.get(key,Fraction(0))+w*prob
        law=next_law
    return (
        sum(w*s*s for (s,v),w in law.items()),
        sum(w*s**4 for (s,v),w in law.items()),
        sum(w*s*v for (s,v),w in law.items()),
        sum(w*s**3*v for (s,v),w in law.items())
    )

def exact_recur(n,c):
    m2=m4=u1=u3=Fraction(1)
    for k in range(2,n+1):
        g=1-Fraction(2*c,k)
        m2,m4,u1,u3=(
            m2+2*g*u1+1,
            m4+4*g*u3+6*m2+4*g*u1+1,
            g*u1+1,
            g*u3+3*m2+3*g*u1+1
        )
    return m2,m4,u1,u3

def float_recur(n,c,beta):
    alpha=1+beta/log(n)
    m2=m4=u1=u3=1.0
    for k in range(2,n+1):
        p=min(1.,c/(k**alpha))
        g=1-2*p
        m2,m4,u1,u3=(
            m2+2*g*u1+1,
            m4+4*g*u3+6*m2+4*g*u1+1,
            g*u1+1,
            g*u3+3*m2+3*g*u1+1
        )
    return m2/n**2,m4/n**4,1-m4/(3*m2*m2)

for n in range(1,13):
    a=exact_moments(n,1)
    b=exact_recur(n,1)
    for i in range(4):
        check(a[i]==b[i],f'exact recurrence: n={n}, coordinate {i}')

for c in [Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(5,2)]:
    mom=[Fraction(1),Fraction(0)]
    for m in range(2,19):
        am=Fraction(m-1,1)/(m-1+2*c)*mom[m-2]
        mom.append(am)
        if m%2==0:
            j=m//2
            beta_mom=Fraction(1)
            for k in range(j):
                beta_mom*=Fraction(2*k+1,2*k+1+2*c)
            check(am==beta_mom,f'beta stationary even moment {m}, rate={c}')
        else:
            check(am==0,f'stationary odd moment {m}, rate={c}')

for beta in [-2., 0., 2.]:
    lam=exp(-beta)
    var=1/(1+2*lam)
    fourth=3/((1+2*lam)*(3+2*lam))
    binder=2/(3+2*lam)
    errors=[]
    for n in [1000,10000,100000,1000000]:
        a,b,d=float_recur(n,1.,beta)
        check(abs(d-(1-b/(3*a*a)))<1e-12,'Binder definition')
        errors.append(abs(a-var))
        print(f'beta={beta:+.0f} N={n:7d} var={a:.10f} fourth={b:.10f} binder={d:.10f}')
    check(all(x>y for x,y in zip(errors,errors[1:])),f'variance error decreasing at beta={beta}')
    print(f'target beta={beta:+.0f} var={var:.10f} fourth={fourth:.10f} binder={binder:.10f}')
print(f'PASSED {COUNT} finite assertions')
