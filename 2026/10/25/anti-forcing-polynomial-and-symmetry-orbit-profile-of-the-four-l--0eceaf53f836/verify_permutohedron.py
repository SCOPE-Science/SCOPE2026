#!/usr/bin/env python3
"""Reproduce the exact anti-forcing distribution of the 4-permutation graph.

No external packages or downloaded data are needed. Uses complete recursion,
a directed-feedback-arc subset DP, and an independent transversal solver.
"""
from collections import Counter
from functools import lru_cache
from itertools import permutations

V = list(permutations(range(4)))
vi = {p: i for i, p in enumerate(V)}
E = []
for u, p in enumerate(V):
    for j in range(3):
        q = list(p)
        q[j], q[j+1] = q[j+1], q[j]
        v = vi[tuple(q)]
        if u < v:
            E.append((u, v))
assert len(V) == 24 and len(E) == 36 and len(set(E)) == 36
edge_index = {frozenset(e): k for k, e in enumerate(E)}
adj = [[] for _ in V]
for k, (a, b) in enumerate(E):
    adj[a].append((b, k))
    adj[b].append((a, k))
assert all(len(a) == 3 for a in adj)
parity = [sum(p[i] > p[j] for i in range(4)
              for j in range(i+1, 4)) % 2 for p in V]
assert sum(x == 0 for x in parity) == 12
assert all(parity[u] != parity[v] for u,v in E)

# Enumerate every matching by branching on the least uncovered vertex.
matchings = []
def enumerate_matchings(uncovered, current):
    if not uncovered:
        matchings.append(tuple(sorted(current)))
        return
    v = (uncovered & -uncovered).bit_length() - 1
    for w, e in adj[v]:
        if uncovered & (1 << w):
            enumerate_matchings(uncovered ^ (1 << v) ^ (1 << w),
                                current + [e])
enumerate_matchings((1 << len(V)) - 1, [])
assert len(matchings) == len(set(matchings)) == 169
assert all(len(m) == 12 and len({z for e in m for z in E[e]}) == 24
           for m in matchings)

# Independent total-count check: Ryser permanent of the 12 by 12 matrix.
left = [v for v in range(len(V)) if not parity[v]]
right = [v for v in range(len(V)) if parity[v]]
ri = {v: i for i,v in enumerate(right)}
rows = [sum(1 << ri[w] for w, _ in adj[v]) for v in left]
permanent = 0
for subset in range(1 << len(right)):
    product = 1
    for r in rows:
        product *= (r & subset).bit_count()
    permanent += (-1 if (len(right) - subset.bit_count()) % 2 else 1) * product
assert permanent == 169

def anti_via_order_dp(m):
    # Contract each matching edge, orient every other edge from its even
    # inversion parity end to its odd end. Alternating cycles -> digraph cycles.
    paired = {v: i for i,e in enumerate(m) for v in E[e]}
    chosen = set(m)
    out = [0] * 12
    for e,(u,v) in enumerate(E):
        if e in chosen:
            continue
        if parity[u]:
            u,v = v,u
        a,b = paired[u],paired[v]
        assert a != b and not (out[a] & (1 << b))
        out[a] |= 1 << b
    dp = [1000] * (1 << 12)
    dp[0] = 0
    for subset in range(1,1 << 12):
        bits = subset
        while bits:
            unit = bits & -bits
            bits -= unit
            a = unit.bit_length() - 1
            rest = subset ^ unit
            # Placing a last: every a -> earlier vertex is a backward edge.
            dp[subset] = min(dp[subset],
                             dp[rest] + (out[a] & rest).bit_count())
    return dp[-1]
values = {m: anti_via_order_dp(m) for m in matchings}
assert Counter(values.values()) == {4:4, 5:16, 6:44, 7:48,
                                    8:39, 9:16, 10:2}

