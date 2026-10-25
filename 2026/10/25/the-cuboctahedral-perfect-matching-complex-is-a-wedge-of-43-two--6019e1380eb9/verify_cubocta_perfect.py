#!/usr/bin/env python3
"""Finite exact certificate for a perfect-matching extension complex.

All graph edges, faces, and matching pairs are specified by increasing
lexicographic ordering. Requires Python 3 and its standard library only.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json


def data():
    cube_edges = [(u, v) for u in range(8) for v in range(u + 1, 8)
                  if (u ^ v).bit_count() == 1]
    assert len(cube_edges) == 12
    graph_edges = [(a, b) for a in range(12) for b in range(a + 1, 12)
                   if set(cube_edges[a]) & set(cube_edges[b])]
    assert len(graph_edges) == 24
    assert Counter(x for e in graph_edges for x in e) == Counter({i: 4 for i in range(12)})
    edge_index = {e: i for i, e in enumerate(graph_edges)}
    graph_edge_set = set(graph_edges)

    def matchings(rest):
        if not rest:
            yield ()
            return
        first = min(rest)
        for second in sorted(rest):
            if first < second and (first, second) in graph_edge_set:
                for tail in matchings(rest - {first, second}):
                    yield ((first, second),) + tail

    perfect = sorted({sum(1 << edge_index[e] for e in m)
                      for m in matchings(set(range(12)))})
    assert len(perfect) == 32
    assert all(p.bit_count() == 6 for p in perfect)
    @lru_cache(None)
    def count(rest_mask):
        if rest_mask == 0:
            return 1
        i = (rest_mask & -rest_mask).bit_length() - 1
        ans = 0
        for j in range(i + 1, 12):
            if (rest_mask >> j) & 1 and (i, j) in graph_edge_set:
                ans += count(rest_mask ^ (1 << i) ^ (1 << j))
        return ans
    assert count((1 << 12) - 1) == len(perfect)
    faces = {0}
    for p in perfect:
        s = p
        while s:
            faces.add(s)
            s = (s - 1) & p
    assert len(faces) == 1429
    assert dict(sorted(Counter(s.bit_count() for s in faces).items())) == {
        0: 1, 1: 24, 2: 192, 3: 520, 4: 468, 5: 192, 6: 32}
    return cube_edges, graph_edges, perfect, faces


def reconstruct_toggle(faces):
    rest = set(faces)
    pairs = []
    for pivot in range(24):
        for smaller in sorted(rest):
            bigger = smaller | (1 << pivot)
            if bigger != smaller and bigger in rest:
                pairs.append([smaller, bigger])
                rest.remove(smaller)
                rest.remove(bigger)
    return pairs, rest


def check_certificate():
    cube_edges, graph_edges, perfect, faces = data()
    certificate = json.loads(Path(__file__).with_name('morse_certificate.json').read_text(encoding='utf-8'))
    assert certificate['schema_version'] == 1
    assert certificate['cube_edges'] == [list(e) for e in cube_edges]
    assert certificate['graph_edges'] == [list(e) for e in graph_edges]
    assert certificate['perfect_matching_masks'] == perfect
    pairs = certificate['matching_pairs']
    critical = certificate['critical_face_masks']
    augmented_pairs, augmented_critical = reconstruct_toggle(faces)
    assert augmented_pairs[0] == [0, 1] and len(augmented_critical) == 43
    assert pairs == augmented_pairs[1:]
    assert critical == sorted(augmented_critical | {1})
    assert len(pairs) == 692
    assert len(critical) == 44
    assert Counter(s.bit_count() for s in critical) == {1: 1, 3: 43}

    vertices_used = set()
    paired = set()
    for lo, hi in pairs:
        assert lo in faces and hi in faces
        assert lo not in vertices_used and hi not in vertices_used
        assert lo & hi == lo and (hi ^ lo).bit_count() == 1
        vertices_used.update((lo, hi))
        paired.add((lo, hi))
    assert vertices_used.isdisjoint(critical)
    assert vertices_used | set(critical) == faces - {0}

    # Acyclicity certificate: Forman's matched Hasse edges point upward,
    # and all other codimension-one Hasse edges point downward.
    degree = {s: 0 for s in faces if s}
    directed = {s: [] for s in faces if s}
    count_hasse = 0
    for hi in faces:
        if not hi:
            continue
        s = hi
        while s:
            bit = s & -s
            lo = hi ^ bit
            if not lo:
                s -= bit
                continue
            if (lo, hi) in paired:
                start, end = lo, hi
            else:
                start, end = hi, lo
            directed[start].append(end)
            degree[end] += 1
            count_hasse += 1
            s -= bit
    assert count_hasse == 4968
    pending = deque(s for s, d in degree.items() if d == 0)
    sorted_vertices = 0
    while pending:
        curr = pending.popleft()
        sorted_vertices += 1
        for nextface in directed[curr]:
            degree[nextface] -= 1
            if degree[nextface] == 0:
                pending.append(nextface)
    assert sorted_vertices == len(faces) - 1 and all(d == 0 for d in degree.values())
    # Independent mod-two chain boundary reductions (only a consistency check).
    layers = {k: sorted(s for s in faces if s.bit_count() == k)
              for k in range(1, 7)}
    ranks = []
    for k in range(2, 7):
        targets = {s: j for j, s in enumerate(layers[k - 1])}
        pivots = {}
        for hi in layers[k]:
            column = 0
            t = hi
            while t:
                bit = t & -t
                column ^= 1 << targets[hi ^ bit]
                t -= bit
            while column:
                highest = column.bit_length() - 1
                if highest not in pivots:
                    pivots[highest] = column
                    break
                column ^= pivots[highest]
        ranks.append(len(pivots))
    assert ranks == [23, 169, 308, 160, 32]
    # Reduced Euler characteristic of a bouquet of 43 two-spheres.
    euler = sum((-1) ** (s.bit_count() - 1) for s in faces if s)
    assert euler == 44
    print('cube_edges=12 graph_edges=24 perfect_matchings=32')
    print('face_sizes=1,24,192,520,468,192,32')
    print('face_hasse_incidences=4968 acyclic_sort_vertices=1428')
    print('matched_pairs=692 critical_face_sizes={1:1,3:43}')
    print('boundary_ranks_mod2=23,169,308,160,32')
    print('euler_characteristic=44')
    print('VERIFY_OK')


if __name__ == '__main__':
    check_certificate()
