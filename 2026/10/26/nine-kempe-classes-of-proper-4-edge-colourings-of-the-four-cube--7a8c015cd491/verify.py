#!/usr/bin/env python3
"""Exact census of proper four-edge-colourings of the four-cube.

Run from the directory containing mk_isomorphism_certificates.json.
Only the Python standard library is required.
"""
import itertools
import json
from collections import Counter, deque
from pathlib import Path


def main():
    vertices = range(16)
    edges = [(u, u ^ (1 << k)) for u in vertices for k in range(4)
             if u < (u ^ (1 << k))]
    assert len(edges) == 32 and len(set(edges)) == 32
    edge_id = {e: i for i, e in enumerate(edges)}
    incident = [[] for _ in vertices]
    for i, (u, v) in enumerate(edges):
        incident[u].append((v, i))
        incident[v].append((u, i))
    assert all(len(row) == 4 for row in incident)
    full_edges = (1 << len(edges)) - 1

    # Method I: enumerate perfect matchings, then unordered partitions into four.
    matchings = []
    def rec_match(occupied, mask):
        if occupied == (1 << 16) - 1:
            matchings.append(mask)
            return
        u = next(v for v in vertices if not (occupied >> v & 1))
        for w, i in incident[u]:
            if not (occupied >> w & 1):
                rec_match(occupied | (1 << u) | (1 << w), mask | (1 << i))
    rec_match(0, 0)
    match_id = {m: i for i, m in enumerate(matchings)}
    assert len(matchings) == len(match_id) == 272
    pairs = [[] for _ in matchings]
    for i, a in enumerate(matchings):
        for j in range(i + 1, len(matchings)):
            if a & matchings[j] == 0:
                pairs[i].append(j)
    factorizations = []
    for i, a in enumerate(matchings):
        for j in pairs[i]:
            b = matchings[j]
            for k in pairs[j]:
                if k <= j or a & matchings[k]:
                    continue
                fourth = full_edges ^ (a | b | matchings[k])
                l = match_id.get(fourth, -1)
                if l > k:
                    factorizations.append((i, j, k, l))
    factor_id = {f: i for i, f in enumerate(factorizations)}
    assert len(factorizations) == len(factor_id) == 1840

    # Method II: independently colour edges, with the colours pinned at vertex 0.
    # Every colour occurs at that vertex, so this fixes colour-name symmetry once.
    fixed_inc = sorted(incident[0], key=lambda t: t[0])
    colour = [-1] * len(edges)
    used_at = [0] * 16
    for c, (_, e) in enumerate(fixed_inc):
        u, v = edges[e]
        colour[e] = c
        used_at[u] |= (1 << c)
        used_at[v] |= (1 << c)
    direct_colourings = {}
    def rec_colouring(remain):
        if remain == 0:
            masks = [0] * 4
            for e, c in enumerate(colour):
                masks[c] |= 1 << e
            f = tuple(sorted(match_id[m] for m in masks))
            assert f not in direct_colourings
            direct_colourings[f] = tuple(colour)
            return
        best_edge = -1
        best_options = 0
        best_count = 5
        for e, (u, v) in enumerate(edges):
            if colour[e] != -1:
                continue
            options = 15 & ~(used_at[u] | used_at[v])
            nopt = options.bit_count()
            if nopt < best_count:
                best_edge, best_options, best_count = e, options, nopt
                if nopt == 0:
                    return
                if nopt == 1:
                    break
        u, v = edges[best_edge]
        while best_options:
            bit = best_options & -best_options
            best_options ^= bit
            colour[best_edge] = bit.bit_length() - 1
            used_at[u] |= bit
            used_at[v] |= bit
            rec_colouring(remain - 1)
            used_at[u] ^= bit
            used_at[v] ^= bit
            colour[best_edge] = -1
    rec_colouring(28)
    assert len(direct_colourings) == 1840
    assert set(direct_colourings) == set(factorizations)

    # Method I for Kempe adjacency: flip each connected two-factor cycle.
    # Each union of two perfect matchings is 2-regular and spanning.
    neighbours = [set() for _ in factorizations]
    for i, f in enumerate(factorizations):
        for p, q in itertools.combinations(range(4), 2):
            a, b = matchings[f[p]], matchings[f[q]]
            ab = a | b
            unseen = set(vertices)
            while unseen:
                seed = min(unseen)
                unseen.remove(seed)
                stack = [seed]
                cycle_edges = 0
                while stack:
                    u = stack.pop()
                    for v, e in incident[u]:
                        if not (ab >> e & 1):
                            continue
                        cycle_edges |= 1 << e
                        if v in unseen:
                            unseen.remove(v)
                            stack.append(v)
                a2, b2 = a ^ cycle_edges, b ^ cycle_edges
                j = factor_id[tuple(sorted(
                    [match_id[a2], match_id[b2]]
                    + [f[t] for t in range(4) if t not in (p, q)]))]
                if i != j:
                    neighbours[i].add(j)
    assert all(i in neighbours[j] for i, adj in enumerate(neighbours) for j in adj)

    # Method II for Kempe adjacency: swap literal colour labels on each
    # alternating-cycle connected component, independently of matching masks.
    for f, cols in direct_colourings.items():
        i = factor_id[f]
        actual = set()
        for a, b in itertools.combinations(range(4), 2):
            subedges = [e for e, c in enumerate(cols) if c == a or c == b]
            remaining = set(subedges)
            while remaining:
                todo = [min(remaining)]
                remaining.remove(todo[0])
                comp = set(todo)
                while todo:
                    e = todo.pop()
                    u, v = edges[e]
                    for x in (u, v):
                        for _, other in incident[x]:
                            if other in remaining and cols[other] in (a, b):
                                remaining.remove(other)
                                comp.add(other)
                                todo.append(other)
                switched = list(cols)
                for e in comp:
                    switched[e] = b if cols[e] == a else a
                naming = {switched[e]: k for k, (_, e) in enumerate(fixed_inc)}
                canonical = [naming[c] for c in switched]
                four_masks = [0] * 4
                for e, c in enumerate(canonical):
                    four_masks[c] |= 1 << e
                f2 = tuple(sorted(match_id[m] for m in four_masks))
                j = factor_id[f2]
                if i != j:
                    actual.add(j)
        assert actual == neighbours[i]

    # Kempe-class partition and exact graph parameters.
    seen = set()
    components = []
    for i in range(len(factorizations)):
        if i in seen:
            continue
        comp = [i]
        seen.add(i)
        for v in comp:
            for w in sorted(neighbours[v]):
                if w not in seen:
                    seen.add(w)
                    comp.append(w)
        components.append(comp)
    assert sorted(map(len, components)) == [16] * 8 + [1712]
    assert len(components) == 9
    assert sum(map(len, components)) == 1840
    assert sum(map(len, neighbours)) // 2 == 8808
    assert len(components[0]) == 1712

    # Permutation signs of the four perfect matchings, from even to odd vertices.
    even = [v for v in vertices if v.bit_count() % 2 == 0]
    odd = [v for v in vertices if v.bit_count() % 2 == 1]
    odd_id = {v: k for k, v in enumerate(odd)}
    matching_signs = []
    for m in matchings:
        partner = {}
        for e, (u, v) in enumerate(edges):
            if m >> e & 1:
                partner[u] = v
                partner[v] = u
        perm = [odd_id[partner[v]] for v in even]
        sign = sum(perm[i] > perm[j] for i in range(8)
                   for j in range(i + 1, 8)) % 2
        matching_signs.append(sign)
    signs = [sum(matching_signs[m] for m in f) % 2 for f in factorizations]
    assert Counter(signs) == {0: 1712, 1: 128}
    assert all(signs[i] == 0 for i in components[0])
    assert all(signs[i] == 1 for comp in components[1:] for i in comp)
    assert all(signs[i] == signs[j] for i, adj in enumerate(neighbours) for j in adj)

    # Enumerate all 24 square faces: rainbow means four different edge colours.
    faces = set()
    for v in vertices:
        for a, b in itertools.combinations(range(4), 2):
            if v >> a & 1 or v >> b & 1:
                continue
            va, vb, vab = v ^ (1 << a), v ^ (1 << b), v ^ (1 << a) ^ (1 << b)
            sq = frozenset(edge_id[tuple(sorted(z))] for z in
                           ((v, va), (v, vb), (va, vab), (vb, vab)))
            faces.add(sq)
    assert len(faces) == 24
    rainbow = []
    for f in factorizations:
        colour_edges = {}
        for c, m_id in enumerate(f):
            m = matchings[m_id]
            for e in range(32):
                if m >> e & 1:
                    colour_edges[e] = c
        rainbow.append(sum(len({colour_edges[e] for e in face}) == 4
                           for face in faces))
    assert all(r % 2 == s for r, s in zip(rainbow, signs))
    assert Counter(rainbow[i] for i in range(1840) if signs[i]) == {9: 128}
    assert Counter(rainbow[i] for i in range(1840) if not signs[i]) == {
        0: 371, 4: 768, 6: 304, 8: 132, 10: 96, 12: 24, 16: 15, 24: 2}

    # Explicit certified isomorphisms from GP(8,3) (the Moebius--Kantor graph)
    # to each small Kempe component. Each row maps named GP vertices to
    # factorization indices, so these checks do not use graph-isomorphism software.
    witnesses = json.loads((Path(__file__).parent /
        'mk_isomorphism_certificates.json').read_text(encoding='utf-8'))
    assert len(witnesses) == 8
    mk_edges = {frozenset((i, (i + 1) % 8)) for i in range(8)}
    mk_edges.update(frozenset((i, i + 8)) for i in range(8))
    mk_edges.update(frozenset((i + 8, (i + 3) % 8 + 8)) for i in range(8))
    assert len(mk_edges) == 24
    for c, mapping in zip(components[1:], witnesses):
        assert len(mapping) == 16 and set(mapping) == set(c)
        for i, j in itertools.combinations(range(16), 2):
            assert (frozenset((i, j)) in mk_edges) == (
                mapping[j] in neighbours[mapping[i]])

    # All eight exceptional components are in a single orbit of Aut(Q4).
    component_label = {i: k for k, c in enumerate(components) for i in c}
    rep = components[1][0]
    images = Counter()
    for axes in itertools.permutations(range(4)):
        for shift in range(16):
            def transform(v):
                return shift ^ sum((1 << axes[k]) for k in range(4) if v >> k & 1)
            eimage = [edge_id[tuple(sorted((transform(u), transform(v))))]
                      for u, v in edges]
            new_masks = []
            for mi in factorizations[rep]:
                m = matchings[mi]
                new_masks.append(sum(1 << eimage[e] for e in range(32) if m >> e & 1))
            target = tuple(sorted(match_id[m] for m in new_masks))
            images[component_label[factor_id[target]]] += 1
    assert images == {i: 48 for i in range(1, 9)}

    def graph_metrics(component):
        ecc = Counter()
        distances = Counter()
        for root in component:
            dist = {root: 0}
            bfs = deque([root])
            while bfs:
                v = bfs.popleft()
                for w in neighbours[v]:
                    if w not in dist:
                        dist[w] = dist[v] + 1
                        bfs.append(w)
            assert len(dist) == len(component)
            ecc[max(dist.values())] += 1
            for d, count in Counter(dist.values()).items():
                if d:
                    distances[d] += count
        assert all(n % 2 == 0 for n in distances.values())
        return dict(ecc), {k: v // 2 for k, v in sorted(distances.items())}
    giant_ecc, giant_distance = graph_metrics(components[0])
    assert giant_ecc == {6: 133, 7: 1342, 8: 237}
    assert giant_distance == {
        1: 8616, 2: 54708, 3: 220188, 4: 496780,
        5: 490860, 6: 181602, 7: 11258, 8: 604}
    assert sum(giant_distance.values()) == 1712 * 1711 // 2
    for c in components[1:]:
        e, distances = graph_metrics(c)
        assert e == {4: 16}
        assert distances == {1: 24, 2: 48, 3: 40, 4: 8}
    print('VERIFY_OK')
    print('perfect_matchings=272, factorizations=1840, two_complete_enumerations=agree')
    print('Kempe_components=9, sizes=1712+8*16, edges=8808')
    print('sign_positive=1712, sign_negative=128, all_negative_rainbow_faces=9')
    print('small_components=8_isomorphic_Moebius-Kantor, one_cube_symmetry_orbit')
    print('giant_radius=6, giant_diameter=8, giant_distance_histogram=' + str(giant_distance))

if __name__ == '__main__':
    main()
