#!/usr/bin/env python3
"""Reproduce the finite pair-covariance identity and square-root overlap transition.

Standard library only: python3 check.py
"""
from fractions import Fraction
from itertools import combinations
from math import comb, lgamma, exp, log, sqrt, e, isqrt

checks = 0

def assert_equal(a,b):
    global checks
    assert a == b, (a,b)
    checks += 1

def probability_both_collected(n,r,s,j):
    union = 2*s-j
    if union > r:
        return Fraction(0)
    return Fraction(comb(n-union,r-union), comb(n,r))

def probability_single_collected(n,r,s):
    return Fraction(comb(n-s,r-s), comb(n,r))

# Enumerate all block choices, for all feasible intersection sizes.
# No probabilistic simulation or floating-point approximation is used here.
for n in range(3,10):
    universe = tuple(range(n))
    for s in range(1,n):
        A = frozenset(range(s))
        for r in range(s,n):
            blocks = [frozenset(block) for block in combinations(universe,r)]
            a = probability_single_collected(n,r,s)
            assert_equal(Fraction(sum(A.issubset(block) for block in blocks),len(blocks)),a)
            previous_b = None
            for j in range(max(0,2*s-n),s+1):
                B = frozenset(tuple(range(j))+tuple(range(s,s+(s-j))))
                assert_equal(len(A&B),j)
                b = probability_both_collected(n,r,s,j)
                actual_b = Fraction(sum(A.issubset(block) and B.issubset(block) for block in blocks),len(blocks))
                assert_equal(actual_b,b)
                if previous_b is not None:
                    assert_equal(previous_b <= b,True)
                previous_b = b
                for k in (1,2,3):
                    joint = (1-2*a+b)**k
                    marginal_sq = ((1-a)**k)**2
                    covariance = joint - marginal_sq
                    assert_equal((covariance>0)-(covariance<0),(b>a*a)-(b<a*a))
                    if r==n-1:
                        assert_equal(joint,Fraction(j,n)**k)
                        assert_equal(covariance,Fraction(j,n)**k-Fraction(s*s,n*n)**k)

# Check a finite, nontrivial overlap-sign transition.
n,r,s = 100,50,12
p = probability_single_collected(n,r,s)
for j in (0,1,2):
    assert_equal(probability_both_collected(n,r,s,j) < p*p,True)
for j in (3,4,5):
    assert_equal(probability_both_collected(n,r,s,j) > p*p,True)

# Numerically check convergence of the exact factorial ratio in the critical regime.
def log_ratio(n,r,s,j):
    def logfall(m,k):
        return lgamma(m+1)-lgamma(m-k+1)
    def log_a(k):
        return logfall(r,k)-logfall(n,k)
    return log_a(2*s-j)-2*log_a(s)

rho=0.45
c=1.1
for j in (0,1,2,3):
    target = j*log(1/rho) -(1-rho)*c*c/rho
    vals=[]
    for n in (10000,40000,160000):
        r=round(rho*n)
        s=round(c*sqrt(n))
        vals.append(log_ratio(n,r,s,j))
    assert_equal(abs(vals[-1]-target) < abs(vals[0]-target),True)
    assert_equal(abs(vals[-1]-target)<0.024,True)

# The limiting global sign census at rho=1/2, c=1 has probability
# 1-2/e of positive pairs and 2/e of negative pairs.
for n in (100,400,2500,10000):
    r = n//2
    s = isqrt(n)
    p = probability_single_collected(n,r,s)
    for j in (0,1):
        assert_equal(probability_both_collected(n,r,s,j) < p*p,True)
    assert_equal(probability_both_collected(n,r,s,2) > p*p,True)
    num_positive = sum(comb(s,j)*comb(n-s,s-j) for j in range(2,s+1))
    p_positive = Fraction(num_positive,comb(n,s))
    assert_equal(abs(float(p_positive) - (1-2/e))<0.008,True)
    # Under independent uniform target choices, E(J)=s^2/n exactly.
    assert_equal(Fraction(s*s,n),Fraction(1))
    p_one = Fraction(s*comb(n-s,s-1),comb(n,s))
    p_intersection = 1-Fraction(comb(n-s,s),comb(n,s))
    p_neg_given_overlap = p_one/p_intersection
    assert_equal(abs(float(p_neg_given_overlap)-1/(e-1))<0.03,True)

print(f"PASS: {checks} exact and numerical assertions")
