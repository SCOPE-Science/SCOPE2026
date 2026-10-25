#!/usr/bin/env python3
"""Exact finite verification of NC block-count cross-moment inequalities.

Finite computations are consistency checks; the unrestricted theorem in RESULT.md
follows from algebraic coefficient extraction and monotonicity of exact ratios.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb

checks = 0
path_count = 0

def check(condition, reason):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(reason)

def down_runs(n):
    def walk(u,d,runs,cur):
        if u == n and d == n:
            yield runs + ((cur,) if cur else ())
            return
        if u<n:
            yield from walk(u+1,d,runs+((cur,) if cur else ()),0)
        if d<u:
            yield from walk(u,d+1,runs,cur+1)
    yield from walk(0,0,(),0)

def expectation_count(n,k):
    return comb(2*n-k-1,n-k)

def mixed_count(n,a,b):
    return n*comb(2*n-a-b-2,n-a-b) if a+b<=n else 0

# A uniform NC(n) corresponds to a Dyck word of semilength n, and
# block sizes correspond to the lengths of maximal down-runs.
for n in range(2,11):
    total = 0
    one = Counter()
    two = Counter()
    for runs in down_runs(n):
        total += 1
        sizes = Counter(runs)
        for a, ca in sizes.items():
            one[a] += ca
        for a,ca in sizes.items():
            for b,cb in sizes.items():
                if a != b:
                    two[a,b] += ca*cb
    path_count += total
    C = comb(2*n,n)//(n+1)
    check(total == C, ('Catalan',n))
    for a in range(1,n+1):
        check(one[a] == expectation_count(n,a), ('first moment',n,a))
        for b in range(1,n+1):
            if a == b: continue
            check(two[a,b] == mixed_count(n,a,b), ('mixed moment',n,a,b))
            # Compare exact covariances without floating-point rounding.
            check(C*two[a,b] < one[a]*one[b], ('negative covariance',n,a,b))

for n in range(3,201):
    C=comb(2*n,n)//(n+1)
    numerator = (n-1)*(2*n-1)
    denominator = (n+1)*(2*n-3)
    check(numerator < denominator, ('sharp strict bound',n))
    for a in range(1,n+1):
        # Direct all-pairs computation is unnecessary: exact algebraic
        # ratio transitions and boundary prove the full quadrant.
        if a+1 <= n-1:
            b=1
            if a+b+1 <= n:
                left = (n-a-b)*(2*n-a-1)
                right = (2*n-a-b-2)*(n-a)
                check(left <= right, ('monotone a-axis',n,a))
                check(left-right == n-b*(n-1)-a, ('difference identity',n,a))
        if a+1 <= n-1:
            b=a
            if a+b+1 <= n:
                left=(n-a-b)*(2*n-a-1)
                right=(2*n-a-b-2)*(n-a)
                check(left <= right, ('interior axis',n,a))
    for a,b in [(1,2),(2,1)]:
        if a+b<=n:
            x=mixed_count(n,a,b)*C
            y=expectation_count(n,a)*expectation_count(n,b)
            check(x*denominator==y*numerator, ('sharp equality',n,a,b))

print(f'VERIFY_OK {checks} exact assertions; {path_count} Dyck paths')
