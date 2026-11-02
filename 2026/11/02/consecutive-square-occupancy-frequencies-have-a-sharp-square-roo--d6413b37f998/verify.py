#!/usr/bin/env python3
"""Exact checks for the critical occupancy-frequency covariance theorem.
Standard-library only. Finite tests do not replace the infinite proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, exp, isqrt, sqrt


def ratio(B, N, r, s):
    assert B >= 3 and 1 <= r < s and N >= r+s
    # Equivalent independently factorized expression for the ratio of joint to product marginals.
    return (Fraction(B-1, B) * Fraction(comb(N-r, s), comb(N, s)) *
            Fraction((B-2)**(N-r-s) * B**N, (B-1)**(2*N-r-s)))


def covariance(B, N, r, s):
    p = Fraction(comb(N, r) * (B-1)**(N-r), B**N)
    q = Fraction(comb(N, s) * (B-1)**(N-s), B**N)
    joint = Fraction(comb(N, r)*comb(N-r, s)*(B-2)**(N-r-s), B**N)
    return B*(B-1)*joint-B*B*p*q, Fraction((B-1)*joint, B*p*q)


checks = 0
# Direct, independent enumeration of all assignments for several small instances.
for B in (3, 4):
    for N in range(3, 8):
        assignments = list(product(range(B), repeat=N))
        occupancy_vectors = [Counter(a) for a in assignments]
        for r in range(1, N):
            for s in range(r+1, N+1):
                if r+s > N:
                    continue
                xs = [sum(c.get(j, 0) == r for j in range(B)) for c in occupancy_vectors]
                ys = [sum(c.get(j, 0) == s for j in range(B)) for c in occupancy_vectors]
                observed = (Fraction(sum(x*y for x, y in zip(xs, ys)), len(xs))-
                            Fraction(sum(xs)*sum(ys), len(xs)**2))
                theoretical, direct_ratio = covariance(B, N, r, s)
                assert observed == theoretical
                assert direct_ratio == ratio(B, N, r, s)
                checks += 2

# Strict log-concavity, checked exactly on a substantially larger finite grid.
for B in (3, 4, 5, 8, 13):
    for r, s in ((1,2), (1,3), (1,4), (1,5), (2,3), (2,7), (4,9)):
        values = [ratio(B, N, r, s) for N in range(r+s, r+s+300)]
        for j in range(1, len(values)-1):
            assert values[j]**2 > values[j-1]*values[j+1]
            checks += 1
        signs = [v > 1 for v in values]
        assert sum(signs[j] != signs[j-1] for j in range(1, len(signs))) <= 2
        checks += 1

# The positive interval around consecutive-square pairs and its square-root scale.
for k in (1, 2, 3):
    r, s, a = k*k, (k+1)*(k+1), k*(k+1)
    assert (r+s-1)**2 == 4*r*s
    checks += 1
    for B in (10, 20, 40, 80, 160, 320):
        half_width = 4*isqrt(a*B)
        lo = max(r+s, a*B-half_width)
        hi = a*B+half_width
        positives = [N for N in range(lo, hi+1) if ratio(B,N,r,s)>1]
        assert positives == list(range(min(positives),max(positives)+1))
        if B >= 80:
            assert abs((min(positives)-a*B)/sqrt(a*B)+1) < .5
            assert abs((max(positives)-a*B)/sqrt(a*B)-1) < .5
        checks += 3

# Central positive covariance approaches the predicted nonzero constant.
for k in (1, 2):
    r, s, a = k*k, (k+1)*(k+1), k*(k+1)
    target = exp(-2*a)*a**(r+s)/(factorial(r)*factorial(s))
    for B in (20, 50, 100, 300):
        cv, rt = covariance(B, a*B, r, s)
        assert cv > 0
        assert abs(float(cv)/target-1) < 3/B
        assert abs(float((rt-1)*B*B)-1) < 3/B
        checks += 3
print(f'PASS: {checks} finite exact-arithmetic/asymptotic consistency assertions')
