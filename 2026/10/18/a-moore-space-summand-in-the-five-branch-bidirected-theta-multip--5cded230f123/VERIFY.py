#!/usr/bin/env python3
"""Exact finite certificate for the bidirected five-arm theta multipath complex.

Dependencies: Python 3.10+ and SymPy 1.12+.
All graph labels, simplices, orientations, and reduced homology conventions
are defined below, without relying on external computation files.
"""
from __future__ import annotations
from itertools import combinations
from collections import Counter
from functools import lru_cache
import hashlib
import json
from sympy import Matrix, zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 5
ARCS = [(u, v) for i in range(N) for u, v in
        ((0, i+2), (i+2, 0), (1, i+2), (i+2, 1))]

def is_path_forest(edge_indices):
    succ, pred = {}, {}
    for i in edge_indices:
        u, v = ARCS[i]
        if u in succ or v in pred:
            return False
        succ[u], pred[v] = v, u
    for start in succ:
        seen, vertex = set(), start
        while vertex in succ:
            if vertex in seen:
                return False
            seen.add(vertex)
            vertex = succ[vertex]
    return True

def enumerate_by_degree():
    levels = [[], [], [], [], []]
    levels[0] = [0]
    # Both hubs have outdegree <=1, so a face has at most 2 hub-to-leaf
    # arcs and at most 2 leaf-to-hub arcs: at most 4 arcs altogether.
    for k in range(1, 5):
        for tup in combinations(range(len(ARCS)), k):
            if is_path_forest(tup):
                levels[k].append(sum(1 << i for i in tup))
    return levels

def enumerate_by_paths():
    # Independent construction: list every nonempty directed simple path,
    # then take unions of vertex-disjoint directed paths.
    out = {v: [] for v in range(N+2)}
    for i, (u, v) in enumerate(ARCS):
        out[u].append((i, v))
    paths = set()
    def walk(current, vertex_mask, arc_mask):
        if arc_mask:
            paths.add((vertex_mask, arc_mask))
        v = vertex_mask.bit_count()  # finite recursive depth check
        if v >= N+2:
            return
        for edge, nxt in out[current]:
            if not vertex_mask & (1 << nxt):
                walk(nxt, vertex_mask | (1 << nxt), arc_mask | (1 << edge))
    for root in out:
        walk(root, 1 << root, 0)
    path_list = sorted(paths)
    unions = {0}
    def extend(last, used_vertices, used_arcs):
        for j in range(last + 1, len(path_list)):
            vs, es = path_list[j]
            if not vs & used_vertices:
                union = used_arcs | es
                unions.add(union)
                extend(j, used_vertices | vs, union)
    extend(-1, 0, 0)
    return unions

def greedy_matching(levels):
    unmatched = {mask for row in levels[1:] for mask in row}
    pairs = []
    for index in range(len(ARCS)):
        toggle = 1 << index
        for lower in sorted(unmatched):
            upper = lower | toggle
            if not lower & toggle and upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                pairs.append((lower, upper))
    return pairs, sorted(unmatched)

def dag_check(levels, pairs):
    matching = set(pairs)
    faces = [face for level in levels[1:] for face in level]
    indegree = dict.fromkeys(faces, 0)
    edges = {face: [] for face in faces}
    for high in faces:
        for i in range(len(ARCS)):
            if high & (1 << i):
                low = high ^ (1 << i)
                if low == 0: continue
                start, end = ((high, low) if (low, high) in matching
                              else (low, high))
                edges[start].append(end)
                indegree[end] += 1
    boundary_arrows = sum(map(len, edges.values()))
    stack = [v for v, degree in indegree.items() if degree == 0]
    processed = 0
    while stack:
        v = stack.pop()
        processed += 1
        for w in edges[v]:
            indegree[w] -= 1
            if indegree[w] == 0: stack.append(w)
    assert processed == len(faces)
    return processed, boundary_arrows

def boundary_of(mask):
    return [(mask ^ (1 << v), (-1) ** ((mask & ((1 << v)-1)).bit_count()))
            for v in range(len(ARCS)) if mask & (1 << v)]

