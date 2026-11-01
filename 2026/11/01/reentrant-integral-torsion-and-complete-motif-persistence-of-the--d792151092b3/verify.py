#!/usr/bin/env python3
"""Exact finite-chain and Smith-reduction verification for the Paley-11 tournaplex.

Usage: python verify.py
Standard-library only. Works with the three accompanying CSV datasets.
"""
from collections import Counter
from itertools import combinations
from functools import reduce as fold
from math import gcd
from pathlib import Path
import csv

N = 11
VERTEX_MASK = (1 << N) - 1
Q = {x*x % N for x in range(1, N)}
ALL = range(1, 1 << N)


def arc(i, j):
    return ((j-i) % N) in Q


def vertices(mask):
    return [i for i in range(N) if (mask >> i) & 1]


def cyc3(a, b, c):
    return ((arc(a, b) and arc(b, c) and arc(c, a)) or
            (arc(b, a) and arc(c, b) and arc(a, c)))


def triangle_masks():
    return tuple(sum(1 << i for i in x)
                 for x in combinations(range(N), 3) if cyc3(*x))


TRI = triangle_masks()
WEIGHT = {m: sum((m & u) == u for u in TRI) for m in ALL}
DIM = {m: m.bit_count()-1 for m in ALL}
LEVELS = sorted(set(WEIGHT.values()))
ORDER = sorted(ALL, key=lambda m: (WEIGHT[m], DIM[m], m))
POSITION = {m: i for i, m in enumerate(ORDER)}


def coefficient_boundary(mask):
    """Signed boundary using increasing vertex orientation."""
    return [(mask ^ (1 << x), 1 if j % 2 == 0 else -1)
            for j, x in enumerate(vertices(mask))]


def verify_chain():
    for m in ALL:
        if DIM[m] < 2:
            continue
        c = Counter()
        for f, a in coefficient_boundary(m):
            for g, b in coefficient_boundary(f):
                c[g] += a*b
        assert not any(c.values()), ('boundary squared', m)


def barcode_2():
    reduced, pivots, births = {}, {}, []
    for j, m in enumerate(ORDER):
        col = 0
        if DIM[m] > 0:
            for f, _ in coefficient_boundary(m):
                col ^= 1 << POSITION[f]
        while col and (col.bit_length()-1) in pivots:
            col ^= reduced[pivots[col.bit_length()-1]]
        reduced[j] = col
        if col:
            pivots[col.bit_length()-1] = j
        else:
            births.append(j)
    bars = Counter()
    for i, j in pivots.items():
        b, d = ORDER[i], ORDER[j]
        if WEIGHT[b] < WEIGHT[d]:
            bars[(DIM[b], WEIGHT[b], WEIGHT[d])] += 1
    infinite = [i for i in births if i not in pivots]
    assert len(infinite) == 1 and DIM[ORDER[infinite[0]]] == 0
    return bars, len(pivots)


def barcode_3():
    reduced, pivots, births = {}, {}, []
    for j, m in enumerate(ORDER):
        col = {}
        if DIM[m] > 0:
            for f, a in coefficient_boundary(m):
                col[POSITION[f]] = a % 3
        while col and max(col) in pivots:
            old = reduced[pivots[max(col)]]
            q = col[max(col)] * pow(old[max(col)], -1, 3) % 3
            for x, a in old.items():
                v = (col.get(x, 0)-q*a) % 3
                if v:
                    col[x] = v
                else:
                    col.pop(x, None)
        if col:
            pivots[max(col)] = j
            reduced[j] = col
        else:
            births.append(j)
    bars = Counter()
    for i, j in pivots.items():
        b, d = ORDER[i], ORDER[j]
        if WEIGHT[b] < WEIGHT[d]:
            bars[(DIM[b], WEIGHT[b], WEIGHT[d])] += 1
    infinite = [i for i in births if i not in pivots]
    assert len(infinite) == 1 and DIM[ORDER[infinite[0]]] == 0
    return bars, len(pivots)


