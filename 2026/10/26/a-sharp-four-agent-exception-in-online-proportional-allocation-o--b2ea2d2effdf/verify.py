#!/usr/bin/env python3
"""Exact check of an online unit-job proportionality boundary.

Run: python3 verify.py
No third-party modules are required.
"""
from collections import deque
from functools import lru_cache
from itertools import combinations


def eligible_sets(n):
    return tuple(s for k in range(2, n + 1) for s in combinations(range(n), k))


def step(d, eligible, recipient, scale):
    assert recipient in eligible and scale % len(eligible) == 0
    t = list(d)
    q = scale // len(eligible)
    for i in eligible:
        t[i] -= q
    t[recipient] += scale
    assert sum(t) == sum(d)
    return tuple(t)


def greedy_responses(d, eligible, scale):
    m = min(d[i] for i in eligible)
    return {step(d, eligible, i, scale)
            for i in eligible if d[i] == m}


# Exact invariant for three machines. The sorted state records six times
# (allocated unit jobs minus eligibility-proportional fractional jobs).
THREE_INVARIANT = {
    (-5, 1, 4), (-4, -1, 5), (-4, 2, 2), (-3, 0, 3),
    (-2, -2, 4), (-2, 1, 1), (-1, -1, 2), (0, 0, 0),
}
assert (0, 0, 0) in THREE_INVARIANT
assert all(sum(s) == 0 and max(s) <= 5 for s in THREE_INVARIANT)
for s in THREE_INVARIANT:
    for eligible in eligible_sets(3):
        for t in greedy_responses(s, eligible, 6):
            assert tuple(sorted(t)) in THREE_INVARIANT, (s, eligible, t)
print('three-machine invariant: 8 sorted states, every transition checked')

# Four-machine four-item safety: enumerate ALL adversarial eligible subsets,
# and ALL minimum-discrepancy tie-breaking outcomes, at every prefix.
levels = [{(0, 0, 0, 0)}]
for depth in range(1, 5):
    nxt = set()
    for d in levels[-1]:
        for eligible in eligible_sets(4):
            for t in greedy_responses(d, eligible, 12):
                assert max(t) <= 12, (depth, d, eligible, t)
                nxt.add(t)
    levels.append(nxt)
expected_counts = (1, 28, 187, 617, 1405)
actual_counts = tuple(len(x) for x in levels)
assert actual_counts == expected_counts, actual_counts
print('four-machine safe prefix counts:', actual_counts)

# Five-job adaptive adversary, in increasing sorted discrepancy order.
# Every possible response is explicitly included, including early failure.
def canonical_step(d, eligible, recipient):
    return tuple(sorted(step(d, eligible, recipient, 12)))

initial = (0, 0, 0, 0)
a = {canonical_step(initial, (0, 1, 2, 3), r) for r in range(4)}
assert a == {(-3, -3, -3, 9)}
b = {canonical_step(s, (0, 1, 2), r)
     for s in a for r in (0, 1, 2)}
assert b == {(-7, -7, 5, 9)}
c = {canonical_step(s, (0, 1, 2), r)
     for s in b for r in (0, 1, 2)}
assert c == {(-11, -11, 9, 13), (-11, 1, 1, 9)}
assert max((-11, -11, 9, 13)) > 12
c_survive = {s for s in c if max(s) <= 12}
d = {canonical_step(s, (1, 2), r) for s in c_survive for r in (1, 2)}
assert d == {(-11, -5, 7, 9)}
e = {canonical_step(s, (2, 3), r) for s in d for r in (2, 3)}
assert e == {(-11, -5, 1, 15), (-11, -5, 3, 13)}
assert all(max(s) > 12 for s in e)
print('four-machine adversary: all outcome branches lose by job five')

# Independent exact minimax calculation at four machines, five jobs.
subsets = eligible_sets(4)
@lru_cache(None)
def force(d, rounds_left):
    if max(d) > 12:
        return True
    if rounds_left == 0:
        return False
    return any(all(force(tuple(sorted(step(d, S, i, 12))), rounds_left - 1)
                   for i in S) for S in subsets)
assert [force((0, 0, 0, 0), h) for h in range(6)] == [
    False, False, False, False, False, True]
print('independent minimax: first forced failure occurs at five jobs')

# For n >= 5, two all-eligible jobs followed by a pair job: if first
# two jobs are assigned together, failure occurs already at job two.
# Otherwise each of their two recipients has fractional share 2/n+1/2 < 1.
for n in range(5, 100):
    assert 4 + n < 2 * n  # 2/n + 1/2 < 1, after multiplying by 2n
print('at least five machines: finite inequality spot checks passed; the all-n proof is algebraic')
print('ALL EXACT CHECKS PASSED')
