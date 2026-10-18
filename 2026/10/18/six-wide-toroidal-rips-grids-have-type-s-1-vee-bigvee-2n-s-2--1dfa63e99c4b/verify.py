"""Standalone exact finite tests for scale-two Rips complexes of thin torus grids.

Run: python3 verify_torus_widths.py
No third-party modules required. The all-parameter proof is in RESULT.md.
"""
from itertools import combinations


def check(m, n):
    assert m == 6 and 7 <= n <= 11
    def v(i, j):
        return (i % m) * n + (j % n)
    def tup(s):
        return tuple(sorted(s))
    def faces(simplices):
        return {f for s in simplices for k in range(1, len(s) + 1)
                for f in combinations(sorted(s), k)}

    diam = {}
    squares = {}
    for i in range(m):
        for j in range(n):
            diam[i, j] = tup((v(i, j), v(i - 1, j), v(i + 1, j),
                               v(i, j - 1), v(i, j + 1)))
            squares[i, j] = tup((v(i, j), v(i + 1, j),
                                  v(i, j + 1), v(i + 1, j + 1)))
    extras = ([tup(v(i, j) for i in range(5)) for j in range(n)]
              if m == 5 else
              [tup(v(i, j) for i in range(parity, 6, 2))
               for j in range(n) for parity in (0, 1)])
    X = faces(list(diam.values()) + list(squares.values()))
    K = faces(list(diam.values()) + list(squares.values()) + extras)

    # Independent brute-force enumeration of every metric clique.
    vertices = list(range(m * n))
    adjacency = {x: set() for x in vertices}
    for x in vertices:
        a, b = divmod(x, n)
        for y in vertices:
            c, d = divmod(y, n)
            if x != y and (min(abs(a-c), m-abs(a-c)) +
                           min(abs(b-d), n-abs(b-d)) <= 2):
                adjacency[x].add(y)
    cliques = set()
    def enumerate_cliques(prefix, candidates):
        for idx, x in enumerate(candidates):
            nxt = prefix + (x,)
            cliques.add(nxt)
            enumerate_cliques(nxt, [y for y in candidates[idx+1:]
                                    if y in adjacency[x]])
    enumerate_cliques((), vertices)
    assert cliques == K, ('facet classification failure', m, n)

    # Exact elementary collapse of X to the canonical triangulated torus.
    remaining = set(X)
    pair_count = 0
    def collapse(low, high):
        nonlocal pair_count
        lo, hi = tup(low), tup(high)
        assert lo in remaining and hi in remaining
        assert len(hi) == len(lo) + 1 and set(lo) < set(hi)
        cofaces = [f for f in remaining if len(f) > len(lo)
                   and set(lo) <= set(f)]
        assert cofaces == [hi], ('non-free face', m, n, lo, cofaces)
        remaining.remove(lo)
        remaining.remove(hi)
        pair_count += 1

    for (i, j), D in sorted(diam.items()):
        center = v(i, j)
        NS = {v(i-1, j), v(i+1, j)}
        EW = sorted((v(i, j-1), v(i, j+1)))
        for subset in (EW, EW[:1], EW[1:], []):
            low = NS | set(subset)
            collapse(low, low | {center})
        for subset in ([a] for a in sorted(NS)):
            low = set(EW) | set(subset)
            collapse(low, low | {center})
        collapse(EW, set(EW) | {center})

    for (i, j), Q in sorted(squares.items()):
        a, b, c, d = (v(i, j), v(i+1, j),
                      v(i, j+1), v(i+1, j+1))
        collapse((a, b, c), (a, b, c, d))
        collapse((b, c), (b, c, d))
    torus = faces(
        [[v(i,j), v(i+1,j), v(i+1,j+1)]
         for i in range(m) for j in range(n)] +
        [[v(i,j), v(i,j+1), v(i+1,j+1)]
         for i in range(m) for j in range(n)])
    assert remaining == torus
    assert pair_count == 9 * m * n

    if m == 5:
        for j, E in enumerate(extras):
            intersection = faces([E]) & X
            assert [sum(len(f) == k for f in intersection)
                    for k in range(1, 5)] == [5, 10, 5, 0]
            assert all(tup((v(i,j), v(i+1,j))) in intersection
                       for i in range(5))
    else:
        for E in extras:
            intersection = faces([E]) & X
            assert intersection == faces(combinations(E, 2))

    # Independent mod-two homology of metric complex (not used for proof).
    by_size = {k: sorted(f for f in cliques if len(f) == k)
               for k in range(1, max(map(len, cliques))+1)}
    ranks = {1: 0}
    for k in range(2, max(by_size) + 1):
        lower_index = {face: idx for idx, face in enumerate(by_size[k-1])}
        pivots = {}
        for face in by_size[k]:
            col = 0
            for missing in range(k):
                lower = face[:missing] + face[missing+1:]
                col ^= 1 << lower_index[lower]
            while col:
                pivot = col.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot] = col
                    break
                col ^= pivots[pivot]
        ranks[k] = len(pivots)
    betti = {k-1: len(by_size[k]) - ranks[k] - ranks.get(k+1, 0)
             for k in by_size}
    assert betti[0] == 1 and betti[1] == 1
    assert betti[2] == (m-4)*n
    assert all(betti[k] == 0 for k in betti if k >= 3)
    print('PASS m=%d n=%d faces=%d base=%d pairs=%d H1_F2=%d H2_F2=%d' %
          (m, n, len(K), len(X), pair_count, betti[1], betti[2]))


if __name__ == '__main__':
    for m in (6,):
        for n in (7, 8, 9, 10, 11):
            check(m, n)
    print('ALL EXACT CHECKS PASSED (finite verification, not the infinite proof).')
