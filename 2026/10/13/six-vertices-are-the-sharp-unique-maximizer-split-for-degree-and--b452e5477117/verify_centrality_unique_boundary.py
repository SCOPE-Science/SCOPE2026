from itertools import combinations, permutations
from fractions import Fraction
from collections import Counter


def pairs_of(n):
    return list(combinations(range(n), 2))


def adjacency_from_mask(n, mask):
    adj = [set() for _ in range(n)]
    for k, (u, v) in enumerate(pairs_of(n)):
        if (mask >> k) & 1:
            adj[u].add(v)
            adj[v].add(u)
    return adj


def bfs(adj, s):
    n = len(adj)
    dist = [-1] * n
    dist[s] = 0
    q = [s]
    for u in q:
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def connected(adj):
    return all(d >= 0 for d in bfs(adj, 0))


def all_distances_bfs(adj):
    return [bfs(adj, s) for s in range(len(adj))]


def all_distances_floyd(adj):
    n = len(adj)
    inf = n + 1
    d = [[0 if i == j else (1 if j in adj[i] else inf) for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            dik = d[i][k]
            for j in range(n):
                x = dik + d[k][j]
                if x < d[i][j]:
                    d[i][j] = x
    return d


def closeness_from_dist(ds):
    n = len(ds)
    return [Fraction(n - 1, sum(ds[v][u] for u in range(n) if u != v)) for v in range(n)]


def betweenness_pair_count(adj, ds):
    """Exact unnormalized Freeman betweenness, unordered endpoint pairs."""
    n = len(adj)
    B = [Fraction(0) for _ in range(n)]
    # shortest-path counts from each source, based only on BFS layers
    sigma = []
    for s in range(n):
        sig = [0] * n
        sig[s] = 1
        order = sorted(range(n), key=lambda v: ds[s][v])
        for u in order:
            for v in adj[u]:
                if ds[s][v] == ds[s][u] + 1:
                    sig[v] += sig[u]
        sigma.append(sig)
    for s in range(n):
        for t in range(s + 1, n):
            total = sigma[s][t]
            assert total > 0
            D = ds[s][t]
            for v in range(n):
                if v == s or v == t:
                    continue
                if ds[s][v] + ds[v][t] == D:
                    B[v] += Fraction(sigma[s][v] * sigma[t][v], total)
    return B


def betweenness_brandes(adj):
    """Independent exact Brandes recurrence; divide ordered-source total by two."""
    n = len(adj)
    CB = [Fraction(0) for _ in range(n)]
    for s in range(n):
        stack = []
        pred = [[] for _ in range(n)]
        sigma = [0] * n
        sigma[s] = 1
        dist = [-1] * n
        dist[s] = 0
        q = [s]
        for v in q:
            stack.append(v)
            for w in adj[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)
        delta = [Fraction(0) for _ in range(n)]
        while stack:
            w = stack.pop()
            for v in pred[w]:
                delta[v] += Fraction(sigma[v], sigma[w]) * (1 + delta[w])
            if w != s:
                CB[w] += delta[w]
    return [x / 2 for x in CB]


def maxset(values):
    m = max(values)
    return frozenset(i for i, x in enumerate(values) if x == m)


def canonical_mask(n, mask):
    pairs = pairs_of(n)
    idx = {e: i for i, e in enumerate(pairs)}
    best = None
    for p in permutations(range(n)):
        m = 0
        for k, (a, b) in enumerate(pairs):
            x, y = sorted((p[a], p[b]))
            if (mask >> idx[(x, y)]) & 1:
                m |= 1 << k
        if best is None or m < best:
            best = m
    return best


def permuted_mask(n, mask, p):
    pairs = pairs_of(n)
    idx = {e: i for i, e in enumerate(pairs)}
    out = 0
    # image edge {p[u],p[v]}
    for k, (u, v) in enumerate(pairs):
        if (mask >> k) & 1:
            a, b = sorted((p[u], p[v]))
            out |= 1 << idx[(a, b)]
    return out


def edge_list(n, mask):
    return [e for k, e in enumerate(pairs_of(n)) if (mask >> k) & 1]


def main():
    connected_expected = {1: 1, 2: 1, 3: 4, 4: 38, 5: 728, 6: 26704}
    connected_counts = {}
    set_disagree = {}
    unique_degree_bet_conflicts = {}
    unique_close_bet_conflicts = {}
    conflict_masks = []

    for n in range(1, 7):
        if n == 1:
            masks = [0]
        else:
            masks = range(1 << len(pairs_of(n)))
        conn = setdiff = udb = ucb = 0
        for mask in masks:
            adj = adjacency_from_mask(n, mask)
            if not connected(adj):
                continue
            conn += 1
            ds1 = all_distances_bfs(adj)
            ds2 = all_distances_floyd(adj)
            assert ds1 == ds2
            deg = [len(adj[v]) for v in range(n)]
            close1 = closeness_from_dist(ds1) if n > 1 else [Fraction(0)]
            # independent closeness formula from Floyd distances
            close2 = [Fraction(n - 1, sum(ds2[v][u] for u in range(n) if u != v)) for v in range(n)] if n > 1 else [Fraction(0)]
            assert close1 == close2
            bet1 = betweenness_pair_count(adj, ds1)
            bet2 = betweenness_brandes(adj)
            assert bet1 == bet2, (n, mask, bet1, bet2)

            D, C, B = maxset(deg), maxset(close1), maxset(bet1)
            if D != B:
                setdiff += 1
            if len(D) == len(B) == 1 and D != B:
                udb += 1
                if n == 6:
                    conflict_masks.append(mask)
                    # all sharp conflicts also have a unique closeness maximizer equal to degree maximizer
                    assert len(C) == 1 and C == D
            if len(C) == len(B) == 1 and C != B:
                ucb += 1
        connected_counts[n] = conn
        set_disagree[n] = setdiff
        unique_degree_bet_conflicts[n] = udb
        unique_close_bet_conflicts[n] = ucb
        assert conn == connected_expected[n], (n, conn)

    assert unique_degree_bet_conflicts == {1:0, 2:0, 3:0, 4:0, 5:0, 6:720}
    assert unique_close_bet_conflicts == {1:0, 2:0, 3:0, 4:0, 5:0, 6:720}
    assert set_disagree[5] == 150
    assert len(conflict_masks) == 720

    classes = Counter(canonical_mask(6, m) for m in conflict_masks)
    assert len(classes) == 1
    rep = next(iter(classes))
    assert classes[rep] == 720

    # The unique class is asymmetric: its orbit under S_6 has size 720.
    orbit = {permuted_mask(6, rep, p) for p in permutations(range(6))}
    assert len(orbit) == 720
    assert orbit == set(conflict_masks)

    adj = adjacency_from_mask(6, rep)
    ds = all_distances_bfs(adj)
    deg = [len(adj[v]) for v in range(6)]
    close = closeness_from_dist(ds)
    bet = betweenness_pair_count(adj, ds)
    assert edge_list(6, rep) == [(0,1),(0,3),(0,5),(1,2),(1,3),(1,4),(2,3),(2,4)]
    assert deg == [3,4,3,3,2,1]
    assert close == [Fraction(5,7), Fraction(5,6), Fraction(5,8), Fraction(5,7), Fraction(5,9), Fraction(5,11)]
    assert bet == [Fraction(4), Fraction(7,2), Fraction(1,2), Fraction(1), Fraction(0), Fraction(0)]
    assert maxset(deg) == frozenset({1})
    assert maxset(close) == frozenset({1})
    assert maxset(bet) == frozenset({0})

    print('VERIFY_OK')
    print('connected_counts', connected_counts)
    print('degree_betweenness_maxset_disagreements', set_disagree)
    print('unique_degree_betweenness_conflicts', unique_degree_bet_conflicts)
    print('unique_closeness_betweenness_conflicts', unique_close_bet_conflicts)
    print('six_vertex_conflict_labeled', len(conflict_masks))
    print('six_vertex_conflict_isomorphism_classes', len(classes))
    print('representative_mask', rep)
    print('representative_edges', edge_list(6, rep))
    print('degree', deg)
    print('closeness', [str(x) for x in close])
    print('betweenness', [str(x) for x in bet])
    print('orbit_size', len(orbit))

if __name__ == '__main__':
    main()
