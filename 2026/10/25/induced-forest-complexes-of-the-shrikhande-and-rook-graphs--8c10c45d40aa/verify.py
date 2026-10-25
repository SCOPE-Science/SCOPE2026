#!/usr/bin/env python3
"""Exhaustive standalone certificate for two induced-forest simplicial complexes.

Requires only Python 3 standard library. Face masks use vertex index 4*a+b.
The complex contains the empty simplex, used solely for reduced-chain accounting.
"""
import itertools
import json
from collections import Counter, defaultdict, deque
from functools import lru_cache

N = 16
VERTICES = list(itertools.product(range(4), repeat=2))


def make_graph(kind):
    differences = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    E = []
    for i, (a, b) in enumerate(VERTICES):
        for j in range(i + 1, N):
            c, d = VERTICES[j]
            if kind == 'Shrikhande':
                isedge = ((c-a) % 4, (d-b) % 4) in differences
            elif kind == 'Rook':
                isedge = a == c or b == d
            else:
                raise ValueError(kind)
            if isedge:
                E.append((i, j))
    return E


def check_srg(E):
    A = [set() for _ in range(N)]
    for i, j in E:
        A[i].add(j)
        A[j].add(i)
    assert len(E) == 48
    assert all(len(z) == 6 for z in A)
    assert all(len(A[i] & A[j]) == 2 for i in range(N) for j in range(i+1, N))
    return sum(1 for i in range(N) for j in A[i] if i<j for k in A[j] if j<k and k in A[i])


def is_forest_union_find(mask, E):
    parent = list(range(N))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, j in E:
        if (mask >> i) & 1 and (mask >> j) & 1:
            a, b = root(i), root(j)
            if a == b:
                return False
            parent[a] = b
    return True


def is_forest_dfs(mask, A):
    visited = set()
    for v in range(N):
        if not ((mask >> v) & 1) or v in visited:
            continue
        stack = [(v, -1)]
        visited.add(v)
        while stack:
            w, parent = stack.pop()
            for u in A[w]:
                if not ((mask >> u) & 1) or u == parent:
                    continue
                if u in visited:
                    return False
                visited.add(u)
                stack.append((u, w))
    return True


def signed_facets(s):
    out = []
    pos = 0
    bits = s
    while bits:
        bit = bits & -bits
        out.append((s ^ bit, (-1 if pos & 1 else 1)))
        bits ^= bit
        pos += 1
    return out


def matching(faces):
    unpaired = set(faces)
    pairs = []
    for v in range(N):
        b = 1 << v
        for s in faces:
            if not (s & b) and s in unpaired and (s | b) in unpaired:
                unpaired.remove(s)
                unpaired.remove(s | b)
                pairs.append((s, s | b))
    assert 0 not in unpaired
    assert (0, 1) in pairs
    return pairs, unpaired


def check_acyclic(faces, pairs):
    face_set = set(faces)
    matched = set(pairs)
    indegree = {f: 0 for f in faces}
    successor = defaultdict(list)
    incidences = 0
    for hi in faces:
        for low, _ in signed_facets(hi):
            assert low in face_set
            # Matched arrows increase dimension; unmatched arrows decrease it.
            if (low, hi) in matched:
                src, dst = low, hi
            else:
                src, dst = hi, low
            successor[src].append(dst)
            indegree[dst] += 1
            incidences += 1
    todo = deque(f for f in faces if indegree[f] == 0)
    count = 0
    while todo:
        f = todo.popleft()
        count += 1
        for dst in successor[f]:
            indegree[dst] -= 1
            if indegree[dst] == 0:
                todo.append(dst)
    assert count == len(faces), (count, len(faces))
    return incidences


def morse_differential(pairs, critical):
    lower_to_upper = dict(pairs)
    upper_to_lower = {upper: lower for lower, upper in pairs}
    critical_by_dim = defaultdict(list)
    for f in sorted(critical, key=lambda s: (s.bit_count(), s)):
        critical_by_dim[f.bit_count()-1].append(f)
    matrices = {}
    for dimension in sorted(critical_by_dim):
        if dimension + 1 not in critical_by_dim:
            continue
        basis = {f: i for i, f in enumerate(critical_by_dim[dimension])}

        @lru_cache(None)
        def projection(s):
            if s in basis:
                return {basis[s]: 1}
            if s in upper_to_lower:
                return {}
            if s not in lower_to_upper:
                raise AssertionError(('unaccounted face', s))
            u = lower_to_upper[s]
            boundary = signed_facets(u)
            matched_sign = next(sign for f, sign in boundary if f == s)
            out = defaultdict(int)
            for face, coeff in boundary:
                if face != s:
                    for idx, factor in projection(face).items():
                        out[idx] -= matched_sign * coeff * factor
            return {idx: value for idx, value in out.items() if value}

        columns = []
        for u in critical_by_dim[dimension+1]:
            out = defaultdict(int)
            for f, coeff in signed_facets(u):
                for idx, factor in projection(f).items():
                    out[idx] += coeff * factor
            columns.append({idx: v for idx, v in out.items() if v})
        matrices[(dimension+1, dimension)] = columns
    return critical_by_dim, matrices


