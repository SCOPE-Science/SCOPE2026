#!/usr/bin/env python3
"""Exact finite verification of the octahedral Morse-complex character.

No external packages are required. Simplices are rooted oriented forests, with
arrows indexed lexicographically by their endpoints. The Hasse-DAG check is an
independent certificate of acyclicity for the stated discrete Morse matching.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations, product, combinations
from math import comb, prod

V = tuple(range(6))
AXES = tuple(range(3))
ARROWS = tuple((v, w) for v in V for w in V if v // 2 != w // 2)
INDEX = {a: i for i, a in enumerate(ARROWS)}
PIVOTS = [20, 19, 15, 7, 23, 12, 16, 8, 18, 10, 3, 2,
          21, 4, 6, 13, 17, 5, 22, 1, 11, 0, 14, 9]
assert len(ARROWS) == 24 and sorted(PIVOTS) == list(range(24))


def enumerate_forests():
    """Enumerate every partial functional orientation with no directed cycle."""
    out = set()
    options = [(-1,) + tuple(w for w in V if v // 2 != w // 2) for v in V]
    for parent in product(*options):
        # No edge may be used in both directions (this is also a directed 2-cycle).
        if any(parent[w] == v for v, w in enumerate(parent) if w >= 0):
            continue
        def cyclic(start):
            seen = set()
            while start >= 0:
                if start in seen:
                    return True
                seen.add(start)
                start = parent[start]
            return False
        if any(cyclic(v) for v in V):
            continue
        mask = 0
        for v, w in enumerate(parent):
            if w >= 0:
                mask |= 1 << INDEX[(v, w)]
        out.add(mask)
    return out


def free_morse_matching(all_faces):
    # At every pivot, pair all currently available faces toggled by that arrow.
    # The unique pair involving the empty face is replaced by one critical 0-cell.
    residual = set(all_faces)
    pairs = []
    reserved_vertex = None
    for t, a in enumerate(PIVOTS):
        bit = 1 << a
        toggles = [(s, s | bit) for s in residual if not (s & bit)
                   and (s | bit) in residual]
        for low, high in toggles:
            residual.remove(low)
            residual.remove(high)
            if low == 0:
                assert reserved_vertex is None
                reserved_vertex = high
            else:
                pairs.append((low, high))
    assert reserved_vertex is not None
    assert len(residual) == 675
    assert all(s.bit_count() == 5 for s in residual)
    assert len(pairs) == 2724
    return pairs, residual, reserved_vertex


def check_hasse_acyclic(all_faces, pairs):
    # Reverse every unmatched cover relation, but direct the matched one upward.
    faces = all_faces - {0}
    paired = set(pairs)
    adj = defaultdict(list)
    indeg = {s: 0 for s in faces}
    n_hasse = 0
    for upper in faces:
        for bit in [1 << i for i in range(24) if upper & (1 << i)]:
            lower = upper ^ bit
            if lower == 0:
                continue
            assert lower in faces
            n_hasse += 1
            if (lower, upper) in paired:
                source, target = lower, upper
            else:
                source, target = upper, lower
            adj[source].append(target)
            indeg[target] += 1
    q = deque(s for s in faces if indeg[s] == 0)
    seen = 0
    while q:
        s = q.popleft()
        seen += 1
        for t in adj[s]:
            indeg[t] -= 1
            if indeg[t] == 0:
                q.append(t)
    assert seen == len(faces), (seen, len(faces))
    return n_hasse


def signed_restriction_sign(mapped):
    inv = sum(mapped[i] > mapped[j] for i in range(len(mapped))
              for j in range(i+1, len(mapped)))
    return 1 if inv % 2 == 0 else -1


def signed_cycle_type(axis_permutation, flips):
    seen = set()
    positive, negative = [], []
    for a in AXES:
        if a in seen:
            continue
        cycle = []
        j = a
        while j not in seen:
            seen.add(j)
            cycle.append(j)
            j = axis_permutation[j]
        (positive if prod(flips[i] for i in cycle) == 1 else negative).append(len(cycle))
    return tuple(sorted(positive, reverse=True)), tuple(sorted(negative, reverse=True))


def group_element_action(p, flips):
    image_v = {2 * i + s: 2 * p[i] + (s if flips[i] == 1 else 1 - s)
               for i in AXES for s in (0, 1)}
    return tuple(INDEX[(image_v[v], image_v[w])] for v, w in ARROWS)


def trace_on_faces(faces_by_degree, arrow_perm):
    signed_traces = []
    for size in range(6):
        tr = 0
        for f in faces_by_degree[size]:
            image = [arrow_perm[i] for i in range(24) if f & (1 << i)]
            if sum(1 << j for j in image) == f:
                tr += signed_restriction_sign(image)
        signed_traces.append(tr)
    # Since H_0=Q and H_4 is the only other nonzero group,
    # the reduced H_4 character is the negative augmented Euler trace.
    homology_trace = -sum((-1)**k * tr for k, tr in enumerate(signed_traces))
    return homology_trace, signed_traces


def symmetric_character(partition, cycles):
    n = sum(partition)
    assert sum(cycles) == n
    if n <= 1:
        return 1
    if n == 2:
        return 1 if partition == (2,) else (-1 if cycles == (2,) else 1)
    if partition == (3,):
        return 1
    if partition == (1, 1, 1):
        return 1 if cycles in ((1, 1, 1), (3,)) else -1
    if partition == (2, 1):
        return {(1, 1, 1): 2, (2, 1): 0, (3,): -1}[cycles]
    raise AssertionError((partition, cycles))


def perm_cycles_on_subset(p, subset):
    seen, out = set(), []
    for a in subset:
        if a in seen:
            continue
        j, length = a, 0
        while j not in seen:
            assert j in subset
            seen.add(j)
            j, length = p[j], length + 1
        out.append(length)
    return tuple(sorted(out, reverse=True))


def wreath_character(p, flips, alpha, beta):
    """Induction formula for irreducibles of (C_2)^3 semidirect S_3."""
    total = 0
    for sel in combinations(AXES, sum(beta)):
        negative = set(sel)
        positive = set(AXES) - negative
        if {p[i] for i in negative} != negative:
            continue
        total += (prod(flips[i] for i in negative)
                  * symmetric_character(alpha, perm_cycles_on_subset(p, positive))
                  * symmetric_character(beta, perm_cycles_on_subset(p, negative)))
    return total


def run():
    all_faces = enumerate_forests()
    by_size = [[f for f in all_faces if f.bit_count() == s] for s in range(6)]
    f_vector = [len(row) for row in by_size]
    assert f_vector == [1, 24, 228, 1072, 2496, 2304]
    assert len(all_faces) == 6125
    pairs, residual, critical_vertex = free_morse_matching(all_faces)
    n_cover = check_hasse_acyclic(all_faces, pairs)
    assert critical_vertex.bit_count() == 1
    assert len(residual) == 675

    conj = defaultdict(list)
    G = []
    for p in permutations(AXES):
        for flips in product((-1, 1), repeat=3):
            ap = group_element_action(p, flips)
            assert sorted(ap) == list(range(24))
            # Check permutation sends every simplicial face to another face.
            assert all(sum(1 << ap[i] for i in range(24) if f & (1 << i))
                       in all_faces for f in all_faces)
            h4, chain_traces = trace_on_faces(by_size, ap)
            cl = signed_cycle_type(p, flips)
            conj[cl].append((h4, p, flips, chain_traces))
            G.append((p, flips, h4))
    assert len(G) == 48 and len(conj) == 10
    assert all(len({e[0] for e in group}) == 1 for group in conj.values())
    assert sorted(len(group) for group in conj.values()) == [1, 1, 3, 3, 6, 6, 6, 6, 8, 8]

    parts = {0: [()], 1: [(1,)], 2: [(2,), (1, 1)],
             3: [(3,), (2, 1), (1, 1, 1)]}
    irrep_multiplicities = {}
    character_matrix = {}
    for nb in range(4):
        for beta in parts[nb]:
            for alpha in parts[3 - nb]:
                irrep = [wreath_character(p, flips, alpha, beta) for p, flips, _ in G]
                char_id = (alpha, beta)
                character_matrix[char_id] = irrep
                pair = sum(tr * ir for (_, _, tr), ir in zip(G, irrep))
                assert pair % 48 == 0
                mult = pair // 48
                assert mult >= 0
                irrep_multiplicities[char_id] = mult
    # Independently check the claimed basis is an orthonormal character table.
    chars = list(character_matrix.values())
    for i, a in enumerate(chars):
        for j, b in enumerate(chars):
            assert sum(x * y for x, y in zip(a, b)) == (48 if i == j else 0)
    # Direct complete reconstruction of every character value.
    assert all(sum(irrep_multiplicities[key] * character_matrix[key][i]
                   for key in irrep_multiplicities) == h4
               for i, (_, _, h4) in enumerate(G))
    assert sum(irrep_multiplicities[(a, b)] * comb(3, sum(b))
               * symmetric_character(a, tuple([1] * sum(a)))
               * symmetric_character(b, tuple([1] * sum(b)))
               for a, b in irrep_multiplicities) == 675
    assert sum(tr for _, _, tr in G) == 48 * 11

    print('Faces by cardinality (empty included):', f_vector)
    print('Nonempty Hasse incidences:', n_cover)
    print('Acyclic matching pairs:', len(pairs))
    print('Critical cells: 1 dimension-zero, 675 dimension-four')
    print('Conjugacy class type: ((positive cycle sizes), (negative cycle sizes)), count, H4 trace')
    for key, group in sorted(conj.items()):
        print(key, len(group), group[0][0], group[0][3])
    print('Bipartition irreducible: multiplicities')
    for key in sorted(irrep_multiplicities):
        print(key, irrep_multiplicities[key])
    print('Fully symmetry-invariant dimension:', sum(tr for _, _, tr in G) // 48)
    print('ALL EXACT CHECKS PASS')


if __name__ == '__main__':
    run()
