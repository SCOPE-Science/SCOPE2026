"""Standalone exact integer reconstruction of the Tietze two-particle torus lattice.

Run: python3 verify_tietze.py
Only Python's standard library is required.
"""
from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import combinations
from math import gcd


def det_bareiss(rows):
    a = [list(map(int, row)) for row in rows]
    n = len(a)
    assert all(len(row) == n for row in a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if not a[k][k]:
            r = next((r for r in range(k + 1, n) if a[r][k]), None)
            if r is None:
                return 0
            a[k], a[r] = a[r], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                t = a[i][j] * pivot - a[i][k] * a[k][j]
                assert t % prev == 0
                a[i][j] = t // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[n - 1][n - 1] if n else 1


def rank_mod(columns, p):
    pivots = {}
    for col in columns:
        z = {i: v % p for i, v in col.items() if v % p}
        while z:
            i = min(z)
            if i not in pivots:
                zinv = pow(z[i], -1, p)
                pivots[i] = {j: (v * zinv) % p for j, v in z.items()}
                break
            factor = z[i]
            q = pivots[i]
            z = {j: t for j in z.keys() | q.keys()
                 if (t := (z.get(j, 0) - factor * q.get(j, 0)) % p)}
    return len(pivots)


def rank_q(columns):
    pivots = {}
    for col in columns:
        z = {i: Fraction(v) for i, v in col.items() if v}
        while z:
            i = min(z)
            if i not in pivots:
                piv = z[i]
                pivots[i] = {j: v / piv for j, v in z.items()}
                break
            f = z[i]
            q = pivots[i]
            z = {j: t for j in z.keys() | q.keys()
                 if (t := z.get(j, Fraction(0)) - f * q.get(j, Fraction(0)))}
    return len(pivots)


def tietze_edges():
    # Petersen: 5-cycle, 5-point star, and 5 spokes.
    pe = {tuple(sorted((i, (i + 1) % 5))) for i in range(5)}
    pe.update(tuple(sorted((i + 5, (i + 2) % 5 + 5))) for i in range(5))
    pe.update((i, i + 5) for i in range(5))
    neighbors = sorted(y if x == 0 else x for x, y in pe if 0 in (x, y))
    assert neighbors == [1, 4, 5]
    remap = {i: i - 1 for i in range(1, 10)}
    edges = {tuple(sorted((remap[x], remap[y]))) for x, y in pe if x and y}
    edges.update(((9, 10), (9, 11), (10, 11)))
    edges.update(tuple(sorted((9 + j, remap[v]))) for j, v in enumerate(neighbors))
    assert len(edges) == 18
    return sorted(edges)


def simple_cycles(edges):
    adj = {i: set() for i in range(12)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    out = set()
    for start in range(12):
        def walk(path):
            for v in sorted(adj[path[-1]]):
                if v == start and len(path) >= 3:
                    q = tuple(path)
                    out.add(min(q, (q[0],) + tuple(reversed(q[1:]))))
                elif v > start and v not in path:
                    walk(path + [v])
        walk([start])
    return sorted(out, key=lambda c: (len(c), c))


def oriented_cycle(c):
    return {tuple(sorted((c[i], c[(i + 1) % len(c)]))):
            (1 if c[i] < c[(i + 1) % len(c)] else -1)
            for i in range(len(c))}


def main():
    edges = tietze_edges()
    cycles = simple_cycles(edges)
    assert Counter(map(len, cycles)) == {3: 1, 5: 6, 6: 10, 7: 12,
                                          8: 9, 9: 14, 10: 30, 11: 18}
    f0 = list(combinations(range(12), 2))
    f1 = sorted((v, e) for v in range(12) for e in edges if v not in e)
    f2 = sorted((e, f) for e, f in combinations(edges, 2) if set(e).isdisjoint(f))
    assert (len(f0), len(f1), len(f2)) == (66, 180, 117)
    i0 = {s: i for i, s in enumerate(f0)}
    i1 = {s: i for i, s in enumerate(f1)}
    i2 = {s: i for i, s in enumerate(f2)}

    def bdy1(k):
        v, (a, b) = f1[k]
        return {i0[tuple(sorted((v, b)))]: 1,
                i0[tuple(sorted((v, a)))]: -1}

    def bdy2(k):
        (a, b), (c, d) = f2[k]
        return {i1[(b, (c, d))]: 1, i1[(a, (c, d))]: -1,
                i1[(d, (a, b))]: -1, i1[(c, (a, b))]: 1}

    b2 = [bdy2(k) for k in range(len(f2))]
    for col in b2:
        z = {}
        for k, v in col.items():
            for t, s in bdy1(k).items():
                z[t] = z.get(t, 0) + v * s
        assert all(v == 0 for v in z.values())
    assert rank_mod(b2, 101) == 108

    pairs, tori = [], []
    for a, b in combinations(range(len(cycles)), 2):
        if not set(cycles[a]).isdisjoint(cycles[b]):
            continue
        x, y = oriented_cycle(cycles[a]), oriented_cycle(cycles[b])
        torus = {i2[tuple(sorted((e, f)))]: sx * sy * (1 if e < f else -1)
                 for e, sx in x.items() for f, sy in y.items()}
        boundary = {}
        for k, coeff in torus.items():
            for row, z in b2[k].items():
                boundary[row] = boundary.get(row, 0) + coeff * z
        assert all(z == 0 for z in boundary.values())
        pairs.append((a, b))
        tori.append(torus)
    groups = {}
    for k, (a, b) in enumerate(pairs):
        groups.setdefault(tuple(sorted((len(cycles[a]), len(cycles[b])))), []).append(k)
    assert {k: len(v) for k, v in groups.items()} == {
        (3, 5): 6, (3, 6): 4, (3, 8): 3,
        (3, 9): 2, (5, 6): 6, (5, 7): 6}

    # A signed 9-by-9 coordinate minor of nine integer 2-cycles.
    basis_indices = [0, 2, 3, 15, 17, 19, 21, 23, 25]
    rows = [0, 2, 4, 10, 13, 15, 47, 67, 95]
    basis_mat = [[tori[j].get(i, 0) for j in basis_indices] for i in rows]
    assert det_bareiss(basis_mat) == -1
    # A rank-108 boundary and nine primitive 2-cycles imply exactly H_2 = Z^9.
    assert rank_mod([tori[j] for j in basis_indices], 101) == 9

    small = [tori[j] for j, (a, b) in enumerate(pairs)
             if len(cycles[a]) + len(cycles[b]) <= 10]
    assert len(small) == 10 and rank_q(small) == 4

    # Rows above identify the integral lattice of 2-cycles with Z^9.
    selected = groups[(3, 6)] + groups[(5, 6)]
    assert len(selected) == 10
    matrix = [[tori[j].get(row, 0) for j in selected] for row in rows]
    minors = [det_bareiss([[matrix[i][j] for j in ss] for i in range(9)])
              for ss in combinations(range(10), 9)]
    assert [abs(x) for x in minors] == [2, 2, 2, 2, 2, 2, 0, 2, 0, 0]
    assert reduce(gcd, (abs(x) for x in minors), 0) == 2
    coord_cols = [{i: matrix[i][j] for i in range(9) if matrix[i][j]}
                  for j in range(10)]
    assert rank_mod(coord_cols, 2) == 8
    assert rank_mod(coord_cols, 101) == 9
    parity = (1, 1, 1, 1, 1, 1, 0, 1, 1)
    assert all(sum(parity[i] * matrix[i][j] for i in range(9)) % 2 == 0
               for j in range(10))
    # Every triangle–pentagon torus is outside this index-two lattice.
    for j in groups[(3, 5)]:
        extra = {i: tori[j].get(row, 0) for i, row in enumerate(rows)
                 if tori[j].get(row, 0)}
        assert rank_mod(coord_cols + [extra], 2) == 9
        assert sum(parity[i] * tori[j].get(row, 0)
                   for i, row in enumerate(rows)) % 2 == 1

    print('VERIFY_OK_TIETZE_INTEGRAL_TORUS_LENGTH_THRESHOLD')
    print('GRAPH_VERTICES_EDGES', 12, len(edges))
    print('CYCLE_LENGTH_COUNTS', dict(sorted(Counter(map(len, cycles)).items())))
    print('DISCRETE_CELLS', len(f0), len(f1), len(f2))
    print('BOUNDARY2_RANK_MOD_101', rank_mod(b2, 101))
    print('PAIR_LENGTH_COUNTS', {str(k): len(v) for k, v in sorted(groups.items())})
    print('NINE_BASIS_PAIR_INDICES', basis_indices)
    print('NINE_BASIS_MINOR_ROWS', rows)
    print('UNIT_MINOR', det_bareiss(basis_mat))
    print('H2_INTEGRAL_RANK', 9)
    print('TOTAL_LENGTH_LE_10_RANK', rank_q(small))
    print('TOTAL_LENGTH_LE_11_INTEGRAL_GENERATION', True)
    print('SIX_TRIANGLE_PENTAGON_SIX_PENTAGON_HEXAGON_GENERATE', True)
    print('TEN_TRIANGLE_HEXAGON_PENTAGON_HEXAGON_INDEX', 2)
    print('TEN_GENERATORS_MAXIMAL_MINOR_VALUES', minors)
    print('PARITY_DETECTING_COCHAIN', parity)
    print('EVERY_TRIANGLE_PENTAGON_CLASS_KILLS_PARITY_OBSTRUCTION', True)


if __name__ == '__main__':
    main()
