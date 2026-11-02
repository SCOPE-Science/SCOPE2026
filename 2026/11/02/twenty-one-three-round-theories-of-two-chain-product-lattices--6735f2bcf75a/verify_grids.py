#!/usr/bin/env python3
"""Exact rank-three first-order types of coordinatewise grid posets.

Uses the Hintikka recursion for tuples, not sampling or isomorphism heuristics.
Run: python3 verify_grids.py
"""
from itertools import product
from collections import defaultdict


def canonical_type(m, n):
    if m < 1 or n < 1:
        raise ValueError('positive side lengths required')
    points = list(product(range(m), range(n)))
    N = len(points)
    le = [[int(x[0] <= y[0] and x[1] <= y[1]) for y in points]
          for x in points]
    # Each quantifier-free triple has six off-diagonal relational bits.
    # Reflexive diagonal atoms are automatically true, and x=y iff both
    # x<=y and y<=x, so equality is encoded exactly by these six bits.
    pair_type = [[None] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            xy = le[x][y] | (le[y][x] << 1)
            # All atomic completions by a third variable z.
            pair_type[x][y] = frozenset(
                xy | (le[x][z] << 2) | (le[z][x] << 3)
                   | (le[y][z] << 4) | (le[z][y] << 5)
                for z in range(N))
    # For a fixed x: all possible two-element pointed one-round types.
    point_type = [frozenset(pair_type[x][y] for y in range(N))
                  for x in range(N)]
    # Closed rank-three type: all one-element pointed two-round types.
    return frozenset(point_type)


def representative(a, b):
    a, b = sorted((a, b))
    if a == 1:
        return 1, min(b, 7)
    if a in (2, 3, 4):
        return a, min(b, 6)
    if a == b == 5:
        return 5, 5
    return 5, 6


def run():
    groups = defaultdict(list)
    for a in range(1, 8):
        for b in range(a, 8):
            groups[canonical_type(a, b)].append((a, b))
    assert len(groups) == 21, len(groups)
    keys_by_rep = {}
    for sig, members in groups.items():
        reps = {representative(*v) for v in members}
        assert len(reps) == 1, (members, reps)
        rep, = reps
        assert rep in members, (rep, members)
        assert rep not in keys_by_rep, rep
        keys_by_rep[rep] = sig
    assert len(keys_by_rep) == 21
    # Explicitly ensure all different canonical representatives are distinct.
    assert len(set(keys_by_rep.values())) == 21
    # All pairs at the seven-coordinate cutoff are covered: 28 instances.
    assert sum(map(len, groups.values())) == 28
    assert representative(5, 6) == (5, 6)
    assert canonical_type(5, 6) == canonical_type(6, 6)
    assert canonical_type(6, 6) == canonical_type(7, 7)
    assert canonical_type(1, 6) != canonical_type(1, 7)
    assert canonical_type(4, 5) != canonical_type(4, 6)
    assert canonical_type(5, 5) != canonical_type(5, 6)
    print('CHECK PASS: 28 finite rectangles, 21 rank-three theories')
    for rep in sorted(keys_by_rep):
        members = sorted(groups[keys_by_rep[rep]])
        print(f'{rep}: {members}')
    # Verify additional unbounded-parameter representatives directly.
    for a, b, c, d in ((5, 6, 5, 12), (5, 6, 12, 12),
                       (2, 6, 2, 12), (1, 7, 1, 12)):
        assert canonical_type(a, b) == canonical_type(c, d)
    print('CHECK PASS: additional direct checks to side length 12')
    print('CHECK PASS: sharp universal representative (5, 6), 30 vertices')

if __name__ == '__main__':
    run()
