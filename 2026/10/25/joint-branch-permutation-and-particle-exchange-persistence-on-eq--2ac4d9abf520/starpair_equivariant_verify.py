"""Finite exact checks for ordered hard-core configurations on equilateral stars.

The geometry and universal representation formulas require mathematical proofs;
these tests independently check the resulting finite graph chain complexes.
"""
from itertools import permutations
from collections import deque


def inspection(m):
    vertices = [(s, i) for s in ('A', 'B') for i in range(m)]
    edges = [(i, j) for i in range(m) for j in range(m) if i != j]
    assert len(edges) == m * (m - 1)
    adj = {v: [] for v in vertices}
    for t, (i, j) in enumerate(edges):
        a, b = ('A', i), ('B', j)
        adj[a].append((b, t))
        adj[b].append((a, t))
    root = vertices[0]
    parent, p_edge = {root: None}, {}
    q = deque([root])
    while q:
        v = q.popleft()
        for w, e in adj[v]:
            if w not in parent:
                parent[w], p_edge[w] = v, e
                q.append(w)
    assert len(parent) == 2 * m
    tree = set(p_edge.values())
    chords = [t for t in range(len(edges)) if t not in tree]
    rank = len(chords)
    assert rank == m * m - 3 * m + 1
    ix = {e: t for t, e in enumerate(edges)}

    def oriented_path(u, v):
        # The unique tree path from u to v, with coefficients in A_i -> B_j edges.
        up = []
        while u is not None:
            up.append(u)
            u = parent[u]
        vp = []
        while v is not None:
            vp.append(v)
            v = parent[v]
        ancestral = set(up)
        common = next(w for w in vp if w in ancestral)
        up_to_common = up[:up.index(common) + 1]
        v_to_common = vp[:vp.index(common) + 1]
        route = up_to_common + list(reversed(v_to_common[:-1]))
        answer = []
        for x, y in zip(route, route[1:]):
            e = next(t for w, t in adj[x] if w == y)
            sign = 1 if x[0] == 'A' else -1
            answer.append((e, sign))
        return answer

    cycles = {}
    for chord in chords:
        i, j = edges[chord]
        cycles[chord] = [(chord, 1)] + oriented_path(('B', j), ('A', i))

    def action_on_edge(e, p, swap):
        i, j = e
        if swap:
            return ix[(p[j], p[i])], -1
        return ix[(p[i], p[j])], 1

    tested = 0
    for p in permutations(range(m)):
        fixed = sum(p[i] == i for i in range(m))
        twocycles = sum(i < p[i] and p[p[i]] == i for i in range(m))
        for swap in (0, 1):
            tr = 0
            for chord in chords:
                for ee, coefficient in cycles[chord]:
                    mapped, sign = action_on_edge(edges[ee], p, swap)
                    if mapped == chord:
                        tr += coefficient * sign
            expected = (fixed * fixed - 3 * fixed + 1) if not swap else (1 - 2 * twocycles)
            assert tr == expected, (m, p, swap, tr, expected)
            # Chain-group fixed-edge and fixed-vertex Lefschetz, independently.
            c0_trace = 0 if swap else 2 * fixed
            c1_trace = (-2 * twocycles) if swap else fixed * (fixed - 1)
            assert tr == c1_trace - c0_trace + 1
            tested += 1
    plus = (rank + 1) // 2  # identity with particle swap has trace exactly 1
    minus = (rank - 1) // 2
    assert plus == (m - 1) * (m - 2) // 2
    assert minus == m * (m - 3) // 2
    return tested, rank


def main():
    checks = 0
    for m in range(3, 8):
        count, rank = inspection(m)
        checks += count
        print('arms', m, 'homology_rank', rank, 'group_actions', count)
    print('STARPAIR_JOINT_ACTION_VERIFIED', checks)


if __name__ == '__main__':
    main()
