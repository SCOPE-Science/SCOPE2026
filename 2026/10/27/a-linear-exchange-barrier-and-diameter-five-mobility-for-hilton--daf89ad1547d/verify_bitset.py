"""Exact labeled extremizer overlap and batch-exchange checks, using bitsets.

Requires only Python 3.9+ standard library; run: python verify_bitset.py
"""
from itertools import combinations
from collections import Counter, deque
from math import comb


def verify(n):
    triples = list(combinations(range(n), 3))
    positions = {t: i for i, t in enumerate(triples)}
    fam = {}
    for t in combinations(range(n), 3):
        q = set(t)
        fam[('A', t)] = sum(1 << positions[e] for e in triples
                               if len(set(e) & q) >= 2)
    for x in range(n):
        choices = [a for a in range(n) if a != x]
        for s in combinations(choices, 3):
            q = set(s)
            fam[('H', x, s)] = sum(1 << positions[e] for e in triples
                                     if e == s or (x in e and bool(q & set(e))))
    keys = list(fam)
    assert len(keys) == (n-2)*comb(n, 3)
    assert len(set(fam.values())) == len(keys)
    assert all(v.bit_count() == 3*n-8 for v in fam.values())
    adj = {k: [] for k in keys}
    min_exchange = 3*n
    for p, a in enumerate(keys):
        for b in keys[:p]:
            distance = 3*n-8-(fam[a] & fam[b]).bit_count()
            min_exchange = min(min_exchange, distance)
            formula = False
            if a[0] == b[0] == 'H':
                formula = a[1] == b[1] and len(set(a[2]) & set(b[2])) == 2
            elif a[0] != b[0]:
                A = a if a[0] == 'A' else b
                H = a if a[0] == 'H' else b
                formula = H[1] in A[1] and set(A[1]) - {H[1]} <= set(H[2])
            if distance == n-4:
                assert formula, (n, a, b, 'unexpected adjacent')
                adj[a].append(b)
                adj[b].append(a)
            else:
                assert not formula, (n, a, b, 'missing adjacent')
                assert distance > n-4, (n, a, b, distance)
    assert min_exchange == n-4
    assert all(len(adj[k]) == 3*(n-3) for k in keys)
    assert sum(map(len, adj.values()))//2 == (n-2)*comb(n,3)*3*(n-3)//2

    def distances(root):
        dist = {root: 0}
        que = deque([root])
        while que:
            v = que.popleft()
            for w in adj[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    que.append(w)
        return Counter(dist.values()), len(dist)

    ca, a_reached = distances(('A', (0,1,2)))
    ch, h_reached = distances(('H', 0, (1,2,3)))
    assert a_reached == h_reached == len(keys)
    assert max(ca) == max(ch) == 5
    print({'n':n, 'families':len(keys), 'minimum_exchange':min_exchange,
           'edges':sum(map(len,adj.values()))//2, 'regular_degree':3*(n-3),
           'diameter':5, 'A_layers':[ca[i] for i in range(6)],
           'H_layers':[ch[i] for i in range(6)]})


if __name__ == '__main__':
    for n in range(7, 11):
        verify(n)
    print('PASS: direct all-pair overlap and orbit-distance checks')
