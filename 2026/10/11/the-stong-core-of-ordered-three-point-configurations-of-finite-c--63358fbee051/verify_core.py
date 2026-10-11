#!/usr/bin/env python3
"""Standalone exact finite-poset verification for the triple-configuration crown-core theorem.

Run: python3 verify_core.py
Uses only the Python standard library. Finite tests supplement, not replace, the proof.
"""
from collections import Counter, deque
from itertools import permutations, product


def le_point(n, x, y):
    return x == y or (x < n <= y and ((y - n - x) % n) in (0, 1))


def below_point(n, x):
    return (x,) if x < n else (x, (x-n) % n, (x-n-1) % n)


def above_point(n, x):
    return (x, n+x, n+(x+1) % n) if x < n else (x,)


def strict_neighbors(n, t, ascending, live):
    options = above_point if ascending else below_point
    result = set()
    for u in product(*(options(n, x) for x in t)):
        if u != t and len(set(u)) == 3 and u in live:
            assert all(le_point(n, x, y) for x, y in zip(t, u)) if ascending else all(le_point(n, y, x) for x, y in zip(t, u))
            result.add(u)
    return result


def is_incomparable(n, x, y):
    return not le_point(n, x, y) and not le_point(n, y, x)


def class_name(n, t):
    lower = [x for x in t if x < n]
    upper = [y for y in t if y >= n]
    if len(lower) not in (1, 2):
        return 'A'
    e = sum(le_point(n, x, y) for x in lower for y in upper)
    if e == 0:
        return 'A'
    assert e in (1, 2)
    return ('L' if len(lower) == 2 else 'U') + str(e)


def check_beat(n, t, ascending, live):
    neighbors = strict_neighbors(n, t, ascending, live)
    if not neighbors:
        return False
    if ascending:
        return any(all(all(le_point(n, a, b) for a, b in zip(y, z)) for y in neighbors) for z in neighbors)
    return any(all(all(le_point(n, a, b) for a, b in zip(z, y)) for y in neighbors) for z in neighbors)


def verify(n):
    total = set(permutations(range(2*n), 3))
    cls = {t:class_name(n, t) for t in total}
    assert len(total) == (2*n)*(2*n-1)*(2*n-2)
    live = set(total)
    if n == 2:
        assert all(not check_beat(n, t, ascending, live) for t in live for ascending in (True, False))
        assert len(live) == 24
        adj = {t: strict_neighbors(n, t, True, live) | strict_neighbors(n, t, False, live) for t in live}
        assert all(len(s) == 2 for s in adj.values())
        remaining = set(live)
        component_sizes = []
        while remaining:
            start = next(iter(remaining))
            q = deque([start]); reached = {start}
            while q:
                for v in adj[q.popleft()]:
                    if v not in reached:
                        reached.add(v); q.append(v)
            remaining.difference_update(reached)
            component_sizes.append(len(reached))
        assert sorted(component_sizes) == [12, 12]
        print('n=2: 24 points; two 12-cycle components; no beat points')
        return
    stage_counts = Counter(cls.values())
    assert stage_counts['L1'] == stage_counts['U1'] == 12*n*(n-2)
    assert stage_counts['L2'] == stage_counts['U2'] == 6*n
    expected_core = (2*n)*(2*n-4)*(2*n-5)
    assert stage_counts['A'] == expected_core
    sequence = [('L1', False), ('U1', True), ('L2', True), ('U2', False)]
    for typ, ascending in sequence:
        removed = sorted(t for t in live if cls[t] == typ)
        for t in removed:
            # Stronger than beat-point property: exactly one surviving strict
            # neighbor in the indicated direction, throughout the sequence.
            nbr = strict_neighbors(n, t, ascending, live)
            assert len(nbr) == 1, (n, typ, t, nbr)
            assert check_beat(n, t, ascending, live)
            live.remove(t)
    core = {t for t in total if all(is_incomparable(n, t[i], t[j]) for i in range(3) for j in range(i+1, 3))}
    assert live == core
    assert len(core) == expected_core
    assert len(total) - len(core) == 12*n*(2*n-3)
    assert all(not check_beat(n, t, ascending, core) for t in core for ascending in (True, False))
    print(f'n={n}: total={len(total)}, core={len(core)}, removed={len(total)-len(core)}, '
          f'classes=[L1:{stage_counts["L1"]},U1:{stage_counts["U1"]},'
          f'L2:{stage_counts["L2"]},U2:{stage_counts["U2"]}]; no core beats')


if __name__ == '__main__':
    for n in range(2, 13):
        verify(n)
    print('VERIFY_OK')
