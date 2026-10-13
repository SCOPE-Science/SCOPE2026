#!/usr/bin/env python3
"""Independent finite verification of a six-cycle strict pooling construction.

Uses only the Python standard library. Run: python3 verify.py
"""
from itertools import combinations, permutations
from math import comb


def even_cycles(points):
    """The six A5-orbit Hamilton cycles on an ordered five-point set."""
    assert len(points) == 5
    cycles = set()
    for p in permutations(range(5)):
        if sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) % 2:
            continue
        cycle = frozenset(frozenset((points[p[i]], points[p[(i + 1) % 5]])) for i in range(5))
        cycles.add(cycle)
    assert len(cycles) == 6
    return sorted(cycles, key=lambda c: tuple(sorted(tuple(sorted(e)) for e in c)))


def petersen_check():
    edges = tuple(map(frozenset, combinations(range(5), 2)))
    cycles = even_cycles(tuple(range(5)))
    matches = [(a, b) for a, b in combinations(edges, 2) if a.isdisjoint(b)]
    assert len(matches) == 15
    count = 0
    for a, b in matches:
        for w in edges:
            if w == a or w == b:
                continue
            hits = [c for c in cycles if w in c and a not in c and b not in c]
            assert hits, (a, b, w)
            count += 1
    assert count == 120
    # Every matching is an incomparable size-two candidate set. Under k tests,
    # their OR-response patterns form an antichain, so 5 tests would allow
    # at most binomial(5,2)=10 patterns, fewer than the 15 matchings.
    assert comb(5, 2) < len(matches) <= comb(6, 3)
    return count


def make_design(m):
    triples = tuple(combinations(range(m), 3))
    items = tuple(('triple', t) for t in triples) + tuple(('loop', k) for k in range(6))
    loops = frozenset(i for i, (kind, _) in enumerate(items) if kind == 'loop')
    first = tuple(frozenset(i for i, (kind, t) in enumerate(items)
                            if kind == 'triple' and j in t) for j in range(m))
    masks = tuple(sum(1 << j for j in t) if kind == 'triple' else 0 for kind, t in items)
    return items, loops, first, masks


def second_stage(y, m, items, loops):
    ys = tuple(j for j in range(m) if y >> j & 1)
    if len(ys) in (0, 3):
        return tuple(frozenset((i,)) for i in sorted(loops))
    if len(ys) == 4:
        return tuple(frozenset((i,)) | loops for i, (kind, t) in enumerate(items)
                     if kind == 'triple' and set(t) <= set(ys))
    if len(ys) == 5:
        cycles = even_cycles(ys)
        return tuple(frozenset(i for i, (kind, t) in enumerate(items)
                               if kind == 'triple' and set(t) <= set(ys)
                               and frozenset(set(ys) - set(t)) in cycle) | loops
                     for cycle in cycles)
    if len(ys) == 6:
        triples = [i for i, (kind, t) in enumerate(items)
                   if kind == 'triple' and set(t) <= set(ys)]
        pairs = tuple((a, b) for a, b in combinations(triples, 2)
                      if set(items[a][1]).isdisjoint(items[b][1]))
        patterns = tuple(combinations(range(5), 2))
        assert len(pairs) == len(patterns) == 10
        return tuple(frozenset(i for pairidx, pair in enumerate(pairs)
                               if j in patterns[pairidx] for i in pair) | loops
                     for j in range(5))
    return ()


def signature(P, pools):
    return sum(1 << j for j, Q in enumerate(pools) if any(i in Q for i in P))


def exhaustive(m, max_weight=None):
    items, loops, first, masks = make_design(m)
    n = len(items)
    if max_weight is None:
        assert n <= 16
    valid = {}
    for P in [()] + list(combinations(range(n), 1)) + list(combinations(range(n), 2)):
        y = 0
        for i in P:
            y |= masks[i]
        pools = second_stage(y, m, items, loops)
        b = signature(P, pools)
        key = (y, b)
        assert key not in valid, (P, valid.get(key), key)
        valid[key] = P
    count = 0
    if max_weight is None:
        sample = (tuple(i for i in range(n) if mask >> i & 1) for mask in range(1 << n))
    else:
        sample = (P for k in range(max_weight + 1) for P in combinations(range(n), k))
    for P in sample:
        y = 0
        for i in P:
            y |= masks[i]
        b = signature(P, second_stage(y, m, items, loops))
        prediction = valid.get((y, b))
        assert (prediction == P) if len(P) <= 2 else (prediction is None), (m, P, prediction, y, b)
        count += 1
    return n, count


if __name__ == '__main__':
    print('PETERSEN_COVER_PAIRS', petersen_check())
    n, cnt = exhaustive(5)
    print('EXHAUSTIVE', n, cnt)
    n, cnt = exhaustive(6, max_weight=4)
    print('LOW_WEIGHT', n, cnt)
    assert n == 26
    print('VERIFY_OK petersen_min=6 two_stage_m5=65536 two_stage_m6_weight_le4')
