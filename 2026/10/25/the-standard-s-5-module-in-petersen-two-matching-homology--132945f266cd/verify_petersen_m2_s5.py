#!/usr/bin/env python3
"""Exact finite verification of the S5-character of Petersen two-matching homology.

Pure Python 3, standard library only. Every checked face is rebuilt from the
Kneser representation rather than supplied by an external certificate.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

FIVE = tuple(range(5))
VERTICES = tuple(combinations(FIVE, 2))
VINDEX = {v: i for i, v in enumerate(VERTICES)}
EDGES = tuple((i, j) for i, j in combinations(range(10), 2)
              if set(VERTICES[i]).isdisjoint(VERTICES[j]))
EINDEX = {e: i for i, e in enumerate(EDGES)}
assert len(VERTICES) == 10 and len(EDGES) == 15


def admissible(mask):
    degree = [0] * 10
    for e, (i, j) in enumerate(EDGES):
        if (mask >> e) & 1:
            degree[i] += 1
            degree[j] += 1
            if degree[i] > 2 or degree[j] > 2:
                return False
    return True


FACES = tuple(mask for mask in range(1 << 15) if admissible(mask))
FACED = frozenset(FACES)
EXPECTED_FACE_VECTOR = (15, 105, 445, 1245, 2358, 2985, 2400, 1095, 215, 6)
face_vector = Counter(mask.bit_count() - 1 for mask in FACES if mask)
assert len(FACES) == 10870
assert tuple(face_vector[i] for i in range(10)) == EXPECTED_FACE_VECTOR


def verify_morse():
    active = set(FACES) - {0}
    mate = {}
    for pivot in range(15):
        b = 1 << pivot
        pairs = [(a, a | b) for a in sorted(active)
                 if (a & b) == 0 and (a | b) in active]
        for lower, upper in pairs:
            assert lower in active and upper in active
            assert (upper ^ lower).bit_count() == 1
            active.remove(lower)
            active.remove(upper)
            mate[lower] = upper
            mate[upper] = lower
    assert len(mate) == 2 * 5432
    assert len(active) == 5
    assert Counter(m.bit_count()-1 for m in active) == Counter({0: 1, 7: 4})
    indegree = {a: 0 for a in FACES if a}
    outgoing = {a: [] for a in FACES if a}
    incidences = 0
    for upper in indegree:
        bits = upper
        while bits:
            b = bits & -bits
            bits ^= b
            lower = upper ^ b
            if lower == 0:
                continue
            assert lower in FACED
            if mate.get(lower) == upper:
                source, target = lower, upper
            else:
                source, target = upper, lower
            outgoing[source].append(target)
            indegree[target] += 1
            incidences += 1
    assert incidences == 63780
    free = deque(v for v, degree in indegree.items() if degree == 0)
    visited = 0
    while free:
        v = free.popleft()
        visited += 1
        for w in outgoing[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                free.append(w)
    assert visited == len(indegree), (visited, len(indegree))
    return len(mate) // 2, len(active), incidences


def action(perm):
    on_v = [VINDEX[tuple(sorted(perm[x] for x in v))] for v in VERTICES]
    return tuple(EINDEX[tuple(sorted((on_v[i], on_v[j])))]
                 for i, j in EDGES)


def orbits(action_perm):
    unseen = set(range(len(action_perm)))
    ans = []
    while unseen:
        initial = min(unseen)
        x = initial
        cyc = []
        while x in unseen:
            unseen.remove(x)
            cyc.append(x)
            x = action_perm[x]
        assert x == initial
        ans.append(tuple(cyc))
    return tuple(ans)


def signed_orbit_trace(perm):
    c = orbits(action(perm))
    ans = 0
    for bits in range(1 << len(c)):
        degrees = [0] * 10
        valid = True
        for i, cycle in enumerate(c):
            if ((bits >> i) & 1) == 0:
                continue
            for k in cycle:
                a, b = EDGES[k]
                degrees[a] += 1
                degrees[b] += 1
                if degrees[a] > 2 or degrees[b] > 2:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            ans += (-1) ** bits.bit_count()
    return ans


def signed_simplex_trace(perm):
    """Second implementation: oriented fixed simplices, not edge orbit sums."""
    edgeperm = action(perm)
    total = 0
    for mask in FACES:
        labels = [i for i in range(15) if (mask >> i) & 1]
        images = [edgeperm[i] for i in labels]
        if set(images) != set(labels):
            continue
        inv = sum(images[i] > images[j]
                  for i in range(len(images)) for j in range(i+1, len(images)))
        total += (-1) ** (len(labels) + inv)
    return total


def cycle_type(perm):
    return tuple(sorted((len(c) for c in orbits(perm)), reverse=True))


def verify_character():
    classes = defaultdict(list)
    all_traces = {}
    for p in permutations(FIVE):
        typ = cycle_type(p)
        trace = signed_orbit_trace(p)
        assert trace == sum(p[i] == i for i in FIVE) - 1, (p, trace)
        classes[typ].append(trace)
        all_traces[p] = trace
    expected = {
        (1, 1, 1, 1, 1): (1, 4),
        (2, 1, 1, 1): (10, 2),
        (2, 2, 1): (15, 0),
        (3, 1, 1): (20, 1),
        (3, 2): (20, -1),
        (4, 1): (30, 0),
        (5,): (24, -1),
    }
    assert len(all_traces) == 120
    for typ, (count, trace) in expected.items():
        assert len(classes[typ]) == count
        assert set(classes[typ]) == {trace}
        rep = next(p for p in all_traces if cycle_type(p) == typ)
        assert signed_simplex_trace(rep) == trace, typ
    assert sum(t*t for t in all_traces.values()) == 120
    assert sum(all_traces.values()) == 0
    return expected


if __name__ == '__main__':
    pairs, critical, incidence = verify_morse()
    print('MORSE', pairs, critical, incidence)
    for typ, (n, tr) in sorted(verify_character().items()):
        print('CLASS', typ, 'elements', n, 'trace', tr)
    print('PETERSEN_M2_S5_STANDARD_CHARACTER_VERIFIED')
