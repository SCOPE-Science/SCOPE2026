#!/usr/bin/env python3
"""Reconstruct the integral CW reduction of a six-vertex multipath complex."""
from collections import Counter, defaultdict, deque
import json
import sys
from itertools import combinations

LEFT = range(3)
RIGHT = range(3, 6)
ARCS = [(u, v) for u in LEFT for v in RIGHT] + [(u, v) for u in RIGHT for v in LEFT]
ARC_ORDER = [0, 9, 1, 10, 2, 11, 3, 12, 4, 13, 5, 14, 6, 15, 7, 16, 8, 17]
EXPECTED_F = (18, 108, 264, 252, 72)
EXPECTED_CRIT = {0: 1, 2: 5, 3: 24, 4: 12}


def multipath_degree_acyclic(mask):
    inc, out = [0] * 6, [0] * 6
    successor = {}
    for i, (u, v) in enumerate(ARCS):
        if not (mask >> i) & 1:
            continue
        inc[v] += 1
        out[u] += 1
        if inc[v] > 1 or out[u] > 1:
            return False
        successor[u] = v
    for start in successor:
        seen, v = set(), start
        while v in successor:
            if v in seen:
                return False
            seen.add(v)
            v = successor[v]
    return True


def multipath_components(mask):
    incoming, outgoing = [0] * 6, [0] * 6
    neighbor = [set() for _ in range(6)]
    for i, (u, v) in enumerate(ARCS):
        if mask & (1 << i):
            incoming[v] += 1
            outgoing[u] += 1
            neighbor[u].add(v)
            neighbor[v].add(u)
    if any(a > 1 or b > 1 for a, b in zip(incoming, outgoing)):
        return False
    visited = set()
    for root in range(6):
        if root in visited:
            continue
        stack, nodes = [root], set()
        while stack:
            v = stack.pop()
            if v in nodes:
                continue
            nodes.add(v)
            stack.extend(neighbor[v] - nodes)
        visited.update(nodes)
        edges = sum(incoming[v] for v in nodes)
        if edges != len(nodes) - 1:
            return False
    return True


def all_faces():
    assert len(ARCS) == 18
    bydim = defaultdict(list)
    for mask in range(1 << 18):
        a = multipath_degree_acyclic(mask)
        b = multipath_components(mask)
        assert a == b, ('membership disagreement', mask)
        if a and mask:
            bydim[mask.bit_count() - 1].append(mask)
    assert tuple(len(bydim[k]) for k in range(5)) == EXPECTED_F
    assert sum(len(x) for x in bydim.values()) == 714
    return bydim


def build_matching(bydim):
    all_nonempty = set().union(*map(set, bydim.values()))
    unmatched = set(all_nonempty)
    pairs = []
    for i in ARC_ORDER:
        bit = 1 << i
        for lower in sorted(unmatched, key=lambda x: (x.bit_count(), x)):
            upper = lower | bit
            if not lower & bit and upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                pairs.append((lower, upper))
    assert len(pairs) == 336
    assert dict(Counter(f.bit_count() - 1 for f in unmatched)) == EXPECTED_CRIT
    assert sum(len(cells) for cells in bydim.values()) == len(pairs) * 2 + len(unmatched)
    return pairs, unmatched


def check_hasse_acyclic(bydim, pairs):
    faces = set().union(*map(set, bydim.values()))
    matched = set(pairs)
    indeg = {f: 0 for f in faces}
    links = defaultdict(list)
    incidences = 0
    for upper in faces:
        for i in range(18):
            if not upper & (1 << i):
                continue
            lower = upper ^ (1 << i)
            if lower == 0:
                continue
            assert lower in faces
            incidences += 1
            source, target = (lower, upper) if (lower, upper) in matched else (upper, lower)
            links[source].append(target)
            indeg[target] += 1
    todo = deque(f for f in sorted(faces) if indeg[f] == 0)
    visited = 0
    while todo:
        f = todo.popleft()
        visited += 1
        for g in links[f]:
            indeg[g] -= 1
            if indeg[g] == 0:
                todo.append(g)
    assert visited == len(faces), ('matching has a closed gradient path', visited)
    return incidences


def integer_reduction(bydim, pairs):
    faces = set().union(*map(set, bydim.values()))
    bd = {}
    for upper in faces:
        bits = [i for i in range(18) if upper & (1 << i)]
        bd[upper] = {upper ^ (1 << i): (-1 if j & 1 else 1)
                     for j, i in enumerate(bits)} if len(bits) > 1 else {}
    remaining = faces.copy()
    pending = list(pairs)
    canceled = 0
    while pending:
        for ix, (lower, upper) in enumerate(pending):
            pivot = bd[upper].get(lower, 0)
            if abs(pivot) == 1:
                break
        else:
            raise AssertionError('No legal unit cancellation')
        d = upper.bit_count()
        old_boundary = dict(bd[upper])
        for cell in list(remaining):
            if cell == upper or cell.bit_count() != d:
                continue
            value = bd[cell].get(lower, 0)
            if value:
                factor = value // pivot
                for target, coefficient in old_boundary.items():
                    update = bd[cell].get(target, 0) - factor * coefficient
                    if update:
                        bd[cell][target] = update
                    else:
                        bd[cell].pop(target, None)
        for cell in list(remaining):
            if cell.bit_count() == d:
                bd[cell].pop(lower, None)
            elif cell.bit_count() == d + 1:
                bd[cell].pop(upper, None)
        remaining.remove(lower)
        remaining.remove(upper)
        del pending[ix]
        canceled += 1
    assert canceled == 336
    assert dict(Counter(f.bit_count() - 1 for f in remaining)) == EXPECTED_CRIT
    critical = {dim: sorted(f for f in remaining if f.bit_count() == dim + 1)
                for dim in EXPECTED_CRIT}
    for upper in remaining:
        assert set(bd[upper]).issubset(remaining)
    assert all(not bd[f] for f in critical[2])
    assert all(not bd[f] for f in critical[4])
    rows, cols = critical[2], critical[3]
    D3 = [[bd[upper].get(lower, 0) for upper in cols] for lower in rows]
    assert len(D3) == 5 and all(len(row) == 24 for row in D3)
    assert sum(1 for row in D3 for v in row if v) == 18
    assert all(abs(v) <= 1 for row in D3 for v in row)
    return critical, D3


