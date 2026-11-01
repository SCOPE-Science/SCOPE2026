#!/usr/bin/env python3
"""Exact finite homotopy verification for the two-matching complex of K_{2,2,2}.

Python 3.9+ standard library only. Run: python3 verify_octahedral_two_matching.py
An edge-subset is encoded as a bitmask in lexicographic edge order.
"""
from collections import Counter
from itertools import combinations

N = 6
EDGES = tuple((i,j) for i in range(N) for j in range(i+1,N) if i//2 != j//2)
assert len(EDGES) == 12


def eligible_degree(mask):
    deg = [0] * N
    for e,(a,b) in enumerate(EDGES):
        if mask & (1 << e):
            deg[a] += 1
            deg[b] += 1
            if deg[a] > 2 or deg[b] > 2:
                return False
    return True

FORBIDDEN = tuple(sum(1 << e for e in triple)
    for v in range(N)
    for triple in combinations([e for e,(a,b) in enumerate(EDGES) if a == v or b == v], 3))
assert len(FORBIDDEN) == 24 and len(set(FORBIDDEN)) == 24

def eligible_forbidden_triples(mask):
    return not any((mask & f) == f for f in FORBIDDEN)


def reduced_boundary(mask):
    """Signed augmented simplicial boundary over Z, including vertex -> empty."""
    out = {}
    position = 0
    for e in range(len(EDGES)):
        if mask & (1 << e):
            out[mask ^ (1 << e)] = (-1) ** position
            position += 1
    return out


def finite_matching(faces):
    remaining = set(faces)
    pair = []
    for e in range(len(EDGES)):
        for low in sorted(remaining):
            high = low | (1 << e)
            if not low & (1 << e) and high in remaining:
                remaining.remove(low)
                remaining.remove(high)
                pair.append((low,high))
    return remaining, pair


def check_acyclic(faces, pairs):
    matched = set(pairs)
    in_deg = {m:0 for m in faces}
    arrows = {m:[] for m in faces}
    incidences = 0
    for high in faces:
        for e in range(len(EDGES)):
            if high & (1 << e):
                low = high ^ (1 << e)
                src,dst = (low,high) if (low,high) in matched else (high,low)
                arrows[src].append(dst)
                in_deg[dst] += 1
                incidences += 1
    queue = [m for m in faces if in_deg[m] == 0]
    for m in queue:
        for nxt in arrows[m]:
            in_deg[nxt] -= 1
            if in_deg[nxt] == 0:
                queue.append(nxt)
    assert len(queue) == len(faces), (len(queue), len(faces))
    return incidences


def cancel_paired_cells(faces, pairs):
    """Integral elementary algebraic Morse cancellation (unit-pivot Schur complement).

    Each cancellation removes one matched adjacent pair in a based free chain
    complex, preserves the chain homotopy type, and uses only +/-1 pivots.
    The sorted choice makes the result deterministic.
    """
    d = {m:reduced_boundary(m) for m in faces}
    pending = set(pairs)
    cancellations = 0
    while pending:
        eligible = []
        for low,high in pending:
            pivot = d[high].get(low,0)
            if abs(pivot) == 1:
                ncol = len(d[high])
                nrow = sum(low in col for c,col in d.items() if c != high)
                eligible.append((ncol*nrow,ncol+nrow,low,high,pivot))
        assert eligible, 'An acyclic pair did not admit a unit cancellation'
        _,_,low,high,pivot = min(eligible)
        dh = d[high]
        for other,col in d.items():
            if other == high:
                continue
            incidence = col.get(low,0)
            if incidence:
                multiplier = incidence * pivot    # pivot = +/-1
                for target,coefficient in dh.items():
                    result = col.get(target,0) - multiplier * coefficient
                    if result:col[target] = result
                    else:col.pop(target,None)
        d.pop(low)
        d.pop(high)
        for col in d.values():
            col.pop(low,None)
            col.pop(high,None)
        pending.remove((low,high))
        cancellations += 1
    return d,cancellations


def mod2_ranks(faces):
    by_degree = {}
    for m in faces:
        by_degree.setdefault(m.bit_count()-1,[]).append(m)
    ranks = {-1:0}
    for k in range(0,6):
        lower = {f:i for i,f in enumerate(by_degree[k-1])}
        pivot_map = {}
        for m in by_degree[k]:
            b = 0
            for e in range(len(EDGES)):
                if m & (1 << e):
                    b ^= 1 << lower[m ^ (1 << e)]
            while b:
                pivot = b.bit_length()-1
                if pivot not in pivot_map:
                    pivot_map[pivot] = b
                    break
                b ^= pivot_map[pivot]
        ranks[k] = len(pivot_map)
    betti = {k:len(by_degree[k]) - ranks[k] - ranks.get(k+1,0)
        for k in range(0,6)}
    return ranks,betti


def determinant3(mat,rows,cols):
    x = [[mat[i][j] for j in cols] for i in rows]
    return (x[0][0]*(x[1][1]*x[2][2]-x[1][2]*x[2][1])
           -x[0][1]*(x[1][0]*x[2][2]-x[1][2]*x[2][0])
           +x[0][2]*(x[1][0]*x[2][1]-x[1][1]*x[2][0]))


def main():
    eligible = [m for m in range(1 << len(EDGES)) if eligible_degree(m)]
    assert all(eligible_degree(m) == eligible_forbidden_triples(m)
               for m in range(1 << len(EDGES)))
    assert len(eligible) == 772
    faces = set(eligible)
    assert 0 in faces
    for m in faces:
        for low in reduced_boundary(m):
            assert low in faces
        dd = {}
        for first,coef1 in reduced_boundary(m).items():
            for second,coef2 in reduced_boundary(first).items():
                dd[second] = dd.get(second,0) + coef1*coef2
        assert not any(dd.values())
    dims = Counter(m.bit_count()-1 for m in eligible)
    assert [dims[i] for i in range(-1,6)] == [1,12,66,196,297,180,20]
    facets = [m for m in eligible if not any((m | (1 << e)) in faces for e in range(12) if not m & (1<<e))]
    facet_dims = Counter(m.bit_count()-1 for m in facets)
    assert facet_dims == {3:3,4:60,5:20}
    critical,pairs = finite_matching(eligible)
    assert len(pairs) == 378
    assert Counter(m.bit_count()-1 for m in critical) == {3:6,4:10}
    assert len(pairs)*2 + len(critical) == len(eligible)
    incidences = check_acyclic(eligible,pairs)
    assert incidences == 2940
    reduced,cancelled = cancel_paired_cells(eligible,pairs)
    assert cancelled == 378
    assert set(reduced) == critical
    assert all(not reduced[m] for m in reduced if m.bit_count() == 4)
    low = sorted(m for m in critical if m.bit_count()==4)
    high = sorted(m for m in critical if m.bit_count()==5)
    matrix = [[reduced[h].get(l,0) for h in high] for l in low]
    assert len(matrix) == 6 and all(len(row)==10 for row in matrix)
    assert matrix[4] == matrix[5] == [0]*10
    assert all(matrix[3][j] == -sum(matrix[i][j] for i in range(3)) for j in range(10))
    unit_minor = determinant3(matrix,(0,1,2),(0,1,4))
    assert unit_minor == 1
    # Unit 3 x 3 minor and a zero fourth independent row prove the Smith
    # invariants are (1,1,1), with no torsion in reduced homology.
    ranks,betti = mod2_ranks(eligible)
    assert [ranks[k] for k in range(0,6)] == [1,11,55,141,153,20]
    assert [betti[k] for k in range(0,6)] == [0,0,0,3,7,0]
    print('graph=K_2,2,2; vertices=6; edges=12')
    print('edges=' + repr(EDGES))
    print('faces_including_empty=772; f_vector=' + repr(tuple(dims[i] for i in range(0,6))))
    print('facet_dimensions=' + repr(dict(sorted(facet_dims.items()))))
    print('independent_membership_checks=4096; chain_squared_zero=PASS')
    print('matching_pairs=378; critical_dimensions=' + repr({3:6,4:10}))
    print('full_Hasse_incidences=2940; acyclic=PASS')
    print('integral_unit_cancellations=' + str(cancelled))
    print('critical_3_masks=' + repr(low))
    print('critical_4_masks=' + repr(high))
    print('integral_Morse_d4_rows=' + repr(matrix))
    print('rank_3_upper_bound=two_zero_rows_plus_one_relation')
    print('rank_3_lower_bound=det_3x3_rows_0_1_2_cols_0_1_4=' + str(unit_minor))
    print('Smith_factors_1_1_1=PASS')
    print('independent_augmented_mod2_boundary_ranks=' + repr(tuple(ranks[i] for i in range(6))))
    print('reduced_homology_ranks=(beta3=3,beta4=7); integral_torsion=NONE')
    print('HOMOTOPY_WEDGE_3_S3_AND_7_S4_VERIFIED')

if __name__ == '__main__':
    main()
