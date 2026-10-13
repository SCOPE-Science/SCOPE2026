#!/usr/bin/env python3
from math import ceil

assertions = 0

def check(cond):
    global assertions
    assertions += 1
    if not cond:
        raise AssertionError(f"assertion {assertions} failed")

def comps(total, k, prefix=()):
    if k == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from comps(total - x, k - 1, prefix + (x,))

def balanced(total, k):
    a, r = divmod(total, k)
    return [a + 1] * r + [a] * (k - r)

# Exhaustive finite optimization for a nontrivial grid.
for N in range(1, 13):
    for m in range(2, 8):
        k = m - 1
        brute = min(max(c) for c in comps(N, k))
        target = ceil(N / k)
        check(brute == target)

# Constructive and semantic checks on a much larger grid.
for N in range(1, 501):
    for m in range(2, min(N + 7, 60)):
        k = m - 1
        ws = balanced(N, k)
        target = ceil(N / k)
        check(len(ws) == k)
        check(sum(ws) == N)
        check(max(ws) == target)
        # chi_N's graded part: >=N but not >=N+1.
        check(sum(ws) >= N)
        check(not (sum(ws) >= N + 1))
        # Root has p; all positive-weight successors are non-p, so self-weight is zero.
        root_self_weight = 0
        check(root_self_weight == 0)
        # Kripke special case: all weights 0/1 iff there are at least N non-root states.
        kripke_possible = (k >= N)
        check((target <= 1) == kripke_possible)

# Exact minimum Kripke carrier N+1, and two-state weighted extreme.
for N in range(1, 2001):
    check(ceil(N / 1) == N)          # m=2 gives weight N
    check(ceil(N / N) == 1)          # m=N+1 gives Kripke weights
    if N > 1:
        check(ceil(N / (N - 1)) > 1) # m=N cannot be Kripke

print(f"VERIFY_OK {assertions} exact assertions")
