#!/usr/bin/env python3
"""Exact simplicial persistence and relative-collapse checks for a ten-vertex graph.

Only Python's standard library is required. Vertex i denotes the i-th two-subset
in lexicographic order; distinct vertices are joined when their labels are disjoint.
"""
import collections
import itertools
import json
from pathlib import Path

VERTICES = tuple(itertools.combinations(range(5), 2))
N = len(VERTICES)
NEIGHBORS = tuple(sum(1 << j for j, b in enumerate(VERTICES)
                      if i != j and set(a).isdisjoint(b))
                  for i, a in enumerate(VERTICES))

EXPECTED_BARS = {
    (2, 1, 2): 4,
    (3, 2, 5): 1,
    (3, 4, 5): 10,
    (4, 5, 6): 61,
    (5, 6, 7): 74,
    (6, 7, 8): 36,
    (7, 8, 9): 9,
    (8, 9, 10): 1,
}
EXPECTED_BETTI = {
    1: {2: 4}, 2: {3: 1}, 3: {3: 1}, 4: {3: 11},
    5: {4: 61}, 6: {5: 74}, 7: {6: 36}, 8: {7: 9},
    9: {8: 1}, 10: {},
}

def component_bound(mask):
    remaining = mask
    maximum = 0
    while remaining:
        frontier = remaining & -remaining
        component = 0
        while frontier:
            component |= frontier
            remaining &= ~frontier
            neighbors = 0
            t = frontier
            while t:
                bit = t & -t
                t ^= bit
                neighbors |= NEIGHBORS[bit.bit_length() - 1]
            frontier = neighbors & remaining
        maximum = max(maximum, component.bit_count())
    return maximum

def component_bound_independent(mask):
    elements = [i for i in range(N) if mask & (1 << i)]
    unused = set(elements)
    maximum = 0
    while unused:
        root = min(unused)
        unused.remove(root)
        discovered = {root}
        frontier = [root]
        while frontier:
            i = frontier.pop()
            for j in sorted(unused):
                if set(VERTICES[i]).isdisjoint(VERTICES[j]):
                    unused.remove(j)
                    discovered.add(j)
                    frontier.append(j)
        maximum = max(maximum, len(discovered))
    return maximum

def all_faces_by_level():
    degrees = {m: component_bound(m) for m in range(1, 1 << N)}
    for mask, val in degrees.items():
        assert val == component_bound_independent(mask), (mask, val)
    return degrees

def persistence(degrees):
    ordered = sorted(degrees, key=lambda m: (degrees[m], m.bit_count(), m))
    location = {m: i for i, m in enumerate(ordered)}
    reduced = {}
    pairs = []
    birth_columns = []
    for i, mask in enumerate(ordered):
        boundary = 0
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            remaining ^= bit
            if mask ^ bit:
                boundary ^= 1 << location[mask ^ bit]
        while boundary:
            pivot = boundary.bit_length() - 1
            if pivot in reduced:
                boundary ^= reduced[pivot]
            else:
                reduced[pivot] = boundary
                pairs.append((pivot, i))
                break
        if boundary == 0:
            birth_columns.append(i)
    matched_births = {b for b, _ in pairs}
    bars = collections.Counter()
    for b, d in pairs:
        t0, t1 = degrees[ordered[b]], degrees[ordered[d]]
        if t0 != t1:
            bars[(ordered[b].bit_count() - 1, t0, t1)] += 1
    inf = [(ordered[b].bit_count() - 1, degrees[ordered[b]])
           for b in birth_columns if b not in matched_births]
    assert inf == [(0, 1)], inf
    assert dict(bars) == EXPECTED_BARS, bars
    return bars, len(pairs), len(ordered)

def rank_gf2(columns):
    pivots = {}
    for vector in columns:
        while vector:
            p = vector.bit_length() - 1
            if p in pivots:
                vector ^= pivots[p]
            else:
                pivots[p] = vector
                break
    return len(pivots)

def boundary_vectors(high, low):
    indices = {mask: i for i, mask in enumerate(low)}
    answer = []
    for mask in high:
        boundary = 0
        t = mask
        while t:
            bit = t & -t
            t ^= bit
            boundary ^= 1 << indices[mask ^ bit]
        answer.append(boundary)
    return answer

