"""Max disjoint homology-support family at K0 (target sharp-boundary certificate).

Enumerates all 512 induced subcomplexes, collects nonempty I with nonzero
reduced Q-homology (exact Fraction boundary-rank via shared routines), then
exhaustively backtracks the maximum pairwise-disjoint subfamily.
Certifies: max size = 3, attained by {123},{456},{789} (the published triple
supports). Hence no four pairwise-disjoint nonempty homology supports exist.
Repro: python3 verify_max_disjoint.py. Stdlib only.
"""
import verify_target_obstruction as V

N = V.N
supp = []
for mask in range(1 << N):
    I = tuple(i for i in range(N) if mask & (1 << i))
    if not I:
        continue
    if V.reduced_betti(I):
        supp.append(set(I))
print(f"nonempty homology supports: {len(supp)}")
assert all(len(s) >= 3 for s in supp), "min support size must be >=3"
supp.sort(key=lambda s: (len(s), sorted(s)))
best = []


def bt(idx, cur):
    if len(cur) > len(best):
        best[:] = list(cur)
    if idx >= len(supp):
        return
    # bound: even taking every remaining set adds at most (remaining slots by vertices)
    # simple vertex-count bound
    used = set().union(*cur) if cur else set()
    # optimistic bound: len(cur) + (#free vertices // 3)
    free = N - len(used)
    if len(cur) + free // 3 <= len(best):
        # still need to try skipping? skipping cannot improve beyond bound either,
        # but bound is uniform over idx so we can prune whole subtree
        return
    s = supp[idx]
    if all(not (s & c) for c in cur):
        cur.append(s)
        bt(idx + 1, cur)
        cur.pop()
    bt(idx + 1, cur)


bt(0, [])
print(f"MAX_DISJOINT_FAMILY_SIZE = {len(best)}")
for s in best:
    print(" member:", sorted(x + 1 for x in s))
assert len(best) == 3, best
assert sorted(sorted(x + 1 for x in s) for s in best) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]], best
print("MAX_DISJOINT_CERT_PASS")
