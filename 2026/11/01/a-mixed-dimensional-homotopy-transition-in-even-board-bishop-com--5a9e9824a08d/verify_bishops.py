#!/usr/bin/env python3
"""Standalone exact integer discrete-Morse certificate for chessboard bishop complexes.

Requires Python 3 standard library only. All squares use zero-based row/column
coordinates. Each matching is specified solely by the pivot-vertex order below.
"""
from collections import Counter, defaultdict
from itertools import combinations

ORDERS = {
    2: (0, 1),
    4: tuple(range(8)),
    6: (3, 9, 16, 17, 7, 11, 4, 5, 15, 13, 1, 0, 12, 14, 8, 6, 2, 10),
}
EXPECT = {
    2: ((1, 2), {0: 1}, 1),
    4: ((1, 8, 14, 4), {1: 3}, 12),
    6: ((1, 18, 98, 184, 100, 8), {2: 14, 3: 3}, 196),
}

def make_faces(n):
    v = [(r, c) for r in range(n) for c in range(n) if (r + c) % 2 == 0]
    nn = len(v)
    attack = []
    for i, (r, c) in enumerate(v):
        attack.append(sum(1 << j for j, (rr, cc) in enumerate(v)
                          if i != j and abs(r - rr) == abs(c - cc)))
    face_by_size = defaultdict(list)
    def extend(cand, f):
        face_by_size[f.bit_count()].append(f)
        while cand:
            t = cand & -cand
            cand -= t
            i = t.bit_length() - 1
            extend(cand & ~attack[i], f | t)
    extend((1 << nn) - 1, 0)
    faces = {f for group in face_by_size.values() for f in group}
    # Independent exhaustive enumeration of ALL 2^nn subsets.
    direct = set()
    for f in range(1 << nn):
        if all((attack[i] & f) == 0
               for i in range(nn) if (f >> i) & 1):
            direct.add(f)
    assert faces == direct
    return v, faces, face_by_size

def certificate(n):
    v, faces, by_size = make_faces(n)
    order = ORDERS[n]
    assert sorted(order) == list(range(len(v)))
    unpaired = set(faces)
    pairs = []
    for i in order:
        t = 1 << i
        for f in sorted(unpaired):
            if f & t:
                continue
            g = f | t
            if g in unpaired:
                unpaired.remove(f)
                unpaired.remove(g)
                pairs.append((f, g))
    ctr = dict(sorted(Counter(f.bit_count()-1 for f in unpaired).items()))
    expected_f, expected_critical, expected_pairs = EXPECT[n]
    face_vector = tuple(len(by_size[k]) for k in range(max(by_size)+1))
    assert face_vector == expected_f
    assert ctr == expected_critical
    assert len(pairs) == expected_pairs
    # Acyclicity certificate: orient every unmatched cover down and each matched
    # cover up. The resulting digraph MUST have a topological ordering.
    matched = set(pairs)
    out = {f: [] for f in faces}
    indeg = {f: 0 for f in faces}
    num_inc = 0
    for f in faces:
        for i in range(len(v)):
            t = 1 << i
            if f & t:
                continue
            g = f | t
            if g not in faces:
                continue
            a, b = (f, g) if (f, g) in matched else (g, f)
            out[a].append(b)
            indeg[b] += 1
            num_inc += 1
    todo = [f for f in faces if indeg[f] == 0]
    reached = 0
    while todo:
        a = todo.pop()
        reached += 1
        for b in out[a]:
            indeg[b] -= 1
            if indeg[b] == 0:
                todo.append(b)
    assert reached == len(faces)
    # Reduced augmented oriented simplicial chain complex over Z.
    boundary = {}
    for f in faces:
        rem, sgn, d = f, 1, {}
        while rem:
            bit = rem & -rem
            rem -= bit
            d[f ^ bit] = sgn
            sgn = -sgn
        boundary[f] = d
    # Check d^2=0 in the unreduced complex.
    for f in faces:
        d2 = {}
        for g, coeff in boundary[f].items():
            for h, c2 in boundary[g].items():
                d2[h] = d2.get(h, 0) + coeff*c2
        assert all(c == 0 for c in d2.values())
    active = set(faces)
    # Integral elementary cancellations of matched pairs, each unit pivot.
    for low, high in pairs:
        assert low in active and high in active
        pivot = boundary[high].get(low, 0)
        assert abs(pivot) == 1
        for face in list(active):
            if face == high or face == low or face.bit_count() != high.bit_count():
                continue
            c = boundary[face].get(low, 0)
            if c == 0:
                continue
            scale = c // pivot
            assert scale * pivot == c
            for g, coeff in boundary[high].items():
                new = boundary[face].get(g, 0) - scale*coeff
                if new:
                    boundary[face][g] = new
                else:
                    boundary[face].pop(g, None)
        active.remove(low)
        active.remove(high)
        for face in active:
            boundary[face].pop(low, None)
            boundary[face].pop(high, None)
    assert active == unpaired
    residual = [(f, boundary[f]) for f in active if boundary[f]]
    assert not residual, residual
    print('BOARD',n,'ONE_COLOR_VERTEX_COUNT',len(v))
    print('FACE_CARDINALITIES_INCLUDING_EMPTY',','.join(map(str,face_vector)))
    print('HASSE_INCIDENCES',num_inc,'MORSE_PAIRS',len(pairs))
    print('CRITICAL_DIMENSIONS',','.join(f'{k}:{v}' for k,v in ctr.items()))
    print('INTEGRAL_MORSE_BOUNDARY_NONZERO',sum(len(boundary[f]) for f in active))

for n in (2,4,6):
    certificate(n)
print('WHOLE_BOARD_HOMOTOPY')
print('B2: S^1')
print('B4: 9*S^3')
print('B6: 196*S^5 + 84*S^6 + 9*S^7')
print('VERIFY_OK')