def determinant_bareiss(A):
    A = [list(row) for row in A]
    n = len(A)
    if n == 1:
        return A[0][0]
    sign, previous = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            pivot = next((j for j in range(k + 1, n) if A[j][k]), None)
            if pivot is None:
                return 0
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        a = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = A[i][j] * a - A[i][k] * A[k][j]
                assert numerator % previous == 0
                A[i][j] = numerator // previous
            A[i][k] = 0
        previous = a
    return sign * A[n - 1][n - 1]


def rank_mod2(bydim, dim):
    row_index = {f: j for j, f in enumerate(bydim[dim - 1])}
    pivots = {}
    for upper in bydim[dim]:
        vec = 0
        for i in range(18):
            if upper & (1 << i):
                vec ^= 1 << row_index[upper ^ (1 << i)]
        while vec:
            index = vec.bit_length() - 1
            if index not in pivots:
                pivots[index] = vec
                break
            vec ^= pivots[index]
    return len(pivots)


def main():
    bydim = all_faces()
    faceset = set().union(*map(set, bydim.values()))
    facets = [f for f in faceset if not any(
        not (f & (1 << i)) and (f | (1 << i)) in faceset
        for i in range(18))]
    assert Counter(f.bit_count() - 1 for f in facets) == {3: 72, 4: 72}
    pairs, unmatched = build_matching(bydim)
    incidences = check_hasse_acyclic(bydim, pairs)
    critical, D3 = integer_reduction(bydim, pairs)
    # A five-column minor of the reduced three-to-two cellular boundary.
    witness_cols = (6304, 33952, 35088, 65676, 67716)
    indices = [critical[3].index(col) for col in witness_cols]
    minor = [[row[i] for i in indices] for row in D3]
    unit = determinant_bareiss(minor)
    assert unit == 1
    ranks = [rank_mod2(bydim, dim) for dim in range(1, 5)]
    assert ranks == [17, 91, 173, 60]
    betti = [len(bydim[d]) - (ranks[d - 1] if d > 0 else 0)
             - (ranks[d] if d < 4 else 0) for d in range(5)]
    assert betti == [1, 0, 0, 19, 12]
    certificate = {
        'arcs': [list(edge) for edge in ARCS],
        'matching_pairs': [list(pair) for pair in pairs],
        'critical_cells': {str(key): value for key, value in critical.items()},
        'morse_boundary_degree_3': D3,
        'morse_boundary_degree_4_zero_shape': [24, 12],
        'unit_minor_upper_cells': list(witness_cols),
        'unit_minor_determinant': unit,
    }
    if len(sys.argv) == 3 and sys.argv[1] == '--write-certificate':
        with open(sys.argv[2], 'w', encoding='utf-8') as target:
            json.dump(certificate, target, separators=(',', ':'), sort_keys=True)
            target.write('\n')
    elif len(sys.argv) == 3 and sys.argv[1] == '--check-certificate':
        with open(sys.argv[2], encoding='utf-8') as source:
            assert json.load(source) == certificate
    else:
        assert len(sys.argv) == 1, 'use --check-certificate PATH'
    print('arc_order:', ARCS)
    print('face_vector:', EXPECTED_F, 'nonempty_faces:', 714)
    print('maximal_faces_by_dimension:', {3: 72, 4: 72})
    print('matching_pairs:', len(pairs), 'critical_cells:', EXPECTED_CRIT)
    print('hasse_incidences:', incidences, 'acyclic:', True)
    print('integral_morse_boundary_D3_shape:', (5, 24))
    print('integral_morse_boundary_D3_nonzeros:', sum(bool(v) for row in D3 for v in row))
    print('integral_morse_boundary_D4_shape:', (24, 12), 'all_zero:', True)
    print('unit_minor_columns:', witness_cols, 'determinant:', unit)
    print('independent_mod2_boundary_ranks:', tuple(ranks))
    print('independent_mod2_betti:', tuple(betti))
    print('reduced_euler_characteristic:', sum((-1) ** i * len(bydim[i]) for i in range(5)) - 1)
    print('K33_BIDIRECTED_MULTIPATH_MIXED_WEDGE_VERIFIED')


if __name__ == '__main__':
    main()
