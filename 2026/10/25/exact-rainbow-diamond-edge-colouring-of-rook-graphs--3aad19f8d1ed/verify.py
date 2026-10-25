"""Finite checks for exact rainbow-diamond edge-colourings of rook graphs.

No external packages are required. This checks the combinatorial construction
against the original edge-adjacency and diamond constraints.
"""
from itertools import combinations


def disjoint_pair_permutation(n):
    pairs = list(combinations(range(n), 2))
    neighbors = {p: [q for q in pairs if set(p).isdisjoint(q)] for p in pairs}
    mate_to_left = {}

    def augment(p, seen):
        for q in neighbors[p]:
            if q in seen:
                continue
            seen.add(q)
            if q not in mate_to_left or augment(mate_to_left[q], seen):
                mate_to_left[q] = p
                return True
        return False

    for p in pairs:
        assert augment(p, set()), ('missing perfect matching', n, p)
    result = {left: right for right, left in mate_to_left.items()}
    assert len(result) == len(pairs)
    assert all(set(p).isdisjoint(q) for p, q in result.items())
    return result


def edges(m, n):
    ans = []
    for i in range(m):
        for a, b in combinations(range(n), 2):
            ans.append(tuple(sorted(((i, a), (i, b)))))
    for a in range(n):
        for i, j in combinations(range(m), 2):
            ans.append(tuple(sorted(((i, a), (j, a)))))
    return ans


def coloring(m, n):
    pair_map = disjoint_pair_permutation(n)
    inverse = {image: preimage for preimage, image in pair_map.items()}
    result = {}
    for i in range(m):
        for a, b in combinations(range(n), 2):
            edge = tuple(sorted(((i, a), (i, b))))
            result[edge] = tuple(sorted(((a + i) % n, (b + i) % n)))
    for a in range(n):
        for i, j in combinations(range(m), 2):
            preimage = inverse[(i, j)]
            edge = tuple(sorted(((i, a), (j, a))))
            result[edge] = tuple(sorted(((x + a) % n for x in preimage)))
    return result


def rook_adjacent(u, v):
    return (u[0] == v[0]) != (u[1] == v[1])


def independent_check(m, n, colors):
    es = edges(m, n)
    assert set(colors) == set(es)
    palette = {c for c in colors.values()}
    assert len(palette) == n * (n - 1) // 2
    for e, f in combinations(es, 2):
        if colors[e] != colors[f]:
            continue
        assert set(e).isdisjoint(f), ('improper edge-colouring', m, n, e, f)
        crossing = sum(rook_adjacent(u, v) for u in e for v in f)
        assert crossing <= 2, ('nonrainbow diamond', m, n, e, f)


def brute_four_vertices(m, n, colors):
    # Directly inspect each four-vertex graph: if it has at least five edges,
    # any five of its edges form a diamond, so all six edges (if present)
    # must carry distinct colours.
    verts = [(i, a) for i in range(m) for a in range(n)]
    tested = 0
    for quad in combinations(verts, 4):
        present = [tuple(sorted((u, v))) for u, v in combinations(quad, 2)
                   if rook_adjacent(u, v)]
        if len(present) >= 5:
            assert len({colors[e] for e in present}) == len(present), (m, n, quad)
            tested += 1
    return tested


def check_small():
    # The 2-by-2 and 2-by-3 graph have 2- and 3-edge-colourings.
    # In the 3-by-3 graph, a five-colour certificate is verified directly.
    e22 = edges(2, 2)
    # For C4, simply color the two horizontal edges 0 and the two vertical 1.
    c22 = {e: 0 if e[0][0] == e[1][0] else 1 for e in e22}
    assert len(set(c22.values())) == 2
    for e, f in combinations(e22, 2):
        if set(e).intersection(f):
            assert c22[e] != c22[f]

    e23 = edges(2, 3)
    c23 = {}
    for e in e23:
        if e[0][0] == e[1][0]:
            c23[e] = (e[0][1] + e[1][1]) % 3
        else:
            c23[e] = (2 * e[0][1]) % 3
    assert len(set(c23.values())) == 3
    for e, f in combinations(e23, 2):
        if set(e).intersection(f):
            assert c23[e] != c23[f]

    e33 = edges(3, 3)
    # Certificate in canonical edge order: row edges first, then column edges.
    witness = [0, 3, 1, 2, 3, 0, 3, 4, 2,
               1, 2, 0, 3, 4, 1, 2, 0, 1]
    c33 = dict(zip(e33, witness))
    assert len(set(c33.values())) == 5
    for e, f in combinations(e33, 2):
        if set(e).intersection(f):
            assert c33[e] != c33[f], (e, f)
    # The graph has nine vertices and eighteen edges, so four colours cannot
    # suffice: a matching has at most four edges, hence 4*4<18.
    assert len(e33) == 18 and 4 * (len({v for e in e33 for v in e}) // 2) < 18


def main():
    check_small()
    checked = 0
    diamonds = 0
    for n in range(4, 10):
        for m in range(2, n + 1):
            c = coloring(m, n)
            independent_check(m, n, c)
            checked += 1
            if n <= 6:
                diamonds += brute_four_vertices(m, n, c)
    print('VERIFY_OK small_cases=3 rook_instances=%d complete_quadruple_diamonds=%d max_column_order=9' % (checked, diamonds))


if __name__ == '__main__':
    main()
