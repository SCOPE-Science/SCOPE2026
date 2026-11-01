#!/usr/bin/env python3
"""Exact finite multipath-complex Morse checker for bidirected K_{2,n}, 3 <= n <= 8.

Standard library only.  Reconstructs faces, checks a complete acyclic matching,
computes the exact signed integral Morse boundary by gradient-path recursion,
and verifies integer-minor witnesses and independent simplicial mod-two homology.
"""
import argparse
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
import json

EXPECTED = {
    3: (115, {1: 1, 2: 6}, 0, 0),
    4: (313, {2: 9, 3: 2}, 2, 1),
    5: (711, {2: 7, 3: 38}, 7, 6),
    6: (1417, {2: 13, 3: 182}, 13, 13),
    7: (2563, {2: 21, 3: 512}, 21, 21),
    8: (4305, {2: 31, 3: 1136}, 31, 31),
}

def arrows(n):
    return ([(a, v) for a in (0, 1) for v in range(2, n + 2)]
            + [(v, a) for v in range(2, n + 2) for a in (0, 1)])

def valid_indices(ids, arcs):
    incoming, outgoing = set(), set()
    successor = {}
    for i in ids:
        a, b = arcs[i]
        if a in outgoing or b in incoming:
            return False
        outgoing.add(a)
        incoming.add(b)
        successor[a] = b
    for start in successor:
        seen = set()
        v = start
        while v in successor:
            if v in seen:
                return False
            seen.add(v)
            v = successor[v]
    return True

def enumerate_faces(n):
    arcs = arrows(n)
    result = {0}
    for k in range(1, 5):
        for ids in combinations(range(len(arcs)), k):
            if valid_indices(ids, arcs):
                result.add(sum(1 << i for i in ids))
    # Independent generation by recursive extension and explicit indegree/outdegree/DFS checks.
    recursive = {0}
    frontier = {0}
    for _ in range(4):
        nxt = set()
        for mask in frontier:
            for i in range(len(arcs)):
                if not mask & (1 << i):
                    new = mask | (1 << i)
                    if new not in recursive:
                        selected = [j for j in range(len(arcs)) if new & (1 << j)]
                        if valid_indices(selected, arcs):
                            nxt.add(new)
        recursive |= nxt
        frontier = nxt
    assert result == recursive, "Independent face enumeration disagrees"
    expected_f = [1, 4*n, 2*n*(3*n-2), 4*n*(n-1)**2,
                  n*(n-2)*(n-1)**2]
    face_vector = [sum(mask.bit_count() == k for mask in result) for k in range(5)]
    assert face_vector == expected_f, (n, face_vector, expected_f)
    return arcs, result, face_vector

def signed_boundary(mask):
    result = []
    k = 0
    rem = mask
    while rem:
        bit = rem & -rem
        rem -= bit
        result.append((mask ^ bit, 1 if k % 2 == 0 else -1))
        k += 1
    return result

def matching_and_acyclicity(faces, arc_count):
    free = set(faces)
    pairs = []
    for i in range(arc_count):
        bit = 1 << i
        lows = [f for f in free if not f & bit and f | bit in free]
        for f in lows:
            g = f | bit
            free.remove(f)
            free.remove(g)
            pairs.append((f, g))
    # Reverse each matched Hasse edge, orient all unmatched Hasse edges downward.
    matchset = set(pairs)
    nexts = defaultdict(list)
    indeg = {f: 0 for f in faces}
    incidences = 0
    for g in faces:
        for f, _ in signed_boundary(g):
            assert f in faces
            incidences += 1
            source, target = (f, g) if (f, g) in matchset else (g, f)
            nexts[source].append(target)
            indeg[target] += 1
    todo = deque(f for f in faces if indeg[f] == 0)
    popped = 0
    while todo:
        f = todo.popleft()
        popped += 1
        for g in nexts[f]:
            indeg[g] -= 1
            if indeg[g] == 0:
                todo.append(g)
    assert popped == len(faces), "Gradient digraph contains a directed cycle"
    assert len(free) + 2*len(pairs) == len(faces)
    return free, pairs, incidences

