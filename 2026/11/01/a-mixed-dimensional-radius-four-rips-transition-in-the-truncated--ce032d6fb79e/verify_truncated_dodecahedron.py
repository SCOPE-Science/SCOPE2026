#!/usr/bin/env python3
"""Exact, dependency-free verification of early graph-metric Rips homology.

This program builds the truncated-dodecahedral graph as the line graph
of the one-edge subdivision of the generalized Petersen graph GP(10,2).
Every face and mod-2 boundary through radius 4 is enumerated exactly.
The relative elementary collapses through radius 3 are replayed, checking
free faces against the complete, current simplicial complex.
"""
from collections import defaultdict, deque
from itertools import combinations


def original_graph():
    adj = [set() for _ in range(20)]
    def add(a, b):
        adj[a].add(b); adj[b].add(a)
    for j in range(10):
        add(j, (j + 1) % 10)
        add(j, j + 10)
        add(j + 10, 10 + (j + 2) % 10)
    assert all(len(a) == 3 for a in adj)
    assert sum(map(len, adj)) // 2 == 30
    return adj


def truncated_graph(H):
    flags = sorted((u, v) for u in range(len(H)) for v in H[u])
    fid = {p: i for i, p in enumerate(flags)}
    assert len(flags) == 60
    adj = [set() for _ in flags]
    def add(a, b):
        adj[a].add(b); adj[b].add(a)
    for u in range(len(H)):
        for a, b in combinations(sorted(H[u]), 2):
            add(fid[u, a], fid[u, b])
        for v in H[u]:
            if u < v:
                add(fid[u, v], fid[v, u])
    assert all(len(a) == 3 for a in adj)
    assert sum(map(len, adj)) // 2 == 90
    return flags, fid, adj


def all_distances(adj):
    out = []
    for root in range(len(adj)):
        d = {root: 0}; q = deque([root])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in d:
                    d[v] = d[u] + 1; q.append(v)
        out.append(d)
    return out


def rips_faces(D, r):
    n = len(D)
    allowed = [sum(1 << j for j in range(i + 1, n)
                   if D[i][j] <= r) for i in range(n)]
    faces = set()
    def extend(mask, choices):
        while choices:
            low = choices & -choices
            choices ^= low
            i = low.bit_length() - 1
            new = mask | low
            faces.add(new)
            extend(new, choices & allowed[i])
    extend(0, (1 << n) - 1)
    return faces


def hamming(mask):
    while mask:
        low = mask & -mask
        mask ^= low
        yield low.bit_length() - 1


def free_collapse(current, protected, stages):
    now = set(current)
    total = 0
    totals = []
    n = max(x.bit_length() for x in current)
    for pairs in stages:
        count = 0
        for f, u in sorted(pairs, key=lambda t: (-t[1].bit_count(), t[0])):
            assert f in now and u in now
            assert f not in protected and u not in protected
            assert f.bit_count() + 1 == u.bit_count() and f & u == f
            cofaces = [f | (1 << j) for j in range(n)
                       if not f & (1 << j) and f | (1 << j) in now]
            assert cofaces == [u], (f, u, cofaces)
            assert all((u | (1 << j)) not in now for j in range(n)
                       if not u & (1 << j))
            now.remove(f); now.remove(u)
            count += 1
        totals.append(count); total += count
    assert now == protected
    return total, totals


def center_of(face, flags, DH, H):
    projections = sorted({flags[i][0] for i in hamming(face)})
    centers = set()
    for u, v in combinations(projections, 2):
        if DH[u][v] == 2:
            neighbors = H[u] & H[v]
            assert len(neighbors) == 1
            centers.update(neighbors)
        else:
            assert DH[u][v] <= 1
    assert len(centers) <= 1
    return next(iter(centers)) if centers else None


