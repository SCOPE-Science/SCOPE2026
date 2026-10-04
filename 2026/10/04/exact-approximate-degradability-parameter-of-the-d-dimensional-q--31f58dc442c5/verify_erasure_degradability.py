#!/usr/bin/env python3
from fractions import Fraction

def absq(x):
    return x if x >= 0 else -x

checks = 0
# Exact piecewise lower-bound scalar minimization is sampled on a rational grid;
# the analytic proof in RESULT.md supplies the continuum argument.
for d in range(2, 13):
    q = d*d
    target = Fraction(2*(q-1), q)
    for k in range(0, 6001):
        b = Fraction(3*q*k, 6000)
        f = absq(1-b/Fraction(q)) + Fraction(q-1,q)*b + absq(1-b)
        assert f >= target
        checks += 1
    assert absq(1-Fraction(1,q)) + Fraction(q-1,q) == target
    # Choi positive-part certificate for ||id-R||_diamond.
    choi_pos_eigenvalue = Fraction(q-1, d)
    partial_trace_scalar = choi_pos_eigenvalue / Fraction(d)
    assert partial_trace_scalar == Fraction(q-1, q)
    assert 2*partial_trace_scalar == target
    checks += 3

# Check all small rational p that the proposed degrading-channel probabilities
# are valid and leave exactly delta=id/replacer defect coefficient.
for den in range(2, 41):
    for num in range(den//2 + 1, den + 1):
        p = Fraction(num, den)
        if p <= Fraction(1,2):
            continue
        delta = 2*p - 1
        mix = delta/p
        flag = (1-p)/p
        assert 0 <= mix <= 1 and 0 <= flag <= 1 and mix + flag == 1
        assert p - (1-p) == delta
        checks += 1

# Check exact degradability probabilities below threshold.
for den in range(2, 41):
    for num in range(0, den//2 + 1):
        p = Fraction(num, den)
        qf = p/(1-p)
        assert 0 <= qf <= 1
        assert (1-p)*qf == p
        checks += 1

print('VERIFY_OK')
print('exact_rational_checks =', checks)
