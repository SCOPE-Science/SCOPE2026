"""Exact, self-contained checks for a four-symbol orientation-aware window code."""
from itertools import product, combinations
from collections import Counter

Q = 4
neg_rev = lambda w: tuple((-a) % Q for a in w[::-1])
rep = lambda w: min(w, neg_rev(w))
triples = sorted({rep(t) for t in product(range(Q), repeat=3)
                  if t != neg_rev(t)})
vertices = sorted({rep(p) for p in product(range(Q), repeat=2)})
assert len(triples) == 28 and len(vertices) == 10
ends = {t: (rep(t[:2]), rep(t[1:])) for t in triples}
degree = Counter()
for src, dst in ends.values():
    degree[src] += 1
    degree[dst] += 1  # A quotient loop contributes twice.
odd = {p for p in vertices if degree[p] % 2}
assert odd == {(0,0),(0,1),(0,3),(1,2),(2,1),(2,2)}

odd_edges = [(t, src, dst) for t, (src, dst) in ends.items()
             if src != dst and src in odd and dst in odd]
matchings = []
for choice in combinations(odd_edges, 3):
    endpoints = [p for _, a, b in choice for p in (a,b)]
    if len(set(endpoints)) == 6:
        matchings.append(tuple(sorted(t for t, _, _ in choice)))
assert len(odd_edges) == 10
assert sorted(matchings) == [
    ((0,0,1),(0,3,2),(1,2,2)),
    ((0,0,3),(0,1,2),(2,2,1)),
]
print('quotient: vertices=10 edges=28 odd_vertices=6; matching_complements=2')

def phi(t, v):
    """Anti-invariant 2-letter coboundary, invariant on negative-reverse 3-orbits."""
    src, dst = t[:2], t[1:]
    weight = lambda p: int(p == v) - int(p == neg_rev(v))
    return weight(src) - weight(dst)

for omitted, v, expected in (
    (matchings[0], (1,2), -2),
    (matchings[1], (0,3), 2),
):
    assert v != neg_rev(v)
    assert all(phi(t,v) == phi(neg_rev(t),v) for t in triples)
    full = sum(phi(t,v) for t in triples)
    left = sum(phi(t,v) for t in triples if t not in omitted)
    assert full == (-1 if v == (1,2) else 1)
    assert left == expected != 0
    print('omitted=', ''.join(map(str, omitted)), 'flux_vertex=',v,
          'full_flux=',full,'remaining_flux=',left)

w = '003122113232010233313033'
W = tuple(map(int,w))
windows = [tuple(W[(i+j)%len(W)] for j in range(3)) for i in range(len(W))]
assert len(W) == 24 and len(set(windows)) == 24
assert all(t != neg_rev(t) for t in windows)
assert not set(windows).intersection({neg_rev(t) for t in windows})
print('witness=',w, 'period=',len(W), 'distinct_windows=',len(set(windows)))
print('CERTIFIED EXACT MAXIMUM=24')
