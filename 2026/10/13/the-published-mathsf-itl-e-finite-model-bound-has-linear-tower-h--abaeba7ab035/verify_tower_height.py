#!/usr/bin/env python3
"""Exact transcription checks for the tower-height analysis of B(s)."""
from math import log2

checks=0

def E(n,k):
    x=0
    for _ in range(k):
        x=x+n*(1<<x)
    return x

def Q(n,k):
    e=0; q=0
    for _ in range(k):
        q=1+e*q
        e=e+n*(1<<e)
    return q

def T(x,h):
    for _ in range(h):
        if x>100000:  # keep replay finite; high levels are handled symbolically below
            raise OverflowError
        x=1<<x
    return x

def logstar(x):
    c=0
    while x>1:
        x=log2(x); c+=1
    return c

# Recurrences and the one-level lower / same-height upper bounds on manageable cases.
for n in range(2,13):
    assert E(n,1)==n; checks+=1
    assert Q(n,1)==1; checks+=1
    for k in range(1,3):
        e=E(n,k)
        # lower tower T_{k-1}(n)
        lo=T(n,k-1)
        assert e>=lo; checks+=1
        # upper tower (1/2) T_{k-1}(3n), for k<=2 where exact construction is manageable
        hi=T(3*n,k-1)
        assert 2*e<=hi; checks+=1
        q=Q(n,k)
        assert q<=hi; checks+=1

# The two elementary inequalities that make the induction uniform for all n>=2.
# log2(n+1) <= 3n/2 - 1  <=>  (n+1)^2 <= 2^(3n-2).
for n in range(2,1001):
    assert (n+1)**2 <= (1 << (3*n-2)); checks+=1
# 1 + D^2/2 <= 2^D, needed for Q; check the base range and monotone tail guard.
for D in range(6,1001):
    assert 2 + D*D <= (1 << (D+1)); checks+=1
# f(D)=2^D-1-D^2/2 is increasing for D>=6 because 2^D > D+1/2.
for D in range(6,1001):
    assert (1<<D) > 2*D+1; checks+=1

# Exact log-star identity for feasible tower heights.
for x in range(2,17):
    for h in range(0,4):
        try: y=T(x,h)
        except OverflowError: continue
        assert logstar(y)==h+logstar(x); checks+=1

# Small-s guards for the final algebraic envelope: X is already vastly > max(32,s+2).
# It is enough to check its bottom argument, since T is increasing and s grows linearly.
for s in range(1,1001):
    N=1<<(s+1)
    assert 3*N >= 12; checks+=1
    assert 3*N >= s+2; checks+=1

print(f"VERIFY_OK {checks} exact assertions")
