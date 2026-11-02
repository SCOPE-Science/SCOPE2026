#!/usr/bin/env python3
"""Exact adjacency-extension spectrum checks for line graphs of Johnson graphs."""
from collections import defaultdict
from itertools import combinations


def spectrum(n, k):
    """Construct Johnson edges, then compute every ordered-pair extension mask."""
    points = [sum(1 << t for t in c) for c in combinations(range(n), k)]
    edges, incident = [], [0] * len(points)
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if (points[i] & points[j]).bit_count() == k-1:
                bit = 1 << len(edges)
                edges.append((i,j))
                incident[i] |= bit
                incident[j] |= bit
    adj = [(incident[u] | incident[v]) ^ (1 << e)
           for e,(u,v) in enumerate(edges)]
    size = len(edges)
    degree = 2*(k*(n-k)-1)
    assert len(adj) == size and all(x.bit_count()==degree for x in adj)
    found = set()
    for a in range(size):
        for b in range(a+1, size):
            ab = bool((adj[a] >> b) & 1)
            both = (adj[a] & adj[b]).bit_count()
            only = degree - both - int(ab)
            neither = size - 2 - both - 2*only
            assert min(both, only, neither)>=0
            found.add((int(ab), int(both>0), int(only>0), int(neither>0)))
    return frozenset(found), size

EXPECTED = {
    4:frozenset({(0,1,1,0),(0,1,1,1),(1,1,1,1)}),
    5:frozenset({(0,1,1,1),(1,1,1,1)}),
    6:frozenset({(0,0,1,1),(0,1,1,1),(1,1,1,1)}),
}
count = 0
for n in range(4,11):
    for k in range(2, n//2+1):
        got, size = spectrum(n,k)
        assert got == EXPECTED[min(n,6)], (n,k,got)
        count += 1
        print('PASS',n,k,'edges',size,'signature_count',len(got))
assert count==16, count
print('PAIR_SPECTRA_PASS; parameter_pairs=',count,'; complete_extension_spectra=',len(EXPECTED))
