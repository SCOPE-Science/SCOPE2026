#!/usr/bin/env python3
"""Reproduce integral discrete-Morse certificates for the Franklin graph."""
from collections import Counter, deque
from functools import lru_cache


def graph_edges():
    n = 12
    cycle = {tuple(sorted((i, (i + 1) % n))) for i in range(n)}
    chords = {tuple(sorted((i, (i + (5 if i % 2 == 0 else -5)) % n)))
              for i in range(n)}
    edges = tuple(sorted(cycle | chords))
    assert len(edges) == 18
    degree = Counter(v for e in edges for v in e)
    assert len(degree) == 12 and set(degree.values()) == {3}
    return edges


def enumerate_matchings(edges):
    masks = [sum(1 << v for v in edge) for edge in edges]
    out = {0}
    def extend(first, used, face):
        for i in range(first, len(edges)):
            if masks[i] & used:
                continue
            added = face | (1 << i)
            assert added not in out
            out.add(added)
            extend(i + 1, used | masks[i], added)
    extend(0, 0, 0)
    return out


def toggle_matching(faces, edge_count):
    unpaired = set(faces)
    pairs = []
    for i in range(edge_count):
        bit = 1 << i
        matches = [(f, f | bit) for f in sorted(unpaired)
                   if not (f & bit) and (f | bit) in unpaired]
        for lo, hi in matches:
            unpaired.remove(lo)
            unpaired.remove(hi)
        pairs.extend(matches)
    empty_pair = [p for p in pairs if p[0] == 0]
    assert len(empty_pair) == 1
    matched = [p for p in pairs if p[0] != 0]
    critical = set(unpaired) | {empty_pair[0][1]}
    assert 0 not in critical
    return matched, critical


def boundary(face):
    """Signed simplicial boundary with edge labels in ascending order."""
    vertices = [i for i in range(face.bit_length()) if face & (1 << i)]
    return [(face ^ (1 << i), -1 if j % 2 else 1)
            for j, i in enumerate(vertices)]


def acyclic_incidence_count(faces, matched):
    nonempty = faces - {0}
    oriented_up = set(matched)
    adj = {f: [] for f in nonempty}
    indegree = {f: 0 for f in nonempty}
    incidences = 0
    for hi in nonempty:
        for lo, _ in boundary(hi):
            if not lo:
                continue
            src, dst = (lo, hi) if (lo, hi) in oriented_up else (hi, lo)
            adj[src].append(dst)
            indegree[dst] += 1
            incidences += 1
    queue = deque(f for f, d in indegree.items() if d == 0)
    visited = 0
    while queue:
        f = queue.popleft()
        visited += 1
        for nxt in adj[f]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    assert visited == len(nonempty), (visited, len(nonempty))
    return incidences


def critical_profile(critical):
    return dict(sorted(Counter(f.bit_count() - 1 for f in critical).items()))


def degree_matrix(matched, critical, low_dim):
    up = dict(matched)
    down = {hi: lo for lo, hi in matched}
    low = sorted(c for c in critical if c.bit_count() == low_dim + 1)
    high = sorted(c for c in critical if c.bit_count() == low_dim + 2)

    @lru_cache(None)
    def reduce_lower(face):
        if face in critical:
            return {face: 1}
        if face in down:
            return {}
        assert face in up
        upper = up[face]
        terms = dict(boundary(upper))
        pivot = terms[face]
        assert pivot in (-1, 1)
        output = Counter()
        for other, coeff in terms.items():
            if other == face:
                continue
            for target, contribution in reduce_lower(other).items():
                output[target] -= pivot * coeff * contribution
        return {f: c for f, c in output.items() if c}

    columns = []
    for cell in high:
        output = Counter()
        for face, incidence in boundary(cell):
            for target, coeff in reduce_lower(face).items():
                output[target] += incidence * coeff
        columns.append(tuple(output.get(face, 0) for face in low))
    return low, high, columns


def automorphisms(edges):
    adj = {v: set() for v in range(12)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    # Deterministic BFS-based vertex order accelerates adjacency pruning.
    order = [0]
    for a in order:
        for v in sorted(adj[a]):
            if v not in order:
                order.append(v)
    assert len(order) == 12
    out = []
    def rec(pos, image, used):
        if pos == len(order):
            out.append(image.copy())
            return
        src = order[pos]
        for tgt in range(12):
            if tgt in used:
                continue
            if all((q in adj[src]) == (image[q] in adj[tgt]) for q in image):
                image[src] = tgt
                used.add(tgt)
                rec(pos + 1, image, used)
                used.remove(tgt)
                del image[src]
    rec(0, {}, set())
    return out


def main():
    edges = graph_edges()
    a_edge, b_edge = (0, 1), (0, 5)
    autos = automorphisms(edges)
    assert len(autos) == 48
    orbit_a = {tuple(sorted((a[0], a[1]))) for a in
               ((p[0], p[1]) for p in autos)}
    orbit_b = {tuple(sorted((p[0], p[5]))) for p in autos}
    assert len(orbit_a) == 6 and len(orbit_b) == 12
    assert orbit_a.isdisjoint(orbit_b) and orbit_a | orbit_b == set(edges)
    assert orbit_a == {(2 * j, 2 * j + 1) for j in range(6)}
    print('graph=Franklin vertices=12 edges=18 automorphisms=48 edge_orbits=6,12')

    expected = {
        'full': (1091, 539, 3942, {0: 1, 3: 12}),
        'A-deletion': (875, 433, 3105, {0: 1, 3: 8}),
        'A-link': (215, 105, 609, {0: 1, 2: 4}),
        'B-deletion': (869, 428, 3075, {0: 1, 2: 1, 3: 11}),
        'B-link': (221, 109, 633, {0: 1, 2: 2}),
    }
    complexes = [
        ('full', edges),
        ('A-deletion', tuple(e for e in edges if e != a_edge)),
        ('A-link', tuple(e for e in edges if not(set(e) & set(a_edge)))),
        ('B-deletion', tuple(e for e in edges if e != b_edge)),
        ('B-link', tuple(e for e in edges if not(set(e) & set(b_edge)))),
    ]
    for name, chosen in complexes:
        faces = enumerate_matchings(chosen)
        matched, critical = toggle_matching(faces, len(chosen))
        data = len(faces)-1, len(matched), acyclic_incidence_count(faces, matched), critical_profile(critical)
        assert data == expected[name], (name, data)
        print(f'{name}: nonempty_faces={data[0]} pairs={data[1]} incidences={data[2]} critical={data[3]}')
        if name == 'B-deletion':
            low, high, matrix = degree_matrix(matched, critical, 2)
            assert len(low) == 1 and len(high) == 11
            vector = tuple(col[0] for col in matrix)
            assert len(vector) == 11 and any(abs(x) == 1 for x in vector)
            assert set(vector) <= {-1, 0, 1}
            print('B-deletion degree_3_to_2=',vector, 'smith_gcd=1')
    print('INTEGRAL_MORSE_VERIFIED')

if __name__ == '__main__':
    main()