def load_bars(filename):
    with (Path(__file__).resolve().parent/filename).open(newline='', encoding='utf-8') as stream:
        rows = list(csv.DictReader(stream))
    data = Counter()
    for row in rows:
        key = (int(row['degree']), int(row['birth']), int(row['death']))
        assert key not in data and int(row['multiplicity']) > 0
        data[key] = int(row['multiplicity'])
    return data


def rank_gf2(cols):
    basis = {}
    for x in cols:
        while x:
            p = x.bit_length()-1
            if p not in basis:
                basis[p] = x
                break
            x ^= basis[p]
    return len(basis)


def direct_betti_2(level):
    by_dim = {d: [m for m in ALL if WEIGHT[m] <= level and DIM[m] == d]
              for d in range(N)}
    ranks = {0: 1}   # augmentation from 11 vertices to the empty simplex
    for d in range(1, N):
        lower = {m: i for i, m in enumerate(by_dim[d-1])}
        cols = []
        for m in by_dim[d]:
            v = 0
            for f, _ in coefficient_boundary(m):
                v ^= 1 << lower[f]
            cols.append(v)
        ranks[d] = rank_gf2(cols)
    return {d: len(by_dim[d]) - ranks[d] - ranks.get(d+1, 0)
            for d in range(N)}


def boundary_rows(level, d):
    """Integer matrix C_d -> C_{d-1}, as sparse row dictionaries."""
    lower = [m for m in ALL if WEIGHT[m] <= level and DIM[m] == d-1]
    upper = [m for m in ALL if WEIGHT[m] <= level and DIM[m] == d]
    ri = {m: i for i, m in enumerate(lower)}
    rows = [{} for _ in lower]
    for j, m in enumerate(upper):
        for f, s in coefficient_boundary(m):
            rows[ri[f]][j] = s
    return rows


def smith_signature(rows):
    """Integral unit-pivot elimination, followed by an exact rank-one test.

    Pivoting on a +-1 entry clears its column by unimodular row operations;
    subsequent unimodular column operations clear the rest of its row without
    changing the remaining submatrix. All residuals in these inputs have rank
    at most one; gcd of all residual entries is its only Smith factor.
    """
    ones = 0
    while True:
        counts = Counter(j for row in rows for j in row)
        best = None
        for i, row in enumerate(rows):
            for j, x in row.items():
                if abs(x) == 1:
                    score = ((len(row)-1)*(counts[j]-1), len(row)+counts[j], i, j)
                    if best is None or score < best:
                        best = score
        if best is None:
            break
        _, _, i, j = best
        prow = rows[i]
        piv = prow[j]
        for k, row in enumerate(rows):
            if k == i or j not in row:
                continue
            factor = piv*row[j]
            for col, value in prow.items():
                new = row.get(col, 0)-factor*value
                if new:
                    row[col] = new
                else:
                    row.pop(col, None)
        rows[i] = {}
        ones += 1
    nonzero = [(i, j, v) for i, row in enumerate(rows) for j, v in row.items()]
    if not nonzero:
        return ones, None
    i0, j0, a = nonzero[0]
    anchor = rows[i0]
    for row in rows:
        for j in set(row)|set(anchor):
            assert a*row.get(j, 0) == row.get(j0, 0)*anchor.get(j, 0), \
                   'unresolved non-rank-one Smith residual'
    factor = fold(gcd, (abs(v) for _, _, v in nonzero), 0)
    assert factor > 0
    return ones, factor


def integral_data(level):
    sizes = {d: sum(WEIGHT[m] <= level and DIM[m] == d for m in ALL)
             for d in range(N)}
    rank = {0: 1}
    torsion = {}
    for d in range(1, N):
        a, b = smith_signature(boundary_rows(level, d))
        rank[d] = a + (b is not None)
        if b is not None and b != 1:
            torsion[d-1] = b
    betti = {d: sizes[d]-rank[d]-rank.get(d+1, 0) for d in range(N)}
    assert all(x >= 0 for x in betti.values())
    return {d: n for d, n in betti.items() if n}, torsion


