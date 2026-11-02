#!/usr/bin/env python3
"""Finite, exact checks for the excursion-conditional energy/occupation identity."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb

checks = 0
for n in range(1, 10):
    groups = defaultdict(lambda: [0, 0, 0])
    total_K = total_X2 = total_KX2 = 0
    total_Q = 0
    for positions in combinations(range(2*n), n):
        ups = set(positions)
        height = 0
        lengths = []
        prev_return = 0
        K = X = Q = 0
        for step in range(1, 2*n+1):
            height += 1 if step-1 in ups else -1
            if step % 2:
                X += 1 if height > 0 else -1
            if step < 2*n:
                Q += height*height
            if height == 0:
                K += 1
                lengths.append((step-prev_return)//2)
                prev_return = step
        assert sum(lengths) == n and len(lengths) == K
        X2 = X*X
        counts = groups[tuple(lengths)]
        counts[0] += 1
        counts[1] += Q
        counts[2] += X2
        total_K += K
        total_X2 += X2
        total_KX2 += K*X2
        total_Q += Q
    paths = comb(2*n,n)
    for vector, (count, qsum, xsum) in groups.items():
        target = sum(m*m for m in vector)
        assert Fraction(xsum,count) == target, (n, vector, 'X2'); checks += 1
        assert Fraction(qsum,count) == 2*target-n, (n, vector, 'Q'); checks += 1
    assert len(groups) == 2**(n-1); checks += 1
    assert Fraction(total_X2,paths) == Fraction(n*(n+2),3); checks += 1
    assert Fraction(total_Q,paths) == Fraction(n*(2*n+1),3); checks += 1
    assert Fraction(total_K,paths) == Fraction(4**n,paths)-1; checks += 1
    covariance = Fraction(total_KX2,paths) - Fraction(total_K*total_X2,paths*paths)
    target_cov = -Fraction(n*(n-1)*4**n,12*paths)
    assert covariance == target_cov, (n,covariance,target_cov);checks += 1
    print(f'n={n}, paths={paths}, excursion_vectors={len(groups)}, covariance={covariance}')

# Independent symbolic coefficient verification: the signed-excursion
# second-moment numerator equals n(n+2)/3 times central binomial.
# (1-4z)^(-3/2) coefficient = (2q+1)*binom(2q,q).
# (1-4z)^(-5/2) coefficient = (2q+1)*(2q+3)*binom(2q,q)/3.
for n in range(1, 101):
    b = comb(2*n,n)
    a3 = (2*n-1)*comb(2*n-2,n-1)
    a5 = 0 if n == 1 else Fraction((2*n-3)*(2*n-1)*comb(2*n-4,n-2),3)
    numerator = 2*a3 + 4*a5
    assert numerator == Fraction(n*(n+2)*b,3); checks += 1
    rational = 4*n*4**(n-1) + (0 if n == 1 else 8*comb(n,2)*4**(n-2))
    assert rational == n*(n+3)*4**(n-1); checks += 1

print(f'PASS: {checks} exact assertions; exhaustive bridge paths through n=9 and coefficient identities through n=100')
