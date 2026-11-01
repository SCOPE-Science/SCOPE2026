#!/usr/bin/env python3
"""Exact finite-chain and discrete-Morse verification for two graph complexes.

Run with Python 3, standard library only. Vertices are indexed 4*a+b.
The exhaustive domain has exactly 2**16 subsets in each case.
"""
import json
from collections import Counter, deque
from functools import lru_cache
from math import gcd

N = 16


def graph_adjacency(kind):
    if kind == 'rook':
        return tuple(sum(1 << j for j in range(N)
                         if i != j and (i // 4 == j // 4 or i % 4 == j % 4))
                     for i in range(N))
    assert kind == 'shrikhande'
    steps = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1))
    return tuple(sum(1 << (4 * ((i // 4 + u) % 4) + (i % 4 + v) % 4)
                     for u, v in steps) for i in range(N))


def check_graph(adj, kind):
    assert len(adj) == N
    assert all(adj[i].bit_count() == 6 and not (adj[i] & (1 << i))
               for i in range(N))
    assert all(bool(adj[i] & (1 << j)) == bool(adj[j] & (1 << i))
               for i in range(N) for j in range(N))
    assert all((adj[i] & adj[j]).bit_count() == 2
               for i in range(N) for j in range(i + 1, N))
    assert sum(x.bit_count() for x in adj) // 2 == 48
    # Local graph is 2K3 for rook and C6 for Shrikhande.
    neighbors = [j for j in range(N) if adj[0] >> j & 1]
    remain = set(neighbors)
    component_sizes = []
    while remain:
        stack = [min(remain)]
        remain.remove(stack[0])
        count = 0
        while stack:
            j = stack.pop()
            count += 1
            for k in list(remain):
                if adj[j] >> k & 1:
                    remain.remove(k)
                    stack.append(k)
        component_sizes.append(count)
    component_sizes.sort()
    assert component_sizes == ([3, 3] if kind == 'rook' else [6])
    assert all((adj[i] & adj[0]).bit_count() == 2 for i in neighbors)


def connected_triples(adj):
    ans = []
    for a in range(N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                ab = bool(adj[a] >> b & 1)
                ac = bool(adj[a] >> c & 1)
                bc = bool(adj[b] >> c & 1)
                if int(ab) + int(ac) + int(bc) >= 2:
                    ans.append((1 << a) | (1 << b) | (1 << c))
    assert len(ans) == 176
    return tuple(ans)


def bfs_two_independent(mask, adj):
    remain = mask
    while remain:
        root = remain & -remain
        remain ^= root
        reached = root
        queue = root
        while queue:
            v = (queue & -queue).bit_length() - 1
            queue &= queue - 1
            new = adj[v] & remain
            remain ^= new
            reached |= new
            queue |= new
        if reached.bit_count() > 2:
            return False
    return True


def faces_of_complex(adj):
    triples = connected_triples(adj)
    # Two independent definitions: forbidden connected triples and graph BFS.
    small = set()
    for mask in range(1 << N):
        triple_free = not any((mask & t) == t for t in triples)
        via_components = bfs_two_independent(mask, adj)
        assert triple_free == via_components, ('bad face', mask)
        if triple_free and mask:
            small.add(mask)
    return small


def matching(faces):
    unpaired = set(faces)
    low_to_high = {}
    high_to_low = {}
    for vertex in range(N):
        bit = 1 << vertex
        for f in sorted(unpaired):
            if f & bit:
                continue
            g = f | bit
            if g in unpaired:
                assert g not in high_to_low and f not in low_to_high
                unpaired.remove(f)
                unpaired.remove(g)
                low_to_high[f] = g
                high_to_low[g] = f
    return unpaired, low_to_high, high_to_low


def signed_boundary(mask):
    bits = mask
    idx = 0
    while bits:
        bit = bits & -bits
        bits ^= bit
        yield (mask ^ bit), (1 if idx % 2 == 0 else -1)
        idx += 1


def acyclic_certificate(faces, low_to_high):
    degree = {f: 0 for f in faces}
    outgoing = {f: [] for f in faces}
    arrows = 0
    for g in faces:
        for f, _ in signed_boundary(g):
            if not f:
                continue
            if low_to_high.get(f) == g:
                source, target = f, g
            else:
                source, target = g, f
            outgoing[source].append(target)
            degree[target] += 1
            arrows += 1
    q = deque(f for f in faces if degree[f] == 0)
    seen = 0
    while q:
        f = q.popleft()
        seen += 1
        for g in outgoing[f]:
            degree[g] -= 1
            if degree[g] == 0:
                q.append(g)
    assert seen == len(faces), (seen, len(faces), 'matching cycle')
    return arrows


def morse_boundary_3_to_2(crit, low_to_high, high_to_low):
    crit_2 = [f for f in crit if f.bit_count() == 3]
    crit_3 = [f for f in crit if f.bit_count() == 4]
    assert len(crit_2) == 1
    c = crit_2[0]

    @lru_cache(None)
    def projection(f):
        # A 2-face paired upward is eliminated using its 3-coface boundary.
        # An upper-matched 2-face represents zero in the Morse quotient.
        if f in crit:
            assert f == c
            return 1
        if f in high_to_low:
            return 0
        t = low_to_high[f]
        assert t.bit_count() == 4
        boundary = tuple(signed_boundary(t))
        pivot = next(eps for face, eps in boundary if face == f)
        assert abs(pivot) == 1
        numerator = -sum(eps * projection(face)
                         for face, eps in boundary if face != f)
        assert numerator % pivot == 0
        return numerator // pivot

    coefficients = [sum(sign * projection(f) for f, sign in signed_boundary(c3))
                    for c3 in sorted(crit_3)]
    assert gcd(*coefficients) == 1
    witness = next((face, coefficient) for face, coefficient in zip(sorted(crit_3), coefficients)
                   if abs(coefficient) == 1)
    return dict(sorted(Counter(coefficients).items())), c, len(crit_3), witness


def f2_rank(vectors):
    pivots = {}
    for column in vectors:
        while column:
            pivot = column.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = column
                break
            column ^= pivots[pivot]
    return len(pivots)


def mod2_betti(faces):
    by_dim = {}
    for f in faces:
        by_dim.setdefault(f.bit_count() - 1, []).append(f)
    rank = {}
    for d in range(1, max(by_dim) + 1):
        target = {f: i for i, f in enumerate(by_dim[d - 1])}
        columns = []
        for t in by_dim[d]:
            col = 0
            for f, _ in signed_boundary(t):
                col ^= 1 << target[f]
            columns.append(col)
        rank[d] = f2_rank(columns)
    bettis = {str(d): len(by_dim[d]) - rank.get(d, 0) - rank.get(d + 1, 0)
              for d in sorted(by_dim)}
    f_vector = {str(d): len(fs) for d, fs in sorted(by_dim.items())}
    return f_vector, bettis, rank


def verify_graph(kind):
    adj = graph_adjacency(kind)
    check_graph(adj, kind)
    faces = faces_of_complex(adj)
    crit, pairs, reversed_pairs = matching(faces)
    assert 2 * len(pairs) + len(crit) == len(faces)
    arrows = acyclic_certificate(faces, pairs)
    coeffs, lone_face, num3, unit_witness = morse_boundary_3_to_2(crit, pairs, reversed_pairs)
    critical_by_dim = dict(sorted(Counter(f.bit_count() - 1 for f in crit).items()))
    assert set(critical_by_dim) == {0, 2, 3}
    assert critical_by_dim[0] == 1 and critical_by_dim[2] == 1
    f_vector, bettis, ranks = mod2_betti(faces)
    assert int(bettis['3']) == num3 - 1
    assert sum(int(n) for d, n in bettis.items() if d not in ('0', '3')) == 0
    assert int(bettis['0']) == 1
    return {
        'graph': kind,
        'vertices': N,
        'edges': 48,
        'connected_triples': 176,
        'total_subsets_checked': 1 << N,
        'augmented_f_vector': {'-1': 1, **f_vector},
        'nonempty_faces': len(faces),
        'morse_matching_pairs': len(pairs),
        'directed_hasse_incidences': arrows,
        'critical_cells': {str(k): v for k, v in critical_by_dim.items()},
        'critical_two_face_bitmask': lone_face,
        'morse_three_to_two_boundary_coefficients': {str(k): v for k, v in coeffs.items()},
        'morse_boundary_gcd': 1,
        'unit_morse_boundary_witness': {'three_face_bitmask': unit_witness[0],
                                        'degree': unit_witness[1]},
        'mod_two_boundary_ranks': {str(k): v for k, v in ranks.items()},
        'mod_two_betti': bettis,
        'integral_wedge_three_sphere_count': num3 - 1,
    }


def main():
    result = [verify_graph(kind) for kind in ('rook', 'shrikhande')]
    assert [x['integral_wedge_three_sphere_count'] for x in result] == [105, 57]
    assert result[0]['augmented_f_vector']['2'] == result[1]['augmented_f_vector']['2'] == 384
    print(json.dumps({'verification': 'SHRIKHANDE_ROOK_TWO_INDEPENDENCE_OK',
                      'results': result}, ensure_ascii=True, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
