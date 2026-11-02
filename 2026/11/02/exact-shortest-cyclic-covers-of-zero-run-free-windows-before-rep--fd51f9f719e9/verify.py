"""Independent finite checks for zero-run-free cyclic covering theorem.

Python 3 standard library only; no external data or services.
The all-parameter proof is in RESULT.md: this program tests finite instances.
"""
from itertools import product
from collections import Counter, deque, defaultdict


def model(q, h, k):
    alphabet = tuple(str(i) for i in range(q))
    bad = '0' * h
    words = [''.join(a) for a in product(alphabet, repeat=k) if bad not in ''.join(a)]
    indeg, outdeg = Counter(), Counter()
    adj = defaultdict(list)
    for w in words:
        u, v = w[:-1], w[1:]
        outdeg[u] += 1
        indeg[v] += 1
        adj[u].append(v)
    nodes = set(indeg) | set(outdeg)
    sources = sorted(v for v in nodes if indeg[v] - outdeg[v] == 1)
    targets = sorted(v for v in nodes if outdeg[v] - indeg[v] == 1)
    assert all(abs(indeg[v] - outdeg[v]) <= 1 for v in nodes)
    return words, nodes, adj, sources, targets


def shortest(adj, origin):
    d = {origin: 0}
    Q = deque([origin])
    while Q:
        u = Q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v] = d[u] + 1
                Q.append(v)
    return d


def assignment_min_cost(cost):
    m = len(cost)
    if not m:
        return 0
    assert m <= 16
    dp = {0: 0}
    for row in cost:
        nd = {}
        for mask, score in dp.items():
            for j, val in enumerate(row):
                if not (mask >> j) & 1:
                    nxt = mask | 1 << j
                    new = score + val
                    if new < nd.get(nxt, 10**20):
                        nd[nxt] = new
        dp = nd
    return dp[(1 << m) - 1]


def construct_cycle(words, sources, targets, h, k):
    d = k - h
    extra = []
    for u, v in zip(sources, targets):
        current = u
        for c in v[h - 1:]:
            w = current + c
            assert '0' * h not in w
            extra.append(w)
            current = w[1:]
        assert current == v
    edges = words + extra
    adj = defaultdict(list)
    for w in edges:
        adj[w[:-1]].append((w[1:],w))
    assert all(not ('0' * h in w) for w in edges)
    vstack = [edges[0][:-1]]
    estack = []
    backwards = []
    while vstack:
        u = vstack[-1]
        if adj[u]:
            v,w = adj[u].pop()
            vstack.append(v)
            estack.append(w)
        else:
            vstack.pop()
            if estack:
                backwards.append(estack.pop())
    tour = backwards[::-1]
    assert len(tour) == len(edges)
    assert all(tour[i][1:] == tour[(i+1)%len(tour)][:-1] for i in range(len(tour)))
    cyclic = ''.join(w[-1] for w in tour)
    assert len(cyclic) == len(edges)
    actual = {(''.join(cyclic[(i+j)%len(cyclic)] for j in range(k))) for i in range(len(cyclic))}
    assert actual == set(words)
    return cyclic, len(extra)


def run():
    cases = 0
    checked_edges = 0
    verified_shortest_pairs = 0
    optimal_sums = 0
    for q, max_h in [(2,5),(3,4),(4,3)]:
        for h in range(2,max_h+1):
            for k in range(h,2*h+1):
                if q**k > 7500:
                    continue
                words, nodes, adj, sources, targets = model(q,h,k)
                d = k-h
                m = 0 if d==0 else (q-1)*(q**(d-1) - (1 if d == h else 0))
                assert len(sources) == len(targets) == m
                predicted_extra = d*m
                _, extra = construct_cycle(words,sources,targets,h,k)
                assert extra == predicted_extra
                if m <= 16:
                    cost = []
                    for u in sources:
                        dist = shortest(adj, u)
                        assert all(v in dist and dist[v] >= d for v in targets)
                        cost.append([dist[v] for v in targets])
                    optimum = assignment_min_cost(cost)
                    assert optimum == predicted_extra, (q,h,k,optimum,predicted_extra)
                    verified_shortest_pairs += m*m
                    optimal_sums += 1
                cases += 1
                checked_edges += len(words)
    print(f'VERIFY_OK q=2..4 h=2..5 cases={cases} admissible_edges={checked_edges} '
          f'checked_source_target_pairs={verified_shortest_pairs} exact_assignment_instances={optimal_sums}')

if __name__ == '__main__':
    run()