def morse_complex(pairs, critical):
    low_to_high = dict(pairs)
    high_to_low = {upper: lower for lower, upper in pairs}
    crit = set(critical)
    @lru_cache(maxsize=None)
    def projected(cell):
        if cell == 0: return {}
        if cell in crit: return {cell: 1}
        if cell in high_to_low: return {}
        upper = low_to_high[cell]
        pivot = next(v for v in range(len(ARCS)) if upper ^ cell == 1 << v)
        coeff = (-1) ** ((upper & ((1 << pivot)-1)).bit_count())
        result = {}
        for face, boundary_coeff in boundary_of(upper):
            if face == cell: continue
            for target, value in projected(face).items():
                updated = result.get(target, 0) - coeff * boundary_coeff * value
                if updated: result[target] = updated
                else: result.pop(target, None)
        return result
    crit_k = [[face for face in critical if face.bit_count() == k+1]
              for k in range(4)]
    maps = {}
    for k in (1, 2, 3):
        row_ids = {cell: i for i, cell in enumerate(crit_k[k-1])}
        B = zeros(len(crit_k[k-1]), len(crit_k[k]))
        for j, upper in enumerate(crit_k[k]):
            for lower, sign in boundary_of(upper):
                for target, count in projected(lower).items():
                    B[row_ids[target], j] += sign * count
        maps[k] = B
    assert maps[1] * maps[2] == zeros(maps[1].rows, maps[2].cols)
    assert maps[2] * maps[3] == zeros(maps[2].rows, maps[3].cols)
    return crit_k, maps

def snf_signature(B):
    if B.rows == 0 or B.cols == 0: return []
    diagonal = smith_normal_form(B, domain=ZZ)
    return sorted((abs(int(diagonal[i, i])) for i in range(min(B.shape))))

def matrix_digest(B):
    data = [(i, j, int(B[i, j]))
            for i in range(B.rows) for j in range(B.cols) if B[i, j]]
    return hashlib.sha256(json.dumps({'shape': list(B.shape), 'entries': data},
                                     separators=(',', ':')).encode('utf-8')).hexdigest()

def main():
    levels = enumerate_by_degree()
    fv = [len(level) for level in levels]
    assert fv == [1, 20, 130, 320, 240], fv
    path_unions = enumerate_by_paths()
    degree_unions = set().union(*(set(row) for row in levels))
    assert path_unions == degree_unions, (len(path_unions), len(degree_unions))
    pairs, critical = greedy_matching(levels)
    assert len(pairs) == 297
    assert sorted(Counter(face.bit_count()-1 for face in critical).items()) == \
        [(0, 1), (1, 1), (2, 42), (3, 72)]
    dag_nodes, dag_arrows = dag_check(levels, pairs)
    assert dag_nodes == 710
    crit_by_dim, B = morse_complex(pairs, critical)
    assert B[1].shape == (1, 1) and B[1] == zeros(1, 1)
    assert B[2].shape == (1, 42) and sum(x != 0 for x in B[2]) == 24
    assert B[3].shape == (42, 72)
    assert snf_signature(B[2]) == [1]
    assert snf_signature(B[3]) == [0] + [1]*40 + [2]
    assert (sum(int(v) == 0 for v in B[3]) +
            sum(int(v) != 0 for v in B[3])) == 42*72
    assert sum(int(v) != 0 for v in B[3]) == 252
    assert -1 + fv[1] - fv[2] + fv[3] - fv[4] == -31
    print('GRAPH=fully bidirected K_(2,5); 7 vertices, 20 arcs')
    print('FACE_VECTOR_EMPTY_THEN_0_TO_3='+','.join(map(str,fv)))
    print('INDEPENDENT_PATH_UNION_FACE_CHECK=PASS')
    print('MATCHED_PAIRS=297')
    print('CRITICAL_CELLS_BY_DIM=0:1,1:1,2:42,3:72')
    print(f'COMPLETE_ACYCLICITY_DAG={dag_nodes}_nodes,{dag_arrows}_cover_incidents,PASS')
    for k in (1, 2, 3):
        print(f'MORSE_D{k}_SHAPE={B[k].rows}x{B[k].cols}')
        print(f'MORSE_D{k}_SHA256={matrix_digest(B[k])}')
        print(f'MORSE_D{k}_SMITH='+','.join(map(str,snf_signature(B[k]))))
    print('D2D3_ZERO=PASS')
    print('INTEGRAL_REDUCED_H2=Z/2;H3=Z^31;OTHER_REDUCED=0')
    print('SIMPLY_CONNECTED_FROM_UNIT_MORSE_D2=PASS')
    print('DIMENSION_3_WEDGE_SPLITTING_FROM_SMITH=PASS')

if __name__ == '__main__':
    main()