def morse_matrix(critical, pairs, low_size):
    lows = sorted(x for x in critical if x.bit_count() == low_size)
    highs = sorted(x for x in critical if x.bit_count() == low_size + 1)
    low_index = {x: i for i, x in enumerate(lows)}
    matched_up = {x: y for x, y in pairs if x.bit_count() == low_size}
    matched_down = {y for x, y in pairs if y.bit_count() == low_size}
    visiting = set()
    @lru_cache(maxsize=None)
    def reduce_low(x):
        if x in low_index:
            return ((low_index[x], 1),)
        if x in matched_down:
            return ()
        assert x in matched_up
        assert x not in visiting, "Gradient-path recursion cycle"
        visiting.add(x)
        high = matched_up[x]
        boundary = dict(signed_boundary(high))
        assert abs(boundary[x]) == 1
        aggregate = defaultdict(int)
        for y, sign in boundary.items():
            if y == x:
                continue
            for j, val in reduce_low(y):
                aggregate[j] -= sign * boundary[x] * val
        visiting.remove(x)
        return tuple(sorted((j, val) for j, val in aggregate.items() if val))
    columns = []
    for high in highs:
        aggregate = defaultdict(int)
        for low, sign in signed_boundary(high):
            for j, val in reduce_low(low):
                aggregate[j] += sign * val
        columns.append(sorted((j, val) for j, val in aggregate.items() if val))
    return lows, highs, columns

def rank_mod2_columns(columns):
    basis = {}
    for c in columns:
        v = 0
        for i, x in c:
            if x & 1:
                v ^= 1 << i
        while v:
            pivot = v.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = v
                break
            v ^= basis[pivot]
    return len(basis)

def direct_ranks_mod2(faces):
    by_dim = [[f for f in faces if f.bit_count() == k] for k in range(5)]
    ranks = []
    for k in range(1, 5):
        row = {f: i for i, f in enumerate(by_dim[k - 1])}
        cols = []
        for g in by_dim[k]:
            cols.append([(row[f], sign) for f, sign in signed_boundary(g)])
        ranks.append(rank_mod2_columns(cols))
    betti = [len(by_dim[k]) - ranks[k-1] - (ranks[k] if k < 4 else 0)
             for k in range(1, 5)]
    return ranks, betti

def determinant_bareiss(a):
    a = [list(row) for row in a]
    n = len(a)
    assert all(len(row) == n for row in a)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            h = next((h for h in range(k+1, n) if a[h][k]), None)
            if h is None:
                return 0
            a[k], a[h] = a[h], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*pivot - a[i][k]*a[k][j]
                q, r = divmod(numerator, prev)
                assert r == 0, "Bareiss nonintegral quotient"
                a[i][j] = q
            a[i][k] = 0
        prev = pivot
    return sign*a[-1][-1]

def minor(columns, rows, column_indices):
    dense = [dict(columns[j]) for j in column_indices]
    return determinant_bareiss([[col.get(i, 0) for col in dense] for i in rows])

def unit_witness(columns, nrows):
    selected = {}
    # Use integral singleton columns as a unimodular diagonal block.
    for j, c in enumerate(columns):
        if len(c) == 1 and abs(c[0][1]) == 1:
            selected.setdefault(c[0][0], j)
    missing = set(range(nrows)) - set(selected)
    for i in sorted(missing):
        for j, c in enumerate(columns):
            d = dict(c)
            if abs(d.get(i, 0)) == 1 and not any(d.get(t, 0) for t in missing - {i}):
                assert j not in selected.values()
                selected[i] = j
                break
        assert i in selected, ('no unit-minor witness', i)
    cols = [selected[i] for i in range(nrows)]
    det = minor(columns, list(range(nrows)), cols)
    assert abs(det) == 1, ('not unimodular', det)
    return cols, det

