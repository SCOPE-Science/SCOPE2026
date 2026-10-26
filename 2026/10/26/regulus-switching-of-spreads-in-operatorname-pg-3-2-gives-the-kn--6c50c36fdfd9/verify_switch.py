#!/usr/bin/env python3
"""Exact enumeration of line-spread regulus switching in PG(3,2).

Scientific verification is finite and self-contained; only Python standard library.
PG(3,2) points = the 15 nonzero vectors in F_2^4, numbered 1..15.
A line is {a,b,a XOR b}.
"""
from itertools import combinations
from collections import Counter, deque
import hashlib, json

points = tuple(range(1, 16))
lines = sorted({tuple(sorted((a,b,a^b))) for a,b in combinations(points, 2)})
assert len(lines) == 35 and len(set(lines)) == 35
line_masks = tuple(sum(1 << (p-1) for p in l) for l in lines)
assert len(set(line_masks)) == 35
all_mask = (1 << 15) - 1

by_point = {p: tuple(i for i, l in enumerate(lines) if p in l) for p in points}

# Cover the least uncovered point; each point occurs in exactly one chosen line.
spreads = []
def enumerate_spreads(uncovered, chosen):
    if not uncovered:
        assert len(chosen) == 5
        spreads.append(tuple(sorted(chosen)))
        return
    p = (uncovered & -uncovered).bit_length()
    for i in by_point[p]:
        lm = line_masks[i]
        if (lm & uncovered) == lm:
            enumerate_spreads(uncovered ^ lm, chosen + [i])
enumerate_spreads(all_mask, [])
spreads = sorted(set(spreads))
assert len(spreads) == 56
SS = [set(s) for s in spreads]
# Distinct incidence fingerprints establish faithfulness of collineations on spreads.
line_fingerprints = [tuple(i for i, S in enumerate(SS) if j in S) for j in range(35)]
assert len(set(line_fingerprints)) == 35
assert {len(f) for f in line_fingerprints} == {8}

# For any 3 lines of a spread, exactly two line partitions cover their 9 points.
# One partition is the original three lines; the other is their opposite regulus.
partitions_by_nine_mask = {}
for t in combinations(range(35), 3):
    mask = line_masks[t[0]] | line_masks[t[1]] | line_masks[t[2]]
    if mask.bit_count() == 9:
        partitions_by_nine_mask.setdefault(mask, []).append(t)
assert len(partitions_by_nine_mask) > 0
switches = set()
for i,s in enumerate(spreads):
    for triple in combinations(s, 3):
        mask = 0
        for l in triple: mask |= line_masks[l]
        versions = partitions_by_nine_mask[mask]
        assert len(versions) == 2
        other = versions[0] if versions[1] == triple else versions[1]
        assert other != triple
        new = tuple(sorted((set(s)-set(triple))|set(other)))
        j = spreads.index(new)
        assert len(SS[i] & SS[j]) == 2
        switches.add(tuple(sorted((i,j))))
assert len(switches) == 280

# Exhaustive pairwise-line test independently matches every regulus switch.
assert switches == {(i,j) for i in range(56) for j in range(i+1,56)
                    if len(SS[i] & SS[j]) == 2}
E = [set() for _ in range(56)]
for i,j in switches:
    E[i].add(j);E[j].add(i)
assert set(map(len,E)) == {10}

# Bitset Bron-Kerbosch with pivot enumerates ALL maximal independent sets
# in the switch graph: maximal cliques of its complement.
FULL = (1 << 56)-1
CM = []
for i in range(56):
    emask = sum(1 << j for j in E[i])
    CM.append(FULL ^ emask ^ (1 << i))
maximal = []
def bits(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length()-1
        mask ^= low

def bron_kerbosch(R, P, X):
    if not (P | X):
        maximal.append(R)
        return
    pivot = max(bits(P|X), key=lambda u: (P & CM[u]).bit_count())
    todo = P & (FULL ^ CM[pivot])
    while todo:
        low = todo & -todo
        v = low.bit_length()-1
        bron_kerbosch(R | low, P & CM[v], X & CM[v])
        P ^= low
        X |= low
        todo ^= low

bron_kerbosch(0, FULL, 0)
assert len(maximal) == len(set(maximal))
# A maximal independent set could be far smaller: all have been enumerated.
maximal_sizes = Counter(x.bit_count() for x in maximal)
assert max(maximal_sizes) == 21
stars = sorted(x for x in maximal if x.bit_count() == 21)
assert len(stars) == 8
assert len(set(stars)) == 8
assert all(sum((stars[k] >> i)&1 for k in range(8)) == 3 for i in range(56))
sig = [tuple(k for k in range(8) if (stars[k] >> i)&1) for i in range(56)]
assert len(set(sig)) == 56 == len(list(combinations(range(8),3)))

# Explicit two-way adjacency test is the requested Kneser isomorphism.
assert all(((i,j) in switches) == set(sig[i]).isdisjoint(sig[j])
           for i in range(56) for j in range(i+1,56))

pair_by_lineoverlap = Counter()
common_neighbors = Counter()
distance_distribution = Counter()
for i in range(56):
    ds={i:0};q=deque([i])
    while q:
        u=q.popleft()
        for v in E[u]:
            if v not in ds:
                ds[v]=ds[u]+1;q.append(v)
    assert len(ds)==56
    for j in range(i+1,56):
        c=len(SS[i]&SS[j]);x=len(E[i]&E[j]);d=ds[j]
        pair_by_lineoverlap[c]+=1
        common_neighbors[(c,x)]+=1
        distance_distribution[d]+=1
assert pair_by_lineoverlap=={0:840,1:420,2:280}
assert common_neighbors=={(2,0):280,(1,4):420,(0,1):840}
assert distance_distribution=={1:280,2:1260}

print('PG_POINTS=15; LINES=35; SPREADS=56')
print('LINE_SPREAD_FINGERPRINTS=DISTINCT_35; SIZE=8')
print('REGULUS_SWITCH_EDGES=280; DEGREE=10; DIAMETER=2')
print('MAXIMAL_NO_SWITCH_SETS='+str(sum(maximal_sizes.values())))
print('MAXIMAL_NO_SWITCH_SIZE_COUNTS='+json.dumps(dict(sorted(maximal_sizes.items())),sort_keys=True))
print('MAXIMUM_NO_SWITCH_SETS=8; SIZE=21; EACH_SPREAD_IN=3')
print('EIGHT_SYMBOL_MAP=ALL_56_TRIPLES; SWITCH_EQ_DISJOINT_TRIPLES=TRUE')
print('UNORDERED_PAIRS_BY_COMMON_LINES='+json.dumps(dict(sorted(pair_by_lineoverlap.items()))))
print('COMMON_SWITCH_NEIGHBOURS='+json.dumps({str(k):v for k,v in sorted(common_neighbors.items())},sort_keys=True))
print('DISTANCE_PAIR_COUNTS='+json.dumps(dict(sorted(distance_distribution.items()))))
print('SPREAD_LIST_SHA256='+hashlib.sha256(json.dumps(spreads,separators=(",",":" )).encode()).hexdigest())
print('SWITCH_EDGE_LIST_SHA256='+hashlib.sha256(json.dumps(sorted(switches),separators=(",",":" )).encode()).hexdigest())
print('PASS')
