#!/usr/bin/env python3
"""Finite consistency checks for the path stable-equilibrium counting formula."""

from collections import defaultdict
from math import comb, log


def enumerate_counts(max_n):
    counts = [defaultdict(int) for _ in range(max_n + 1)]

    def visit(weight, active, last_block_was_two, nonempty):
        if nonempty:
            n = weight - 1
            if 1 <= n <= max_n:
                counts[n][active] += 1
        if weight + 2 <= max_n + 1:
            visit(weight + 2, active + 1, False, True)
        if not last_block_was_two and weight + 3 <= max_n + 1:
            visit(weight + 3, active + 2, True, True)

    visit(0, 0, False, False)
    return counts


def formula_count(n, active):
    k = n - active + 1
    m = 2 * active - n - 1
    if k < 1 or m < 0 or m > (k + 1) // 2:
        return 0
    return comb(k - m + 1, m)


max_n = 25
counts = enumerate_counts(max_n)
checks = 0
for n in range(1, max_n + 1):
    for active in range(1, n + 1):
        assert counts[n].get(active, 0) == formula_count(n, active)
        checks += 1

totals = [0] * (max_n + 1)
for n in range(1, max_n + 1):
    totals[n] = sum(counts[n].values())
assert totals[1:6] == [1, 1, 1, 2, 1]
for n in range(6, max_n + 1):
    assert totals[n] == totals[n - 2] + totals[n - 5]

# Bisection for the unique root r in (0, 1) of r^2 + r^5 = 1.
lo, hi = 0.0, 1.0
for _ in range(200):
    mid = (lo + hi) / 2
    if mid * mid + mid**5 < 1:
        lo = mid
    else:
        hi = mid
r = (lo + hi) / 2
lam = 1 / r
s = r**3
alpha_star = (1 + 3 * s) / (2 + 5 * s)
assert abs(r * r + r**5 - 1) < 1e-14
assert 0.5 < alpha_star < 0.6

print(f"PASS: {checks} active-count comparisons for n=1..{max_n}")
print("PASS: total-count recurrence for n=6..25")
print(f"r={r:.12f}; lambda={lam:.12f}; alpha_star={alpha_star:.12f}")
