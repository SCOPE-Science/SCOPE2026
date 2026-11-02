"""Independent eight-symbol Fano-plane verification of packing trades.

Run: python verify_fano_cosets.py
Only Python's standard library is needed.
"""
from itertools import combinations, permutations
from collections import Counter, deque

SYMS = set(range(8))
triples = tuple(combinations(range(8), 3))
# Geometric lines encode complementary 4+4 partitions of eight symbols.
def four_partition(Q):
    Q = frozenset(Q)
    assert len(Q) == 4
    R = frozenset(SYMS - Q)
    return min(tuple(sorted(Q)), tuple(sorted(R)))

line_system = {four_partition(Q) for Q in combinations(range(8), 4)}
assert len(line_system) == 35
spread_lines = {}
for T in triples:
    S = frozenset(four_partition(set(T) | {x}) for x in SYMS - set(T))
    assert len(S) == 5
    spread_lines[frozenset(T)] = S
assert len(spread_lines) == 56

# Independent generation by the unique seven-point Steiner triple system.
base_lines = frozenset(frozenset((a-1, b-1, (a ^ b)-1))
                       for a, b in combinations(range(1, 8), 2))
assert len(base_lines) == 7
all_planes = set()
for omitted in range(8):
    present = sorted(SYMS - {omitted})
    here = set()
    for ordered in permutations(present):
        fano = frozenset(frozenset(ordered[i] for i in block)
                         for block in base_lines)
        here.add(fano)
    assert len(here) == 30
    all_planes.update(here)
assert len(all_planes) == 240
planes = tuple(sorted((tuple(sorted(tuple(sorted(t)) for t in P))
                       for P in all_planes)))
planes = [frozenset(map(frozenset, P)) for P in planes]
assert len(set(planes)) == 240

# Every seven-block Fano configuration is a complete spread packing.
packings = set()
for F in planes:
    assert len(F) == 7 and len(set().union(*F)) == 7
    union = set()
    for T in F:
        assert not union & spread_lines[T]
        union.update(spread_lines[T])
    assert union == line_system
    packings.add(frozenset(F))
assert len(packings) == 240
index = {F:i for i,F in enumerate(planes)}

# A legal move swaps the omitted symbol z and one present symbol y.
# It replaces exactly the three Fano blocks through y, fixing four blocks.
adj = [set() for _ in planes]
for i,F in enumerate(planes):
    omitted = next(iter(SYMS - set().union(*F)))
    for y in SYMS - {omitted}:
        image = frozenset(frozenset(omitted if x == y else y if x == omitted else x
                                    for x in T) for T in F)
        assert image in index
        j = index[image]
        assert len(F & image) == 4
        adj[i].add(j)
    assert len(adj[i]) == 7
for i,j in combinations(range(240), 2):
    exactly_three = len(planes[i] & planes[j]) == 4
    assert (j in adj[i]) == exactly_three
assert all(i in adj[j] for i in range(240) for j in adj[i])
assert sum(map(len,adj)) // 2 == 840

# The omitted-symbol move is an odd permutation of the eight labels.
# Transitivity of the full symmetric group follows from the exhaustive
# permutation generation; the stabilizer of a Fano configuration is even.
def parity(p):
    return (-1) ** sum(p[i] > p[j] for i in range(8) for j in range(i+1,8))
reference = base_lines
signs = {}
for perm in permutations(range(8)):
    image = frozenset(frozenset(perm[i] for i in T) for T in reference)
    sign = parity(perm)
    if image in signs:
        assert signs[image] == sign
    else:
        signs[image] = sign
assert len(signs) == 240
assert Counter(signs.values()) == {-1:120, 1:120}
assert all(signs[planes[i]] == -signs[planes[j]]
           for i in range(240) for j in adj[i])

expected = (1, 7, 42, 105, 77, 8)
for root in range(240):
    dist = {root: 0}
    q = deque([root])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    assert len(dist) == 240
    assert tuple(Counter(dist.values())[d] for d in range(6)) == expected

print('EIGHT_SYMBOL_FANO_COSSET_240_PACKINGS_PASS')
print('ALL_STAR_TRANSPOSITION_TRADES_AND_TWO_CHIRALITIES_PASS')
print('ALL_ROOTS_DIAMETER_5_DISTANCE_DISTRIBUTION_PASS', expected)
