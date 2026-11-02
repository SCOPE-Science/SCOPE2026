#!/usr/bin/env python3
"""Finite-chain and asymptotic checks for reset-walk entropy on complete bipartite graphs.
Standard library only; no external data or nondeterministic simulation.
"""
import math
from fractions import Fraction

checks=0

def check(c, why):
    global checks
    checks+=1
    if not c: raise AssertionError(why)

def h(r):
    return -sum(x*math.log(x) for x in (r,1-r) if x>0)

def entropy(vals):
    return -sum(float(x)*math.log(float(x)) for x in vals if x>0)

def exact_formula(m,n,r):
    q=1-r
    a=r+q/m
    b=q/m
    g=-sum(k*math.log(k) for k in (a,) if k>0)-(m-1)*b*math.log(b) if b>0 else 0.0
    return (h(r)+q*math.log(n)+q*g)/(2-r)

def direct(m,n,r):
    """Construct all rows explicitly, verify stated stationary masses and row entropies."""
    q=1-r
    pi=[r+q*q/(m*(2-r))]+[q*q/(m*(2-r))]*(m-1)+[q/(n*(2-r))]*n
    P=[]
    for i in range(m+n):
        if i<m:
            P.append([r]+[0.0]*(m-1)+[q/n]*n)
        else:
            P.append([r+q/m]+[q/m]*(m-1)+[0.0]*n)
    check(abs(sum(pi)-1)<1e-12,'normalization')
    for row in P:check(abs(sum(row)-1)<1e-12,'row stochasticity')
    for j in range(m+n):
        check(abs(sum(pi[i]*P[i][j] for i in range(m+n))-pi[j])<1e-12,'stationarity')
    return sum(pi[i]*entropy(P[i]) for i in range(m+n))

def golden_max(m,n):
    # Since asymptotic theorems do not assert finite-size unimodality, also scan a grid.
    lo,hi=1e-15, 1-1e-13
    a=lo+(hi-lo)*.3819660112501051
    b=lo+(hi-lo)*.6180339887498949
    fa,fb=exact_formula(m,n,a),exact_formula(m,n,b)
    for _ in range(175):
        if fa<fb:
            lo=a; a=b;fa=fb;b=lo+(hi-lo)*.6180339887498949;fb=exact_formula(m,n,b)
        else:
            hi=b;b=a;fb=fa;a=lo+(hi-lo)*.3819660112501051;fa=exact_formula(m,n,a)
    x=(lo+hi)/2
    return x, exact_formula(m,n,x)

for m in range(1,9):
    for n in range(1,8):
        for r in (.0,1/11,1/4,2/3, .999):
            check(abs(direct(m,n,r)-exact_formula(m,n,r))<5e-13,'finite transition entropy')
        check(abs(exact_formula(m,n,0)-.5*math.log(m*n))<1e-12,'base rate')
        check(abs(exact_formula(m,n,1))<1e-12,'full reset')

for n in (1,2,5,10):
    for m in (10**5,10**6,10**7):
        r,v=golden_max(m,n)
        s=(m**3*n)**(-.25)
        check(abs(r/s-1)<.09,'unbalanced optimal rate')
        gain=v-exact_formula(m,n,0)
        check(abs(gain/s-1)<.18,'unbalanced optimal gain')
        # Independent finite grid compares reported maximum with values on all coarse scales.
        for trial in (.001,.01,.1,1,10,100):
            r0=min(.99,max(1e-15,s*trial))
            check(v>=exact_formula(m,n,r0)-1e-10,'unbalanced comparison')

for rho in (.25,.5,1,2,4):
    for m in (1000,10000,100000):
        n=round(m*rho)
        r,v=golden_max(m,n)
        t=(math.sqrt(1+4/math.sqrt(rho))-1)/2
        check(abs(m*r/t-1)<.025,'balanced optimal rate')
        gain=v-exact_formula(m,n,0)
        gain_lim=(2*t-math.log(1+t))/(2*m)
        check(abs(gain/gain_lim-1)<.025,'balanced optimal gain')
        for trial in (.1, .3, 1, 3, 10):
            rr=min(.99,r*trial)
            check(v>=exact_formula(m,n,rr)-1e-10,'balanced comparison')

print('PASS: %d deterministic checks (finite transition matrices, asymptotic scaling, gain and comparison grids)'%checks)
