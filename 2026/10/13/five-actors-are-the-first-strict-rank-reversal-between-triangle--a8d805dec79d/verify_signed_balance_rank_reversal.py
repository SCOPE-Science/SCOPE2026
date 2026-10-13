#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter, defaultdict
from fractions import Fraction

EXPECTED_CLASS_TABLE = {
    3: [((0,0),1), ((1,1),1)],
    4: [((0,0),1), ((2,1),6), ((4,2),1)],
    5: [((0,0),1), ((3,1),10), ((4,2),15), ((5,3),12), ((6,2),15), ((7,3),10), ((10,4),1)],
}
EXPECTED_FULL_SIGNINGS = {3:8,4:64,5:1024}

def edge_pairs(n):
    return list(combinations(range(n),2))

def triangles(n):
    return list(combinations(range(n),3))

def sign_from_mask(mask, eidx):
    return -1 if (mask >> eidx) & 1 else 1

def unbalanced_triangle_count(n, full_mask):
    pairs = edge_pairs(n)
    idx = {e:i for i,e in enumerate(pairs)}
    u = 0
    for a,b,c in triangles(n):
        prod = (
            sign_from_mask(full_mask, idx[(a,b)]) *
            sign_from_mask(full_mask, idx[(a,c)]) *
            sign_from_mask(full_mask, idx[(b,c)])
        )
        if prod < 0:
            u += 1
    return u

def frustration_by_coloring(n, full_mask):
    pairs = edge_pairs(n)
    best = len(pairs)+1
    for colors in range(1 << (n-1)):   # vertex 0 fixed to color 0
        bad = 0
        for ei,(u,v) in enumerate(pairs):
            cu = 0 if u == 0 else ((colors >> (u-1)) & 1)
            cv = 0 if v == 0 else ((colors >> (v-1)) & 1)
            negative = ((full_mask >> ei) & 1) == 1
            # balanced target: positive within groups, negative across groups
            if negative != (cu != cv):
                bad += 1
        best = min(best,bad)
    return best

def switch_mask(n, full_mask, switch_bits):
    pairs = edge_pairs(n)
    out = 0
    for ei,(u,v) in enumerate(pairs):
        su = 0 if u == 0 else ((switch_bits >> (u-1)) & 1)
        sv = 0 if v == 0 else ((switch_bits >> (v-1)) & 1)
        neg = ((full_mask >> ei) & 1) ^ (su ^ sv)
        if neg:
            out |= 1 << ei
    return out

def frustration_by_switching(n, full_mask):
    return min(switch_mask(n, full_mask, x).bit_count() for x in range(1 << (n-1)))

def normalize_at_zero(n, full_mask):
    # Unique switch with vertex 0 unswitched making every 0-i edge positive.
    pairs = edge_pairs(n)
    idx = {e:i for i,e in enumerate(pairs)}
    switch_bits = 0
    for v in range(1,n):
        if (full_mask >> idx[(0,v)]) & 1:
            switch_bits |= 1 << (v-1)
    return switch_mask(n, full_mask, switch_bits)

def triangle_pattern(n, full_mask):
    pairs = edge_pairs(n)
    idx = {e:i for i,e in enumerate(pairs)}
    pat = 0
    for ti,(a,b,c) in enumerate(triangles(n)):
        parity = (
            ((full_mask >> idx[(a,b)]) & 1) ^
            ((full_mask >> idx[(a,c)]) & 1) ^
            ((full_mask >> idx[(b,c)]) & 1)
        )
        if parity:
            pat |= 1 << ti
    return pat

def permute_triangle_pattern(n, pat, perm):
    tris = triangles(n)
    tidx = {t:i for i,t in enumerate(tris)}
    out = 0
    for ti,t in enumerate(tris):
        if (pat >> ti) & 1:
            tt = tuple(sorted(perm[v] for v in t))
            out |= 1 << tidx[tt]
    return out

def canonical_triangle_pattern(n, pat):
    return min(permute_triangle_pattern(n, pat, p) for p in permutations(range(n)))

def normalized_negative_edges(n, normalized_full_mask):
    pairs = edge_pairs(n)
    return [e for i,e in enumerate(pairs) if (normalized_full_mask >> i) & 1]

