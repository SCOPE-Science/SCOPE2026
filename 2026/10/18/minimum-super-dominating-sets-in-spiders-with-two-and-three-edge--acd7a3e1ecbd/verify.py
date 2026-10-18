"""Independent exhaustive and constructive checks for super domination on short-arm spiders.

Run with Python 3.9 or later: python verify.py
Vertex 0 is the hub. Each arm is indexed outward from its hub.
"""
from itertools import product
from collections import Counter


def graph(a, b):
    arms = []
    neighbors = [0]
    for length in [2] * a + [3] * b:
        last = 0
        arm = []
        for unused in range(length):
            u = len(neighbors)
            neighbors.append(0)
            neighbors[last] |= 1 << u
            neighbors[u] |= 1 << last
            arm.append(u)
            last = u
        arms.append(arm)
    return neighbors, arms


def qualifies(neighbors, selected):
    n = len(neighbors)
    white = ((1 << n) - 1) ^ selected
    witness_targets = 0
    for v, adj in enumerate(neighbors):
        if (selected >> v) & 1:
            outside = adj & white
            if outside and not outside & (outside - 1):
                witness_targets |= outside
    return witness_targets == white


def predicted(a, b):
    """Return the exact list of predicted minimum-set vertex masks."""
    neighbors, arms = graph(a, b)
    short = arms[:a]
    long = arms[a:]
    result = set()
    def as_mask(center_black, short_patterns, long_patterns):
        x = int(center_black)
        for arm, chars in zip(short + long, short_patterns + long_patterns):
            for v, char in zip(arm, chars):
                if char == 'B':
                    x |= 1 << v
        return x
    if b == 0:
        for p in product(('BW','WB'), repeat=a):
            result.add(as_mask(True, p, ()))
        for j in range(a):
            p = ['WB'] * a
            p[j] = 'BB'
            result.add(as_mask(False, tuple(p), ()))
    else:
        for p in product(('BBW', 'BWB', 'WBB'), repeat=b):
            if 'BBW' in p:
                result.add(as_mask(False, ('WB',) * a, p))
        for j in range(b):
            for p in product(('BBW', 'BWB'), repeat=b-1):
                states = list(p)
                states.insert(j, 'WWB')
                result.add(as_mask(True, ('BW',) * a, tuple(states)))
    return result


def expected_size(a, b):
    return a + 1 if b == 0 else a + 2 * b


def expected_count(a, b):
    return 2 ** a + a if b == 0 else 3 ** b - 2 ** b + b * 2 ** (b - 1)


def exhaustive(a, b):
    neigh, _ = graph(a, b)
    n = len(neigh)
    found = set()
    best = n + 1
    # Graph-based enumeration: no use of arm classification.
    for s in range(1 << n):
        k = s.bit_count()
        if k > best:
            continue
        if qualifies(neigh, s):
            if k < best:
                best = k
                found.clear()
            found.add(s)
    return best, found


def run():
    tested = 0
    exhaustive_subsets = 0
    for a in range(9):
        for b in range(7):
            if a + b < 3:
                continue
            neigh, arms = graph(a, b)
            if len(neigh) > 17:
                continue
            target = predicted(a, b)
            assert len(target) == expected_count(a, b), (a, b, 'formula')
            assert all(x.bit_count() == expected_size(a, b) for x in target)
            assert all(qualifies(neigh, x) for x in target)
            best, found = exhaustive(a, b)
            assert best == expected_size(a, b), (a, b, best)
            assert found == target, (a, b, len(found), len(target), found ^ target)
            tested += 1
            exhaustive_subsets += 1 << len(neigh)
    # Large profiles check each constructive configuration by graph neighborhoods.
    stress_sets = 0
    profiles = 0
    for a, b in [(0, k) for k in range(3, 10)] + [(k, 1) for k in range(2, 30)] + [(k, 2) for k in range(1, 30)] + [(5, k) for k in range(3, 10)] + [(k, 0) for k in range(3, 10)]:
        neigh, _ = graph(a, b)
        expected = expected_count(a, b)
        target = predicted(a, b)
        assert len(target) == expected, (a, b)
        for x in target:
            assert x.bit_count() == expected_size(a, b)
            assert qualifies(neigh, x)
        stress_sets += len(target)
        profiles += 1
    print(f'PASS: exhaustive classification in {tested} graph profiles ({exhaustive_subsets} subsets searched).')
    print(f'PASS: {stress_sets} explicit minimum configurations in {profiles} additional profiles.')
    print('PASS: both stated formulas and center-color subfamily classification.')

if __name__ == '__main__':
    run()