def run_case(n):
    arcs, faces, fv = enumerate_faces(n)
    critical, pairs, incidences = matching_and_acyclicity(faces, len(arcs))
    histogram = dict(sorted(Counter(f.bit_count()-1 for f in critical).items()))
    assert len(faces) == EXPECTED[n][0] and histogram == EXPECTED[n][1]
    low_size = 2 if n == 3 else 3
    lows, highs, cols = morse_matrix(critical, pairs, low_size)
    assert len(cols) == len(highs)
    mod2 = rank_mod2_columns(cols)
    assert mod2 == EXPECTED[n][3]
    raw_ranks, raw_betti = direct_ranks_mod2(faces)
    if n == 3:
        assert all(not c for c in cols)
        witness = {'kind': 'zero_matrix', 'rank': 0}
    elif n == 4:
        # Rank 2 over Q, rank 1 in characteristic 2, with a unit entry.
        determinant = minor(cols, [0, 2], [0, 1])
        assert abs(determinant) == 2 and any(abs(v) == 1 for c in cols for _,v in c)
        witness = {'kind': 'smith_1_2', 'rows': [0,2], 'columns': [0,1], 'minor': determinant}
    elif n == 5:
        chosen = [0,1,2,3,4,5,10]
        determinant = minor(cols, list(range(7)), chosen)
        assert abs(determinant) == 2
        witness = {'kind': 'smith_six_1_one_2', 'rows': list(range(7)), 'columns': chosen, 'minor': determinant}
    else:
        chosen, determinant = unit_witness(cols, len(lows))
        assert len(lows) == EXPECTED[n][2]
        witness = {'kind': 'full_unimodular', 'rows': list(range(len(lows))), 'columns': chosen, 'minor': determinant}
    expected_betti = {
        3: [0,1,6,0], 4: [0,0,8,1], 5: [0,0,1,32],
        6: [0,0,0,169], 7: [0,0,0,491], 8: [0,0,0,1105]
    }
    # Betti indices correspond to reduced H_0,H_1,H_2,H_3.
    # The empty face is the augmented chain basis; H_0 vanishes here.
    assert raw_betti == expected_betti[n], (n,raw_betti)
    return {'n':n,'arcs':len(arcs),'f_augmented':fv, 'faces':len(faces),
            'matched_pairs':len(pairs), 'hasse_incidences':incidences,
            'critical_cells':histogram,'low_size':low_size,
            'critical_low_masks':lows, 'critical_high_masks':highs,
            'morse_columns':cols, 'morse_mod2_rank':mod2,
            'independent_simplicial_mod2_ranks':raw_ranks,
            'independent_simplicial_mod2_betti_reduced':raw_betti,
            'integral_minor_witness':witness}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--make-certificate')
    ap.add_argument('--verify')
    args=ap.parse_args()
    assert not (args.make_certificate and args.verify)
    cases=[run_case(n) for n in sorted(EXPECTED)]
    output={'schema_version':1,'definition':'bidirected complete bipartite graph K_{2,n}; multipath faces are directed vertex-disjoint path unions', 'cases':cases}
    if args.make_certificate:
        with open(args.make_certificate,'w',encoding='utf-8') as f:
            json.dump(output,f,ensure_ascii=False,sort_keys=True,separators=(',',':'))
            f.write('\n')
    if args.verify:
        with open(args.verify,'r',encoding='utf-8') as f:
            stored=json.load(f)
        assert stored==json.loads(json.dumps(output)), 'Certificate is not exactly reproducible'
    for c in cases:
        print('n={n} faces={faces} pairs={matched_pairs} critical={critical_cells} MorseF2rank={morse_mod2_rank} simplicialF2={independent_simplicial_mod2_betti_reduced} minor={integral_minor_witness}'.format(**c))
    print('BIDIRECTED_K2N_INTEGRAL_MOORE_WINDOW_VERIFIED')

if __name__=='__main__':
    main()
