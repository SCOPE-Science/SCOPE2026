"""Standalone finite verification for the logarithmic near-complete fair coupon crossover.
Python 3, standard library only. Experiments do not substitute for the proof.
"""
from itertools import combinations, product
from fractions import Fraction
from math import comb, factorial, exp, lgamma, log, pi

def falling(n, r):
    z = 1
    for i in range(r):
        z *= n - i
    return z

def factorial_moment(N, M, t, r):
    if r > M and t > 0:
        return Fraction(0)
    return Fraction(falling(M, r)**t, falling(N, r)**(t-1))

def enumerate_unseen(N, M, t):
    """Enumerate all ordered independent missing-set sequences."""
    full = (1 << N) - 1
    choices = [sum(1 << j for j in s) for s in combinations(range(N), M)]
    counts = [0] * (N + 1)
    for seq in product(choices, repeat=t):
        unseen = full
        for mask in seq:
            unseen &= mask
        counts[unseen.bit_count()] += 1
    return counts, len(choices)**t

def check_exact(N, M, t):
    counts, total = enumerate_unseen(N, M, t)
    assert sum(counts) == total
    for r in range(M + 2):
        from_enum = Fraction(sum(counts[k]*falling(k, r) for k in range(N + 1)),total)
        assert from_enum == factorial_moment(N, M, t, r), (N, M, t, r, from_enum)
    # Pairwise unseen indicators have negative covariance.
    if N > 1:
        one = Fraction(M, N) ** t
        two = Fraction(M*(M-1),N*(N-1)) ** t
        assert two <= one**2
    return M + 2

num = 0
for N, M, time in [(6,3,1),(6,3,2),(6,3,3),(5,1,1),(5,1,2),(5,1,3),(5,1,4),(10,4,1),(10,4,2)]:
    num += check_exact(N,M,time)

# Spot-check the logarithmic asymptotic on several large integer pairs.
for x in (-1.0,0.0,1.0):
    target = exp(x)/(2*pi)**0.5
    deviations = []
    for c in (8,12,18,24,32):
        m = round(exp(c + .5*log(c) - x))
        assert m > 2*c
        logN = sum(log(m-i) for i in range(c)) - lgamma(c+1)
        nu = exp(logN+(c+1)*log(c/m))
        delta = c-log(m)+.5*log(log(m))
        matched = exp(delta)/(2*pi)**0.5
        assert abs(log(nu/matched)) < .2
        deviations.append(abs(log(nu/target)))
    assert deviations[-1] < deviations[0]
    assert deviations[-1] < .12, (x,deviations)
    num+=5

# Exact star expected time: sum of stages to c+1 distinct centers.
for m in range(4,15):
    for c in range(1, m-1):
        expectation = sum((Fraction(m, m-j) for j in range(c+1)), Fraction(0))
        formula = m*sum((Fraction(1,j) for j in range(m-c,m+1)),Fraction(0))
        assert expectation == formula
        num += 1
print('PASS',num,'finite checks; exact enumeration and asymptotic numerical checks')
