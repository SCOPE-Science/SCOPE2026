#!/usr/bin/env python3
"""Supplemental exact-arithmetic and numerical checks for a cubic Allee patch model.

This program checks algebraic identities and representative numerical trajectories.
The accompanying written proof supplies the all-parameter statements.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import product
from math import ceil

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def f(x, theta, rate=1):
    return rate*x*(x-theta)*(1-x)


def group_flow(p, rate, mixing, theta, final=12.0):
    # Two symmetry classes: fraction p initially occupied and 1-p vacant.
    u, v = 1.0, 0.0
    steps = ceil(final*mixing/.08)
    h = final/steps
    def rhs(a, b):
        q = p*a+(1-p)*b
        return (rate*a*(a-theta)*(1-a)+mixing*(q-a),
                rate*b*(b-theta)*(1-b)+mixing*(q-b))
    for _ in range(steps):
        a1,b1=rhs(u,v)
        a2,b2=rhs(u+h*a1/2,v+h*b1/2)
        a3,b3=rhs(u+h*a2/2,v+h*b2/2)
        a4,b4=rhs(u+h*a3,v+h*b3)
        u+=h*(a1+2*a2+2*a3+a4)/6
        v+=h*(b1+2*b2+2*b3+b4)/6
    return p*u+(1-p)*v


def root_binary(p, mu):
    a,b=p-.01,p+.01
    for _ in range(35):
        mid=(a+b)/2
        if group_flow(p,1.0,mu,mid)>mid:
            a=mid
        else:
            b=mid
    return (a+b)/2

# Exact expansion of the cubic reaction in centered moments.
for n in range(2,8):
    for numerators in product(range(0,4),repeat=n):
        if sum(numerators)==0 or sum(numerators)==3*n:
            continue
        xs=[F(k,3) for k in numerators]
        q=sum(xs)/n
        z=[x-q for x in xs]
        V=sum(t*t for t in z)/n
        T=sum(t*t*t for t in z)/n
        for theta in [F(1,7),F(1,2),F(5,6)]:
            lhs=sum(f(x,theta) for x in xs)/n-f(q,theta)
            rhs=(1+theta-3*q)*V-T
            verify(lhs==rhs,'cubic average identity')

# Two-class exact boundary identity and binomial moment coefficient.
for n in range(2,18):
    for m in range(1,n):
        p=F(m,n)
        V=p*(1-p)
        T=p*(1-p)*(1-2*p)
        coefficient=(1-2*p)*V/2-T/3
        verify(coefficient==p*(1-p)*(1-2*p)/6,'binomial coefficient')
        for k in range(1,12):
            w=F(k,12)
            u=p+(1-p)*w
            v=p-p*w
            actual=p*f(u,p)+(1-p)*f(v,p)
            expected=p*(1-p)*(1-2*p)*w*w*(1-w)
            verify(actual==expected,'binary boundary drift')

# The exact two-patch cancellation and a three-patch coefficient.
verify(F(1,3)*F(2,3)*F(1,3)/6==F(1,81),'three-patch coefficient')
verify(F(1,2)*F(1,2)*(1-2*F(1,2))==0,'balanced cancellation')

# Matched mean and variance, opposite skewness.
A=[F(9,10),F(2,5),F(1,5)]
B=[1-x for x in A]
for X,sign in [(A,-1),(B,1)]:
    q=sum(X)/3
    var=sum((x-q)**2 for x in X)/3
    skew=sum((x-q)**3 for x in X)/3
    verify(q==F(1,2),'mean')
    verify(var==F(13,150),'variance')
    verify(-skew/3==sign*F(1,250),'skewness correction')

# Supplemental finite-rate ODE computations; these do not prove the asymptotics.
for n,m in [(2,1),(3,1),(3,2),(4,1),(4,2),(5,1),(5,3),(8,1)]:
    p=m/n
    c=p*(1-p)*(1-2*p)/6
    for mu in [10.0,30.0,60.0]:
        theta=root_binary(p,mu)
        verify(abs(mu*(theta-p)-c)<.0003,'finite-rate asymptotic')
        if p<.5:
            verify(theta>p,'minority sign')
        elif p>.5:
            verify(theta<p,'majority sign')
        else:
            verify(abs(theta-p)<1e-8,'balanced threshold')
# Independent three-patch integrations verify the skewness-sensitive sign.
def full_flow(initial, mixing, theta, final=12.0):
    x=[float(v) for v in initial]
    steps=ceil(final*mixing/.08)
    h=final/steps
    def rhs(values):
        q=sum(values)/len(values)
        return [v*(v-theta)*(1-v)+mixing*(q-v) for v in values]
    for _ in range(steps):
        k1=rhs(x)
        k2=rhs([v+h*k/2 for v,k in zip(x,k1)])
        k3=rhs([v+h*k/2 for v,k in zip(x,k2)])
        k4=rhs([v+h*k for v,k in zip(x,k3)])
        x=[v+h*(a+2*b+2*c+d)/6 for v,a,b,c,d in zip(x,k1,k2,k3,k4)]
    return sum(x)/len(x)

for initial,sign in [(A,-1),(B,1)]:
    for mixing in [20.0,50.0]:
        lo,hi=.499,.501
        for _ in range(32):
            mid=(lo+hi)/2
            if full_flow(initial,mixing,mid)>mid:
                lo=mid
            else:
                hi=mid
        critical=(lo+hi)/2
        verify((critical-.5)*sign>0,'skewness direction')
        verify(abs(mixing*(critical-.5)-sign/250)<0.0001,
               'skewness first correction')
print('VERIFY_OK assertions='+str(checks))
