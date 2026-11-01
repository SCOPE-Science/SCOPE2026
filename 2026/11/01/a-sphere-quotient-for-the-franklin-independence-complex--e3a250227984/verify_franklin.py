"""Exact finite certificate for a sphere quotient of the Franklin independence complex.

Usage: python3 verify_franklin.py franklin_collapse_certificate.json
Python standard library only. The algorithm reconstructs all source cells and
checks every quotient elementary collapse and all links of the residual surface.
"""
import collections
import functools
import itertools
import json
import sys


def graph():
    n = 12
    adjacency = [set() for _ in range(n)]
    for v in range(n):
        for w in ((v + 1) % n, (v - 1) % n,
                  (v + (5 if v % 2 == 0 else -5)) % n):
            adjacency[v].add(w)
            adjacency[w].add(v)
    assert all(len(x) == 3 for x in adjacency)
    assert sum(map(len, adjacency)) == 36
    return adjacency


def automorphisms(adj):
    n = len(adj)
    # Breadth-first vertex order accelerates exact adjacency-preserving backtracking.
    order = [0]
    head = 0
    while head < len(order):
        for w in sorted(adj[order[head]]):
            if w not in order:
                order.append(w)
        head += 1
    assert len(order) == n
    p = [-1] * n
    used = set()
    result = []

    def search(k):
        if k == n:
            result.append(tuple(p))
            return
        v = order[k]
        for w in range(n):
            if w in used or len(adj[v]) != len(adj[w]):
                continue
            if any((a in adj[v]) != (p[a] in adj[w])
                   for a in order[:k]):
                continue
            p[v] = w
            used.add(w)
            search(k + 1)
            used.remove(w)
            p[v] = -1

    search(0)
    assert len(result) == len(set(result)) == 48
    for p in result:
        assert all((v in adj[u]) == (p[v] in adj[p[u]])
                   for u in range(n) for v in range(n))
    return result


def independent_masks(adj):
    n = len(adj)
    bad = [sum(1 << j for j in adj[i]) for i in range(n)]
    faces = set()
    for mask in range(1, 1 << n):
        if all(not (mask & bad[i]) for i in range(n) if mask & (1 << i)):
            faces.add(mask)
    return faces


def chains_with_final_mask(mask):
    # Independently enumerate ordered set partitions of the final face.
    # The successive unions of blocks are exactly the strictly nested chains.
    def recur(remaining, current, chain):
        if not remaining:
            yield chain
            return
        nonempty_subset = remaining
        while nonempty_subset:
            next_face = current | nonempty_subset
            yield from recur(remaining ^ nonempty_subset,
                             next_face, chain + (next_face,))
            nonempty_subset = (nonempty_subset - 1) & remaining
    yield from recur(mask, 0, ())


def build_orbit_complex(adj, perms):
    faces = independent_masks(adj)
    assert len(faces) == 195
    assert collections.Counter(m.bit_count() for m in faces) == {
        1: 12, 2: 48, 3: 76, 4: 45, 5: 12, 6: 2
    }
    images = {m: tuple(sum(1 << p[i] for i in range(12)
                            if m & (1 << i)) for p in perms)
              for m in faces}

    @functools.lru_cache(None)
    def canonical(chain):
        return min(tuple(images[m][j] for m in chain)
                   for j in range(len(perms)))

    cells = set()
    for final_mask in faces:
        for chain in chains_with_final_mask(final_mask):
            cells.add(canonical(chain))
    dims = collections.Counter(len(c) - 1 for c in cells)
    assert [dims[d] for d in range(6)] == [16, 81, 180, 203, 120, 30]
    assert len(cells) == 630
    facets = {}
    all_subfaces = {}
    for c in cells:
        facets[c] = tuple(canonical(c[:j] + c[j + 1:])
                          for j in range(len(c))) if len(c) > 1 else ()
        assert len(set(facets[c])) == len(facets[c])
        all_subfaces[c] = {
            canonical(tuple(c[j] for j in range(len(c)) if mask & (1 << j)))
            for mask in range(1, (1 << len(c)) - 1)
        }
        assert all(x in cells for x in facets[c])
        assert all(x in cells for x in all_subfaces[c])
    return cells, facets, all_subfaces, canonical


