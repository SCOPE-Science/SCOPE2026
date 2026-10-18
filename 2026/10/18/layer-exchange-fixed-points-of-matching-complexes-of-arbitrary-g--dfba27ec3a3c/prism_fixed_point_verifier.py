"""Independent finite checks for the layer-swap fixed matching theorem.

Run: python3 prism_fixed_point_verifier.py
No external packages are required. Finite checks supplement the all-graph proof.
"""
from itertools import combinations
from collections import deque, Counter


def perfect_matchings(n, base_edges):
    adj = {v: [] for v in range(n)}
    for u, v in base_edges:
        adj[u].append(v)
        adj[v].append(u)

    def rec(remaining):
        if not remaining:
            return [()]
        v = min(remaining)
        return [((v, w),) + tail
                for w in sorted(adj[v]) if w in remaining
                for tail in rec(remaining - {v, w})]

    return rec(set(range(n)))


def test_graph(n, base_edges, check_orbits=False):
    base_edges = tuple(sorted(base_edges))
    edges = tuple((v, n + v) for v in range(n)) + base_edges
    edge_num = len(edges)
    incident = [set(e) for e in edges]
    faces = {0}
    for idx in range(edge_num):
        bit = 1 << idx
        faces |= {f | bit for f in tuple(faces)
                  if all(incident[idx].isdisjoint(incident[j])
                         for j in range(idx) if f & (1 << j))}

    base_index = {e: n + i for i, e in enumerate(base_edges)}
    partner = {}
    unmatched = set()
    for face in faces:
        remaining = set(range(n))
        while remaining:
            v = min(remaining)
            selected = [w for w in sorted(remaining - {v})
                        if (min(v, w), max(v, w)) in base_index
                        and face & (1 << base_index[(min(v, w), max(v, w))])]
            if selected:
                if len(selected) != 1:
                    raise AssertionError('nonmatching core set')
                remaining.difference_update({v, selected[0]})
                continue
            other = face ^ (1 << v)
            if other not in faces:
                raise AssertionError('invalid pivot edge')
            partner[face] = other
            break
        else:
            unmatched.add(face)
    for face, other in partner.items():
        assert partner.get(other) == face
        assert abs(face.bit_count() - other.bit_count()) == 1
    assert len(faces) == 2 * (len(partner) // 2) + len(unmatched)
    pm = perfect_matchings(n, base_edges)
    expected_critical = {sum(1 << base_index[e] for e in m) for m in pm}
    assert unmatched == expected_critical

    # Every augmented Hasse cover directed: matched bottom to top,
    # unmatched top to bottom. Kahn traversal proves *global* acyclicity.
    outgoing = {f: [] for f in faces}
    indeg = {f: 0 for f in faces}
    cover_count = 0
    for face in faces:
        for idx in range(edge_num):
            bit = 1 << idx
            if face & bit:
                continue
            higher = face | bit
            if higher not in faces:
                continue
            cover_count += 1
            a, b = (face, higher) if partner.get(face) == higher else (higher, face)
            outgoing[a].append(b)
            indeg[b] += 1
    q = deque(f for f in faces if indeg[f] == 0)
    visited = 0
    while q:
        f = q.popleft()
        visited += 1
        for g in outgoing[f]:
            indeg[g] -= 1
            if indeg[g] == 0:
                q.append(g)
    assert visited == len(faces), 'directed cycle exists'

    if check_orbits:
        # Orbit of each base edge is both horizontal copies; an orbit of
        # a whisker is the corresponding fixed vertical prism rung.
        prism_orbits = []
        for v in range(n):
            prism_orbits.append((((v, 0), (v, 1)),))
        for u, v in base_edges:
            prism_orbits.append((((u, 0), (v, 0)), ((u, 1), (v, 1))))
        for mask in range(1 << edge_num):
            union = [e for j, orbit in enumerate(prism_orbits) if mask & (1 << j)
                     for e in orbit]
            selected_vertices = [v for e in union for v in e]
            is_invariant_matching = len(selected_vertices) == len(set(selected_vertices))
            assert (mask in faces) == is_invariant_matching
    return len(faces), len(partner) // 2, len(unmatched), cover_count


def main():
    total = 0
    total_covers = 0
    for n in range(5):
        all_edges = list(combinations(range(n), 2))
        for mask in range(1 << len(all_edges)):
            graph_edges = [e for i, e in enumerate(all_edges) if mask & (1 << i)]
            _, _, _, covers = test_graph(n, graph_edges, check_orbits=(n <= 4))
            total += 1
            total_covers += covers
    assert total == 76  # 1+1+2+8+64
    print(f'ALL_LABELED_GRAPHS_N_LE_4: {total} verified (orbit model, Morse pairing, global acyclicity, perfect matchings)')
    print(f'ALL_LABELED_GRAPHS_TOTAL_COVER_CHECKS: {total_covers}')
    for family in ['complete_6', 'cycle_6', 'complete_bipartite_3_3', 'path_7', 'edgeless_7', 'complete_7']:
        n = 7 if family.endswith('_7') else 6
        if family.startswith('complete_') and not 'bipartite' in family:
            E = list(combinations(range(n), 2))
        elif family.startswith('cycle_'):
            E = [(v, v + 1) for v in range(n - 1)] + [(0, n - 1)]
        elif 'bipartite' in family:
            E = [(u, v) for u in range(3) for v in range(3, 6)]
        elif family.startswith('path_'):
            E = [(v, v + 1) for v in range(n - 1)]
        else:
            E = []
        faces, pairs, crit, covers = test_graph(n, E)
        print(f'{family}: faces={faces}, pairs={pairs}, critical={crit}, covers={covers}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
