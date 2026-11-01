#!/usr/bin/env python3
"""Exact finite certificate for the Shrikhande three-clique-free homotopy type.

Uses Python 3 standard library only. All face masks, Hasse arrows, and integer
Morse boundary coefficients are reconstructed rather than trusted as data.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations

N = 16
EXPECTED_F = (16, 120, 528, 1452, 2496, 2568, 1424, 330, 16)
EXPECTED_RANKS = (15, 105, 423, 1029, 1467, 1101, 314, 16)
EXPECTED_CRITICAL_5 = (2652, 3242, 24816, 41200, 49392)
EXPECTED_CRITICAL_6 = (7818, 11804, 19754, 22648, 29872, 31768,
                       35660, 41704, 43188, 45776, 46728, 53728, 54084, 57712)
EXPECTED_MORSE = (
    (0, 1, 0, -1, 0, -1, 1, -1, 0, -1, 1, 0, 0, 0),
    (1, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1),
)
D = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}


def neighbors():
    adj = [0] * N
    for a in range(N):
        x, y = divmod(a, 4)
        for b in range(N):
            if a == b:
                continue
            u, v = divmod(b, 4)
            if ((u - x) % 4, (v - y) % 4) in D:
                adj[a] |= 1 << b
    assert all((adj[a] >> a) & 1 == 0 for a in range(N))
    assert all((adj[a] >> b) & 1 == (adj[b] >> a) & 1
               for a in range(N) for b in range(N))
    assert all(adj[a].bit_count() == 6 for a in range(N))
    assert all((adj[a] & adj[b]).bit_count() == 2
               for a, b in combinations(range(N), 2))
    return adj


def triangles(adj):
    tri = []
    for a, b, c in combinations(range(N), 3):
        if (adj[a] >> b) & (adj[a] >> c) & (adj[b] >> c) & 1:
            tri.append((1 << a) | (1 << b) | (1 << c))
    assert len(tri) == 32
    return tri


def faces_of_complex(tri, adj):
    # First enumerator: triangle-hyperedge containment.
    faces = [s for s in range(1, 1 << N)
             if not any((s & t) == t for t in tri)]
    assert len(faces) == 8950
    # Second enumerator: directly test triple adjacencies in selected subsets.
    face_set = set(faces)
    for s in range(1, 1 << N):
        vert = [i for i in range(N) if s >> i & 1]
        good = not any(((adj[a] >> b) & 1) and
                       ((adj[a] >> c) & 1) and
                       ((adj[b] >> c) & 1)
                       for a, b, c in combinations(vert, 3))
        assert good == (s in face_set)
    f = Counter(s.bit_count() - 1 for s in faces)
    assert tuple(f.get(k, 0) for k in range(9)) == EXPECTED_F
    print('FACES_OK', EXPECTED_F, 'triangles=32', flush=True)
    return faces


def matching(faces):
    available = set(faces)
    lo_up, up_lo = {}, {}
    for v in range(N):
        bit = 1 << v
        # The pairs at each stage are disjoint, independent of visit order.
        for s in sorted(available):
            u = s | bit
            if (s & bit) == 0 and u in available and s in available:
                available.remove(s)
                available.remove(u)
                lo_up[s] = u
                up_lo[u] = s
    assert len(lo_up) == len(up_lo) == 4465
    crit = defaultdict(list)
    for s in sorted(available):
        crit[s.bit_count() - 1].append(s)
    assert {k: len(v) for k, v in crit.items()} == {0: 1, 5: 5, 6: 14}
    assert tuple(crit[5]) == EXPECTED_CRITICAL_5
    assert tuple(crit[6]) == EXPECTED_CRITICAL_6
    assert len(set(lo_up) | set(up_lo) | set(available)) == len(faces)
    print('MATCHING_OK pairs=4465 critical=(one_0,five_5,fourteen_6)', flush=True)
    return lo_up, up_lo, crit


def check_dag(faces, lo_up):
    # Orient every unmatched cover down, every matched cover up.
    indeg = {s: 0 for s in faces}
    outgoing = defaultdict(list)
    incidences = 0
    for u in faces:
        for j in range(N):
            if not (u >> j & 1):
                continue
            s = u ^ (1 << j)
            if s == 0:
                continue
            incidences += 1
            x, y = (s, u) if lo_up.get(s) == u else (u, s)
            outgoing[x].append(y)
            indeg[y] += 1
    queue = deque(s for s, d in indeg.items() if d == 0)
    seen = 0
    while queue:
        x = queue.popleft()
        seen += 1
        for y in outgoing[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                queue.append(y)
    assert incidences == 48272
    assert seen == len(faces) == 8950
    print('ACYCLIC_OK nodes=8950 incidences=48272', flush=True)


def incidence(u, s):
    bit = u ^ s
    assert bit.bit_count() == 1 and (u & s) == s
    return (-1) ** ((s & (bit - 1)).bit_count() % 2)


def morse_matrix(lo_up, crit):
    crit_lo = crit[5]
    ix = {s: i for i, s in enumerate(crit_lo)}

    @lru_cache(maxsize=None)
    def project(s):
        # Exact algebraic Morse reduction of a 5-chain, with signed
        # 5->6 gradient paths; zero for cells paired to dimension 4.
        if s in ix:
            return {ix[s]: 1}
        if s not in lo_up:
            return {}
        u = lo_up[s]
        assert u.bit_count() == 7
        eps = incidence(u, s)  # eps^{-1}=eps for incidence coefficients
        out = defaultdict(int)
        for j in range(N):
            if (u >> j) & 1:
                t = u ^ (1 << j)
                if t == s:
                    continue
                factor = -eps * incidence(u, t)
                for row, val in project(t).items():
                    out[row] += factor * val
        return {i: z for i, z in out.items() if z != 0}

    mat = [[0] * len(crit[6]) for _ in crit_lo]
    for col, u in enumerate(crit[6]):
        for j in range(N):
            if u >> j & 1:
                t = u ^ (1 << j)
                for row, val in project(t).items():
                    mat[row][col] += incidence(u, t) * val
    assert tuple(map(tuple, mat)) == EXPECTED_MORSE
    return mat


def exact_minor_det(mat, cols):
    n = len(mat)
    determinant = 0
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j]
                         for i in range(n) for j in range(i + 1, n))
        prod = 1
        for i in range(n):
            prod *= mat[i][cols[perm[i]]]
        determinant += (-1 if inversions % 2 else 1) * prod
    return determinant


def raw_mod2_ranks(faces):
    by = defaultdict(list)
    for s in faces:
        by[s.bit_count() - 1].append(s)
    ranks = []
    for k in range(1, 9):
        ix = {s: i for i, s in enumerate(by[k - 1])}
        basis = {}
        for u in by[k]:
            col = 0
            for j in range(N):
                if u >> j & 1:
                    col ^= 1 << ix[u ^ (1 << j)]
            while col:
                p = col.bit_length() - 1
                if p in basis:
                    col ^= basis[p]
                else:
                    basis[p] = col
                    break
        ranks.append(len(basis))
    assert tuple(ranks) == EXPECTED_RANKS
    betti = [len(by[k]) - (ranks[k - 1] if k else 0) -
             (ranks[k] if k < 8 else 0) for k in range(9)]
    betti[0] -= 1
    assert betti == [0, 0, 0, 0, 0, 0, 9, 0, 0]
    print('RAW_MOD2_OK ranks', ranks, 'reduced_betti', betti, flush=True)


def main():
    adj = neighbors()
    tri = triangles(adj)
    faces = faces_of_complex(tri, adj)
    lo_up, up_lo, crit = matching(faces)
    check_dag(faces, lo_up)
    mat = morse_matrix(lo_up, crit)
    columns = (0, 1, 4, 9, 11)
    det = exact_minor_det(mat, columns)
    assert det == 1
    assert len(mat) == 5 and all(len(row) == 14 for row in mat)
    print('INTEGER_MORSE_OK shape=5x14 unit_minor_columns=', columns,
          'det=', det, flush=True)
    raw_mod2_ranks(faces)
    print('ALL_VERIFY_OK')


if __name__ == '__main__':
    main()
