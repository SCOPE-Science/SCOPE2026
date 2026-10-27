#!/usr/bin/env python3
"""Dependency-free checks for the exact multi-seed threshold-cascade law."""
from fractions import Fraction
from itertools import product
from math import comb, exp, lgamma, log, log1p, ceil, sqrt, pi

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def pmf_exact(N, s, k):
    if k < s or k > N:
        return Fraction(0, 1)
    if k == s:
        q = Fraction(1, 1)
    else:
        q = Fraction(s * (k ** (k-s-1)), N ** (k-s))
    outside = Fraction((N-k) ** (N-k) if k < N else 1, N ** (N-k))
    return Fraction(comb(N-s, k-s), 1) * q * outside

def direct_counts(N, s):
    counts = {}
    for thresholds in product(range(1, N+1), repeat=N-s):
        active = s
        while True:
            nxt = s + sum(t <= active for t in thresholds)
            if nxt == active:
                break
            active = nxt
        counts[active] = counts.get(active, 0) + 1
    return counts

def pmf_float(N, s, k):
    if k == N:
        return s / N
    if k == s:
        return exp((N-s) * log1p(-s/N)) if N > s else 1.0
    lp = (lgamma(N-s+1) - lgamma(k-s+1) - lgamma(N-k+1)
          + log(s) + (k-s-1)*log(k) - (k-s)*log(N)
          + (N-k)*log1p(-k/N))
    return exp(lp)

# Exact rational normalization over all seed counts, including endpoint conventions.
for N in range(1, 31):
    for s in range(1, N+1):
        masses = [pmf_exact(N, s, k) for k in range(s, N+1)]
        check(sum(masses, Fraction(0, 1)) == 1, f"normalization N={N}, s={s}")
        check(masses[-1] == Fraction(s, N), f"full-cascade mass N={N}, s={s}")

# Exhaustively enumerate every threshold assignment for N<=7 and compare every mass.
for N in range(1, 8):
    for s in range(1, N+1):
        counts = direct_counts(N, s)
        denom = N ** (N-s)
        for k in range(s, N+1):
            observed = Fraction(counts.get(k, 0), denom)
            check(observed == pmf_exact(N, s, k), f"enumeration N={N}, s={s}, k={k}")

# Numerical corroboration of the fixed-s macroscopic-tail coefficient.
for eps in (0.25, 0.5, 0.75):
    coeff = sqrt(2/pi) * sqrt((1-eps)/eps)
    N = 1600
    for s in (1, 2, 3):
        tail = sum(pmf_float(N, s, k) for k in range(ceil(eps*N), N+1))
        ratio = sqrt(N) * tail / (s*coeff)
        check(abs(ratio - 1.0) < 0.04, f"tail ratio eps={eps}, N={N}, s={s}: {ratio}")

print(f"VERIFY_OK {CHECKS} assertions; exact rational normalization N<=30; exhaustive threshold assignments N<=7; tail coefficients at three cutoffs")
