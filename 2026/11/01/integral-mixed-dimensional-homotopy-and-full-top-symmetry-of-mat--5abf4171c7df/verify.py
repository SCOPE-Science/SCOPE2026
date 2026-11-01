#!/usr/bin/env python3
"""Exact integral Morse and equivariant homology calculation for N(L(K_7)).

Requires only Python's standard library. Faces are nonempty bitmasks of the 21
lexicographically indexed edges of K_7. No probabilistic or floating arithmetic.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 7
EDGES = list(combinations(range(N), 2))
EDGE_ID = {e: i for i, e in enumerate(EDGES)}


def all_faces():
    faces = set()
    for a, b in EDGES:
        nb = sum(1 << i for i, (c, d) in enumerate(EDGES)
                 if (a == c or a == d or b == c or b == d) and (a, b) != (c, d))
        sub = nb
        while sub:
            faces.add(sub)
            sub = (sub - 1) & nb
    return faces


def boundary(face):
    """Oriented simplicial boundary with ascending edge indices."""
    parity = 0
    for i in range(len(EDGES)):
        if face & (1 << i):
            yield face ^ (1 << i), (1 if parity % 2 == 0 else -1)
            parity += 1


def make_matching(faces):
    """Sequential element toggles in lexicographic edge order."""
    unmatched = set(faces)
    low_to_high = {}
    high_to_low = {}
    for v in range(len(EDGES)):
        bit = 1 << v
        for low in sorted(unmatched):
            if low & bit:
                continue
            high = low | bit
            if high in unmatched:
                assert low in unmatched
                unmatched.remove(low)
                unmatched.remove(high)
                low_to_high[low] = high
                high_to_low[high] = low
    return unmatched, low_to_high, high_to_low


def certify_acyclic(faces, low_to_high):
    """Check the full matched/reversed Hasse digraph is acyclic."""
    ordered = sorted(faces)
    loc = {f: i for i, f in enumerate(ordered)}
    indeg = [0] * len(ordered)
    forward = [[] for _ in ordered]
    incidences = 0
    for high in ordered:
        if high.bit_count() == 1:
            continue
        for low, _ in boundary(high):
            assert low in loc
            if low_to_high.get(low) == high:
                src, dst = low, high
            else:
                src, dst = high, low
            forward[loc[src]].append(loc[dst])
            indeg[loc[dst]] += 1
            incidences += 1
    queue = deque(i for i, d in enumerate(indeg) if not d)
    reached = 0
    while queue:
        i = queue.popleft()
        reached += 1
        for j in forward[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                queue.append(j)
    assert reached == len(faces)
    return incidences


def add_entry(dct, key, coeff):
    dct[key] += coeff
    if dct[key] == 0:
        del dct[key]


def zero_morse_boundary(critical, low_to_high, high_to_low):
    """Integral differential from critical 4-cells to critical 3-cells."""
    @lru_cache(None)
    def project_three(face):
        assert face.bit_count() == 4
        if face in critical:
            return {face: 1}
        if face in high_to_low:
            return {}
        higher = low_to_high[face]
        assert higher.bit_count() == 5
        pivot = next(s for f, s in boundary(higher) if f == face)
        result = defaultdict(int)
        for lower, sign in boundary(higher):
            if lower == face:
                continue
            for c, multiplicity in project_three(lower).items():
                result[c] -= pivot * sign * multiplicity
        return {c: v for c, v in result.items() if v}

    critical_four = sorted(c for c in critical if c.bit_count() == 5)
    for cell in critical_four:
        out = defaultdict(int)
        for face, sign in boundary(cell):
            for c, coefficient in project_three(face).items():
                out[c] += sign * coefficient
        assert all(v == 0 for v in out.values()), (cell, dict(out))
    return critical_four


def lift_top_cycles(critical_four, low_to_high):
    """Construct seven explicit integral simplicial 4-cycles."""
    low_three = {low for low, high in low_to_high.items() if low.bit_count() == 4}
    dependencies = {}
    indeg = {a: 0 for a in low_three}
    for low in low_three:
        high = low_to_high[low]
        nxt = {f for f, _ in boundary(high) if f != low and f in low_three}
        dependencies[low] = nxt
        for f in nxt:
            indeg[f] += 1
    queue = deque(sorted(a for a, d in indeg.items() if not d))
    order = []
    while queue:
        a = queue.popleft()
        order.append(a)
        for f in sorted(dependencies[a]):
            indeg[f] -= 1
            if indeg[f] == 0:
                queue.append(f)
    assert len(order) == len(low_three)

    cycles = []
    for cell in critical_four:
        chain = defaultdict(int, {cell: 1})
        differential = defaultdict(int)
        for f, s in boundary(cell):
            add_entry(differential, f, s)
        for low in order:
            coeff = differential.get(low, 0)
            if not coeff:
                continue
            high = low_to_high[low]
            pivot = next(s for f, s in boundary(high) if f == low)
            new_coeff = -pivot * coeff
            add_entry(chain, high, new_coeff)
            for f, s in boundary(high):
                add_entry(differential, f, new_coeff * s)
        assert not differential, (cell, dict(differential))
        assert chain[cell] == 1
        cycles.append(dict(chain))
    return cycles


def character_check(critical, low_to_high, high_to_low, critical_four, cycles):
    """Exact signed S_7 actions on integral fourth homology."""
    @lru_cache(None)
    def project_four(face):
        assert face.bit_count() == 5
        if face in critical:
            return {face: 1}
        if face in high_to_low:
            return {}
        higher = low_to_high[face]
        assert higher.bit_count() == 6
        pivot = next(s for f, s in boundary(higher) if f == face)
        result = defaultdict(int)
        for lower, sign in boundary(higher):
            if lower == face:
                continue
            for c, multiplicity in project_four(lower).items():
                result[c] -= pivot * sign * multiplicity
        return {c: v for c, v in result.items() if v}

    def image_of_cycle(cycle, permutation):
        moved_edge = [EDGE_ID[tuple(sorted((permutation[a], permutation[b])))]
                      for a, b in EDGES]
        out = defaultdict(int)
        for face, coefficient in cycle.items():
            moved = [moved_edge[i] for i in range(len(EDGES)) if face & (1 << i)]
            mask = sum(1 << i for i in moved)
            inversions = sum(moved[i] > moved[j]
                             for i in range(len(moved)) for j in range(i + 1, len(moved)))
            sign = -1 if inversions % 2 else 1
            for c, k in project_four(mask).items():
                out[c] += sign * coefficient * k
        return [out.get(c, 0) for c in critical_four]

    def transposition(a, b):
        p = list(range(N))
        p[a], p[b] = p[b], p[a]
        return p

    # Integral lifts have Morse coordinates the standard seven basis vectors.
    for j, cycle in enumerate(cycles):
        vector = [sum(coeff * project_four(face).get(c, 0)
                      for face, coeff in cycle.items()) for c in critical_four]
        assert vector == [int(i == j) for i in range(N)]

    # Build a signed permutation basis from the orbit of the first top cycle.
    w = [[int(i == 0) for i in range(N)]]
    for i in range(1, N):
        w.append([-v for v in image_of_cycle(cycles[0], transposition(0, i))])
    assert all(sum(v != 0 for v in vec) == 1 for vec in w)
    assert all(abs(v) <= 1 for vec in w for v in vec)
    assert set(next(i for i, v in enumerate(vec) if v) for vec in w) == set(range(N))

    def apply_to_vector(vector, images):
        return [sum(vector[j] * images[j][i] for j in range(N)) for i in range(N)]

    for i in range(N - 1):
        p = transposition(i, i + 1)
        images = [image_of_cycle(z, p) for z in cycles]
        for j in range(N):
            assert apply_to_vector(w[j], images) == [-v for v in w[p[j]]]

    def integer_partitions(total, largest=None):
        if total == 0:
            yield ()
            return
        if largest is None:
            largest = total
        for c in range(min(total, largest), 0, -1):
            for rest in integer_partitions(total - c, c):
                yield (c,) + rest

    chars = {}
    for parts in integer_partitions(N):
        p = list(range(N))
        s = 0
        for k in parts:
            for j in range(k):
                p[s + j] = s + (j + 1) % k
            s += k
        images = [image_of_cycle(z, p) for z in cycles]
        trace = sum(images[i][i] for i in range(N))
        expected = (-1 if (N - len(parts)) % 2 else 1) * parts.count(1)
        assert trace == expected, (parts, trace, expected)
        chars['+'.join(map(str, parts))] = trace
    assert len(chars) == 15
    return chars


def main():
    faces = all_faces()
    by_dimension = Counter(f.bit_count() - 1 for f in faces)
    fvector = [by_dimension[d] for d in range(10)]
    assert fvector == [21, 210, 1190, 3780, 5187, 4410, 2520, 945, 210, 21]
    critical, low_to_high, high_to_low = make_matching(faces)
    assert len(low_to_high) == len(high_to_low) == 9120
    assert 2 * len(low_to_high) + len(critical) == len(faces)
    assert Counter(f.bit_count() - 1 for f in critical) == {0: 1, 3: 246, 4: 7}
    incidences = certify_acyclic(faces, low_to_high)
    assert incidences == 98805
    critical_four = zero_morse_boundary(critical, low_to_high, high_to_low)
    assert critical_four == [62, 930, 14370, 100388, 299048, 335920, 671792]
    cycles = lift_top_cycles(critical_four, low_to_high)
    assert [len(c) for c in cycles] == [6, 36, 36, 36, 36, 36, 36]
    assert all(max(abs(v) for v in c.values()) == 1 for c in cycles)
    chars = character_check(critical, low_to_high, high_to_low, critical_four, cycles)
    print('exact_faces:', len(faces))
    print('face_vector:', fvector)
    print('morse_pairs:', len(low_to_high))
    print('directed_hasse_incidences:', incidences)
    print('critical_cells:', dict(sorted(Counter(f.bit_count() - 1 for f in critical).items())))
    print('integral_morse_boundary_4_to_3: zero (7 by 246)')
    print('top_cycle_supports:', [len(c) for c in cycles])
    print('integral_S7_top_module: sign tensor permutation lattice on seven labels')
    print('S7_adjacent_transposition_checks:', N - 1)
    print('S7_conjugacy_class_checks:', len(chars))
    print('characters:', chars)
    print('result: PASS')


if __name__ == '__main__':
    main()
