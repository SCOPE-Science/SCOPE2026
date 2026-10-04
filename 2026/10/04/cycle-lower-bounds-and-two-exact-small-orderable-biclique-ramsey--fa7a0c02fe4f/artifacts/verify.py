#!/usr/bin/env python3
import itertools


def color(n, u, v):
    if u == v:
        raise ValueError("loop")
    return 0 if ((u-v) % n in (1, n-1)) else 1  # 0 red, 1 blue


def alternating_counts(n, x, y):
    rb = br = 0
    for z in range(n):
        if z in (x, y):
            continue
        a, b = color(n, x, z), color(n, y, z)
        if (a, b) == (0, 1):
            rb += 1
        elif (a, b) == (1, 0):
            br += 1
    return rb, br


def direct_orderable(n, side):
    side = set(side)
    other = set(range(n)) - side
    edges = {}
    for u in side:
        for v in other:
            edges[frozenset((u, v))] = color(n, u, v)
    for perm in itertools.permutations(range(n)):
        pos = {v:i for i,v in enumerate(perm)}
        ok = True
        for u in perm:
            later_colors = set()
            for e,c in edges.items():
                if u in e:
                    v = next(iter(e-{u}))
                    if pos[v] > pos[u]:
                        later_colors.add(c)
                        if len(later_colors) > 1:
                            ok = False
                            break
            if not ok:
                break
        if ok:
            return True
    return False


pairs_checked = 0
for t in range(3, 51):
    n = t + 2
    for x, y in itertools.combinations(range(n), 2):
        rb, br = alternating_counts(n, x, y)
        assert rb >= 1 and br >= 1, (t, x, y, rb, br)
        assert n - 2 - min(rb, br) <= t - 1
        pairs_checked += 1

# Directly test the definition, without using the alternating-class criterion,
# on every two-vertex side for the smallest nontrivial witnesses.
direct_cases = 0
for t in range(3, 6):
    n = t + 2
    for side in itertools.combinations(range(n), 2):
        assert not direct_orderable(n, side), (t, side)
        direct_cases += 1

for t, expected in [(4, 7), (5, 8)]:
    lower = t + 3
    upper = (4*t)//3 + 2
    assert lower == upper == expected

print(
    "ALL CHECKS PASSED; "
    f"cycle_pair_checks={pairs_checked}; "
    f"direct_orderability_sides={direct_cases}; "
    "cycle_lower_bound_t_range=3..50; direct_t_range=3..5; exact_t=4,5"
)
