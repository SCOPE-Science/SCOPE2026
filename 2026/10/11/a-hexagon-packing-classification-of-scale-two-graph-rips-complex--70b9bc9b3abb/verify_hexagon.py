"""Reproducible finite-case checks of graph-distance Rips complexes.

No external packages. Run: python3 verify_hexagon.py
Checks, not a substitute for the all-graph proof.
"""
from itertools import combinations
from collections import deque


def graph(edges):
    vertices = set()
    for u, v in edges:
        if u == v:
            raise ValueError('loops are excluded')
        vertices.update((u, v))
    vertices = sorted(vertices)
    adj = {v: set() for v in vertices}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def cycle(n):
    return [(i, (i + 1) % n) for i in range(n)]


def attached_cycle(a, b, mode='vertex'):
    edges = cycle(a)
    if mode == 'vertex':
        label = {0: 0}
        label.update({i: a + i - 1 for i in range(1, b)})
    elif mode == 'bridge':
        label = {i: a + i for i in range(b)}
        edges.append((0, a))
    else:
        raise ValueError(mode)
    return edges + [(label[i], label[(i + 1) % b]) for i in range(b)]


def theta(a, b, c):
    edges = []
    next_label = 2
    for length in (a, b, c):
        previous = 0
        for _ in range(length - 1):
            edges.append((previous, next_label))
            previous = next_label
            next_label += 1
        edges.append((previous, 1))
    return edges


def shortest(adj):
    output = {}
    for source in adj:
        d = {source: 0}
        q = deque([source])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if w not in d:
                    d[w] = d[v] + 1
                    q.append(w)
        assert len(d) == len(adj), 'expected connected example'
        output[source] = d
    return output


def simple_six_cycles(adj):
    found = set()
    for start in adj:
        def extend(path):
            if len(path) == 6:
                if start in adj[path[-1]]:
                    edges = frozenset(frozenset((path[i], path[(i + 1) % 6]))
                                      for i in range(6))
                    found.add(edges)
                return
            for w in adj[path[-1]]:
                if w not in path:
                    extend(path + [w])
        extend([start])
    return found


def girth(adj):
    best = 10 ** 9
    for root in adj:
        dist = {root: 0}
        parent = {root: None}
        q = deque([root])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    parent[w] = v
                    q.append(w)
                elif parent[v] != w:
                    best = min(best, dist[w] + dist[v] + 1)
    return best


def all_rips_faces(adj, d):
    vertices = sorted(adj)
    all_faces = set()
    # Building cliques by extensions avoids enumerating the full power set.
    def walk(current, available):
        for i, v in enumerate(available):
            new_face = frozenset(current | {v})
            all_faces.add(new_face)
            walk(new_face, [w for w in available[i + 1:] if d[v][w] <= 2])
    walk(frozenset(), vertices)
    return all_faces


def central_faces(adj):
    faces = set()
    for c in adj:
        closed = sorted(adj[c] | {c})
        for r in range(1, len(closed) + 1):
            faces.update(frozenset(t) for t in combinations(closed, r))
    return faces


def gf2_rank(columns):
    basis = {}
    for x in columns:
        while x:
            p = x.bit_length() - 1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p] = x
                break
    return len(basis)


def reduced_betti(faces):
    dims = sorted({len(f) for f in faces})
    by_size = {size: sorted((tuple(sorted(f)) for f in faces if len(f) == size))
               for size in dims}
    ranks = {}
    for size in dims:
        if size <= 1:
            continue
        row = {f: i for i, f in enumerate(by_size[size - 1])}
        columns = []
        for face in by_size[size]:
            mask = 0
            for sub in combinations(face, size - 1):
                mask ^= 1 << row[sub]
            columns.append(mask)
        ranks[size] = gf2_rank(columns)
    out = {}
    for size in dims:
        rank_down = 1 if size == 1 else ranks.get(size, 0)
        rank_up = ranks.get(size + 1, 0)
        out[size - 1] = len(by_size[size]) - rank_down - rank_up
    return out


