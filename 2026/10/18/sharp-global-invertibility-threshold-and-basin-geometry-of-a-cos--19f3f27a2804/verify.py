#!/usr/bin/env python3
"""Finite diagnostic checks for an explicit normal-return map theorem.

Only standard-library arithmetic is used. These checks do not replace the
analytic inequalities or the proof for all real parameters and angles.
"""
from fractions import Fraction as Q
from math import acos, asin, atan, cos, isclose, pi, sin, sqrt

checks = 0

def check(condition, explanation):
    global checks
    if not condition:
        raise AssertionError(explanation)
    checks += 1


def data(e, theta):
    R = 3 + e*cos(2*theta)
    p = -2*e*sin(2*theta)
    pp = -4*e*cos(2*theta)
    W = sqrt(R*R - (R*R-1)*p*p)
    return R,p,pp,W


def f(e, theta):
    R,p,_,_ = data(e,theta)
    S = sqrt(R*R+p*p)
    return theta-atan(p/R)+asin(R*p/S)


def deriv(e, theta):
    R,p,pp,W = data(e,theta)
    A = R*(R*R-1)/(W*(R*R+W))
    B = p*p*(W+p*p)/(W*(R*R+p*p))
    return 1+pp*A+B

# Rational identities underlying the global lower bound, independently tested.
for e in [Q(1,50), Q(1,10), Q(1,4), Q(1,3), Q(9,25), Q(39,100)]:
    for k in range(101):
        u = Q(k,100)
        R = 3+e*u
        c = R/(R+2)
        Z = R*u+c*(1-u)
        K = R*R-(R*R-1)*4*e*e
        check(K/R >= c, 'exact bound for K/R')
        check(Z*(R*R+Z)-u*R*R*(R+1) == (R-c)**2*(1-u)**2, 'exact factorization')
        check(4*e*e*(R-1)*(R+2) < R*R, 'uniform small slope criterion')

critical=(sqrt(97)-7)/8
check(abs(4*critical*(2+critical)/(3+critical)-1)<1e-13, 'critical equation')
for e in [0.002,0.11,0.29,critical-0.001,critical,critical+0.001,0.375,0.399]:
    for k in range(512):
        t=2*pi*k/512
        R,p,pp,W=data(e,t)
        check(R>1 and abs(R*p/sqrt(R*R+p*p))<1, 'normal intersects disk transversely')
        check(R*R+2*p*p-R*pp>0,'positive outer polar curvature')
        check(abs((f(e,t+1e-6)-f(e,t-1e-6))/(2e-6)-deriv(e,t))<1e-7,'independent numerical derivative')
        check(abs(f(e,t)-t)<pi/2,'phase lift bound')
for e in [0.002,0.11,0.29,critical-0.001]:
    check(min(deriv(e,2*pi*k/512) for k in range(512))>0,'global increasing map below critical')
for e in [critical+0.001,0.375,0.399]:
    check(deriv(e,0)<0 and deriv(e,pi/2)>1, 'fold and repeller on opposite extrema')
    check(-1<deriv(e,0)<0,'attracting despite folding')
for e in [0.1,0.3,critical-0.001]:
    for t in [0.2,1.2,2.2,4.4,5.7]:
        x=t
        for _ in range(280): x=f(e,x)
        distance=min(abs(x-j*pi) for j in [-2,-1,0,1,2,3])
        check(distance<0.005,'basin convergence sample')
print('All',checks,'finite diagnostics passed. Critical amplitude =', format(critical,'.15f'))
