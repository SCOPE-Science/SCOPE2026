#!/usr/bin/env python3
"""Exhaustive integral discrete-Morse certificate for the 2-independence complex of Q4.

Run: python3 verify_q4_ind2.py certificate.json
Requires Python 3.9+ standard library only.
"""
import collections
import functools
import json
import sys

N = 16


def graph_neighbors():
    return [sum(1 << (v ^ (1 << j)) for j in range(4)) for v in range(N)]


def independent_two(mask, neighbors):
    # Every induced connected component has at most two vertices precisely
    # when every selected vertex has at most one selected neighbor.
    return all((neighbors[v] & mask).bit_count() <= 1
               for v in range(N) if mask & (1 << v))


def enumerate_faces():
    adj = graph_neighbors()
    return {m for m in range(1, 1 << N) if independent_two(m, adj)}


def match_by_pivots(faces, order):
    unmatched = set(faces)
    pairs = []
    pivot_counts = []
    for v in order:
        bit = 1 << v
        layer = [(low, low | bit) for low in sorted(unmatched)
                 if not low & bit and low | bit in unmatched]
        assert all(low in unmatched and up in unmatched and up == low | bit
                   for low, up in layer)
        assert len({z for a, b in layer for z in (a, b)}) == 2 * len(layer)
        for low, up in layer:
            unmatched.remove(low)
            unmatched.remove(up)
        pivot_counts.append(len(layer))
        pairs.extend(layer)
    return unmatched, pairs, pivot_counts


def down_faces(mask):
    return [(mask ^ (1 << v), (-1)**i)
            for i, v in enumerate(v for v in range(N) if mask & (1 << v))]


def acyclic_check(faces, pairs):
    lower_to_upper = dict(pairs)
    indegree = {m: 0 for m in faces}
    # Directed Hasse graph: unmatched arrows downward, paired arrows upward.
    downward = {}
    edges = 0
    for higher in faces:
        lower_list = []
        for lower, _ in down_faces(higher):
            if lower not in faces:
                continue
            edges += 1
            if lower_to_upper.get(lower) == higher:
                indegree[higher] += 1
            else:
                indegree[lower] += 1
                lower_list.append(lower)
        downward[higher] = lower_list
    q = collections.deque(x for x in faces if indegree[x] == 0)
    count = 0
    while q:
        face = q.popleft()
        count += 1
        if face in lower_to_upper:
            higher = lower_to_upper[face]
            indegree[higher] -= 1
            if indegree[higher] == 0:
                q.append(higher)
        for lower in downward[face]:
            indegree[lower] -= 1
            if indegree[lower] == 0:
                q.append(lower)
    assert count == len(faces), (count, len(faces))
    return edges


def morse_boundaries(critical, pairs):
    lower_to_upper = dict(pairs)
    upper_to_lower = {up: lower for lower, up in pairs}
    @functools.lru_cache(None)
    def reduce(k_minus_one):
        if k_minus_one in critical:
            return {k_minus_one: 1}
        if k_minus_one in upper_to_lower:
            return {}
        higher = lower_to_upper[k_minus_one]
        boundary = dict(down_faces(higher))
        coefficient = boundary.pop(k_minus_one)
        assert coefficient in (-1, 1)
        ans = collections.Counter()
        for face, incidence in boundary.items():
            for target, c in reduce(face).items():
                ans[target] -= coefficient * incidence * c
        return {j: a for j, a in ans.items() if a}
    result = {}
    for higher in sorted(c for c in critical if c.bit_count() == 5):
        ans = collections.Counter()
        for lower, coefficient in down_faces(higher):
            for target, c in reduce(lower).items():
                ans[target] += coefficient * c
        result[str(higher)] = {str(j): a for j, a in sorted(ans.items()) if a}
    return result


def f2_boundary_ranks(faces):
    by_dim = [[m for m in sorted(faces) if m.bit_count() == d + 1]
              for d in range(8)]
    ranks = []
    for d in range(1, 8):
        lower_index = {f: i for i, f in enumerate(by_dim[d-1])}
        pivots = {}
        for mask in by_dim[d]:
            col = 0
            for lower, _ in down_faces(mask):
                col ^= 1 << lower_index[lower]
            while col:
                highest = col.bit_length() - 1
                if highest not in pivots:
                    pivots[highest] = col
                    break
                col ^= pivots[highest]
        ranks.append(len(pivots))
    return ranks


def main(path):
    with open(path, 'r', encoding='utf-8') as handle:
        expected = json.load(handle)
    order = expected['vertex_pivot_order']
    assert sorted(order) == list(range(N))
    faces = enumerate_faces()
    assert len(faces) == 3054
    f_vector = [sum(m.bit_count() == d+1 for m in faces) for d in range(8)]
    assert f_vector == [16,120,464,964,960,440,80,10]
    critical, pairs, pivot_counts = match_by_pivots(faces, order)
    assert len(pairs) == 1517
    assert len(critical) == 20
    assert sorted(critical) == expected['critical_masks']
    assert pivot_counts == expected['matching_pairs_per_pivot']
    c_counts = dict(sorted(collections.Counter(m.bit_count()-1 for m in critical).items()))
    assert c_counts == {0:1,3:17,4:2}
    directed_edges = acyclic_check(faces, pairs)
    assert directed_edges == expected['directed_hasse_edges']
    morse = morse_boundaries(critical, pairs)
    assert morse == expected['morse_boundary_dimension_four']
    assert len(morse) == 2
    assert set(tuple(sorted(v.items())) for v in morse.values()) == set(tuple(sorted(v.items())) for v in expected['morse_boundary_dimension_four'].values())
    assert all(set(map(int, v)).issubset(critical) for v in morse.values())
    ranks = f2_boundary_ranks(faces)
    assert ranks == [15,105,359,589,370,70,10]
    betti = [f_vector[d] - (ranks[d-1] if d > 0 else 0)
             - (ranks[d] if d < 7 else 0) - (1 if d==0 else 0)
             for d in range(8)]
    assert betti == [0,0,0,16,1,0,0,0]
    print('VERIFY_OK faces=3054 matching_pairs=1517 critical_0=1 critical_3=17 critical_4=2 '
          f'hasse_edges={directed_edges} integral_morse_d4={morse} '
          'mod2_reduced_betti=[0,0,0,16,1,0,0,0]')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 verify_q4_ind2.py certificate.json')
    main(sys.argv[1])