# Exhibit and verify the full natural relabeling / position-reversal action.
automorphisms = []
for symbol_permutation in permutations(range(4)):
    for reverse in (False, True):
        vertex_map = [vi[tuple(symbol_permutation[p[j]] for j in
                        (range(3,-1,-1) if reverse else range(4)))]
                      for p in V]
        edge_map = [edge_index[frozenset((vertex_map[u],vertex_map[v]))]
                    for u,v in E]
        assert len(set(vertex_map)) == 24
        assert len(set(edge_map)) == len(E)
        automorphisms.append(tuple(edge_map))
assert len(automorphisms) == len(set(automorphisms)) == 48

remaining = set(matchings)
orbits = []
while remaining:
    representative = min(remaining)
    orbit = {tuple(sorted(s[e] for e in representative))
             for s in automorphisms}
    assert orbit <= remaining
    assert all(values[m] == values[representative] for m in orbit)
    remaining -= orbit
    orbits.append((representative,len(orbit)))
assert len(orbits) == 17 and sum(size for _,size in orbits) == 169

def two_factor_lengths(m):
    others = set(range(len(E))) - set(m)
    a = [[] for _ in V]
    for e in others:
        u,v = E[e]
        a[u].append(v)
        a[v].append(u)
    assert all(len(row) == 2 for row in a)
    unseen = set(range(24))
    lengths = []
    while unseen:
        start = min(unseen)
        stack = [start]
        unseen.remove(start)
        size = 0
        while stack:
            u = stack.pop()
            size += 1
            for v in a[u]:
                if v in unseen:
                    unseen.remove(v)
                    stack.append(v)
        lengths.append(size)
    return tuple(sorted(lengths))

table = Counter((size, values[m], two_factor_lengths(m))
                for m,size in orbits)
EXPECTED_TABLE = Counter({
    (1,8,(4,4,4,4,4,4)):1,
    (2,10,(6,6,6,6)):1,
    (4,4,(12,12)):1,
    (4,5,(24,)):1,
    (4,7,(6,6,12)):1,
    (4,9,(24,)):1,
    (6,8,(12,12)):1,
    (8,6,(4,4,4,12)):1,
    (8,7,(8,8,8)):1,
    (8,8,(6,18)):1,
    (12,5,(4,10,10)):1,
    (12,6,(4,20)):1,
    (12,7,(24,)):1,
    (12,9,(6,6,12)):1,
    (24,6,(8,16)):1,
    (24,7,(24,)):1,
    (24,8,(6,18)):1,
})
assert table == EXPECTED_TABLE

# Independent algorithm: hit every other perfect matching by an edge not in M.
# Equivalence is direct: if a second matching survives, M is not unique.
def independent_minimum_transversal(m):
    mset = set(m)
    constraints = sorted({sum(1 << e for e in n if e not in mset)
                          for n in matchings if n != m},
                         key=lambda mask: mask.bit_count())
    minimal = []
    for candidate in constraints:
        if not any((candidate & prior) == prior for prior in minimal):
            minimal.append(candidate)
    @lru_cache(None)
    def recurse(unhit):
        if not unhit:
            return 0
        smallest = min(unhit, key=lambda j: minimal[j].bit_count())
        bits = minimal[smallest]
        best = 1000
        while bits:
            ebit = bits & -bits
            bits -= ebit
            still = frozenset(i for i in unhit if not (minimal[i] & ebit))
            best = min(best, 1 + recurse(still))
        return best
    return recurse(frozenset(range(len(minimal))))

for representative,size in orbits:
    assert independent_minimum_transversal(representative) == values[representative]

print('VERTICES=24 EDGES=36 MATCHINGS=169 RYSER=169')
print('ANTI_FORCING_POLYNOMIAL=4z^4+16z^5+44z^6+48z^7+39z^8+16z^9+2z^10')
print('NATURAL_AUTOMORPHISMS=48 MATCHING_ORBITS=17')
for (size, af, typ), mult in sorted(table.items()):
    print('ORBIT size=%d anti=%d twofactor=%s multiplicity=%d' %
          (size, af, ','.join(map(str,typ)), mult))
print('TRANSVERSAL_CHECKS=17')
print('VERIFY_OK')