def verify_example(name, edges):
    adj = graph(edges)
    assert girth(adj) >= 6, name
    d = shortest(adj)
    hexes = simple_six_cycles(adj)
    used = set()
    for hexagon in hexes:
        assert used.isdisjoint(hexagon), name + ': hexagons not edge-disjoint'
        used.update(hexagon)
    h = len(hexes)
    beta = sum(map(len, adj.values())) // 2 - len(adj) + 1
    assert 0 <= h <= beta
    rips = all_rips_faces(adj, d)
    B = central_faces(adj)
    assert B <= rips
    excluded = rips - B
    # A centered triple is a triple in a closed graph neighborhood.
    # Two alternating triples occur for each hexagon, no other non-centered faces.
    assert all(len(f) == 3 for f in excluded), (name, excluded)
    expected = set()
    for hexagon in hexes:
        neighbor = {}
        for pair in hexagon:
            u, v = tuple(pair)
            neighbor.setdefault(u, set()).add(v)
            neighbor.setdefault(v, set()).add(u)
        for start in neighbor:
            q = [start]
            previous = None
            while len(q) < 6:
                nxt = next(x for x in neighbor[q[-1]] if x != previous)
                previous = q[-1]
                q.append(nxt)
            expected.add(frozenset((q[0], q[2], q[4])))
    assert excluded == expected, (name, len(excluded), len(expected))
    # Independently certify a complete elementary collapse B -> G.
    work = set(B)
    for center in sorted(adj):
        nn = sorted(adj[center])
        for k in range(len(nn), 1, -1):
            for vertices in combinations(nn, k):
                smaller = frozenset(vertices)
                bigger = smaller | {center}
                assert smaller in work and bigger in work
                assert not any(smaller < other and other != bigger
                               for other in work), (name, center, smaller)
                work.remove(smaller)
                work.remove(bigger)
    target = {frozenset((v,)) for v in adj}
    target |= {frozenset((u, v)) for u in adj for v in adj[u]}
    assert work == target, (name, 'collapse residue', work ^ target)
    homology = reduced_betti(rips)
    assert homology.get(0, 0) == 0, (name, homology)
    assert homology.get(1, 0) == beta - h, (name, homology)
    assert homology.get(2, 0) == h, (name, homology)
    assert all(k <= 2 or v == 0 for k, v in homology.items())
    print('%s: vertices=%d edges=%d hexagons=%d beta=%d noncentral=%d GF2=%s'
          % (name, len(adj), sum(map(len, adj.values())) // 2,
             h, beta, len(excluded), homology))


def main():
    examples = [
        ('single C6', cycle(6)),
        ('C6 and C6 at a vertex', attached_cycle(6, 6, 'vertex')),
        ('C6 and C7 at a vertex', attached_cycle(6, 7, 'vertex')),
        ('C6 and C8 joined by a bridge', attached_cycle(6, 8, 'bridge')),
        ('C6 and C6 joined by a bridge', attached_cycle(6, 6, 'bridge')),
        ('theta with path lengths 3,3,4', theta(3, 3, 4)),
        ('theta with path lengths 3,3,5', theta(3, 3, 5)),
        ('theta with path lengths 3,4,5', theta(3, 4, 5)),
        ('two long cycles', attached_cycle(8, 9, 'vertex')),
    ]
    for name, edges in examples:
        verify_example(name, edges)
    # A boundary counterexample to extending the packing formula without
    # edge-disjointness: three 6-cycles share paths and a new tetrahedron appears.
    bad = graph(theta(3, 3, 3))
    bad_hexes = simple_six_cycles(bad)
    assert girth(bad) == 6 and len(bad_hexes) == 3
    assert any(not a.isdisjoint(b) for a, b in combinations(bad_hexes, 2))
    noncentral = all_rips_faces(bad, shortest(bad)) - central_faces(bad)
    assert any(len(face) == 4 for face in noncentral)
    print('overlapping-hexagon boundary: three overlapping cycles; noncentered tetrahedra present')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
