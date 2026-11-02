#!/usr/bin/env python3
"""Independent exhaustive checks of the length-two tandem-duplication census.
The small-length check uses the channel directly and a general graph
independence search; it does not use the signature-decomposition identity.
"""
from functools import lru_cache

EXPECTED = {3:8, 4:16, 5:28, 6:48, 7:84, 8:148, 9:260}

def outputs(n, i):
    x = format(i, '0%db' % n)
    return frozenset(x[:j+2]+x[j:j+2]+x[j+2:] for j in range(n-1))

def max_clique_bitsets(neighbors):
    # Bron--Kerbosch with a greedy upper bound; search maximizes compatible sets.
    N = len(neighbors)
    best = 0
    def bound(P):
        # Color remaining compatibility graph; each color is stable.
        colors = 0
        while P:
            colors += 1
            Q = P
            while Q:
                bit = Q & -Q
                v = bit.bit_length()-1
                P &= ~bit
                Q &= ~bit
                Q &= ~neighbors[v]
        return colors
    def visit(P, k):
        nonlocal best
        if not P:
            best = max(best, k)
            return
        if k + bound(P) <= best:
            return
        while P:
            bit = P & -P
            v = bit.bit_length()-1
            P &= ~bit
            if k + 1 + bound(P & neighbors[v]) > best:
                visit(P & neighbors[v], k+1)
            if k + bound(P) <= best:
                return
    visit((1<<N)-1, 0)
    return best

# Direct graph generated from duplication outputs. Verify small parameters
# without the derivative transform or composition graph.
for n in range(3, 10):
    out = [outputs(n,i) for i in range(1<<n)]
    adj = [0]*(1<<n)
    for i in range(1<<n):
        for j in range(i+1,1<<n):
            if not out[i].isdisjoint(out[j]):
                adj[i] |= 1<<j
                adj[j] |= 1<<i
    comp = [((1<<(1<<n))-1) & ~(adj[i] | (1<<i)) for i in range(1<<n)]
    val = max_clique_bitsets(comp)
    assert val == EXPECTED[n], (n, val, EXPECTED[n])
    print(n, val)
print('CROSSCHECK_OK')
