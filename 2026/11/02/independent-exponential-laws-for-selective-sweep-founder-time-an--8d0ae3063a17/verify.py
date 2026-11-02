#!/usr/bin/env python3
"""Finite exact and numerical checks for geometric selective-sweep asymptotics."""
from fractions import Fraction as F
from math import ceil, exp, log

checks = 0

def check(condition, explanation):
    global checks
    if not condition:
        raise AssertionError(explanation)
    checks += 1

def geom_pgf(p, s):
    return p*s/(1-(1-p)*s)

# Finite-generation exact-rational iterates of the geometric offspring pgf.
for p in (F(1, 2), F(2, 3), F(3, 5)):
    for s in (F(1, 7), F(1, 3), F(3, 4), F(1, 1)):
        value = s
        for k in range(9):
            check(value == geom_pgf(p**k, s), f"pgf p={p} k={k} s={s}")
            value = geom_pgf(p, value)

# Exact geometric small-value inequality P(q G < delta) <= delta.
for p in (F(1, 2), F(2, 3), F(3, 5)):
    for k in range(9):
        q = p**k
        for delta in (F(1, 2), F(1, 7), F(1, 17), F(1, 101)):
            # Strict qG < delta means G <= ceil(delta/q)-1.
            fraction = delta/q
            threshold = (fraction.numerator + fraction.denominator - 1)//fraction.denominator - 1
            probability = 1-(1-q)**max(0, threshold)
            check(probability <= delta, f"geometric low tail p={p} k={k} delta={delta}")

# The top-two Poisson-score gap has a separate analytic proof in RESULT.md.
# A finite program does not certify the independence or limiting gap law.

# Finite exceedance sums for the transformed triangular exponential scores.
# The expected limiting counts in rectangles x in [0,L], z > 0 are 1-exp(-L).
def b_value(n):
    b = log(n)
    for _ in range(14):
        b -= (b+log(b)-log(n))/(1+1/b)
    return b

for L in (0.5, 1.0):
    target = 1-exp(-L)
    errors = []
    for n in (1000, 5000, 20000, 100000):
        b = b_value(n)
        assert abs(b*exp(b)/n-1) < 1e-12
        observed = sum(exp(-b/(1-i/n)) for i in range(1, min(n, ceil(L*n/b))))
        errors.append(abs(observed-target))
        check(observed > 0, "positive expected exceedances")
    check(all(errors[j+1] < errors[j] for j in range(len(errors)-1)), "finite-intensity convergence trend")
    check(errors[-1] < 0.025, "finite-intensity absolute deviation")

print(f"PASS {checks} assertions")
print("Exact geometric PGF iteration: PASS")
print("Exact lower-tail probability bound: PASS")
print("Finite score-exceedance intensity trend: PASS")
print("Boundary: numerical/finite tests do not certify the infinite limit.")
