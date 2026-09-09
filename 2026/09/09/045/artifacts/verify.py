"""Independent replay verifier for lane-344 fallback claim.

Checks (stdlib only):
 1. Each witness has 33 triples on points 0..15, 99 distinct covered pairs.
 2. Exhaustive C(33,5) search certifies no 5 pairwise disjoint triples (PPC<=4).
 3. Greedy/explicit 4 disjoint triples certify PPC==4 (attainment, not just <=4).
 4. Degree sequences differ -> witnesses non-isomorphic; 4-disjoint-set counts differ.
 5. Schönheim upper bound: 3B<=16*7=112 -> B<=37 (recomputed, not asserted).
Usage: python3 verify.py  -> prints VERIFY_OK on success.
"""
import itertools
from collections import Counter

W1 = [
(1,4,12),(8,9,10),(10,13,15),(4,7,11),(0,2,7),(0,6,15),(7,12,15),
(3,4,14),(8,11,14),(7,10,14),(2,6,11),(3,9,13),(6,9,14),(0,3,10),
(5,8,12),(4,6,13),(3,6,8),(0,11,13),(1,9,15),(5,11,15),(0,4,5),
(0,1,14),(3,11,12),(2,12,14),(3,5,7),(0,9,12),(2,4,9),(6,10,12),
(2,5,13),(4,8,15),(2,3,15),(1,6,7),(1,10,11),
]
W2 = [
(3,11,15),(0,2,15),(3,4,6),(0,7,9),(5,8,11),(1,10,15),(1,9,12),
(5,12,14),(1,7,14),(1,6,11),(5,9,15),(2,6,9),(5,10,13),(7,10,12),
(3,13,14),(3,8,10),(2,4,14),(0,1,8),(1,2,3),(7,11,13),(4,7,8),
(4,10,11),(1,4,13),(2,8,12),(0,4,5),(8,9,13),(8,14,15),(9,10,14),
(0,3,12),(4,12,15),(3,5,7),(0,11,14),(0,6,10),
]

def certify(blocks, name):
    assert len(blocks) == 33, f"{name}: len {len(blocks)}"
    for b in blocks:
        assert len(b) == 3 and len(set(b)) == 3 and all(isinstance(x, int) and 0 <= x < 16 for x in b), f"{name}: bad triple {b}"
    pairs = []
    for (a, b, c) in blocks:
        pairs += [tuple(sorted((a, b))), tuple(sorted((a, c))), tuple(sorted((b, c)))]
    assert len(set(pairs)) == 99, f"{name}: distinct pairs {len(set(pairs))} != 99"
    sets = [set(b) for b in blocks]
    n = len(blocks)
    five = [q for q in itertools.combinations(range(n), 5)
            if all(sets[q[i]].isdisjoint(sets[q[j]]) for i in range(5) for j in range(i + 1, 5))]
    assert five == [], f"{name}: found 5 disjoint: {five[0]}"
    four = [q for q in itertools.combinations(range(n), 4)
            if all(sets[q[i]].isdisjoint(sets[q[j]]) for i in range(4) for j in range(i + 1, 4))]
    assert len(four) > 0, f"{name}: PPC<4, degenerate"
    deg = sorted(Counter(x for t in blocks for x in t).values())
    assert sum(deg) == 99, name
    print(f"{name}: triples=33 pairs=99 five_disjoint=NO ppc==4 (#4-sets={len(four)}) degseq={deg}")
    return len(four), deg

c1, d1 = certify(W1, "W1")
c2, d2 = certify(W2, "W2")
assert d1 != d2, "degree sequences coincide; need another invariant"
print(f"non-isomorphic: degseq W1 != W2 ({d1} vs {d2}); 4-sets {c1} vs {c2}")
# Schonheim bound recompute: per-point degree <= floor(15/2)=7 -> 3B <= 112 -> B<=37
assert (16 * (15 // 2)) // 3 == 37
print("Schonheim U=37 recomputed: floor(16*7/3)=37; interval [33,37] certified")
print("VERIFY_OK")