def load_integral():
    with (Path(__file__).resolve().parent/'integral_stages.csv').open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    out = {}
    for row in rows:
        level = int(row['level'])
        def parse(s):
            if not s.strip():
                return {}
            return {int(y.split(':')[0]):int(y.split(':')[1])
                    for y in s.split(';')}
        out[level] = (parse(row['free_ranks']), parse(row['torsion_orders']))
    assert sorted(out) == LEVELS
    return out


def main():
    assert Q == {1,3,4,5,9}
    assert len(TRI) == 55
    assert LEVELS == [0,1,2,3,4,5,6,7,8,11,12,13,18,19,28,40,55]
    for x in range(N):
        assert sum(arc(x,y) for y in range(N) if x!=y) == 5
    for i,j in combinations(range(N),2):
        assert sum(arc(i,x) and arc(j,x) for x in range(N) if x not in (i,j)) == 2
    # Direct triple count versus the recurrence that adds the maximal vertex.
    rec = {0:0}
    T = set(TRI)
    for mask in ALL:
        bit = 1 << (mask.bit_length()-1)
        small = mask ^ bit
        new_tri = sum((bit|(1<<a)|(1<<b)) in T
                      for a,b in combinations(vertices(small),2))
        rec[mask] = rec[small] + new_tri
        assert rec[mask] == WEIGHT[mask]
    # Each of the 55 affine automorphisms preserves the entire weight function.
    for shift in range(N):
        for mul in Q:
            perm = [(mul*i+shift)%N for i in range(N)]
            assert all(WEIGHT[m] == WEIGHT[sum(1<<perm[i] for i in vertices(m))]
                       for m in ALL)
    verify_chain()
    bars2, p2 = barcode_2()
    bars3, p3 = barcode_3()
    assert bars2 == load_bars('barcode_F2.csv')
    assert bars3 == load_bars('barcode_F3.csv')
    expected_integral = load_integral()
    for t in LEVELS:
        free, torsion = integral_data(t)
        assert (free, torsion) == expected_integral[t], ('integral stage', t)
        obs2 = direct_betti_2(t)
        pred2 = {d: sum(v for (dim,b,e),v in bars2.items()
                        if dim==d and b<=t<e) for d in range(N)}
        assert obs2 == pred2, ('Betti', t)
        # Universal coefficient theorem independently checks the mod-two ranks.
        assert all(obs2[d] == free.get(d,0)+int(d in torsion)+int(d-1 in torsion)
                   for d in range(N)), ('UCT', t)
        pred3 = {d: sum(v for (dim,b,e),v in bars3.items()
                        if dim==d and b<=t<e) for d in range(N)}
        assert all(pred3[d] == free.get(d,0) for d in range(N)), ('mod3', t)
    assert sum(bars2.values()) == 727 and len(bars2) == 20
    assert sum(bars3.values()) == 726 and len(bars3) == 18
    assert expected_integral[0][1] == {2:2}
    assert expected_integral[12][1] == {5:2}
    assert all(not torsion for t,(_,torsion) in expected_integral.items() if t not in (0,12))
    print('PALEY11_TOURNAPLEX_PERSISTENCE_AND_INTEGRAL_SMITH_OK')
    print('vertices=11 triples=165 directed_cyclic_triples=55 nonempty_faces=2047')
    print('affine_symmetries=55 boundary_squared_zero=verified')
    print('levels=' + ','.join(map(str, LEVELS)))
    print('F2_positive_bars=727 interval_types=20 finite_pairs=' + str(p2))
    print('F3_positive_bars=726 interval_types=18 finite_pairs=' + str(p3))
    print('integral_torsion_levels=0:H2=Z/2,12:H5=Z/2')
    print('all_integral_stages=17 rank_and_smith_checked')
    print('direct_mod2_stage_betti=17 verified')


if __name__ == '__main__':
    main()
