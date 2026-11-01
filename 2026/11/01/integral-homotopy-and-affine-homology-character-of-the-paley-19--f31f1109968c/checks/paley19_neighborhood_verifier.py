#!/usr/bin/env python3
"""Exact finite verification: quadratic-residue tournament of order 19.

Constructs an ordinary out-neighborhood simplicial complex. Checks full acyclic
matching, reduced integral Morse differential, a unimodular minor, independent
mod-two homology, and the natural affine-group Lefschetz character.
Requires only the Python 3 standard library.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations

N = 19
Q = frozenset((i*i) % N for i in range(1, N))


def outgoing(v):
    return sum(1 << w for w in range(N) if (w-v) % N in Q)


def by_facets():
    F = {0}
    for v in range(N):
        facet = outgoing(v)
        s = facet
        while s:
            F.add(s)
            s = (s-1) & facet
    return F


def by_witness():
    # Independent predicate, scanning all potential subsets with nonzero size.
    facets = [outgoing(v) for v in range(N)]
    result = {0}
    for s in range(1, 1 << N):
        if any((s & f) == s for f in facets):
            result.add(s)
    return result


def matching(F):
    unused = set(F) - {0}
    pairs = []
    for v in range(N):
        bit = 1 << v
        for s in sorted(unused, key=lambda x: (x.bit_count(), x)):
            if s not in unused or (s & bit):
                continue
            t = s | bit
            if t in unused:
                unused.remove(s)
                unused.remove(t)
                pairs.append((s, t))
    return unused, pairs


def verify_acyclic(F, pairs):
    nonempty = set(F) - {0}
    matched = set(pairs)
    indegree = {s: 0 for s in nonempty}
    adjacency = {s: [] for s in nonempty}
    incidence_count = 0
    for t in nonempty:
        b = t
        while b:
            v = b & -b
            b -= v
            s = t ^ v
            if s == 0:
                continue
            assert s in nonempty
            source, target = ((s, t) if (s, t) in matched else (t, s))
            adjacency[source].append(target)
            indegree[target] += 1
            incidence_count += 1
    ready = [s for s in nonempty if indegree[s] == 0]
    processed = 0
    while ready:
        source = ready.pop()
        processed += 1
        for target in adjacency[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                ready.append(target)
    return processed, len(nonempty), incidence_count


def signed_boundary(t):
    return [(t ^ (1 << v), (-1)**i)
            for i, v in enumerate(v for v in range(N) if (t >> v) & 1)]


def morse_boundary(critical, pairs):
    C2 = sorted(s for s in critical if s.bit_count() == 3)
    C3 = sorted(s for s in critical if s.bit_count() == 4)
    index = {s:i for i,s in enumerate(C2)}
    lower_to_upper = {s:t for s,t in pairs if s.bit_count() == 3}

    @lru_cache(None)
    def reduce_triangle(s):
        if s in index:
            res = [0] * len(C2)
            res[index[s]] = 1
            return tuple(res)
        if s not in lower_to_upper:
            # An upper cell of a matching between dimensions 1 and 2.
            return (0,) * len(C2)
        upper = lower_to_upper[s]
        b = signed_boundary(upper)
        coeff_s = dict(b)[s]
        assert coeff_s in (-1,1)
        result = [0] * len(C2)
        for other, coeff in b:
            if other == s:
                continue
            reduced = reduce_triangle(other)
            for k, value in enumerate(reduced):
                result[k] -= coeff * coeff_s * value
        return tuple(result)

    columns = []
    for cell in C3:
        answer = [0] * len(C2)
        for s, coeff in signed_boundary(cell):
            red = reduce_triangle(s)
            for k, value in enumerate(red):
                answer[k] += coeff * value
        columns.append(answer)
    return C2, C3, columns


def determinant3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def binary_ranks(F):
    groups = {k: sorted(s for s in F if s.bit_count()==k+1)
              for k in range(9)}
    ranks = {}
    for k in range(1, 9):
        idx = {s:i for i,s in enumerate(groups[k-1])}
        pivots = {}
        for upper in groups[k]:
            b = upper
            mask = 0
            while b:
                bit=b & -b
                b -= bit
                mask ^= 1 << idx[upper ^ bit]
            while mask:
                lead = mask.bit_length()-1
                if lead not in pivots:
                    pivots[lead] = mask
                    break
                mask ^= pivots[lead]
        ranks[k] = len(pivots)
    betti = {k:len(groups[k]) - ranks.get(k,0) - ranks.get(k+1,0)
             for k in groups}
    betti[0] -= 1
    return ranks, betti


def lefschetz(F, perm):
    total = 0
    for s in F:
        if not s:
            continue
        vertices = [v for v in range(N) if s >> v & 1]
        moved = [perm[v] for v in vertices]
        if sum(1 << v for v in moved) != s:
            continue
        inversions = sum(moved[i] > moved[j] for i in range(len(moved))
                         for j in range(i+1, len(moved)))
        total += (-1)**(len(vertices)-1+inversions)
    return total


def main():
    assert Q == frozenset({1,4,5,6,7,9,11,16,17})
    assert all(((j-i)%N in Q) != ((i-j)%N in Q)
               for i in range(N) for j in range(i+1,N))
    facets = [outgoing(v) for v in range(N)]
    assert len(set(facets))==19
    assert all(f.bit_count()==9 for f in facets)
    assert all((a&b).bit_count()==4 for a,b in combinations(facets,2))
    F=by_facets()
    assert F==by_witness()
    fvector=tuple(sum(s.bit_count()==k+1 for s in F) for k in range(9))
    assert fvector == (19,171,969,2223,2394,1596,684,171,19)
    assert len(F)==8247
    critical,pairs=matching(F)
    types=Counter(s.bit_count()-1 for s in critical)
    assert types==Counter({0:1,2:4,3:81})
    assert len(pairs)==4080
    processed, total, incidences=verify_acyclic(F,pairs)
    assert (processed,total,incidences)==(8246,8246,40014)
    C2,C3,cols=morse_boundary(critical,pairs)
    assert len(C2)==4 and len(C3)==81
    # An exact integral kernel relation and a primitive maximal-rank minor.
    assert all(c[0] - 2*c[1] - c[2] + c[3] == 0 for c in cols)
    minor=determinant3([[cols[j][i] for j in (0,1,4)] for i in (0,1,2)])
    assert minor==-1
    # Hence the integral boundary has rank 3 and all nonzero Smith factors 1.
    ranks, betti=binary_ranks(F)
    assert betti == {0:0,1:0,2:1,3:78,4:0,5:0,6:0,7:0,8:0}
    assert sum((-1)**i*v for i,v in enumerate(fvector))==-76
    # Since the affine group has odd order, its 1D rational H2-module is trivial.
    chars=Counter()
    group=set()
    for a in sorted(Q):
        for b in range(N):
            perm=tuple((a*v+b)%N for v in range(N))
            group.add(perm)
            assert all(((j-i)%N in Q)==((perm[j]-perm[i])%N in Q)
                       for i in range(N) for j in range(N))
            # L=1+tr(H2)-tr(H3)=2-tr(H3).
            chars[2-lefschetz(F,perm)] += 1
    assert len(group)==171
    assert chars == Counter({78:1, 2:18, -3:38, 0:114})
    assert sum(trace*number for trace,number in chars.items())==0
    print('PALEY19_NEIGHBORHOOD_INTEGRAL_WEDGE_AND_AFFINE_CHARACTER_OK')
    print('residue_set:',sorted(Q))
    print('faces_including_empty:',len(F),'f_vector:',fvector)
    print('matching_pairs:',len(pairs),'critical_cells:',dict(sorted(types.items())))
    print('matched_hasse_topological_sort:',processed,'of',total,'incidences:',incidences)
    print('morse_matrix_shape:',(len(C2),len(C3)), 'exact_kernel_row_relation:',(1,-2,-1,1))
    print('unimodular_minor_rows:',(0,1,2),'columns:',(0,1,4),'determinant:',minor)
    print('critical_2_faces:',[tuple(v for v in range(N) if s>>v&1) for s in C2])
    print('critical_3_faces_for_minor:',[tuple(v for v in range(N) if C3[j]>>v&1) for j in (0,1,4)])
    print('mod2_boundary_ranks:',dict(sorted(ranks.items())))
    print('mod2_reduced_betti:',dict(sorted(betti.items())))
    print('affine_group_order:',len(group),'third_homology_trace_distribution:',dict(sorted(chars.items())))
    print('affine_invariant_dimensions_h2_h3:',(1,0))

if __name__=='__main__':
    main()