def cycle_basis(high, low):
    indices = {mask: i for i, mask in enumerate(low)}
    pivots = {}
    cycles = []
    for i, mask in enumerate(high):
        vec = 0
        t = mask
        while t:
            bit = t & -t
            t ^= bit
            vec ^= 1 << indices[mask ^ bit]
        coordinates = 1 << i
        while vec:
            p = vec.bit_length() - 1
            if p not in pivots:
                pivots[p] = (vec, coordinates)
                break
            previous_vec, previous_coordinates = pivots[p]
            vec ^= previous_vec
            coordinates ^= previous_coordinates
        if not vec:
            cycles.append(coordinates)
    return cycles

def per_level_homology(degrees):
    complexes = {}
    for r in range(1, 11):
        levels = collections.defaultdict(list)
        for m, threshold in degrees.items():
            if threshold <= r:
                levels[m.bit_count() - 1].append(m)
        for faces in levels.values():
            faces.sort()
        ranks = {}
        for k in sorted(levels):
            if k >= 1:
                ranks[k] = rank_gf2(boundary_vectors(levels[k], levels[k - 1]))
        betti = {k: len(levels[k]) - ranks.get(k, 0) - ranks.get(k+1, 0)
                 for k in levels}
        betti[0] -= 1  # connected, one reduced degree-zero generator removed
        betti = {k: v for k, v in betti.items() if v}
        assert betti == EXPECTED_BETTI[r], (r, betti)
        complexes[r] = levels
    return complexes

def inclusion_check(complexes, bars):
    pairs_checked = 0
    for a in range(1, 11):
        for b in range(a, 11):
            source, target = complexes[a], complexes[b]
            for k in range(1, 9):
                if k not in source:
                    continue
                cycle_vectors = cycle_basis(source[k], source[k - 1])
                index = {m: i for i, m in enumerate(target[k])}
                embedded = []
                for vec in cycle_vectors:
                    res = 0
                    while vec:
                        bit = vec & -vec
                        vec ^= bit
                        res ^= 1 << index[source[k][bit.bit_length() - 1]]
                    embedded.append(res)
                target_boundaries = boundary_vectors(target[k+1], target[k]) if k+1 in target else []
                observed = rank_gf2(target_boundaries + embedded) - rank_gf2(target_boundaries)
                predicted = sum(v for (degree, start, stop), v in bars.items()
                                if degree == k and start <= a and b < stop)
                assert observed == predicted, (a, b, k, observed, predicted)
                pairs_checked += 1
    return pairs_checked

def check_collapse(degrees):
    certificate = json.loads(Path(__file__).with_name('collapse_pairs.json').read_text())
    core = {m for m, t in degrees.items() if t <= 2}
    remaining = {m for m, t in degrees.items() if t <= 3}
    assert len(remaining) == 380 and len(core) == 260
    assert len(certificate) == 60
    for low, high in certificate:
        assert low in remaining - core and high in remaining - core
        assert high.bit_count() == low.bit_count() + 1
        assert low & high == low
        cofaces = [m for m in remaining if low != m and (m & low) == low]
        assert cofaces == [high], (low, high, cofaces)
        remaining.remove(low)
        remaining.remove(high)
    assert remaining == core
    return len(certificate)

def main():
    degrees = all_faces_by_level()
    bars, pairs, numfaces = persistence(degrees)
    complexes = per_level_homology(degrees)
    inclusions = inclusion_check(complexes, bars)
    collapses = check_collapse(degrees)
    print('VERTICES', N, 'EDGES', sum(m.bit_count() for m in NEIGHBORS)//2)
    print('NONEMPTY_FACES', numfaces, 'BOUNDARY_PIVOT_PAIRS', pairs)
    print('FACE_COUNTS', [(r, sum(t <= r for t in degrees.values())) for r in range(1, 11)])
    for k in sorted(bars):print('BAR', *k, bars[k])
    print('HOMOLOGY_LEVELS', len(complexes), 'INCLUSION_RANK_CHECKS', inclusions)
    print('ELEMENTARY_RELATIVE_COLLAPSES', collapses)
    print('VERIFY_OK')
if __name__ == '__main__':main()
