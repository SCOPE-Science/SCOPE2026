"""Check the three-grain directed-cycle avalanche-complex classification.

Uses only Python's standard library. The proof is given separately;
finite computations here are independent checks, not an infinite proof.
"""
from collections import Counter
from itertools import combinations
from math import gcd


def predicted(n, face):
    a, b, c = (face[1]-face[0], face[2]-face[1], n-face[2]+face[0])
    g = gcd(n, a, b)
    N = n // g
    gaps = (a, b, c)
    if a == b == c:
        return (g, 0, 0, "filled triangles")
    if sorted(gaps) == [n//4, n//4, n//2] and n % 4 == 0:
        return (g, 0, g, "tetrahedral boundaries")
    if len(set(gaps)) == 2:
        return (g, g, 0, "one circle per component")
    if n % 2 == 0 and n//2 in gaps:
        return (g, g*(N//2+1), 0, "antipodal circles")
    return (g, g*(N+1), 0, "generic circles")


def orbit(n, face):
    return {tuple(sorted((v+t)%n for v in face)) for t in range(n)}


def dynamics(n, face):
    # An independent parallel-firing simulation, not a call to orbit().
    chips = [int(i in face) for i in range(n)]
    seen = set()
    output = set()
    while tuple(chips) not in seen:
        seen.add(tuple(chips))
        firing = {i for i, x in enumerate(chips) if x >= 1}
        output.add(tuple(sorted(firing)))
        new = [chips[i] - (i in firing) + ((i-1)%n in firing) for i in range(n)]
        chips = new
    return output


def graph_components(n, edges):
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    unseen = set(range(n))
    comps = []
    while unseen:
        root = min(unseen)
        stack = [root]
        unseen.remove(root)
        component = {root}
        while stack:
            for v in adj[stack.pop()]:
                if v in unseen:
                    unseen.remove(v)
                    component.add(v)
                    stack.append(v)
        comps.append(component)
    return comps


def rank_mod2(rows):
    pivots = {}
    for r in rows:
        while r:
            p = r.bit_length()-1
            if p in pivots:
                r ^= pivots[p]
            else:
                pivots[p] = r
                break
    return len(pivots)


def actual(n, face, check_rank=False):
    tris = orbit(n, face)
    # Check that the physical dynamics gives these *actual* firing sets.
    assert dynamics(n, face) == tris, (n, face, "dynamics differs")
    faces_of_tris = {t: {tuple(sorted(e)) for e in combinations(t, 2)} for t in tris}
    edges = set().union(*faces_of_tris.values())
    comps = graph_components(n, edges)
    incidence = Counter(e for pairs in faces_of_tris.values() for e in pairs)
    # Exhaust all triangle/free-edge cancellations to test the two-dimensional reduction.
    remaining = set(tris)
    while True:
        choice = None
        for tri in sorted(remaining):
            for edge in sorted(faces_of_tris[tri]):
                if incidence[edge] == 1:
                    choice = (tri, edge)
                    break
            if choice is not None:
                break
        if choice is None:
            break
        tri, edge = choice
        remaining.remove(tri)
        edges.remove(edge)
        for e in faces_of_tris[tri]:
            incidence[e] -= 1
    assert all(incidence[e] > 0 for t in remaining for e in faces_of_tris[t])
    if not remaining:
        b2 = 0
        b1 = len(edges) - n + len(comps)
    else:
        # Remaining triangles should be precisely disjoint tetrahedron boundaries.
        remaining_edges = set().union(*(faces_of_tris[t] for t in remaining))
        rcomps = graph_components(n, remaining_edges | edges)
        for component in rcomps:
            f = [tri for tri in remaining if set(tri) <= component]
            if f:
                assert len(component) == 4 and len(f) == 4
                assert set(f) == set(combinations(sorted(component), 3))
        b2 = len(remaining)//4
        b1 = 0
    if check_rank:
        edge_index = {e: i for i, e in enumerate(sorted(set().union(*faces_of_tris.values())))}
        col_rows = [sum(1 << edge_index[e] for e in faces_of_tris[t]) for t in tris]
        r2 = rank_mod2(col_rows)
        expected_b2 = len(tris) - r2
        expected_b1 = len(edge_index) - (n-len(comps)) - r2
        assert (expected_b1, expected_b2) == (b1, b2), (n, face, "mod2 disagreement")
    return (len(comps), b1, b2, len(tris), len(remaining))


def run(max_n=30):
    total = 0
    histogram = Counter()
    example = {}
    max_faces = 0
    for n in range(3, max_n+1):
        for face in combinations(range(n), 3):
            prediction = predicted(n, face)
            comps, b1, b2, nf, residual = actual(n, face, check_rank=(n<=15))
            assert (comps, b1, b2) == prediction[:3], (n, face, prediction, comps, b1, b2)
            kind = prediction[3]
            histogram[kind] += 1
            example.setdefault(kind, (n, face, comps, b1, b2))
            max_faces = max(max_faces, nf)
            total += 1
        if n in (4, 8, 12, 16, 20, 25, max_n):
            print(f"PASS n=3..{n}; binary three-grain configurations={total}")
    print("Complete classification verification, direct firing simulation, full simplicial collapses: PASS")
    print(f"All triples checked: {total}, largest distinct triangle orbit: {max_faces}")
    print("Exact mod-two boundary ranks checked for every triple with 3 <= n <= 15")
    for kind in sorted(histogram):
        print(f"{kind}: {histogram[kind]} cases; example={example[kind]}")

if __name__ == '__main__':
    run()
