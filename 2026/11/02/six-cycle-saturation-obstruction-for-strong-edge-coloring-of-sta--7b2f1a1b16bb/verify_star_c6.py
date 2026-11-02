"""Independent finite checks of an explicit strong edge coloring of K_{1,r} square C_6.

Run with Python 3. No third-party packages are needed.
"""

from itertools import combinations

# Rows: center (0), leaf 1, leaf 2. 0-based cycle edge index i means (i,i+1 mod 6).
SPOKES = ((0, 1), (2, 3), (4, 0), (7, 2), (5, 6), (8, 7))
CENTER = (5, 6, 8, 1, 3, 4)
LEAF1 = (7, 1, 3, 0, 2, 6)
LEAF2 = (8, 7, 5, 4, 0, 2)


def colored_edges(r):
    assert r >= 2
    result = []
    for i in range(6):
        j = (i + 1) % 6
        result.append(((0, i), (0, j), CENTER[i]))
        for a in range(1, r + 1):
            if a == 1:
                spoke = SPOKES[i][0]
                ring = LEAF1[i]
            elif a == 2:
                spoke = SPOKES[i][1]
                ring = LEAF2[i]
            else:
                spoke = 9 + 2 * (a - 3) + i % 2
                ring = LEAF1[i]
            result.append(((0, i), (a, i), spoke))
            result.append(((a, i), (a, j), ring))
    return result


def graph_edges(r):
    return {frozenset((x, y)) for x, y, _ in colored_edges(r)}


def check(r):
    given = colored_edges(r)
    underlying = graph_edges(r)
    assert len(given) == 6 + 12 * r
    assert len(underlying) == len(given)
    assert set(c for _, _, c in given) == set(range(2 * r + 5))
    conflicts = 0
    for (u, v, c), (x, y, d) in combinations(given, 2):
        share_or_adjacent = any(
            a == b or frozenset((a, b)) in underlying
            for a in (u, v) for b in (x, y)
        )
        if share_or_adjacent:
            conflicts += 1
            assert c != d, (r, u, v, x, y, c)
    return conflicts


def local_clique_check(r):
    # Verify all r*6 local cliques of 2r+4 mutually conflicting edges.
    given = colored_edges(r)
    underlying = graph_edges(r)
    def label(u, v):
        return next(c for x, y, c in given if {u, v} == {x, y})
    def actual_edge(u,v):
        return (u,v)
    def strongly_conflict(edge1,edge2):
        return any(x == y or frozenset((x,y)) in underlying for x in edge1 for y in edge2)
    for i in range(6):
        for a in range(1, r + 1):
            subset = []
            subset.extend(actual_edge((0, j), (b, j)) for j in (i, (i+1)%6) for b in range(1,r+1))
            subset.extend(actual_edge((0, j), (0, (j+1)%6)) for j in ((i-1)%6,i,(i+1)%6))
            subset.append(actual_edge((a,i),(a,(i+1)%6)))
            cols = [label(*edge) for edge in subset]
            assert len(cols) == 2*r+4
            assert len(set(cols)) == 2*r+4
            assert all(strongly_conflict(x,y) for x,y in combinations(subset,2))


def lower_obstruction_combinatorics():
    # A color appearing on any horizontal leaf edge is impossible if every
    # 2r+4-clique is saturated: 2S+3H+E=6, with H,E <=2.
    forbidden = lambda i: {(i + d) % 6 for d in (-1,0,1,2)}
    allowed_pairs = [(i,(i+3)%6) for i in range(3)]
    for i in range(6):
        for j in range(6):
            if j not in {(i-1)%6,i,(i+1)%6}:
                assert len(forbidden(i)|forbidden(j)) == 6
    for i,j in allowed_pairs:
        assert len(forbidden(i)|forbidden(j)) == 6
    for h in range(3):
        for e in range(3):
            for s in range(4):
                if 2*s+3*h+e != 6 or e == 0:
                    continue
                assert (h,e,s) in {(0,2,2),(1,1,1)}


if __name__ == '__main__':
    lower_obstruction_combinatorics()
    total = 0
    for r in range(2, 31):
        total += check(r)
        if r <= 7:
            local_clique_check(r)
    print('VERIFY_OK: saturation obstruction; 29 strong colorings (r=2..30);', total, 'conflict pairs; 6 clique checks per leaf for r<=7')
