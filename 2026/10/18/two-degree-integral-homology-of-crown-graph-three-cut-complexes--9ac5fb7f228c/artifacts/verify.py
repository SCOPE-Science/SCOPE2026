"""Independent finite checks for the crown-graph 3-cut homology theorem.

Only Python's standard library is needed. The all-n proof instead uses the
published shellability theorem for multiple chessboard complexes.
"""
from itertools import combinations
from math import comb


def rank_mod2(columns):
    pivots = {}
    for col in columns:
        while col:
            bit = col.bit_length() - 1
            if bit in pivots:
                col ^= pivots[bit]
            else:
                pivots[bit] = col
                break
    return len(pivots)


def disconn_triples(n):
    bad = []
    for vertices in combinations(range(2*n), 3):
        edges = set()
        for u, v in combinations(vertices, 2):
            if (u < n) != (v < n) and (u % n) != (v % n):
                edges.add((u, v))
        seen = {vertices[0]}
        while True:
            updated = seen | {v for u, v in edges if u in seen} | {u for u, v in edges if v in seen}
            if updated == seen:
                break
            seen = updated
        if len(seen) != 3:
            bad.append(frozenset(vertices))
    return bad


def faces_by_dimension(n, mode, bad):
    out = {}
    for mask in range(1 << (2*n)):
        f = frozenset(i for i in range(2*n) if mask >> i & 1)
        if mode == 'alexander':
            ok = all(not d <= f for d in bad)
        elif mode == 'cut':
            ok = any(d.isdisjoint(f) for d in bad)
        elif mode == 'chessboard':
            a = {i for i in f if i < n}
            b = {i-n for i in f if i >= n}
            ok = len(a) <= 2 and len(b) <= 2 and a.isdisjoint(b)
        else:
            raise ValueError(mode)
        if ok:
            out.setdefault(len(f)-1, []).append(f)
    return out


def betti2(faces):
    dims = sorted(d for d in faces if d >= 0)
    if not dims:
        return {}
    ranks = {}
    for d in dims:
        if d == 0:
            ranks[d] = 1  # augmented differential to the empty simplex
            continue
        previous = {f: i for i, f in enumerate(faces[d-1])}
        cols = []
        for f in faces[d]:
            col = 0
            for v in f:
                col |= 1 << previous[f - {v}]
            cols.append(col)
        ranks[d] = rank_mod2(cols)
    return {d: len(faces[d]) - ranks[d] - ranks.get(d+1, 0)
            for d in dims if len(faces[d]) - ranks[d] - ranks.get(d+1, 0)}


def expected_beta3(n):
    return 1 - 2*n + 2*n*(n-1) - n*(n-1)*(n-2) + comb(n, 2)*comb(n-2, 2)


def run():
    cases = 0
    for n in range(5, 8):
        bad = disconn_triples(n)
        y = faces_by_dimension(n, 'alexander', bad)
        x = faces_by_dimension(n, 'chessboard', bad)
        expected = {d: set(x.get(d, [])) for d in y}
        expected[1].update(frozenset((i, n+i)) for i in range(n))
        for d in y:
            assert set(y[d]) == expected[d], (n, d, 'dual decomposition mismatch')
        assert {d: len(x[d]) for d in (0, 1, 2, 3)} == {
            0: 2*n,
            1: 2*n*(n-1),
            2: n*(n-1)*(n-2),
            3: comb(n, 2)*comb(n-2, 2),
        }
        assert betti2(x) == {3: expected_beta3(n)}
        assert betti2(y) == {1: n, 3: expected_beta3(n)}
        cases += 1
        print(f'n={n}: Alexander dual verified; X homology H3={expected_beta3(n)}; dual H1={n}, H3={expected_beta3(n)}')
    for n in (5, 6):
        bad = disconn_triples(n)
        cut = faces_by_dimension(n, 'cut', bad)
        got = betti2(cut)
        want = {2*n-6: expected_beta3(n), 2*n-4: n}
        assert got == want, (n, got, want)
        assert max(cut) == 2*n-4
        assert len(cut[2*n-6]) == comb(2*n, 2*n-5)
        cases += 1
        print(f'n={n}: direct cut-complex homology {got} verified')
    print(f'VERIFY_OK cases={cases}')


if __name__ == '__main__':
    run()
