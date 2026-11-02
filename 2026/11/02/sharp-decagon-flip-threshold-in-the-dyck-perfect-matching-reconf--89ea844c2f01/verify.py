"""Exhaustive Dyck-graph cycle-flip verification from Shrikhande triangles."""
from itertools import combinations
from collections import Counter, deque


def components(graph):
    seen = set()
    sizes = []
    for v in range(len(graph)):
        if v in seen:
            continue
        todo = [v]
        seen.add(v)
        for u in todo:
            for w in graph[u]:
                if w not in seen:
                    seen.add(w)
                    todo.append(w)
        sizes.append(len(todo))
    return Counter(sizes)


def main():
    v = [(i, j) for i in range(4) for j in range(4)]
    ix = {x: i for i, x in enumerate(v)}
    sh = [set() for _ in v]
    for k, (a, b) in enumerate(v):
        for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)):
            sh[k].add(ix[((a + da) % 4, (b + db) % 4)])
    triangles = [triple for triple in combinations(range(16), 3)
                 if all(j in sh[i] for i, j in combinations(triple, 2))]
    assert len(triangles) == 32
    g = [set() for _ in triangles]
    for i, j in combinations(range(32), 2):
        if len(set(triangles[i]) & set(triangles[j])) == 2:
            g[i].add(j)
            g[j].add(i)
    assert all(len(row) == 3 for row in g)
    assert sum(map(len, g)) == 96
    print('DYCK_OK vertices=32 edges=48', flush=True)

    # Duplicate-free recursion chooses the least still-uncovered vertex.
    matchings = []
    def enumerate_matchings(mask, edges):
        if mask.bit_count() == 32:
            matchings.append(frozenset(edges))
            return
        a = next(k for k in range(32) if not (mask >> k) & 1)
        for b in g[a]:
            if not (mask >> b) & 1:
                enumerate_matchings(mask | (1 << a) | (1 << b),
                                    edges + [tuple(sorted((a, b)))])
    enumerate_matchings(0, [])
    assert len(matchings) == 417
    assert len(set(matchings)) == 417
    print('MATCHINGS_OK count=417', flush=True)

    # Direct pairwise symmetric-difference method; a legal move consists
    # of exactly one alternating simple cycle (not several disjoint cycles).
    transitions = {k: [set() for _ in matchings] for k in (6, 8, 10)}
    for i, a in enumerate(matchings):
        for j in range(i + 1, len(matchings)):
            changed = a.symmetric_difference(matchings[j])
            k = len(changed)
            if k not in transitions:
                continue
            sub = {}
            for u, v in changed:
                sub.setdefault(u, []).append(v)
                sub.setdefault(v, []).append(u)
            if len(sub) != k or any(len(row) != 2 for row in sub.values()):
                continue
            start = next(iter(sub))
            seen = {start}
            todo = [start]
            for u in todo:
                for v in sub[u]:
                    if v not in seen:
                        seen.add(v)
                        todo.append(v)
            if len(seen) == k:
                transitions[k][i].add(j)
                transitions[k][j].add(i)

    counts = {k: sum(map(len, tr)) // 2 for k, tr in transitions.items()}
    assert counts == {6: 864, 8: 96, 10: 2736}, counts
    assert components(transitions[6]) == {1: 45, 124: 3}
    assert components(transitions[8]) == {1: 372, 45: 1}
    assert components(transitions[10]) == {1: 21, 396: 1}
    print('SINGLE_OK edges6=864 edges8=96 edges10=2736', flush=True)

    def merged(lengths):
        return [set().union(*(transitions[k][i] for k in lengths))
                for i in range(len(matchings))]

    small = merged((6, 8))
    assert components(small) == {124: 3, 45: 1}
    assert sum(map(len, small)) // 2 == 960
    big = merged((6, 8, 10))
    assert components(big) == {417: 1}
    assert sum(map(len, big)) // 2 == 3696
    assert components(merged((8, 10))) == {417: 1}
    print('THRESHOLD_OK cutoff8_components=4 cutoff10_connected=1', flush=True)

    ecc = Counter()
    for s in range(len(big)):
        dist = [-1] * len(big)
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for w in big[u]:
                if dist[w] < 0:
                    dist[w] = dist[u] + 1
                    q.append(w)
        assert min(dist) == 0
        ecc[max(dist)] += 1
    assert ecc == {4: 360, 5: 57}, ecc
    print('METRIC_OK radius=4 diameter=5 ecc4=360 ecc5=57', flush=True)
    print('ALL_VERIFY_OK', flush=True)


if __name__ == '__main__':
    main()
