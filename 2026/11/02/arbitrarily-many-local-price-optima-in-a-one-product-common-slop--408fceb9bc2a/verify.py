#!/usr/bin/env python3
"""Rational interval certification for finite illustrative logistic-pricing instances.

The unbounded-mode theorem is analytical; this script certifies only the
specified finite derivative signs without floating-point assumptions.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial

TERMS = 400

@lru_cache(None)
def exp_interval(x):
    """Exact rational interval enclosing exp(x) for an integer x."""
    assert isinstance(x, int)
    if x < 0:
        lo, hi = exp_interval(-x)
        return 1 / hi, 1 / lo
    if x == 0:
        return F(1), F(1)
    term = F(1)
    lower = term
    for k in range(1, TERMS + 1):
        term *= F(x, k)
        lower += term
    first_omitted = term * F(x, TERMS + 1)
    ratio = F(x, TERMS + 2)
    assert ratio < 1
    return lower, lower + first_omitted / (1 - ratio)


def q_derivative_interval(p, v):
    """Enclose d/dp (p/(1+exp(p-v))) exactly."""
    lo, hi = exp_interval(p - v)
    coefficient = 1-p
    a = 1 + coefficient * lo
    b = 1 + coefficient * hi
    nlo, nhi = min(a, b), max(a, b)
    dlo, dhi = (1 + lo) ** 2, (1 + hi) ** 2
    candidates = [nlo/dlo, nlo/dhi, nhi/dlo, nhi/dhi]
    return min(candidates), max(candidates)


def mixed_derivative_interval(p, values, weights):
    lower = upper = F(0)
    for v, w in zip(values, weights):
        lo, hi = q_derivative_interval(p, v)
        lower += w * lo
        upper += w * hi
    return lower, upper


def decimal_str(f):
    return f'{float(f):+.12e}'


def certify():
    vals = [2, 15, 40, 80]
    weights = [F(1), F(1,100), F(1,100000), F(1,1000000000)]
    witness_pairs = [(0,3), (10,15), (35,41), (75,81)]
    assertions = 0
    for m in range(1,5):
        assert sum(weights[:m]) > 0
        assert len(vals[:m]) == m
        assert all(weights[j]>0 for j in range(m))
        assert all(vals[j]<vals[j+1] for j in range(m-1))
        assertions += 4
        print('segments',m)
        previous = -1
        for a,b in witness_pairs[:m]:
            assert previous<a<b
            previous=b
            assertions += 1
            lo, hi = mixed_derivative_interval(a, vals[:m], weights[:m])
            assert lo > 0, (m, a, decimal_str(lo), decimal_str(hi))
            assertions += 1
            print('  dR/dp at',a, 'is positive, lower bound', decimal_str(lo))
            lo, hi = mixed_derivative_interval(b, vals[:m], weights[:m])
            assert hi < 0, (m, b, decimal_str(lo), decimal_str(hi))
            assertions += 1
            print('  dR/dp at',b, 'is negative, upper bound', decimal_str(hi))
        # Positive normalization cannot change derivative signs.
        assert sum(weights[:m]) != 0
        assertions += 1
    print('PASS: %d exact rational assertions; finite witnesses only' % assertions)


if __name__ == '__main__':
    certify()
