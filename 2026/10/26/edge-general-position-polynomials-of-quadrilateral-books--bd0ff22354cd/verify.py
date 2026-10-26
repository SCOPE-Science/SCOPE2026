#!/usr/bin/env python3
"""Independent shortest-path and exact-enumerator checks for square-page books.

Requires Python 3.9 or later, standard library only.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def add(*polys):
    n = max(map(len, polys))
    return [sum(p[i] if i < len(p) else 0 for p in polys) for i in range(n)]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def scale(c, a):
    return [c*x for x in a]


def power(a, r):
    v = [1]
    for _ in range(r):
        v = mul(v, a)
    return v


def shift(p, k):
    return [0] * k + list(p)


def closed_polynomial(r):
    """Independent binomial-sum expression in the theorem."""
    E = power([1,1], r)
    # U: choose at least two horizontal edges in one layer; vertical leaf
    # edges are allowed only on pages outside this chosen set.
    U = [0] * (r + 1)
    for a in range(2, r+1):
        U = add(U, shift(scale(comb(r,a), power([1,1], r-a)), a))
    # V: choose at least two edges in each layer, then vertical leaf
    # edges may be chosen only outside the union of the chosen page sets.
    V = [0] * (3*r+1)
    for a in range(2, r+1):
        for b in range(2, r+1):
            for t in range(max(0,a+b-r), min(a,b)+1):
                ways = comb(r,a)*comb(a,t)*comb(r-a,b-t)
                V = add(V, shift(scale(ways, power([1,1], r-a-b+t)), a+b))
    no_spine = add(mul(E, mul([1,r], [1,r])), scale(2, mul([1,r], U)), V)
    with_spine = shift(add(mul(E, [1,2*r,r]), scale(2, U)), 1)
    return add(no_spine, with_spine)


def structural_polynomial(r):
    """Enumerate page sets under the three-edge obstruction description."""
    ans = Counter()
    for aa in range(1 << r):
        a = aa.bit_count()
        for bb in range(1 << r):
            b = bb.bit_count()
            blocked = (aa if a >= 2 else 0) | (bb if b >= 2 else 0)
            free = ((1 << r) - 1) ^ blocked
            cc = free
            while True:
                k = a + b + cc.bit_count()
                ans[k] += 1
                if not aa or not bb or (aa == bb and a == 1):
                    ans[k+1] += 1
                if cc == 0:
                    break
                cc = (cc-1) & free
    return [ans[k] for k in range(3*r+2)]


def graph(r):
    vs = range(2*r+2)
    edges = [(0,1)]
    for i in range(r):
        edges += [(0,2+2*i), (1,3+2*i), (2+2*i,3+2*i)]
    edges = [tuple(sorted(e)) for e in edges]
    adjacency = [set() for _ in vs]
    for u,v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    return adjacency, edges


def shortest_path_obstructions(r):
    """Construct all geodesics from graph distances, not from edge types."""
    adj, edges = graph(r)
    label = {e:i for i,e in enumerate(edges)}
    forbidden = set()
    for s in range(len(adj)):
        dist = [None] * len(adj)
        dist[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if dist[w] is None:
                    dist[w] = dist[v] + 1
                    q.append(w)
        for t in range(s+1, len(adj)):
            if dist[t] < 3:
                continue
            def paths(v, visited, used):
                if v == t:
                    if len(used) >= 3:
                        for e in combinations(used,3):
                            forbidden.add(sum(1 << x for x in e))
                    return
                for w in adj[v]:
                    if w not in visited and dist[w] == dist[v]+1:
                        # Reverse BFS distance guarantees geodesicity; instead
                        # use fixed length and target check for every path.
                        paths(w, visited | {w}, used + [label[tuple(sorted((v,w)))]])
            # A shortest s-t path increases distance from s every step.
            paths(s,{s},[])
    return sorted(forbidden),len(edges)


def brute_polynomial(r):
    forbidden, m = shortest_path_obstructions(r)
    assert m == 3*r+1
    tally = Counter()
    for subset in range(1 << m):
        if not any((subset & f) == f for f in forbidden):
            tally[subset.bit_count()] += 1
    return [tally[k] for k in range(m+1)], len(forbidden)


def main():
    for r in range(1,7):
        a = closed_polynomial(r)
        b = structural_polynomial(r)
        a += [0] * (len(b)-len(a))
        assert a == b, (r,a,b)
        assert sum(a) == 5**r + (2*r+6)*3**(r-1) + (r*r+9*r-4)*2**(r-2) if r >= 2 else sum(a) == 16
        maxima = [k for k,v in enumerate(a) if v][-1]
        expected = max(2*r,r+3) if r >= 2 else 4
        assert maxima == expected
        multiplicity = r if r == 2 else r+1 if r == 3 else 1
        assert a[maxima] == multiplicity, (r,a[maxima],multiplicity)
        if r <= 5:
            c, triple_count = brute_polynomial(r)
            assert c == a, (r,c,a)
            print(f'r={r} paths=verified forbidden_triples={triple_count} total={sum(a)} max={maxima} optima={a[maxima]}')
        else:
            print(f'r={r} paths=not_enumerated two_counting_methods=agree total={sum(a)} max={maxima} optima={a[maxima]}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
