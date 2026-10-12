#!/usr/bin/env python3
"""Exact finite-field replay of a three-group parity-check construction.
Only Python standard library. No external data or heuristic thresholds.
"""
from itertools import combinations, product
from collections import Counter
from pathlib import Path
import json

P = 5

def basis_vectors(m):
    if m == 1:
        return ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return ((1, m, -m), (m*m, m, -m*m), (m, -m, 1))

def parity_check():
    h = [[int(c//4 == r) for c in range(12)] for r in range(3)]
    blocks = [basis_vectors(m) for m in (1, 2, 3)]
    for a in range(3):
        h.append([0 if c%4 == 0 else blocks[c//4][c%4-1][a] % P
                  for c in range(12)])
    return h, blocks

def elimination(matrix):
    a = [[x % P for x in row] for row in matrix]
    if not a:
        return 0, [], []
    rows, cols = len(a), len(a[0])
    pivots = []
    k = 0
    for j in range(cols):
        t = next((i for i in range(k, rows) if a[i][j]), None)
        if t is None:
            continue
        a[k], a[t] = a[t], a[k]
        inv = pow(a[k][j], -1, P)
        a[k] = [inv*x % P for x in a[k]]
        for i in range(rows):
            if i != k and a[i][j]:
                s = a[i][j]
                a[i] = [(x - s*y) % P for x, y in zip(a[i], a[k])]
        pivots.append(j)
        k += 1
        if k == rows:
            break
    return k, a, pivots

def null_basis(H):
    rk, R, pv = elimination(H)
    free = [i for i in range(12) if i not in pv]
    G = []
    for j in free:
        g = [0] * 12
        g[j] = 1
        for i, piv in enumerate(pv):
            g[piv] = -R[i][j] % P
        G.append(tuple(g))
    return rk, G

def nrm(w):
    first = next(x for x in w if x % P)
    return tuple(x * pow(first, -1, P) % P for x in w)

def sub(u, v):
    return tuple((x-y) % P for x, y in zip(u, v))

def cross(u, v):
    return nrm((u[1]*v[2]-u[2]*v[1],
                u[2]*v[0]-u[0]*v[2],
                u[0]*v[1]-u[1]*v[0]))

def incidence_supports(blocks):
    points, lines = [], []
    for block in blocks:
        a = [(0,0,0)] + [tuple(x % P for x in v) for v in block]
        points.append({e:nrm(sub(a[e[1]],a[e[0]]))
                       for e in combinations(range(4),2)})
        lines.append({f:cross(sub(a[f[1]],a[f[0]]),
                               sub(a[f[2]],a[f[0]]))
                      for f in combinations(range(4),3)})
    supports = set()
    counts = {}
    for i in range(3):
        for j in range(3):
            if i == j: continue
            z = 0
            for pair, pt in points[i].items():
                for triple, ln in lines[j].items():
                    if sum(x*y for x,y in zip(pt,ln)) % P == 0:
                        # The local parity equations demand two and three
                        # nonzero coefficients in the indicated blocks.
                        S = frozenset({4*i+t for t in pair} |
                                      {4*j+t for t in triple})
                        assert len(S)==5 and S not in supports
                        supports.add(S)
                        z += 1
            counts[(i,j)] = z
    assert counts == {(0,1):3, (0,2):3, (1,0):3,
                      (1,2):2, (2,0):3, (2,1):2}
    assert len(supports) == 16
    return supports

def main():
    H, blocks = parity_check()
    assert len(H) == 6 and all(len(r)==12 for r in H)
    r, G = null_basis(H)
    assert r == 6 and len(G)==6
    assert all(sum(H[a][j]*g[j] for j in range(12))%P==0
               for g in G for a in range(6))
    # Enumerate every one of the 5^6 words, including the zero word.
    wd = Counter()
    by_support = {5:Counter(),6:Counter()}
    for a in product(range(P), repeat=6):
        word = tuple(sum(a[t]*G[t][j] for t in range(6))%P
                     for j in range(12))
        support = frozenset(j for j,x in enumerate(word) if x)
        w = len(support)
        wd[w] += 1
        if w in by_support:
            by_support[w][support] += 1
    expected = {0:1, 5:64,6:276,7:748,8:2060,9:3800,
                10:4460,11:3084,12:1132}
    assert wd == expected and sum(wd.values()) == P**6
    assert len(by_support[5]) == 16 and len(by_support[6]) == 69
    # Compare independently generated supports against the finite witness list.
    manifest = json.loads((Path(__file__).resolve().parent /
                           'artifacts' / 'circuits.json').read_text('utf-8'))
    assert manifest['field_order'] == 5 and manifest['coordinate_base'] == 1
    for t in (5, 6):
        stored = {frozenset(x-1 for x in E) for E in
                  manifest['minimal_dependent_parity_check_column_sets'][str(t)]}
        assert len(stored) == len(by_support[t])
        assert stored == set(by_support[t])
    assert set(by_support[5].values()) == {4}
    assert set(by_support[6].values()) == {4}
    five = set(by_support[5])
    six = set(by_support[6])
    assert max(len(a&b) for a,b in combinations(five,2)) == 3
    # A second method counts five-circuits from point/line incidences,
    # without generating codewords or using a nullspace basis.
    assert five == incidence_supports(blocks)
    # Independent erasure rank test of every erased coordinate set.
    rank_profiles = {}
    for t in range(5,7):
        frequency = Counter()
        for E in combinations(range(12),t):
            rank,_,_ = elimination([[row[j] for j in E] for row in H])
            deficiency = t-rank
            frequency[deficiency] += 1
            if deficiency:
                assert deficiency == 1
                if t == 5:
                    assert frozenset(E) in five
                else:
                    assert (frozenset(E) in six) != any(S<=set(E) for S in five)
        rank_profiles[t] = frequency
    assert rank_profiles[5] == {0:776,1:16}
    assert rank_profiles[6] == {0:743,1:181}
    # No size-six set can contain two distinct five-circuits.
    extensions = set()
    for S in five:
        for x in range(12):
            if x not in S:
                e = frozenset(set(S)|{x})
                assert e not in extensions
                extensions.add(e)
    assert len(extensions)==112 and not (extensions & six)
    assert 112 + len(six) == 181
    assert all(len(S)==5 for S in five) and all(len(S)==6 for S in six)
    print('GF(5) rank(H)=6; code [12,6,5]')
    print('Five-circuits=16; six-circuits=69')
    print('Failed five-erasures=16/792; failed six-erasures=181/924')
    print('All failed sets through size six have nullity one')
    print('VERIFY_OK')

if __name__=='__main__': main()