all_class_data = {}
for n in (3,4,5):
    pairs = edge_pairs(n)
    m = len(pairs)
    stats_by_class = {}
    normalized_class_counts = Counter()
    rep_by_class = {}
    full_stats = Counter()

    # Independent full-signing enumeration.
    for full_mask in range(1 << m):
        U = unbalanced_triangle_count(n, full_mask)
        L1 = frustration_by_coloring(n, full_mask)
        L2 = frustration_by_switching(n, full_mask)
        assert L1 == L2
        full_stats[(U,L1)] += 1

    assert sum(full_stats.values()) == EXPECTED_FULL_SIGNINGS[n]

    # Switching-normalized classification.
    normalized_seen = set()
    for full_mask in range(1 << m):
        norm = normalize_at_zero(n, full_mask)
        normalized_seen.add(norm)

    assert len(normalized_seen) == 1 << ((n-1)*(n-2)//2)

    for norm in sorted(normalized_seen):
        # all 0-i edges are positive
        for v in range(1,n):
            ei = pairs.index((0,v))
            assert ((norm >> ei) & 1) == 0
        U = unbalanced_triangle_count(n, norm)
        L = frustration_by_coloring(n, norm)
        pat = triangle_pattern(n, norm)
        can = canonical_triangle_pattern(n, pat)
        old = stats_by_class.get(can)
        assert old is None or old == (U,L)
        stats_by_class[can] = (U,L)
        normalized_class_counts[can] += 1
        rep_by_class.setdefault(can, norm)

    compact = sorted(
        [((U,L), normalized_class_counts[c]) for c,(U,L) in stats_by_class.items()],
        key=lambda x:(x[0][0],x[0][1],x[1])
    )
    assert compact == EXPECTED_CLASS_TABLE[n], (n, compact)

    # Full-signing multiplicities must be normalized counts times switching class size.
    expected_full = Counter()
    for c,(U,L) in stats_by_class.items():
        expected_full[(U,L)] += normalized_class_counts[c] * (1 << (n-1))
    assert expected_full == full_stats

    all_class_data[n] = (stats_by_class, normalized_class_counts, rep_by_class)

# Minimal strict rank reversal.
for n in (3,4):
    vals = list(all_class_data[n][0].values())
    for a in vals:
        for b in vals:
            Ua,La = a
            Ub,Lb = b
            assert not (Ua < Ub and La > Lb)

stats5,counts5,reps5 = all_class_data[5]
classes5 = list(stats5)
reversals = []
for i,c1 in enumerate(classes5):
    for c2 in classes5[i+1:]:
        U1,L1 = stats5[c1]
        U2,L2 = stats5[c2]
        if (U1-U2)*(L1-L2) < 0:
            reversals.append((c1,c2))
assert len(reversals) == 1

cA,cB = reversals[0]
if stats5[cA] != (5,3):
    cA,cB = cB,cA
assert stats5[cA] == (5,3)
assert stats5[cB] == (6,2)
assert counts5[cA] == 12
assert counts5[cB] == 15

repA = reps5[cA]
repB = reps5[cB]
negA = normalized_negative_edges(5, repA)
negB = normalized_negative_edges(5, repB)
assert negA == [(1,2),(1,4),(2,3)]
assert negB == [(1,4),(2,3)]

TA = Fraction(10-5,10)
FA = Fraction(1,1) - Fraction(2*3,10)
TB = Fraction(10-6,10)
FB = Fraction(1,1) - Fraction(2*2,10)
assert (TA,FA,TB,FB) == (Fraction(1,2),Fraction(2,5),Fraction(2,5),Fraction(3,5))
assert TA > TB and FA < FB

# Counts of raw labeled signings in the two reversal types.
rawA = counts5[cA] * (1 << 4)
rawB = counts5[cB] * (1 << 4)
assert (rawA,rawB) == (192,240)

print("VERIFY_OK")
print("K3_CLASS_TABLE", EXPECTED_CLASS_TABLE[3])
print("K4_CLASS_TABLE", EXPECTED_CLASS_TABLE[4])
print("K5_CLASS_TABLE", EXPECTED_CLASS_TABLE[5])
print("REVERSAL_A", {"U":5,"L":3,"T":"1/2","F":"2/5","negative_edges":negA,"raw_signings":rawA})
print("REVERSAL_B", {"U":6,"L":2,"T":"2/5","F":"3/5","negative_edges":negB,"raw_signings":rawB})
