#!/usr/bin/env python3
from itertools import permutations, combinations
from fractions import Fraction
from collections import defaultdict, Counter, deque
from math import gcd

L = (1, 2, 3, 4)
N = sum(L)
ORDER = (9, 3, 6, 7, 0, 4, 5, 1, 2, 8)
EXPECTED_F = (10, 45, 100, 60)
EXPECTED_RANKS_Q = (9, 36, 58)
EXPECTED_CRITICAL = {0: 1, 2: 6, 3: 2}
EXPECTED_CRITICAL_CELLS = {
    (9,),
    (0, 3, 6), (1, 3, 4), (2, 3, 6), (2, 4, 7), (3, 4, 8), (4, 5, 7),
    (1, 2, 4, 8), (2, 4, 5, 8),
}

def facets_from_definition():
    facets = set()
    for x in range(N):
        for p in permutations(range(len(L))):
            s = x
            vs = [x]
            for j in p[:-1]:
                s = (s + L[j]) % N
                vs.append(s)
            assert len(set(vs)) == len(L)
            facets.add(tuple(sorted(vs)))
    # All candidates have cardinality 4 here, so deduplication already gives the facets.
    return sorted(facets)

def face_dictionary(facets):
    faces = defaultdict(set)
    for F in facets:
        for r in range(1, len(F) + 1):
            for s in combinations(F, r):
                faces[r - 1].add(tuple(s))
    return {d: set(v) for d, v in faces.items()}

def all_faces(faces):
    return {frozenset(f) for dimfaces in faces.values() for f in dimfaces}

def greedy_element_matching(face_set):
    unmatched = set(face_set)
    pairs = []
    for v in ORDER:
        for F in sorted(list(unmatched), key=lambda s: (len(s), tuple(sorted(s)))):
            if F not in unmatched or v in F:
                continue
            G = F | {v}
            if G in unmatched:
                unmatched.remove(F)
                unmatched.remove(G)
                pairs.append((F, G))
    return pairs, unmatched

def hasse_covers(face_set):
    covers = []
    for F in face_set:
        for v in range(N):
            if v not in F:
                G = F | {v}
                if G in face_set:
                    covers.append((F, G))
    return covers

def verify_acyclic(face_set, pairs, covers):
    matched = {(F, G) for F, G in pairs}
    adj = {F: [] for F in face_set}
    indeg = {F: 0 for F in face_set}
    for F, G in covers:
        # Standard discrete-Morse orientation: unmatched covers downward, matched covers upward.
        if (F, G) in matched:
            u, v = F, G
        else:
            u, v = G, F
        adj[u].append(v)
        indeg[v] += 1
    q = deque([x for x in face_set if indeg[x] == 0])
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == len(face_set)

def boundary_matrix(faces, d):
    rows = sorted(faces[d - 1])
    cols = sorted(faces[d])
    rid = {f: i for i, f in enumerate(rows)}
    A = [[Fraction(0) for _ in cols] for _ in rows]
    for j, c in enumerate(cols):
        for i in range(len(c)):
            face = c[:i] + c[i + 1:]
            A[rid[face]][j] = Fraction(1 if i % 2 == 0 else -1)
    return A

def rank_q(A):
    if not A:
        return 0
    M = [row[:] for row in A]
    m, n = len(M), len(M[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if M[i][c] != 0), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                a = M[i][c]
                M[i] = [M[i][j] - a * M[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def main():
    # Parameter arithmetic checks.
    assert gcd(*L) == 1
    assert len(set(L)) == 4
    assert sum(sorted(L)) == 10
    # Genericity fails already because 1+2=3.
    assert L[0] + L[1] == L[2]

    facets = facets_from_definition()
    assert len(facets) == 60
    faces = face_dictionary(facets)
    fvec = tuple(len(faces[d]) for d in range(4))
    assert fvec == EXPECTED_F
    face_set = all_faces(faces)
    assert len(face_set) == sum(EXPECTED_F) == 215

    pairs, critical = greedy_element_matching(face_set)
    assert len(pairs) == 103
    assert len(critical) == 9
    crit_counts = Counter(len(F) - 1 for F in critical)
    assert dict(crit_counts) == EXPECTED_CRITICAL
    assert {tuple(sorted(F)) for F in critical} == EXPECTED_CRITICAL_CELLS

    covers = hasse_covers(face_set)
    assert len(covers) == 630
    assert verify_acyclic(face_set, pairs, covers)

    ranks = tuple(rank_q(boundary_matrix(faces, d)) for d in (1, 2, 3))
    assert ranks == EXPECTED_RANKS_Q
    b0 = EXPECTED_F[0] - ranks[0]
    b1 = EXPECTED_F[1] - ranks[0] - ranks[1]
    b2 = EXPECTED_F[2] - ranks[1] - ranks[2]
    b3 = EXPECTED_F[3] - ranks[2]
    assert (b0, b1, b2, b3) == (1, 0, 6, 2)

    # The verified acyclic matching yields a CW complex with one 0-cell,
    # six 2-cells and two 3-cells, and no 1-cells. Its rational H_3 has
    # dimension 2, equal to the number of 3-cells, so the cellular boundary
    # C_3 -> C_2 has rank zero. Since its entries are integers, that boundary
    # is identically zero. The 2-skeleton is a wedge of six 2-spheres, and
    # pi_2 -> H_2 is an isomorphism there, so both 3-cell attaching maps are
    # null-homotopic. Hence the homotopy type is (vee^6 S^2) vee (vee^2 S^3).

    print('facets=60')
    print('f_vector=10,45,100,60')
    print('faces=215')
    print('hasse_covers=630')
    print('morse_pairs=103')
    print('critical_counts=dim0:1,dim2:6,dim3:2')
    print('boundary_ranks_Q=d1:9,d2:36,d3:58')
    print('betti_Q=1,0,6,2')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
