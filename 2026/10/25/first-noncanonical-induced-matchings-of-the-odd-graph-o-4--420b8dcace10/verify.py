#!/usr/bin/env python3
"""Exhaustive finite certificate for induced matchings of KG(7,3).

Run: python3 verify.py . Requires only the Python 3 standard library.
The two independent-search implementations use different adjacency tests.
"""
from collections import Counter
from itertools import combinations, permutations

GROUND = range(7)
TRIPLES = tuple(combinations(GROUND, 3))
VERTEX = tuple(sum(1 << x for x in triple) for triple in TRIPLES)
EDGES = tuple((a, b) for a in range(len(VERTEX))
              for b in range(a + 1, len(VERTEX))
              if VERTEX[a] & VERTEX[b] == 0)
LABELS = tuple(next(x for x in GROUND if not ((VERTEX[a] | VERTEX[b]) & (1 << x)))
               for a, b in EDGES)
assert len(VERTEX) == 35 and len(EDGES) == 70
assert Counter(LABELS) == Counter({x: 10 for x in GROUND})

# Criterion A: for distinct graph edges, every pair of endpoints intersects.
def compatible(a, b):
    if a == b:
        return False
    i, j = EDGES[a]
    k, l = EDGES[b]
    return all(VERTEX[x] & VERTEX[y] for x in (i, j) for y in (k, l))

COMPATIBLE = tuple(sum(1 << j for j in range(70) if compatible(i, j))
                   for i in range(70))
assert all((bool(COMPATIBLE[i] & (1 << j)) ==
            bool(COMPATIBLE[j] & (1 << i))) for i in range(70) for j in range(70))


def sets_bitset(size, fixed=None):
    """Independent sets of given size in the edge-conflict graph."""
    if fixed is None:
        starts = range(70)
    else:
        starts = (fixed,)

    def continue_search(selected, candidates):
        if len(selected) == size:
            yield selected
            return
        if candidates.bit_count() < size - len(selected):
            return
        while candidates:
            lowest = candidates & -candidates
            nxt = lowest.bit_length() - 1
            candidates -= lowest
            if candidates.bit_count() + 1 < size - len(selected):
                return
            yield from continue_search(selected + (nxt,), candidates & COMPATIBLE[nxt])

    for start in starts:
        suffix = COMPATIBLE[start] & ~((1 << (start + 1)) - 1)
        yield from continue_search((start,), suffix)


# Criterion B: direct graph adjacency via set disjointness, no compatibility table.
SET_VERTICES = tuple(frozenset(t) for t in TRIPLES)

def direct_compatible(e, f):
    aa, ab = EDGES[e]
    ba, bb = EDGES[f]
    for u in (aa, ab):
        for v in (ba, bb):
            if not SET_VERTICES[u].intersection(SET_VERTICES[v]):
                return False
    return True


def anchored_direct(size):
    def expand(chosen, next_index):
        if len(chosen) == size:
            yield chosen
            return
        if 70 - next_index < size - len(chosen):
            return
        for e in range(next_index, 70):
            if all(direct_compatible(e, prev) for prev in chosen):
                yield from expand(chosen + (e,), e + 1)
    yield from expand((0,), 1)


def profile(selection):
    return tuple(sorted(Counter(LABELS[i] for i in selection).values(), reverse=True))


def main():
    for size, expected in ((7, 642), (8, 36)):
        a = set(sets_bitset(size, fixed=0))
        b = set(anchored_direct(size))
        assert a == b, (size, len(a), len(b))
        assert len(a) == expected, (size, len(a))
        print('anchored', size, len(a), sorted(Counter(profile(q) for q in a).items()))

    all7 = set(sets_bitset(7))
    assert len(all7) == 6420
    expected = {(7,): 840, (6, 1): 420, (4, 2, 1): 2520,
                (4, 1, 1, 1): 1680, (2, 2, 2, 1): 840,
                (1, 1, 1, 1, 1, 1, 1): 120}
    assert Counter(profile(q) for q in all7) == expected

    all8 = set(sets_bitset(8))
    assert len(all8) == 315
    assert Counter(profile(q) for q in all8) == {(8,): 315}
    # Each 8-set is contained in one canonical ten-edge class.
    for q in all8:
        assert len(set(LABELS[e] for e in q)) == 1

    idx = {s: i for i, s in enumerate(VERTEX)}
    edgeidx = {e: i for i, e in enumerate(EDGES)}
    permutations_on_edges = []
    for sigma in permutations(GROUND):
        image_vertex = tuple(idx[sum(1 << sigma[x] for x in GROUND if b & (1 << x))]
                             for b in VERTEX)
        image_edge = tuple(edgeidx[tuple(sorted((image_vertex[a], image_vertex[b])))]
                           for a, b in EDGES)
        permutations_on_edges.append(image_edge)
    assert len(permutations_on_edges) == 5040
    assert {mp[0] for mp in permutations_on_edges} == set(range(70))

    remaining = all7.copy()
    orbit_types = Counter()
    while remaining:
        representative = min(remaining)
        orbit = {tuple(sorted(p[e] for e in representative)) for p in permutations_on_edges}
        assert orbit <= all7
        assert len(orbit) in (120, 420, 840, 1680, 2520)
        orbit_types[(profile(representative), len(orbit))] += 1
        remaining.difference_update(orbit)

    expected_orbits = Counter({((7,), 420): 2, ((6, 1), 420): 1,
              ((4, 2, 1), 2520): 1, ((4, 1, 1, 1), 1680): 1,
              ((2, 2, 2, 1), 840): 1,
              ((1, 1, 1, 1, 1, 1, 1), 120): 1})
    assert orbit_types == expected_orbits
    assert sum(len_orbit * mult for (p, len_orbit), mult in orbit_types.items()) == 6420
    assert sum(cnt for p, cnt in expected.items() if len(p) > 1) == 5580

    print('total size 7', len(all7), 'mixed size 7', 5580)
    print('total size 8', len(all8), 'mixed size 8', 0)
    print('orbits', sorted(orbit_types.items()))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
