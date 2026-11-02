#!/usr/bin/env python3
"""An independent symbolic-transfer checker of the odd-prism exchange graph.
Uses only its explicit bit-vector presentation, not forest or cycle testing.
Run: python3 verify_prism_coordinates.py
"""
from collections import Counter, deque
from itertools import combinations


def plus(v):
    return (1 ^ v[1],) + v[2:] + (v[0],)


def minus(v):
    return (v[-1], 1 ^ v[0]) + v[1:-1]


def square_count(neigh):
    opposite = Counter()
    for adj in neigh:
        for a, b in combinations(sorted(adj), 2):
            opposite[(a,b)] += 1
    return sum(v*(v-1)//2 for v in opposite.values())//2


def check(n):
    k = (n-1)//2
    assert k >= 2
    states = [(i, tuple((mask>>j)&1 for j in range(k))) for i in range(n) for mask in range(1<<k)]
    pos = {state:idx for idx, state in enumerate(states)}
    adj = [set() for _ in states]
    for ix, (i,v) in enumerate(states):
        for j in range(1,k):
            w = list(v)
            w[j] ^= 1
            adj[ix].add(pos[i, tuple(w)])
        adj[ix].add(pos[((i+2)%n, plus(v))])
        adj[ix].add(pos[((i-2)%n, minus(v))])
    assert len(states) == n*(1<<k)
    assert all(len(a)==k+1 for a in adj)
    assert all(i in adj[j] for j,a in enumerate(adj) for i in a)
    assert all((sum(states[i][1]) - sum(states[j][1]))%2 for i,a in enumerate(adj) for j in a)
    seen={0};q=deque([0])
    while q:
        for j in adj[q.popleft()]:
            if j not in seen:
                seen.add(j)
                q.append(j)
    assert len(seen)==len(states)
    expected_squares = n * (1 << (k-2)) * ((k-1)*(k-2)//2 + 2*(k-2))
    assert square_count(adj)==expected_squares
    for mask in range(1<<k):
        v=tuple((mask>>j)&1 for j in range(k))
        assert minus(plus(v))==v and plus(minus(v))==v
        w=v
        for _ in range(n):w=plus(w)
        assert w==plus(v), (n,v,w)
    print(f'COORDINATE_PASS n={n} vertices={len(states)} edges={len(states)*(k+1)//2} squares={expected_squares} bipartite=yes')


if __name__=='__main__':
    for n in (5,7,9,11,13,15,17):
        check(n)
    print('PRISM_SYMBOLIC_TRANSFER_PASS')
