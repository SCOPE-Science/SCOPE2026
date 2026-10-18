"""Exhaustive incidence-graph verifier for paired domination in Biaff(3).

Run with Python 3.10+: python verification/verify_incidence.py
All sets are built as bit masks. No third-party modules are used.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

N = 18
neighbours = [0] * N
for x in range(3):
    for y in range(3):
        p = 3 * x + y
        for m in range(3):
            b = (y - m * x) % 3
            l = 9 + 3 * m + b
            neighbours[p] |= 1 << l
            neighbours[l] |= 1 << p
assert all(mask.bit_count() == 3 for mask in neighbours)
closed = [(1 << i) | neighbours[i] for i in range(N)]


def mask_of(indices):
    return sum(1 << i for i in indices)


def covers_all(s):
    union = 0
    for i in range(N):
        if s >> i & 1:
            union |= closed[i]
    return union == (1 << N) - 1


@lru_cache(maxsize=None)
def has_perfect_matching(s):
    if not s:
        return True
    v = (s & -s).bit_length() - 1
    cand = neighbours[v] & s
    while cand:
        bit = cand & -cand
        if has_perfect_matching(s ^ (1 << v) ^ bit):
            return True
        cand ^= bit
    return False


def paired_sets(k):
    # Every induced perfect matching in this bipartite graph requires k/2
    # points and k/2 lines. Hence these loops exhaust all possibilities.
    a = k // 2
    for p in combinations(range(9), a):
        pm = mask_of(p)
        for l in combinations(range(9, 18), a):
            s = pm | mask_of(l)
            if covers_all(s) and has_perfect_matching(s):
                yield s


def components(vertices):
    index = {s: i for i, s in enumerate(vertices)}
    adj = [set() for _ in vertices]
    for i, s in enumerate(vertices):
        for v in range(N):
            if not (s >> v & 1):
                continue
            # A single exchange must stay on its own bipartite side:
            # otherwise the selected point/line counts cease to be equal.
            side = range(9) if v < 9 else range(9, 18)
            for w in side:
                if not (s >> w & 1):
                    j = index.get(s ^ (1 << v) ^ (1 << w))
                    if j is not None:
                        adj[i].add(j)
    assert all(i in adj[j] for i, row in enumerate(adj) for j in row)
    remaining = set(range(len(vertices)))
    out = []
    while remaining:
        seed = min(remaining)
        todo = [seed]
        remaining.remove(seed)
        comp = {seed}
        while todo:
            v = todo.pop()
            for w in adj[v]:
                if w in remaining:
                    remaining.remove(w)
                    comp.add(w)
                    todo.append(w)
        out.append(comp)
    return adj, out


def diameter(adj, comp):
    maximum = 0
    for s in comp:
        dis = {s: 0}
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in dis:
                    dis[v] = dis[u] + 1
                    queue.append(v)
        assert set(dis) == comp
        maximum = max(maximum, max(dis.values()))
    return maximum


if __name__ == '__main__':
    by_k = {}
    for k in (2, 4, 6, 8):
        s = list(paired_sets(k))
        by_k[k] = s
        print(f'paired_dominating_{k}={len(s)}')
    assert [len(by_k[k]) for k in (2, 4, 6, 8)] == [0, 0, 9, 216]
    for k, want_components, want_edges, want_diam in ((6, 9, 0, 0), (8, 9, 648, 3)):
        adj, comps = components(by_k[k])
        edges = sum(map(len, adj)) // 2
        degrees = dict(Counter(map(len, adj)))
        sizes = sorted(Counter(map(len, comps)).items())
        diams = sorted(Counter(diameter(adj, c) for c in comps).items())
        print(f'k={k} components={len(comps)} sizes={sizes} edges={edges} degrees={degrees} diameters={diams}')
        assert len(comps) == want_components
        assert edges == want_edges
        assert diams == [(want_diam, 9)]
        assert sizes == ([(1, 9)] if k == 6 else [(24, 9)])
        if k == 8:
            assert degrees == {6: 216}
    print('VERIFY_OK')