def determinant(a):
    n = len(a)
    total = 0
    for p in itertools.permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        term = (-1 if inversions & 1 else 1)
        for i, j in enumerate(p):
            term *= a[i][j]
        total += term
    return total


def mod2_rank(columns):
    pivots = {}
    for column in columns:
        while column:
            p = column.bit_length()-1
            if p in pivots:
                column ^= pivots[p]
            else:
                pivots[p] = column
                break
    return len(pivots)


def simplicial_mod2_ranks(faces):
    levels = defaultdict(list)
    for f in faces:
        levels[f.bit_count()].append(f)
    ranks = {}
    for k in range(1, max(levels)+1):
        rows = {f: idx for idx, f in enumerate(levels[k-1])}
        columns = []
        for u in levels[k]:
            column = 0
            for f, _ in signed_facets(u):
                column ^= 1 << rows[f]
            columns.append(column)
        ranks[k] = mod2_rank(columns)
    return ranks


def analyze(kind):
    E = make_graph(kind)
    triangles = check_srg(E)
    assert triangles == 32
    adjacency = [set() for _ in range(N)]
    for u, v in E:
        adjacency[u].add(v)
        adjacency[v].add(u)
    fs = []
    for mask in range(1 << N):
        a = is_forest_union_find(mask, E)
        b = is_forest_dfs(mask, adjacency)
        assert a == b, ('forest predicate disagreement', kind, mask)
        if a:
            fs.append(mask)
    fvector = [sum(f.bit_count() == k for f in fs) for k in range(8)]
    expect_f = ([1, 16, 120, 528, 1440, 2352, 1952, 512]
                if kind == 'Shrikhande' else
                [1, 16, 120, 528, 1392, 2160, 1728, 576])
    assert fvector == expect_f, (kind, fvector)
    pairs, critical = matching(fs)
    incidences = check_acyclic(fs, pairs)
    critical_by_dim, matrices = morse_differential(pairs, critical)
    counts = {str(dim): len(lst) for dim, lst in critical_by_dim.items()}
    expected_crit = ({'4': 2, '5': 143, '6': 36} if kind == 'Shrikhande'
                     else {'4': 4, '5': 37, '6': 72})
    assert counts == expected_crit, (kind, counts)
    d65 = matrices[(6, 5)]
    assert all(not col for col in d65)
    d54 = matrices[(5, 4)]
    small_dim = len(critical_by_dim[4])
    col_indices = ((7, 8) if kind == 'Shrikhande' else (0, 1, 2, 4))
    minor = [[d54[j].get(i, 0) for j in col_indices] for i in range(small_dim)]
    det = determinant(minor)
    assert abs(det) == 1
    ranks = simplicial_mod2_ranks(fs)
    expected_ranks = ({1: 1, 2: 15, 3: 105, 4: 423, 5: 1017, 6: 1335, 7: 476}
                      if kind == 'Shrikhande' else
                      {1: 1, 2: 15, 3: 105, 4: 423, 5: 969, 6: 1191, 7: 504})
    assert ranks == expected_ranks
    mod2_betti = {d-1: fvector[d] - ranks.get(d, 0) - ranks.get(d+1, 0)
                  for d in range(1, len(fvector))}
    expected_betti = ({5: 141, 6: 36} if kind == 'Shrikhande' else {5: 33, 6: 72})
    assert {k: v for k, v in mod2_betti.items() if v} == expected_betti
    assert (len(pairs), incidences) == ((3370, 34656) if kind == 'Shrikhande' else (3204, 32608))
    assert all(abs(v) == 1 for col in d54 for v in col.values())
    return {
        'name': kind,
        'graph_vertices': N,
        'graph_edges': len(E),
        'triangles': triangles,
        'strongly_regular_parameters': [16, 6, 2, 2],
        'faces_including_empty': len(fs),
        'face_vector_by_cardinality_0_to_7': fvector,
        'matched_pairs_including_empty_pair': len(pairs),
        'critical_reduced_by_dimension': counts,
        'directed_hasse_incidences_checked': incidences,
        'morse_differential_6_to_5_all_zero': True,
        'morse_differential_5_to_4_nonzero_entries': sum(len(c) for c in d54),
        'primitive_minor_column_indices': list(col_indices),
        'primitive_minor_critical_5_masks': [critical_by_dim[5][j] for j in col_indices],
        'critical_4_masks': critical_by_dim[4],
        'primitive_minor_matrix': minor,
        'primitive_minor_determinant': det,
        'ordinary_simplicial_mod2_boundary_ranks': {str(k): v for k, v in ranks.items()},
        'wedge_spheres': {str(k): v for k, v in expected_betti.items()},
    }


if __name__ == '__main__':
    reports = [analyze('Shrikhande'), analyze('Rook')]
    print(json.dumps(reports, sort_keys=True, indent=2))
    print('VERIFY_OK')
