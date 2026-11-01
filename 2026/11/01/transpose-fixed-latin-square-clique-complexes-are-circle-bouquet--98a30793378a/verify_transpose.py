"""Exact finite checks for row/column-interchange fixed-locus theorem.

No third-party imports. Run: python verify_transpose.py
Checks orbit graph from the original Latin-square adjacency, independent expected
classification, maximal faces (small cases), and mod-two reduced homology.
Finite checks corroborate but do not establish the unrestricted theorem.
"""
from itertools import combinations


def orbits(q):
    return sorted({tuple(sorted({(a, b), (b, a)}))
                   for a in range(q) for b in range(q)})


def adjacent(x, y):
    if x == y:
        return False
    return (x[0] == y[0] or x[1] == y[1]
            or (x[0] ^ x[1]) == (y[0] ^ y[1]))


def formula_edge(u, v):
    if len(u) == len(v) == 1:
        return True
    if len(u) == len(v) == 2:
        return (u[0][0] ^ u[0][1]) == (v[0][0] ^ v[0][1])
    if len(u) == 2:
        u, v = v, u
    return v[0][0] == u[0][0] or v[0][1] == u[0][0]


def verify_orbit_graph(q):
    os = orbits(q)
    assert len(os) == q * (q + 1) // 2
    edges = set()
    for i, j in combinations(range(len(os)), 2):
        # This side uses ONLY the original graph adjacency, independently
        # of formula_edge and of the classification.
        actual = all(adjacent(a, b) for a in os[i] for b in os[j])
        expected = formula_edge(os[i], os[j])
        assert actual == expected, (q, os[i], os[j])
        if actual:
            edges.add((i, j))
    return os, edges


def facets(q, os):
    D = tuple(i for i, o in enumerate(os) if len(o) == 1)
    assert len(D) == q
    fs = [D]
    for h in range(1, q):
        P = tuple(i for i, o in enumerate(os) if len(o) == 2
                  and (o[0][0] ^ o[0][1]) == h)
        assert len(P) == q // 2
        fs.append(P)
    for i, o in enumerate(os):
        if len(o) != 2:
            continue
        a, b = o[0]
        ds = [j for j, d in enumerate(os) if len(d) == 1
              and d[0][0] in (a, b)]
        assert len(ds) == 2
        fs.append(tuple(sorted([i] + ds)))
    return tuple(fs)


def binary_rank(columns):
    pivots = {}
    for v in columns:
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)



def explicit_collapse_to_graph(q, all_faces):
    """Find and verify a sequence of elementary free-face collapses."""
    F = {frozenset(face) for face in all_faces}
    original_count = len(F)
    pairs = 0
    while any(len(f) >= 3 for f in F):
        maximal = [f for f in F if not any(f < g for g in F)]
        pair = None
        for s in sorted(maximal, key=lambda f: (-len(f), sorted(f))):
            if len(s) < 3:
                continue
            for i in sorted(s):
                t = s - {i}
                if sum(t <= m for m in maximal) == 1:
                    pair = (s, t)
                    break
            if pair is not None:
                break
        assert pair is not None, 'A higher-dimensional cell has no free face'
        F.remove(pair[0]); F.remove(pair[1]); pairs += 1
    vertices = {next(iter(f)) for f in F if len(f) == 1}
    edges = [f for f in F if len(f) == 2]
    assert len(F) == original_count - 2 * pairs
    # Verify connectivity of the remaining graph.
    seen = {next(iter(vertices))}
    frontier = list(seen)
    while frontier:
        a = frontier.pop()
        for e in edges:
            if a not in e:
                continue
            for b in e:
                if b not in seen:
                    seen.add(b); frontier.append(b)
    assert seen == vertices
    assert len(edges) - len(vertices) + 1 == (q - 1) * (q // 2 - 1)
    return pairs, len(vertices), len(edges)

def test_homology(q, os, edges):
    fs = facets(q, os)
    # Verify every claimed facet is a clique. Check exhaustively that
    # every clique is contained in one of the claimed facets, using
    # an exhaustive graph-clique enumerator, independent of facet logic.
    for f in fs:
        assert all(tuple(sorted((a, b))) in edges for a, b in combinations(f, 2))
    exact_cliques = [tuple([v]) for v in range(len(os))]
    for k in range(1, q):
        nxt = []
        for c in exact_cliques:
            if len(c) != k:
                continue
            for v in range(c[-1] + 1, len(os)):
                if all((u, v) in edges for u in c):
                    nxt.append(c + (v,))
        exact_cliques.extend(nxt)
    expected_faces = set()
    for facet in fs:
        for k in range(1, len(facet) + 1):
            expected_faces.update(combinations(sorted(facet), k))
    assert set(exact_cliques) == expected_faces
    faces = [[] for _ in range(q)]
    for c in expected_faces:
        faces[len(c) - 1].append(c)
    for f in faces:
        f.sort()
    r = [0] * (q + 1)
    for k in range(1, q):
        lookup = {f: j for j, f in enumerate(faces[k - 1])}
        cols = []
        for f in faces[k]:
            cols.append(sum(1 << lookup[s] for s in combinations(f, k)))
        r[k] = binary_rank(cols)
    betti = {k: len(faces[k]) - r[k] - r[k + 1]
             for k in range(q) if faces[k]}
    betti[0] -= 1
    assert betti.get(1) == (q - 1) * (q // 2 - 1)
    assert all(v == 0 for k, v in betti.items() if k != 1)
    return betti, len(expected_faces), len(fs), explicit_collapse_to_graph(q, expected_faces)


def main():
    for q in (4, 8, 16, 32):
        os, es = verify_orbit_graph(q)
        assert len(facets(q, os)) == 1 + (q - 1) + q * (q - 1) // 2
        msg = 'q={} orbits={} orbit_edges={}'.format(q, len(os), len(es))
        if q <= 8:
            betti, nfaces, nfacets, collapse = test_homology(q, os, es)
            msg += ' faces={} facets={} reduced_mod2_betti={} collapse={}'.format(
                nfaces, nfacets, betti, collapse)
        print('CHECK_OK', msg)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