def build_pairing(H, flags, fid, DH, C1, C2, C3):
    # First remove all cliques with a projected distance-two pair.
    extra = set()
    centers = {}
    for f in C3:
        v = center_of(f, flags, DH, H)
        if v is not None:
            extra.add(f); centers[f] = v
    B = C3 - extra
    assert C1 <= C2 <= B <= C3
    pairs_far = []
    for f in extra:
        v = centers[f]
        pivot = 1 << fid[v, min(H[v])]
        if not (f & pivot):
            u = f | pivot
            assert u in extra and centers[u] == v
            pairs_far.append((f, u))

    # Next remove the mixed faces of two adjacent flag-fibres whose
    # two endpoints both use non-bridge flags (distance exactly three).
    pairs_edge = []
    for f in B - C2:
        roots = sorted({flags[i][0] for i in hamming(f)})
        assert len(roots) == 2 and roots[1] in H[roots[0]]
        v, w = roots
        pivot = 1 << fid[v, w]
        assert any(flags[i][0] == v and i != fid[v, w] for i in hamming(f))
        assert any(flags[i][0] == w and i != fid[w, v] for i in hamming(f))
        if not f & pivot:
            u = f | pivot
            assert u in B - C2
            pairs_edge.append((f, u))
    assert len(pairs_far) * 2 == len(extra)
    assert len(pairs_edge) * 2 == len(B - C2)
    free_collapse(C3, C2, [pairs_far, pairs_edge])

    # The radius-two cross-fibre faces collapse onto the original
    # fibre cliques and reversal edges. Two subphases per base edge.
    cross_a, cross_b = [], []
    for f in C2 - C1:
        roots = sorted({flags[i][0] for i in hamming(f)})
        assert len(roots) == 2 and roots[1] in H[roots[0]]
        v, w = roots
        a = fid[v, w]; b = fid[w, v]
        nonbridge_v = any(flags[i][0] == v and i != a for i in hamming(f))
        nonbridge_w = any(flags[i][0] == w and i != b for i in hamming(f))
        assert not (nonbridge_v and nonbridge_w)
        if nonbridge_v:
            if not f & (1 << a):
                u = f | (1 << a)
                assert u in C2 - C1
                cross_a.append((f, u))
        else:
            assert nonbridge_w and f & (1 << a)
            if not f & (1 << b):
                u = f | (1 << b)
                assert u in C2 - C1
                cross_b.append((f, u))
    assert (len(cross_a) + len(cross_b)) * 2 == len(C2 - C1)
    free_collapse(C2, C1, [cross_a, cross_b])
    return len(pairs_far), len(pairs_edge), len(cross_a), len(cross_b)


def mod2_betti(faces):
    bysize = defaultdict(list)
    for f in faces:
        bysize[f.bit_count()].append(f)
    for faces_at_k in bysize.values():
        faces_at_k.sort()
    ranks = {}
    for k in range(2, max(bysize) + 1):
        rows = {f: j for j, f in enumerate(bysize[k-1])}
        pivots = {}
        for f in bysize[k]:
            column = 0
            for i in hamming(f):
                column ^= (1 << rows[f ^ (1 << i)])
            while column:
                pivot = column.bit_length() - 1
                if pivot in pivots:
                    column ^= pivots[pivot]
                else:
                    pivots[pivot] = column
                    break
        ranks[k] = len(pivots)
    betti = {k - 1: len(bysize[k]) - ranks.get(k, 0) - ranks.get(k+1, 0)
             for k in bysize}
    # beta_0 is unreduced, all other degrees are ordinary/reduced alike.
    return dict(sorted((k-1, len(v)) for k, v in bysize.items())), ranks, betti


def verify():
    H = original_graph()
    flags, fid, adj = truncated_graph(H)
    DH = all_distances(H)
    D = all_distances(adj)
    assert len(D[0]) == 60
    assert max(max(x.values()) for x in D) == 10
    stages = {r: rips_faces(D, r) for r in range(1, 5)}
    expected = {1: 170, 2: 530, 3: 2250, 4: 13554}
    assert {r: len(x) for r, x in stages.items()} == expected
    pairs = build_pairing(H, flags, fid, DH, stages[1], stages[2], stages[3])
    assert pairs == (320, 540, 90, 90), pairs
    assert 2 * (pairs[0]+pairs[1]) == len(stages[3]-stages[2])
    assert 2 * (pairs[2]+pairs[3]) == len(stages[2]-stages[1])
    profile = {}
    for r in range(1, 5):
        fs, ranks, betti = mod2_betti(stages[r])
        profile[r] = betti
        print('radius', r, 'faces', fs, 'boundary_ranks', ranks,
              'homology_F2', betti)
    assert profile[1] == {0:1,1:11,2:0}
    assert all(profile[r].get(0) == 1 and profile[r].get(1) == 11
               and all(profile[r].get(k, 0) == 0 for k in profile[r] if k > 1)
               for r in (2, 3))
    assert profile[4] == {0:1,1:0,2:1,3:0,4:12,5:0,6:0,7:0}
    assert sum((-1)**(f.bit_count()-1) for f in stages[4]) == 14
    print('collapses r3_to_r2', pairs[:2], 'r2_to_r1',pairs[2:])
    print('persistent_F2_through_r4: H1 11x[1,4); H2 1 birth at 4; H4 12 births at 4; later deaths unexamined')
    print('VERIFY_TRUNCATED_DODECAHEDRON_RIPS_MOD2_PASS')


if __name__ == '__main__':
    verify()
