#!/usr/bin/env python3
from collections import Counter, deque
from itertools import combinations

N = 18
SHIFTS = [5, 7, -7, 7, -7, -5]
MATCH_ORDER = [9, 6, 5, 11, 12, 17, 16, 13, 10, 14, 0, 2, 15, 8, 3, 7, 1, 4]
EXPECTED_F2 = {0: 18, 1: 81, 2: 108, 3: 18}
EXPECTED_F3 = {0: 18, 1: 135, 2: 540, 3: 1215, 4: 1458, 5: 729}
EXPECTED_DISTANCE4_COMPONENTS = [
    [0, 10, 14], [1, 11, 15], [2, 6, 16],
    [3, 7, 17], [4, 8, 12], [5, 9, 13],
]


def graph():
    adj = [set() for _ in range(N)]
    for i in range(N):
        j = (i + 1) % N
        adj[i].add(j); adj[j].add(i)
    for i in range(N):
        j = (i + SHIFTS[i % 6]) % N
        adj[i].add(j); adj[j].add(i)
    assert all(len(a) == 3 for a in adj)
    assert sum(map(len, adj)) // 2 == 27
    return adj


def distances(adj):
    ds = []
    for s in range(N):
        d = [-1] * N
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    q.append(v)
        assert min(d) >= 0
        ds.append(d)
    return ds


def is_face(mask, r, ds):
    verts = [i for i in range(N) if mask >> i & 1]
    return all(ds[a][b] <= r for a, b in combinations(verts, 2))


def faces_at(r, ds):
    return [m for m in range(1, 1 << N) if is_face(m, r, ds)]


def face_vector(faces):
    c = Counter(m.bit_count() - 1 for m in faces)
    return dict(sorted(c.items()))


def toggle_matching(faces):
    face_set = set(faces)
    unmatched = set(faces)
    pairs = []
    for v in MATCH_ORDER:
        bit = 1 << v
        for low in sorted(unmatched):
            if low & bit:
                continue
            high = low | bit
            if high in unmatched and high in face_set:
                unmatched.remove(low)
                unmatched.remove(high)
                pairs.append((low, high))
    return pairs, unmatched


def verify_acyclic(faces, pairs):
    face_set = set(faces)
    pair_set = set(pairs)
    out = {m: [] for m in faces}
    indeg = {m: 0 for m in faces}
    for high in faces:
        if high.bit_count() <= 1:
            continue
        bits = [i for i in range(N) if high >> i & 1]
        for i in bits:
            low = high & ~(1 << i)
            if low not in face_set:
                continue
            if (low, high) in pair_set:
                a, b = low, high
            else:
                a, b = high, low
            out[a].append(b)
            indeg[b] += 1
    q = deque([m for m in faces if indeg[m] == 0])
    seen = 0
    while q:
        u = q.popleft(); seen += 1
        for v in out[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    assert seen == len(faces), (seen, len(faces))


def rank_mod2(columns):
    pivots = {}
    rank = 0
    for x in columns:
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                rank += 1
                break
    return rank


def betti_mod2(faces):
    by_dim = {}
    for m in faces:
        by_dim.setdefault(m.bit_count() - 1, []).append(m)
    maxd = max(by_dim)
    ranks = {}
    for k in range(1, maxd + 1):
        rows = {m: i for i, m in enumerate(sorted(by_dim.get(k - 1, [])))}
        cols = []
        for high in sorted(by_dim.get(k, [])):
            x = 0
            for i in range(N):
                if high >> i & 1:
                    low = high & ~(1 << i)
                    x ^= 1 << rows[low]
            cols.append(x)
        ranks[k] = rank_mod2(cols)
    betti = []
    for k in range(maxd + 1):
        nk = len(by_dim.get(k, []))
        betti.append(nk - ranks.get(k, 0) - ranks.get(k + 1, 0))
    return betti, ranks


def distance4_components(ds):
    adj4 = [set() for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if ds[i][j] == 4:
                adj4[i].add(j); adj4[j].add(i)
    comps = []
    seen = set()
    for s in range(N):
        if s in seen:
            continue
        q = [s]; seen.add(s); c = []
        while q:
            u = q.pop(); c.append(u)
            for v in sorted(adj4[u]):
                if v not in seen:
                    seen.add(v); q.append(v)
        comps.append(sorted(c))
    return sorted(comps), adj4


def main():
    adj = graph()
    ds = distances(adj)
    assert max(max(row) for row in ds) == 4
    shell = Counter(ds[i][j] for i in range(N) for j in range(i + 1, N))
    assert shell == Counter({1: 27, 2: 54, 3: 54, 4: 18}), shell

    f2 = faces_at(2, ds)
    assert face_vector(f2) == EXPECTED_F2
    pairs, critical = toggle_matching(f2)
    assert len(pairs) == 99
    crit = Counter(m.bit_count() - 1 for m in critical)
    assert crit == Counter({2: 26, 0: 1}), crit
    verify_acyclic(f2, pairs)
    b2, r2 = betti_mod2(f2)
    assert b2 == [1, 0, 26, 0], b2

    comps, adj4 = distance4_components(ds)
    assert comps == EXPECTED_DISTANCE4_COMPONENTS, comps
    assert all(len(adj4[v]) == 2 for v in range(N))
    assert all(all(v in adj4[u] for u, v in combinations(c, 2)) for c in comps)

    f3 = faces_at(3, ds)
    assert face_vector(f3) == EXPECTED_F3
    assert len(f3) == 4**6 - 1
    b3, r3 = betti_mod2(f3)
    assert b3 == [1, 0, 0, 0, 0, 64], b3

    print('VERIFY_OK')
    print('vertices=18 edges=27 diameter=4')
    print('distance_shell_pairs=' + repr(dict(sorted(shell.items()))))
    print('scale2_face_vector=' + repr(EXPECTED_F2))
    print('scale2_matching_pairs=99 critical={0: 1, 2: 26} acyclic=True')
    print('scale2_mod2_betti=' + repr(b2) + ' boundary_ranks=' + repr(r2))
    print('distance4_components=' + repr(comps))
    print('scale3_face_vector=' + repr(EXPECTED_F3))
    print('scale3_mod2_betti=' + repr(b3) + ' boundary_ranks=' + repr(r3))

if __name__ == '__main__':
    main()
