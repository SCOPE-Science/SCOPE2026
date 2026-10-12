"""Independent enumeration of semitotal maximal independent sets in central graphs.
Python 3.9+; no dependencies. All objects are finite simple graphs.
"""
from collections import Counter, deque
from itertools import combinations, product


def construction(parts):
    labels = [p for p, n in enumerate(parts) for _ in range(n)]
    n = len(labels)
    edges = [(u, v) for u in range(n) for v in range(u+1, n)
             if labels[u] != labels[v]]
    E = set(edges)
    adj = [set() for _ in range(n+len(edges))]
    for u in range(n):
        for v in range(u+1, n):
            if (u, v) not in E:
                adj[u].add(v)
                adj[v].add(u)
    for i, (u, v) in enumerate(edges):
        w = n+i
        adj[u].add(w)
        adj[v].add(w)
        adj[w].update((u, v))
    return labels, edges, adj


def dists(adj):
    ans = []
    for s in range(len(adj)):
        d = [-1] * len(adj)
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u]+1
                    q.append(v)
        ans.append(d)
    return ans


def test_set(mask, adj, dist):
    V = len(adj)
    selected = [i for i in range(V) if mask & (1 << i)]
    chosen = set(selected)
    # Independence and domination, tested against the actual graph.
    if any(adj[u] & chosen for u in selected):
        return False
    if any(not (adj[u] & chosen) for u in range(V) if u not in chosen):
        return False
    if any(not any(dist[u][v] == 2 for v in selected if v != u)
           for u in selected):
        return False
    return True


def formula(parts):
    labels, edges, _ = construction(parts)
    r, n = len(parts), len(labels)
    by_part = [[u for u in range(n) if labels[u] == i] for i in range(r)]
    masks = set()
    for b in range(1 << r):
        S = tuple(i for i in range(r) if b & (1 << i))
        residual = [parts[i] - int(i in S) for i in range(r)]
        # Outside originals in a completely unchosen part need a residual edge.
        if any(sum(residual[j] for j in range(r) if j != i) == 0
               for i in range(r) if i not in S):
            continue
        # A lone chosen original needs a residual edge in its own part.
        if len(S) == 1:
            i = S[0]
            if residual[i] == 0 or sum(residual[j] for j in range(r)
                                       if j != i) == 0:
                continue
        # A lone chosen subdivision vertex needs a distance-two witness.
        if sum(residual) == 2:
            active = [i for i in range(r) if residual[i] > 0]
            if len(active) == 2 and not any(i in S for i in active):
                continue
        for picked in product(*(by_part[i] for i in S)):
            X = set(picked)
            mask = sum(1 << u for u in X)
            for j, (u, v) in enumerate(edges):
                if u not in X and v not in X:
                    mask |= 1 << (n+j)
            if mask in masks:
                raise AssertionError('duplicate set in formula')
            masks.add(mask)
    return masks


def run():
    nprofiles, candidates = 0, 0
    for r in range(2, 6):
        for parts in product((1, 2, 3), repeat=r):
            labels, edges, adj = construction(parts)
            N = len(adj)
            if N > 18:
                continue
            D = dists(adj)
            predicted = formula(parts)
            observed = {mask for mask in range(1 << N)
                        if test_set(mask, adj, D)}
            assert observed == predicted, (parts, len(observed), len(predicted))
            nprofiles += 1
            candidates += 1 << N
    print('PASS exhaustive_profiles', nprofiles)
    print('PASS exhaustive_vertex_subsets', candidates)
    # Larger profiles: exhaustively verify all templates, without claiming all
    # subsets of the larger central graph have been enumerated.
    for parts in [(2, 3, 2), (3, 3, 3), (1, 1, 4, 2), (2, 2, 2, 2)]:
        _, _, adj = construction(parts)
        D = dists(adj)
        F = formula(parts)
        assert all(test_set(m, adj, D) for m in F)
    print('PASS larger_profile_template_checks', 4)
    # Polynomial reference values follow directly from actual selected sets.
    for parts in [(1, 1), (1, 1, 1), (1, 1, 1, 1),
                  (2, 2), (2, 2, 2), (1, 2, 2)]:
        counter = Counter(m.bit_count() for m in formula(parts))
        print('PROFILE', ','.join(map(str, parts)),
              ' '.join('%d:%d' % (k, v) for k, v in sorted(counter.items())))


if __name__ == '__main__':
    run()
