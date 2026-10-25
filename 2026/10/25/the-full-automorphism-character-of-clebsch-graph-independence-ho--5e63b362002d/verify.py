#!/usr/bin/env python3
"""Exact finite verification for the Clebsch independence-complex symmetry character."""
from collections import Counter, deque
from itertools import permutations


def permutation_sign(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i + 1, len(p))) % 2 else 1


def permute_bits(x, p):
    return sum(((x >> i) & 1) << p[i] for i in range(5))


def rank_mod_two(columns):
    pivots = {}
    for c in columns:
        while c:
            bit = c.bit_length() - 1
            if bit in pivots:
                c ^= pivots[bit]
            else:
                pivots[bit] = c
                break
    return len(pivots)


def main():
    points = [x for x in range(32) if x.bit_count() % 2 == 0]
    assert len(points) == 16
    at = {x: i for i, x in enumerate(points)}
    neighbors = [set(j for j, y in enumerate(points)
                     if (x ^ y).bit_count() == 4)
                 for x in points]
    assert all(len(ns) == 5 for ns in neighbors)
    for i in range(16):
        for j in range(i + 1, 16):
            assert len(neighbors[i] & neighbors[j]) == (0 if j in neighbors[i] else 2)

    faces = []
    for m in range(1, 1 << 16):
        if all(not (m >> i & 1 and m >> j & 1)
               for i in range(16) for j in neighbors[i] if i < j):
            faces.append(m)
    assert len(faces) == 392
    profile = Counter(m.bit_count() - 1 for m in faces)
    assert [profile[i] for i in range(5)] == [16, 80, 160, 120, 16]
    assert sum((-1)**d * profile[d] for d in profile) - 1 == -9
    face_set = set(faces)

    # An explicit face-poset matching, independently checked for acyclicity.
    remain = set(faces)
    matching = set()
    for i in range(16):
        bit = 1 << i
        for low in sorted(remain):
            high = low | bit
            if not low & bit and high in remain:
                assert high.bit_count() == low.bit_count() + 1
                remain.remove(low)
                remain.remove(high)
                matching.add((low, high))
    assert len(matching) == 191
    assert Counter(m.bit_count() - 1 for m in remain) == {0: 1, 3: 9}

    indeg = {m: 0 for m in faces}
    arrows = {m: [] for m in faces}
    incidences = 0
    for high in faces:
        if high.bit_count() == 1:
            continue
        for i in range(16):
            if high >> i & 1:
                low = high ^ (1 << i)
                if (low, high) in matching:
                    source, target = low, high
                else:
                    source, target = high, low
                arrows[source].append(target)
                indeg[target] += 1
                incidences += 1
    assert incidences == 1200
    queue = deque(m for m in faces if indeg[m] == 0)
    visited = 0
    while queue:
        m = queue.popleft()
        visited += 1
        for z in arrows[m]:
            indeg[z] -= 1
            if indeg[z] == 0:
                queue.append(z)
    assert visited == 392

    # A second, algebraic check of simplicial boundaries over the prime field.
    by_dim = [[m for m in faces if m.bit_count() - 1 == d] for d in range(5)]
    ranks = []
    for d in range(1, 5):
        row = {m: i for i, m in enumerate(by_dim[d - 1])}
        cols = []
        for f in by_dim[d]:
            boundary = 0
            for i in range(16):
                if f >> i & 1:
                    boundary ^= 1 << row[f ^ (1 << i)]
            cols.append(boundary)
        ranks.append(rank_mod_two(cols))
    assert ranks == [15, 65, 95, 16]

    # The full symmetry group comprises 16 translations and 120 permutations.
    # Every automorphism fixing zero permutes its five neighbors; each remaining
    # vertex is determined by a distinct pair of these neighbors.
    zero = at[0]
    around = sorted(neighbors[zero])
    outer = [v for v in range(16) if v != zero and v not in neighbors[zero]]
    labels = {tuple(v for v in around if v in neighbors[w]) for w in outer}
    assert len(outer) == 10 and len(labels) == 10
    assert all(len(z) == 2 for z in labels)

    def signed_trace(vertex_perm):
        total = 1  # The empty face in the reduced Lefschetz calculation.
        for mask in faces:
            image_mask = 0
            image_list = []
            for i in range(16):
                if mask >> i & 1:
                    j = vertex_perm[i]
                    image_mask |= 1 << j
                    image_list.append(j)
            if image_mask != mask:
                continue
            total += (-1)**mask.bit_count() * permutation_sign(image_list)
        return total

    def orbit_trace(vertex_perm):
        # Independent calculation: each selected vertex-cycle contributes -1.
        cycles = []
        seen = set()
        for i in range(16):
            if i in seen:
                continue
            c = []
            j = i
            while j not in seen:
                seen.add(j)
                c.append(j)
                j = vertex_perm[j]
            cycles.append(c)
        eligible = []
        for c in cycles:
            if all(j not in neighbors[i] for i, j in __import__('itertools').combinations(c, 2)):
                eligible.append(c)
        conflicts = []
        for i, a in enumerate(eligible):
            conflicts.append(sum(1 << j for j, b in enumerate(eligible)
                                 if any(y in neighbors[x] for x in a for y in b)))
        # Evaluate the independence polynomial of the orbit-conflict graph at -1.
        def polynomial(m):
            if not m:
                return 1
            b = m & -m
            i = b.bit_length() - 1
            return polynomial(m ^ b) - polynomial(m & ~(b | conflicts[i]))
        return polynomial((1 << len(eligible)) - 1)

    character_by_cycle_type = {}
    checked = 0
    for sigma in permutations(range(5)):
        sign = permutation_sign(sigma)
        fixed = [i for i in range(5) if sigma[i] == i]
        sigma_perm = [at[permute_bits(x, sigma)] for x in points]
        for translation in points:
            vperm = [at[points[y] ^ translation] for y in sigma_perm]
            assert sorted(vperm) == list(range(16))
            observed = signed_trace(vperm)
            second = orbit_trace(vperm)
            expected = sign * (len(fixed) - 1 +
                               sum(1 if not (translation >> i & 1) else -1
                                   for i in fixed))
            assert observed == second == expected, (sigma, translation, observed, second, expected)
            checked += 1
        if sigma == tuple(range(5)):
            assert [signed_trace([at[x ^ a] for x in points])
                    for a in points] == [9 if a.bit_count() == 0 else
                                         (5 if a.bit_count() == 2 else 1)
                                         for a in points]
        kind = []
        used = set()
        for i in range(5):
            if i in used:
                continue
            j, size = i, 0
            while j not in used:
                used.add(j)
                size += 1
                j = sigma[j]
            kind.append(size)
        kind = tuple(sorted(kind, reverse=True))
        actual = signed_trace(sigma_perm)
        character_by_cycle_type.setdefault(kind, actual)
        assert character_by_cycle_type[kind] == actual
    assert checked == 1920 and len(character_by_cycle_type) == 7
    assert character_by_cycle_type == {
        (1, 1, 1, 1, 1): 9, (2, 1, 1, 1): -5,
        (3, 1, 1): 3, (2, 2, 1): 1,
        (4, 1): -1, (3, 2): 1, (5,): -1}
    print('FACES', [profile[i] for i in range(5)])
    print('ACyclic_MATCHING_PAIRS', len(matching), 'CRITICAL', sorted((x.bit_count()-1 for x in remain)))
    print('MOD2_BOUNDARY_RANKS', ranks)
    print('AUTOMORPHISMS', checked, 'CLASS_CHARACTER', sorted(character_by_cycle_type.items()))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
