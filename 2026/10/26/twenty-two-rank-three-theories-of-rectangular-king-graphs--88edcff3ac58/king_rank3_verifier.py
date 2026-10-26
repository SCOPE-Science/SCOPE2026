#!/usr/bin/env python3
"""Exact rank-three first-order profiles of rectangular king graphs.

Pure adjacency/equality only. A 0-type is an equality/adjacency diagram;
a (r+1)-type is an atomic r-type and the SET of its one-vertex
extensions' r-types. Thus these programs perform complete quantifier-rank
three calculations, not finite samples of first-order formulas.
"""
import itertools
import hashlib
import json


def king(m, n):
    verts = list(itertools.product(range(m), range(n)))
    N = len(verts)
    E = [[False] * N for _ in range(N)]
    for a, (i, j) in enumerate(verts):
        for b, (k, l) in enumerate(verts):
            E[a][b] = a != b and abs(i-k) <= 1 and abs(j-l) <= 1
    return E


def exact_type(E):
    """Nested atomic-diagram extensions, including all repeated vertices."""
    N = len(E)
    def atomic(a,b,c):
        return ((a==b), (a==c), (b==c), E[a][b], E[a][c], E[b][c])
    pairs = {}
    for a in range(N):
        for b in range(N):
            pairs[a,b] = ((a==b), E[a][b],
                          frozenset(atomic(a,b,c) for c in range(N)))
    point_types = frozenset(
        frozenset(pairs[a,b] for b in range(N)) for a in range(N)
    )
    return point_types


def independent_bit_type(E):
    """Independent neighborhood-mask interpretation of the same 3-game."""
    N = len(E)
    vertex_types = set()
    for a in range(N):
        pair_types = set()
        for b in range(N):
            msk = 0
            for c in range(N):
                if c != a and c != b:
                    msk |= 1 << (2 * int(E[a][c]) + int(E[b][c]))
            pair_types.add((a == b, E[a][b], msk))
        vertex_types.add(frozenset(pair_types))
    return frozenset(vertex_types)


def canonical_classes(tfun):
    classes = {}
    for a in range(1, 8):
        for b in range(a, 8):
            classes.setdefault(tfun(king(a,b)), []).append((a,b))
    result = sorted(classes.values(), key=lambda group: min(group))
    return result


def group_label(group):
    a,b = min(group, key=lambda xy:(xy[0]*xy[1],xy))
    return f'{a}x{b}'


def main():
    A = canonical_classes(exact_type)
    B = canonical_classes(independent_bit_type)
    assert A == B, 'independent type recursions disagree'
    assert len(A) == 22, len(A)
    assert len(set(t for g in A for t in g)) == 28
    min_reps = [min(g,key=lambda xy: (xy[0]*xy[1],xy)) for g in A]
    assert max(x*y for x,y in min_reps) == 30
    assert (5,6) in min_reps
    assert [(3,7),(4,6),(4,7)] in A
    assert [(5,6),(5,7),(6,6),(6,7),(7,7)] in A
    # Every larger coordinate is already equivalent to 7, as proved via
    # the EF product lemma and the 7-vertex undirected-path cutoff.
    canon = {p:i+1 for i,g in enumerate(A) for p in g}
    for m in range(1,13):
        for n in range(m,13):
            j = canon[tuple(sorted((min(m,7),min(n,7))))]
            # full atomic recursion on every independently constructed graph
            target = exact_type(king(*min_reps[j-1]))
            assert exact_type(king(m,n)) == target, (m,n,j)
    # Full path rank-3 stability, separate from the infinite proof.
    p7 = exact_type(king(1,7))
    for n in range(7,31):
        assert exact_type(king(1,n)) == p7
    cert = {
        'method':'exact atomic three-variable extension types and independent neighborhood masks',
        'language':'simple undirected graph adjacency and equality',
        'rank':3,
        'canonical_parameter_pairs':28,
        'class_count':len(A),
        'least_representatives':[{'m':a,'n':b,'order':a*b} for a,b in min_reps],
        'classes':[
           {'class':i+1,'representative':list(min_reps[i]),
            'canonical_pairs':[list(p) for p in g]}
           for i,g in enumerate(A)
        ],
        'largest_minimum_order':30,
        'nontrivial_equivalences':[[[3,7],[4,6]],[[5,6],[7,7]]],
        'tested_parameter_pairs_up_to_12':78,
        'complete_theoretical_upper_reduction':'min(m,7), min(n,7) via 3-round product strategy',
    }
    print(f'CANONICAL_OK pairs=28 classes={len(A)} independent_algorithms=2')
    print('PATH_CHECK_OK n=7..30')
    print('EXTERNAL_PARAMS_OK unordered_pairs_m_n_1_to_12=78')
    print('CROSS_SHAPE_EQUIVALENCE_OK 3x7=4x6 5x6=7x7')
    print('SHARP_BOUND_OK minimum_maximum_representative_order=30')
    print('VERIFY_OK')
    with open('classification.json','w',encoding='utf-8') as f:
        json.dump(cert,f,indent=2,ensure_ascii=False)
        f.write('\n')

if __name__=='__main__':
    main()
