"""Exhaustive 3-extension check for the 64-vertex binary Latin-square graph.
No external dependencies. Every unordered anchor triple and all eight patterns are evaluated.
"""
from itertools import combinations
from collections import Counter

Q = 8
V = tuple((r,c) for r in range(Q) for c in range(Q))
N = len(V)
ADJ = tuple(sum(1 << j for j,(s,d) in enumerate(V)
                if j != i and (r == s or c == d or (r ^ c) == (s ^ d)))
            for i,(r,c) in enumerate(V))
ALL = (1 << N) - 1
mins = {e: [N+1]*8 for e in range(4)}
zero = 0
freq = Counter()
for x,y,z in combinations(range(N),3):
    anchors = (x,y,z)
    e = sum(bool(ADJ[a] & (1 << b)) for a,b in ((x,y),(x,z),(y,z)))
    available = ALL ^ (1 << x) ^ (1 << y) ^ (1 << z)
    for pattern in range(8):
        candidate = available
        for bit,v in enumerate(anchors):
            candidate &= ADJ[v] if (pattern >> bit) & 1 else ALL ^ ADJ[v]
        n = candidate.bit_count()
        mins[e][pattern] = min(mins[e][pattern], n)
        freq[n] += 1
        if n == 0:
            zero += 1
            raise AssertionError((anchors, pattern, e))
print('vertices', N)
print('anchor_triples', N*(N-1)*(N-2)//6)
print('tested_patterns', sum(freq.values()))
print('zero_patterns', zero)
print('minima_by_induced_edge_count', mins)
print('global_minimum', min(min(x) for x in mins.values()))
