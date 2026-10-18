#!/usr/bin/env python3
"""Exact finite-instance tests for a one-row random coordinate-descent theorem."""
from fractions import Fraction as Q
from itertools import product

def risk_by_paths(b, schedule, y=Q(3,2)):
    n=len(schedule)
    total=Q(0)
    for path in product(range(b),repeat=n):
        x=[Q(0)]*b
        for k,i in enumerate(path):
            residual=y-sum(x)
            x[i]+=schedule[k]*residual
        total+=sum((a-y/b)**2 for a in x)
    return total/(b**n)

def terminal_residual(b,schedule,y=Q(3,2)):
    r=y
    for h in schedule:
        r*=1-h
    return r

def baseline_risk(b,n,h,y=Q(3,2)):
    q=1-h
    return y*y*q**(2*n)/b + y*y*(b-1)*h*(1-q**(2*n))/(b*(2-h))

cases=0
for b in (2,3,4):
    for n in range(1,6 if b==2 else 5 if b==3 else 4):
        schedule=[Q(1,n+b-1-k) for k in range(n)]
        observed=risk_by_paths(b,schedule)
        expected=Q(3,2)**2*Q(b-1,b*(n+b-1))
        assert observed==expected,(b,n,observed,expected)
        assert terminal_residual(b,schedule)==Q(3,2)*Q(b-1,n+b-1)
        exact=[Q(1,n-k) for k in range(n)]
        assert risk_by_paths(b,exact)==Q(3,2)**2*Q(b-1,b*n)
        assert terminal_residual(b,exact)==0
        cases+=4
        for h in (Q(1,5),Q(1,2),Q(3,4),Q(5,4)):
            direct=risk_by_paths(b,[h]*n)
            formula=baseline_risk(b,n,h)
            assert direct==formula,(b,n,h,direct,formula)
            cases+=1
        # The risk-optimal path beats alternative schedules even when they interpolate.
        assert observed<=risk_by_paths(b,[Q(1)]*n)
        cases+=1
for b in (2,3,4):
    for h in (Q(1,5),Q(1,2),Q(3,4),Q(1),Q(5,4)):
        for n in range(5):
            delta=baseline_risk(b,n+1,h)-baseline_risk(b,n,h)
            expected=-Q(3,2)**2*h*(2-b*h)*(1-h)**(2*n)/b
            assert delta==expected,(b,h,n)
            cases+=1
print('PASS:', cases, 'exact-rational identities and exhaustive coordinate-path checks.')
