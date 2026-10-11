#!/usr/bin/env python3
"""Exact integral discrete-Morse proof for the Desargues matching complex.

Python standard library only. Run: python verify_desargues_homotopy.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

SUBSETS2 = list(combinations(range(5), 2))
SUBSETS3 = list(combinations(range(5), 3))
EDGES = tuple(
    (a, 10 + b) for a, s in enumerate(SUBSETS2)
    for b, t in enumerate(SUBSETS3) if set(s).issubset(t)
)
ORDER = (24, 11, 9, 0, 5, 6, 7, 16, 14, 26, 18, 27, 20,
         19, 28, 17, 23, 21, 29, 2, 25, 1, 22, 4, 3,
         8, 15, 12, 13, 10)


def graph_checks():
    assert len(EDGES) == 30 and len(set(EDGES)) == 30
    deg = Counter(v for e in EDGES for v in e)
    assert len(deg) == 20 and set(deg.values()) == {3}
    # Explicit graph isomorphism GP(10,3) -> middle-level graph.
    phi = (0, 10, 4, 16, 7, 19, 9, 15, 3, 12,
           11, 1, 17, 5, 13, 8, 18, 2, 14, 6)
    assert set(phi) == set(range(20))
    gp_edges = set()
    for i in range(10):
        gp_edges.add(frozenset((i, (i+1) % 10)))
        gp_edges.add(frozenset((i, i+10)))
        gp_edges.add(frozenset((i+10, (i+3) % 10+10)))
    assert {frozenset((phi[i],phi[j])) for ij in gp_edges
            for i,j in [tuple(ij)]} == {frozenset(x) for x in EDGES}


def all_faces():
    faces = set()
    def recurse(i, occupied, face):
        if i == len(EDGES):
            faces.add(face)
            return
        recurse(i+1, occupied, face)
        a,b = EDGES[i]
        endpoint_mask = (1<<a) | (1<<b)
        if occupied & endpoint_mask == 0:
            recurse(i+1, occupied | endpoint_mask, face | (1<<i))
    recurse(0,0,0)
    assert Counter(f.bit_count() for f in faces) == dict(enumerate(
        (1,30,375,2540,10155,24486,34945,27840,11040,1720,60)))
    return faces


def matching(faces):
    available = set(faces)
    pairs = []
    for vertex in ORDER:
        bit = 1<<vertex
        for lower in tuple(available):
            if lower & bit == 0 and (lower | bit) in available:
                upper = lower | bit
                available.remove(lower)
                available.remove(upper)
                pairs.append((lower,upper))
    assert len(pairs) == 56568
    # The augmented pair (empty, singleton) is not an ordinary CW pairing.
    empty_pair = [(a,b) for a,b in pairs if a == 0]
    assert len(empty_pair) == 1
    pairs = [(a,b) for a,b in pairs if a != 0]
    critical = available | {empty_pair[0][1]}
    assert len(pairs) == 56567
    assert Counter(v.bit_count()-1 for v in critical) == {0:1,5:8,6:48}
    return pairs,critical


def hodge_check(faces,pairs):
    """Topologically sort the entire *ordinary* oriented Hasse diagram."""
    lower_to_upper = dict(pairs)
    # A directed edge points upward for matched incidence, downward otherwise.
    arcs = defaultdict(list)
    indeg = {s:0 for s in faces if s}
    incidence = 0
    for upper in indeg:
        rem = upper
        while rem:
            bit = rem & -rem
            rem -= bit
            lower = upper ^ bit
            if not lower:
                continue
            incidence += 1
            source,target = ((lower,upper) if lower_to_upper.get(lower)==upper
                             else (upper,lower))
            arcs[source].append(target)
            indeg[target] += 1
    assert incidence == 680370
    todo=deque(s for s,d in indeg.items() if d==0)
    visited=0
    while todo:
        a=todo.popleft();visited+=1
        for b in arcs.get(a,()):
            indeg[b]-=1
            if indeg[b]==0:
                todo.append(b)
    assert visited == len(faces)-1, (visited,len(faces)-1)
    return incidence


def orient_boundary(mask):
    """Yield codimension-one faces with standard ordered-simplex signs."""
    bit_index = 0
    while mask:
        lowbit = mask & -mask
        yield lowbit, (1 if bit_index % 2==0 else -1)
        mask ^= lowbit
        bit_index += 1


def integral_morse_d6(pairs,critical):
    lower_up=dict(pairs)
    matched_uppers={b for a,b in pairs}

    @lru_cache(None)
    def reduce_lower(simplex):
        if simplex in lower_up:
            upper=lower_up[simplex]
            pivot=next(sign for bit,sign in orient_boundary(upper)
                       if upper ^ bit == simplex)
            out=defaultdict(int)
            for bit,sign in orient_boundary(upper):
                next_face=upper ^ bit
                if next_face == simplex:
                    continue
                for c,val in reduce_lower(next_face).items():
                    out[c] -= pivot*sign*val
            return {k:v for k,v in out.items() if v}
        if simplex in matched_uppers:
            return {}
        assert simplex in critical
        return {simplex:1}

    critical_5=sorted(s for s in critical if s.bit_count()==6)
    critical_6=sorted(s for s in critical if s.bit_count()==7)
    assert len(critical_5)==8 and len(critical_6)==48
    idx={mask:j for j,mask in enumerate(critical_5)}
    mat=[[0 for _ in critical_6] for _ in critical_5]
    for j,higher in enumerate(critical_6):
        acc=defaultdict(int)
        for bit,sign in orient_boundary(higher):
            for lower,val in reduce_lower(higher ^ bit).items():
                acc[lower] += sign*val
        for lower,val in acc.items():
            mat[idx[lower]][j] = val
    assert sum(bool(v) for row in mat for v in row)==25
    assert all(v in (-1,0,1) for row in mat for v in row)
    # Exact integer normal form without numeric or floating-point rank estimates:
    # every column is 0, +(e0-e1), -(e0-e1), +/-e3, or +/-(e6-e7).
    vectors=(tuple(int(i==0)-int(i==1) for i in range(8)),
             tuple(int(i==3) for i in range(8)),
             tuple(int(i==6)-int(i==7) for i in range(8)))
    columns=[tuple(mat[i][j] for i in range(8)) for j in range(48)]
    assert all(tuple(c[0]*vectors[0][i]+c[3]*vectors[1][i]+c[6]*vectors[2][i] for i in range(8)) == c for c in columns)
    assert all(max(abs(v) for v in (c[0],c[3],c[6])) <= 1 for c in columns)
    assert [columns[2], columns[9], columns[36]] == list(vectors)
    assert set(columns) - {(0,)*8}
    return mat,reduce_lower.cache_info()


def main():
    graph_checks()
    faces=all_faces()
    pairs,critical=matching(faces)
    incidence=hodge_check(faces,pairs)
    mat,cache=integral_morse_d6(pairs,critical)
    print('DESARGUES_HOMOTOPY_VERIFY_OK',
          'faces_with_empty='+str(len(faces)),
          'matched_pairs='+str(len(pairs)),
          'critical=1x0+8x5+48x6',
          'oriented_incidences='+str(incidence),
          'integer_d6=3_unit_pivots',
          'homotopy=5xS5+45xS6',
          'gradient_expansions='+str(cache.misses))

if __name__ == '__main__':
    main()
