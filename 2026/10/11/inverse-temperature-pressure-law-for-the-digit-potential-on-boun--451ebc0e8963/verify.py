#!/usr/bin/env python3
"""Independent finite-language and finite-precision checks of stated identities.

The theorem for all irrational slopes and all temperatures is analytic, not
certified by the finite experiments here. Standard-library only.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import ceil, exp, floor, sqrt

# Rational Fibonacci-convergent test slope. Used only for finite words.
a_rat = Fraction(233, 377)
N = 13

def ceiling(q):
    return -(-q.numerator // q.denominator)

a = [ceiling((i+1)*a_rat)-ceiling(i*a_rat) for i in range(N)]
# Exact rational enclosure of (sqrt(5)-1)/2 verifies that the finite
# prefixes are those of the genuine irrational golden-ratio slope.
lo, hi = Fraction(61803398874989,10**14), Fraction(61803398874990,10**14)
assert (2*lo+1)**2 < 5 < (2*hi+1)**2
for q in (lo, hi):
    assert [ceiling((i+1)*q)-ceiling(i*q) for i in range(N)] == a
assert a[0] == 1
assert all(v in (0, 1) for v in a)

# Independent direct lexicographic language test and weighted counts.
lex_counts = []
for n in range(N+1):
    counts = defaultdict(int)
    for word in product((0, 1), repeat=n):
        if all(word[i:] <= tuple(a[:n-i]) for i in range(n)):
            counts[sum(word)] += 1
    lex_counts.append(dict(counts))

# Return-loop renewal polynomial recurrence: Z_n=T_n+sum L_k Z_(n-k).
rec_counts = [{0: 1}]
assert lex_counts[0] == rec_counts[0]
for n in range(1, N+1):
    result = defaultdict(int)
    result[ceiling(n*a_rat)] += 1
    for k in range(1, n+1):
        if a[k-1] != 1:
            continue
        loop_weight = k*a_rat.numerator//a_rat.denominator
        for ones, count in rec_counts[n-k].items():
            result[ones+loop_weight] += count
    rec_counts.append(dict(result))
    assert rec_counts[n] == lex_counts[n], (n, rec_counts[n], lex_counts[n])

# Numerical roots use the genuine irrational golden slope; finite truncation
# errors are not mistaken for proofs. Report residual and geometric tail bound.
alpha = (sqrt(5)-1)/2
cut = 25000
nvals = []
frac = []
for n in range(1, cut+1):
    f = (n*alpha) % 1.0
    if f <= alpha:
        nvals.append(n)
        frac.append(f)
assert len(nvals) > 14000

def series(t, d):
    return sum(exp(-t*f-d*n) for n, f in zip(nvals, frac))

for t in (20, 60, 200, 500):
    lower, upper = 0.05/t, 5.0/t
    assert series(t,lower) > 1.0 > series(t,upper)
    for _ in range(58):
        mid = (lower+upper)/2
        if series(t, mid)>1.0:
            lower = mid
        else:
            upper = mid
    d = (lower+upper)/2
    err = exp(-d*(cut+1))/(1-exp(-d))
    assert abs(series(t,d)-1) < 1e-9
    assert 0.4 < t*d < 1.3
    assert err < 1e-6
    print(f't={t:3d}; t*(P-t*alpha) approximation={t*d:.9f}; '+
          f'tail absolute upper bound={err:.2e}')
print(f'VERIFY_OK: direct lexicographic and renewal-polynomial counts agree '
      f'for every word length 0..{N} ({sum(2**n for n in range(N+1))} tested binary words).')