def analyze_residual(active, facets, canonical):
    groups = {d: set(c for c in active if len(c) == d + 1)
              for d in range(6)}
    assert [len(groups[d]) for d in range(6)] == [7, 15, 10, 0, 0, 0]
    degree_edge = collections.Counter(f for c in groups[2] for f in facets[c])
    assert set(degree_edge) == groups[1]
    assert all(v == 2 for v in degree_edge.values())

    vertices = groups[0]
    vertex_incidence = collections.defaultdict(set)
    for e in groups[1]:
        for v in facets[e]:
            vertex_incidence[v].add(e)

    graph = {v: set() for v in vertices}
    for e in groups[1]:
        a, b = facets[e]
        assert a != b
        graph[a].add(b)
        graph[b].add(a)
    seen = set()
    stack = [next(iter(vertices))]
    while stack:
        v = stack.pop()
        if v not in seen:
            seen.add(v)
            stack.extend(graph[v] - seen)
    assert seen == vertices

    link_lengths = []
    for v in vertices:
        edge_nodes = vertex_incidence[v]
        neighbors = collections.defaultdict(list)
        for t in groups[2]:
            vset = {canonical((mask,)) for mask in t}
            if v not in vset:
                continue
            adjacent_edges = [e for e in facets[t] if e in edge_nodes]
            assert len(adjacent_edges) == 2
            a, b = adjacent_edges
            assert a != b
            neighbors[a].append(b)
            neighbors[b].append(a)
        assert set(neighbors) == edge_nodes
        assert all(len(neighbors[e]) == 2 for e in edge_nodes)
        visited = set()
        walk = [next(iter(edge_nodes))]
        while walk:
            x = walk.pop()
            if x not in visited:
                visited.add(x)
                walk.extend(neighbors[x])
        assert visited == edge_nodes
        link_lengths.append(len(edge_nodes))
    assert sorted(link_lengths) == [2, 2, 2, 4, 4, 6, 10]
    assert sum((-1)**d * len(groups[d]) for d in groups) == 2
    return sorted(link_lengths)


def verify(filename):
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
    assert data['graph'] == {'vertex_count': 12,
                             'lcf_jump_pattern': [5, -5],
                             'repeat_count': 6}
    adj = graph()
    perms = automorphisms(adj)

    # Independent signed-Lefschetz/Burnside check of the quotient Euler number.
    faces = independent_masks(adj)
    reduced_euler_traces = []
    for p in perms:
        total = -1
        for mask in faces:
            vertices = [i for i in range(12) if mask & (1 << i)]
            images = [p[i] for i in vertices]
            if set(images) != set(vertices):
                continue
            inversions = sum(images[i] > images[j]
                             for i in range(len(images))
                             for j in range(i + 1, len(images)))
            total += (-1) ** (len(vertices) - 1 + inversions)
        reduced_euler_traces.append(total)
    assert collections.Counter(reduced_euler_traces) == {
        4: 1, -2: 1, 0: 15, 1: 16, 2: 15
    }
    assert sum(reduced_euler_traces) == 48
    assert 1 + sum(reduced_euler_traces) // 48 == 2
    cells, facets, subfaces, canonical = build_orbit_complex(adj, perms)
    assert data['quotient_cell_counts_by_dimension'] == [16, 81, 180, 203, 120, 30]
    active = set(cells)
    assert len(data['collapse_pairs']) == 299
    for step in data['collapse_pairs']:
        low = tuple(step['free'])
        high = tuple(step['coface'])
        assert low in active and high in active
        assert len(high) == len(low) + 1
        assert low in facets[high]
        assert [c for c in active if low in subfaces[c]] == [high], (
            'not a geometrically free face', step)
        active.remove(low)
        active.remove(high)
    assert data['residual_cell_counts_by_dimension'] == [7, 15, 10, 0, 0, 0]
    for d in range(3):
        assert {tuple(c) for c in data['residual_cells'][str(d)]} == {
            c for c in active if len(c) == d + 1}
    assert sorted(data['residual_vertex_link_lengths']) == analyze_residual(
        active, facets, canonical)
    print('AUTOMORPHISMS=48; ORIGINAL_NONEMPTY_FACES=195; '
          'QUOTIENT_CELLS=630; VALID_COLLAPSES=299; '
          'RESIDUAL=(7,15,10); ALL_VERTEX_LINKS_CIRCULAR; '
          'EULER=2; CONNECTED=YES')
    print('FRANKLIN_QUOTIENT_SPHERE_VERIFY_OK')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 verify_franklin.py certificate.json')
    verify(sys.argv[1])
