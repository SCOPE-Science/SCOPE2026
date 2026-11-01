"""Exact finite combinatorial certificate for a reflection-fixed matching complex.

Run with Python 3; no third-party packages are required.
The script reconstructs the symmetry orbit graph and the complete face poset,
checks every elementary Morse pairing, and tests acyclicity on every cover.
"""

from collections import Counter, deque

ORDERS = {
    1: (4, 3, 2, 1, 0),
    2: tuple(range(9, -1, -1)),
    3: (7, 1, 0, 14, 9, 3, 6, 4, 13, 8, 5, 10, 12, 11, 2),
    4: (2, 11, 10, 1, 4, 18, 0, 17, 12, 19, 8, 9, 5, 16, 13, 15, 3, 6, 14, 7),
    5: tuple(range(24, -1, -1)),
}
EXPECTED_CRITICAL = {
    1: {0: 1},
    2: {0: 1, 2: 1},
    3: {0: 1, 3: 1},
    4: {0: 1, 4: 4},
    5: {0: 1, 5: 11},
}


def normalized_edge(u, v):
    assert u != v
    return tuple(sorted((u, v)))


def original_edges(n):
    edges = []
    for c in range(n):
        for r in range(2):
            edges.append(normalized_edge((r, c), (r + 1, c)))
        if c + 1 < n:
            for r in range(3):
                edges.append(normalized_edge((r, c), (r, c + 1)))
    return set(edges)


def reflecting_edge(edge, n):
    return normalized_edge(*((r, n - 1 - c) for r, c in edge))


def half_grid_with_terminal_leaves(m):
    edges = []
    for c in range(m):
        for r in range(2):
            edges.append(normalized_edge(3 * c + r, 3 * c + r + 1))
        if c < m - 1:
            for r in range(3):
                edges.append(normalized_edge(3 * c + r, 3 * (c + 1) + r))
        else:
            for r in range(3):
                edges.append(normalized_edge(3 * c + r, 3 * m + r))
    return edges


def endpoint_label(v, m):
    if v < 3 * m:
        return (v % 3, v // 3)
    return (v - 3 * m, m)


def check_orbit_graph(m, edges):
    n = 2 * m
    all_edges = original_edges(n)
    remaining = set(all_edges)
    genuine_orbits = set()
    while remaining:
        e = next(iter(remaining))
        orbit = frozenset((e, reflecting_edge(e, n)))
        assert orbit <= remaining
        remaining -= orbit
        vertices = [u for edge in orbit for u in edge]
        assert len(vertices) == len(set(vertices)), 'inadmissible orbit'
        genuine_orbits.add(orbit)
    mapped = []
    for a, b in edges:
        representative = normalized_edge(endpoint_label(a, m), endpoint_label(b, m))
        assert representative in all_edges
        orbit = frozenset((representative, reflecting_edge(representative, n)))
        mapped.append(orbit)
    assert set(mapped) == genuine_orbits
    assert len(set(mapped)) == len(edges) == 5 * m
    for i in range(len(edges)):
        for j in range(i):
            overlap_half = bool(set(edges[i]) & set(edges[j]))
            vertices_i = set(u for e in mapped[i] for u in e)
            vertices_j = set(u for e in mapped[j] for u in e)
            overlap_original = bool(vertices_i & vertices_j)
            assert overlap_half == overlap_original, (m, i, j)


def all_matching_faces(edges):
    edge_masks = tuple(sum(1 << v for v in e) for e in edges)
    out = []

    def visit(first, used_vertices, face):
        if face:
            out.append(face)
        for j in range(first, len(edges)):
            if edge_masks[j] & used_vertices:
                continue
            visit(j + 1, used_vertices | edge_masks[j], face | (1 << j))

    visit(0, 0, 0)
    assert len(out) == len(set(out))
    return out


def complete_morse_matching(faces, edge_order):
    remaining = set(faces)
    matched_up = set()
    pairs = set()
    for i in edge_order:
        b = 1 << i
        for face in faces:
            larger = face | b
            if not face & b and face in remaining and larger in remaining:
                assert larger.bit_count() == face.bit_count() + 1
                remaining.remove(face)
                remaining.remove(larger)
                matched_up.add((face, larger))
                pairs.add(face)
                pairs.add(larger)
    assert pairs.isdisjoint(remaining)
    assert len(pairs) + len(remaining) == len(faces)
    return remaining, matched_up


def check_acyclic(faces, matched_up):
    """Orient unmatched covers downward, matched covers upward; check full DAG."""
    nodes = set(faces)
    outgoing = {f: [] for f in faces}
    indegree = {f: 0 for f in faces}
    directed_covers = 0
    for greater in faces:
        bitset = greater
        while bitset:
            b = bitset & (-bitset)
            bitset -= b
            lesser = greater ^ b
            if not lesser:  # the empty face is excluded from the Morse poset
                continue
            assert lesser in nodes
            if (lesser, greater) in matched_up:
                frm, to = lesser, greater
            else:
                frm, to = greater, lesser
            outgoing[frm].append(to)
            indegree[to] += 1
            directed_covers += 1
    queue = deque(f for f in faces if indegree[f] == 0)
    reached = 0
    while queue:
        f = queue.popleft()
        reached += 1
        for g in outgoing[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                queue.append(g)
    assert reached == len(faces), (reached, len(faces))
    return directed_covers


def main():
    for m in range(1, 6):
        edges = half_grid_with_terminal_leaves(m)
        check_orbit_graph(m, edges)
        assert sorted(ORDERS[m]) == list(range(len(edges)))
        faces = all_matching_faces(edges)
        critical, pair_set = complete_morse_matching(faces, ORDERS[m])
        profile = dict(Counter(f.bit_count() - 1 for f in critical))
        assert profile == EXPECTED_CRITICAL[m], (m, profile)
        cover_count = check_acyclic(faces, pair_set)
        print('m=%d n=%d vertices=%d faces=%d covers=%d pairs=%d critical=%s' % (
            m, 2 * m, len(edges), len(faces), cover_count,
            len(pair_set), profile))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
