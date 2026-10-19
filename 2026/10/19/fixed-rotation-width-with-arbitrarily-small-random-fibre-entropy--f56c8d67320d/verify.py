#!/usr/bin/env python3
"""Finite consistency checks for a sine-map Bernoulli circle cocycle.

No finite check replaces the analytic entropy or interval theorem.
"""
import itertools
import math
from fractions import Fraction

assertions = 0

def check(condition, explanation):
    global assertions
    if not condition:
        raise AssertionError(explanation)
    assertions += 1

def lift(K, x):
    return x + K * math.sin(2.0 * math.pi * x)

def inv_quarter(K, target):
    lo, hi = 0.0, 0.25
    for _ in range(80):
        m = (lo + hi) / 2
        if lift(K, m) < target:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2

for K in (1, 2, 3, 4, 7, 16, 64, 128):
    check(abs(lift(K, .25) - (.25 + K)) < 1e-10, "positive extremal lift")
    check(abs(lift(K, .75) - (.75 - K)) < 1e-10, "negative extremal lift")
    check(abs(lift(K, 1.0) - lift(K, 0.0) - 1.0) < 1e-10, "degree one")
    branches = [(inv_quarter(K, j), inv_quarter(K, j + .25)) for j in range(K + 1)]
    for j, (left, right) in enumerate(branches):
        check(left <= right + 1e-12, "increasing branch")
        check(abs(lift(K, left) - j) < 3e-10, "left endpoint")
        check(abs(lift(K, right) - j - .25) < 3e-10, "right endpoint")
        check(0 <= left <= .25000001 and 0 <= right <= .25000001, "interval in quarter")
        if j:
            check(branches[j-1][1] < left, "positive gap between branches")
    check(math.log(K + 1) <= math.log(1+2*math.pi*K), "entropy bound nonempty")

# Exact finite observation-clock identity, independent of map details.
for n in range(1, 11):
    for word in itertools.product((0, 1), repeat=n):
        counts = [sum(word[:j]) for j in range(n)]
        check(set(counts) == set(range(sum(word[:n-1]) + 1)), "Bowen observation indices")

for K in (1, 2, 3, 5, 10, 100, 1000):
    for D in (Fraction(1, 3), Fraction(1), Fraction(2), Fraction(7, 2)):
        if 2*K <= D:
            continue
        p = D/(2*K)
        check(Fraction(0) < p < Fraction(1), "nontrivial probability")
        check(p*K == D/2, "exact random rotation endpoint")
        low = float(p) * math.log(K+1)
        up = float(p) * math.log(1+2*math.pi*K)
        check(0 < low <= up, "strict entropy bounds")

for K in (50, 500, 5000, 50000):
    up = math.log(1 + 2 * math.pi * K)/(2*K)
    check(up > 0 and up < 0.3, "width-one entropy upper tends small")

print(f"PASS: {assertions} finite assertions. Infinite results require the written proof.")
