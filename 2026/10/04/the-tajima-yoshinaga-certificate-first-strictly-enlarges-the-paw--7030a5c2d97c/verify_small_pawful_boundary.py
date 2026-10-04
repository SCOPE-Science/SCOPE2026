#!/usr/bin/env python3
"""Exact census for the Tajima--Yoshinaga Definition 5.1 certificate through 6 vertices.
Uses only the Python standard library.
"""
from itertools import permutations
from collections import defaultdict, Counter, deque


def edge_list(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def transform_mask(n, mask, perm):
    E = edge_list(n)
    idx = {e: k for k, e in enumerate(E)}
    out = 0
    for k, (i, j) in enumerate(E):
        if (mask >> k) & 1:
            a, b = perm[i], perm[j]
            if a > b:
                a, b = b, a
            out |= 1 << idx[(a, b)]
    return out


def canonical_mask(n, mask):
    return min(transform_mask(n, mask, p) for p in permutations(range(n)))


def unlabeled_representatives(n):
    perms = list(permutations(range(n)))
    total = 1 << (n * (n - 1) // 2)
    seen = set()
    reps = []
    for mask in range(total):
        if mask in seen:
            continue
        orbit = {transform_mask(n, mask, p) for p in perms}
        seen.update(orbit)
        reps.append(min(orbit))
    assert len(seen) == total
    return reps


def adjacency(n, mask):
    A = [set() for _ in range(n)]
    for k, (i, j) in enumerate(edge_list(n)):
        if (mask >> k) & 1:
            A[i].add(j)
            A[j].add(i)
    return A


def distances(A):
    n = len(A)
    D = [[n + 1] * n for _ in range(n)]
    for s in range(n):
        D[s][s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in A[u]:
                if D[s][v] > D[s][u] + 1:
                    D[s][v] = D[s][u] + 1
                    q.append(v)
    return D


def connected(D):
    return all(x < len(D) + 1 for x in D[0])


def diameter(D):
    return max(max(row) for row in D)


def is_pawful(A, D):
    n = len(A)
    if not connected(D) or diameter(D) > 2:
        return False
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if D[x][y] == 2 and D[y][z] == 2 and D[x][z] == 1:
                    if not any(D[a][x] == D[a][y] == D[a][z] == 1 for a in range(n)):
                        return False
    return True


def has_definition_5_1_certificate(A, D, want_witness=False):
    """Decide existence of the maps f1,f2 in Tajima--Yoshinaga Definition 5.1.

    f1(a,c)=b selects a common neighbor for each ordered distance-2 pair (a,c).
    f2(a,b,d)=g selects a common neighbor g of b,d for each ordered triple
    with a~b and d(b,d)=2.  Condition (iii) filters f2 choices.  Condition
    (ii) becomes pairwise incompatibilities between f2 choices plus forbidden
    values for f1.  Exhaustive backtracking is therefore exact.
    """
    n = len(A)
    if not connected(D) or diameter(D) > 2:
        return (False, None) if want_witness else False

    Xp = [(a, c) for a in range(n) for c in range(n) if D[a][c] == 2]
    common = {
        p: [b for b in range(n) if D[p[0]][b] == 1 and D[b][p[1]] == 1]
        for p in Xp
    }
    Yp = [
        (a, b, d)
        for a in range(n)
        for b in range(n)
        for d in range(n)
        if D[a][b] == 1 and D[b][d] == 2
    ]

    choices = {}
    for y in Yp:
        a, b, d = y
        C = common[(b, d)]
        vals = [g for g in C if not (D[a][g] == 2 and len(C) != 1)]
        if not vals:
            return (False, None) if want_witness else False
        choices[y] = vals

    order = sorted(Yp, key=lambda y: (len(choices[y]), y))
    assigned = {}
    forbidden_f1 = defaultdict(Counter)

    def incompatible_with_prior(y, g):
        a, b, d = y
        # Current q=(a,b,g,d) forbids every selected q2=(*,a,b,g).
        if D[a][g] == 2:
            for u in range(n):
                y2 = (u, a, g)
                if y2 in assigned and assigned[y2] == b:
                    return True
        # A previous q'=(A,B,G,D') forbids current q when q=(*,A,B,G).
        for (A, B, Dp), G in assigned.items():
            if A == b and B == g and G == d:
                return True
        return False

    def rec(i):
        if i == len(order):
            f1 = {}
            for p in Xp:
                allowed = [b for b in common[p] if forbidden_f1[p][b] == 0]
                if not allowed:
                    return None
                f1[p] = allowed[0]
            return dict(assigned), f1

        y = order[i]
        a, b, d = y
        for g in choices[y]:
            if incompatible_with_prior(y, g):
                continue
            if D[a][g] == 2:
                p = (a, g)
                if all(x == b or forbidden_f1[p][x] > 0 for x in common[p]):
                    continue
            assigned[y] = g
            if D[a][g] == 2:
                forbidden_f1[(a, g)][b] += 1
            ans = rec(i + 1)
            if ans is not None:
                return ans
            if D[a][g] == 2:
                forbidden_f1[(a, g)][b] -= 1
                if forbidden_f1[(a, g)][b] == 0:
                    del forbidden_f1[(a, g)][b]
            del assigned[y]
        return None

    ans = rec(0)
    return ((ans is not None), ans) if want_witness else (ans is not None)


def mask_from_edges(n, edges):
    idx = {e: k for k, e in enumerate(edge_list(n))}
    mask = 0
    for i, j in edges:
        if i > j:
            i, j = j, i
        mask |= 1 << idx[(i, j)]
    return mask


def verify_source_witness():
    # Figure 3 of Tajima--Yoshinaga, converted from labels 1..6 to 0..5.
    G1_edges = [
        (0, 1), (0, 4), (1, 4), (1, 2), (4, 3),
        (2, 3), (1, 5), (5, 3), (4, 5), (5, 2),
    ]
    mask = mask_from_edges(6, G1_edges)
    A = adjacency(6, mask)
    D = distances(A)

    f1_triples_1based = [
        (1,2,3),(1,5,4),(1,2,6),(2,6,4),(3,2,1),
        (3,6,5),(4,5,1),(4,6,2),(5,6,3),(6,2,1),
    ]
    f2_quads_1based = [
        (2,1,2,3),(5,1,2,3),(2,1,5,4),(5,1,5,4),(2,1,2,6),(5,1,2,6),
        (1,2,5,4),(3,2,6,4),(5,2,6,4),(6,2,6,4),
        (2,3,2,1),(4,3,2,1),(6,3,2,1),(2,3,6,5),(4,3,6,5),(6,3,6,5),
        (3,4,5,1),(5,4,5,1),(6,4,5,1),(3,4,6,2),(5,4,6,2),(6,4,6,2),
        (1,5,2,3),(2,5,6,3),(4,5,6,3),(6,5,6,3),
        (2,6,2,1),(3,6,2,1),(4,6,5,1),(5,6,5,1),
    ]
    f1 = {(a-1, c-1): b-1 for a,b,c in f1_triples_1based}
    f2 = {(a-1, b-1, d-1): g-1 for a,b,g,d in f2_quads_1based}

    Xp = {(a,c) for a in range(6) for c in range(6) if D[a][c] == 2}
    Yp = {(a,b,d) for a in range(6) for b in range(6) for d in range(6)
          if D[a][b] == 1 and D[b][d] == 2}
    assert set(f1) == Xp
    assert set(f2) == Yp
    for (a,c), b in f1.items():
        assert D[a][b] == D[b][c] == 1 and D[a][c] == 2
    for (a,b,d), g in f2.items():
        assert D[a][b] == D[b][g] == D[g][d] == 1 and D[b][d] == 2
        assert not any((u,a,g) in f2 and f2[(u,a,g)] == b for u in range(6))
        if D[a][g] == 2:
            assert f1[(a,g)] != b
            assert [h for h in range(6) if D[b][h] == D[h][d] == 1] == [g]
    return canonical_mask(6, mask)


def main():
    source_g1 = verify_source_witness()
    rows = []
    nonpawful_certified = []
    for n in range(1, 7):
        reps = unlabeled_representatives(n)
        con = diam2 = paw = cert = strict = 0
        for mask in reps:
            A = adjacency(n, mask)
            D = distances(A)
            if connected(D):
                con += 1
                if diameter(D) <= 2:
                    diam2 += 1
                    p = is_pawful(A, D)
                    s = has_definition_5_1_certificate(A, D)
                    paw += int(p)
                    cert += int(s)
                    if s and not p:
                        strict += 1
                        nonpawful_certified.append((n, mask))
        row = (n, len(reps), con, diam2, paw, cert, strict)
        rows.append(row)
        print("CENSUS", *row)

    expected = [
        (1, 1,   1,   1,  1,  1, 0),
        (2, 2,   1,   1,  1,  1, 0),
        (3, 4,   2,   2,  2,  2, 0),
        (4, 11,  6,   5,  5,  5, 0),
        (5, 34,  21, 15, 13, 13, 0),
        (6, 156, 112, 60, 47, 48, 1),
    ]
    assert rows == expected
    assert nonpawful_certified == [(6, source_g1)]

    A = adjacency(6, source_g1)
    D = distances(A)
    ok, witness = has_definition_5_1_certificate(A, D, True)
    assert ok and witness is not None and not is_pawful(A, D)
    f2, f1 = witness
    assert len(f1) == 10 and len(f2) == 30
    print("SOURCE_G1_CANONICAL_MASK", source_g1)
    print("CERTIFICATE_SIZES", len(f1), len(f2))
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
