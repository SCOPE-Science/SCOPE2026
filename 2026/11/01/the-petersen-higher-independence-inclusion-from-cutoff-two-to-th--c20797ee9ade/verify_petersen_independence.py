#!/usr/bin/env python3
"""Exact finite integer-chain verification for the Petersen higher-independence inclusion.

Run: python3 verify_petersen_independence.py
No external libraries, file dependencies, or network access required.
"""
from itertools import combinations
from collections import Counter, defaultdict, deque
from functools import lru_cache

VERTICES = tuple(combinations(range(5), 2))
N = len(VERTICES)
NEIGHBORS = tuple(sum(1 << j for j, w in enumerate(VERTICES)
                      if i != j and set(v).isdisjoint(w))
                  for i, v in enumerate(VERTICES))


def good(mask, cutoff):
    todo = mask
    while todo:
        first = todo & -todo
        todo ^= first
        reached = first
        frontier = first
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            v = bit.bit_length() - 1
            nxt = NEIGHBORS[v] & todo
            frontier |= nxt
            reached |= nxt
            todo ^= nxt
        if reached.bit_count() > cutoff:
            return False
    return True


def oriented_boundary(mask):
    return {mask ^ (1 << i): (-1 if (mask & ((1 << i) - 1)).bit_count() % 2 else 1)
            for i in range(N) if mask & (1 << i)}


def build(cutoff):
    faces = {m for m in range(1 << N) if good(m, cutoff)}
    unmatched = faces.copy()
    pairs = {}
    upper = {}
    for i in range(N):
        for face in sorted(unmatched):
            other = face | (1 << i)
            if not (face & (1 << i)) and other in unmatched:
                unmatched.remove(face)
                unmatched.remove(other)
                pairs[face] = other
                upper[other] = face
    assert len(faces) == 2 * len(pairs) + len(unmatched)
    # The Hasse digraph: unmatched covering relations point downward,
    # while matching relations point upward. Every edge is constructed.
    adj = {m: [] for m in faces}
    indeg = {m: 0 for m in faces}
    count = 0
    for higher in faces:
        for lower in oriented_boundary(higher):
            if pairs.get(lower) == higher:
                src, dst = lower, higher
            else:
                src, dst = higher, lower
            adj[src].append(dst)
            indeg[dst] += 1
            count += 1
    work = deque(m for m, val in indeg.items() if val == 0)
    visited = 0
    while work:
        a = work.popleft()
        visited += 1
        for b in adj[a]:
            indeg[b] -= 1
            if indeg[b] == 0:
                work.append(b)
    assert visited == len(faces), "Nonacyclic Morse matching"
    @lru_cache(None)
    def project(face):
        if face in unmatched:
            return {face: 1}
        if face in upper:
            return {}
        b = pairs[face]
        coefficients = oriented_boundary(b)
        s = coefficients.pop(face)
        result = defaultdict(int)
        for other, coeff in coefficients.items():
            for critical, val in project(other).items():
                result[critical] -= coeff * val * s
        return {critical: val for critical, val in result.items() if val}
    crit = {d: tuple(sorted(a for a in unmatched if a.bit_count() - 1 == d))
            for d in range(-1, 6)}
    def morse_boundary(face):
        result = defaultdict(int)
        for child, coeff in oriented_boundary(face).items():
            for critface, v in project(child).items():
                result[critface] += coeff * v
        return {a: v for a, v in result.items() if v}
    return faces, pairs, crit, project, morse_boundary, count


def check():
    assert len(VERTICES) == 10
    assert sum(t.bit_count() for t in NEIGHBORS) == 30
    f2, p2, c2, P2, d2, h2 = build(2)
    f3, p3, c3, P3, d3, h3 = build(3)
    assert f2.issubset(f3)
    assert len(f2) == 261 and len(p2) == 130 and len(f3) == 381 and len(p3) == 187
    assert Counter(m.bit_count() - 1 for m in f2) == {-1: 1, 0: 10, 1: 45, 2: 90, 3: 80, 4: 30, 5: 5}
    assert Counter(m.bit_count() - 1 for m in f3) == {-1: 1, 0: 10, 1: 45, 2: 120, 3: 140, 4: 60, 5: 5}
    assert {d: v for d,v in c2.items() if v} == {3: (912,)}
    assert {d: v for d,v in c3.items() if v} == {2: (530,), 3: (660,712,792,808), 4: (944,976)}
    assert all(d2(a) == {} for a in c2[3])
    assert [d3(a).get(530, 0) for a in c3[3]] == [-1,0,-1,0]
    assert [[d3(a).get(b, 0) for b in c3[3]] for a in c3[4]] == [[1,0,-1,1],[1,1,-1,0]]
    # A 25-tetrahedron oriented integral cycle for the cutoff-two complex.
    SUPPORT = [15,113,135,147,165,177,267,275,329,337,402,525,526,
               549,585,609,624,646,676,688,778,840,848,898,912]
    COEFF = [1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,1,1,-1,1,
             -1,-1,-1,1,1,1,-1,-1,1]
    assert len(SUPPORT) == len(COEFF) == 25
    assert all(x in f2 and x.bit_count() == 4 for x in SUPPORT)
    boundary = defaultdict(int)
    for simplex, coeff in zip(SUPPORT, COEFF):
        for lower, sign in oriented_boundary(simplex).items():
            boundary[lower] += coeff * sign
    assert all(v == 0 for v in boundary.values()), "The integral chain is not a cycle"
    def project_cycle(proj):
        out = defaultdict(int)
        for simplex, coeff in zip(SUPPORT, COEFF):
            for crit, val in proj(simplex).items():
                out[crit] += coeff * val
        return {k:v for k,v in out.items() if v}
    assert project_cycle(P2) == {912:1}
    assert project_cycle(P3) == {660:-1,792:1}
    # In the integral Morse model for cutoff three, put
    # x = [792]-[660], u=[712], v=[808]. Then ∂_4 has columns
    # -x+v and -x+u. Thus the 3-homology is freely generated by x,
    # and the integer cycle above maps precisely to x.
    assert d3(944) == {660:1,792:-1,808:1}
    assert d3(976) == {660:1,712:1,792:-1}
    assert h2 > 0 and h3 > 0
    print('PETERSEN_IND2_TO_IND3_INTEGRAL_HOMOTOPY_EQUIVALENCE_OK')
    print('ind2_faces=%d ind3_faces=%d hasse_edges=(%d,%d)' % (len(f2),len(f3),h2,h3))
    print('critical_ind2=%s critical_ind3=%s' % (c2[3], (c3[2], c3[3], c3[4])))
    print('integral_generator_support=25 integral_degree=+1')

if __name__ == '__main__':
    check()
