"""Degree-gap obstruction: NO nontrivial 4-fold Massey product exists in
H^+(Z_K0;Q) at all (any supports, any input degrees) — target deepening.

Lemma D (standard Massey degree): deg<x1..xn> = sum|xi| - n + 2, so a 4-fold
has degree sum|xi| - 2.
Certified here from the exact 512-subset Hochster sweep:
 (i)  lowest positive degree with H^p != 0 is 5 (H^1=H^2=H^3=H^4=0);
 (ii) highest degree with H^p != 0 is 14 (H^15 = 0; theoretical max
      q+|I|+1 <= 5+9+1 = 15 since max facet size is 6, so H^>=16 = 0
      automatically and H^15 = 0 is checked).
Hence any 4-fold of positive classes has degree >= 4*5-2 = 18 > 14, i.e. lies
in the zero group, so every defined value is m = 0 and phi(m) = 0 != 1.
In particular the target's degree-3 quadruple (output slot 10, nonempty but
input group H^3 = 0) and any disjoint-support quadruple are dead as special
cases. Triples sit exactly at top degree (5+5+5-1 = 14, H^14 = Q^8), so the
hierarchy stops sharply at order 3 by degree alone.
Repro: python3 verify_degree_gap.py. Stdlib only.
"""
import verify_target_obstruction as V

N = V.N
CACHE = {}
for mask in range(1 << N):
    I = tuple(i for i in range(N) if mask & (1 << i))
    CACHE[I] = V.reduced_betti(I)

Hp = {}
for I, b in CACHE.items():
    for q, d in b.items():
        Hp[q + len(I) + 1] = Hp.get(q + len(I) + 1, 0) + d

print("HOCHSTER_TABLE:", {p: Hp.get(p, 0) for p in range(0, 20)})
# (i) lowest positive degree
low = min(p for p in Hp if p >= 1 and Hp[p] > 0)
for p in (1, 2, 3, 4):
    assert Hp.get(p, 0) == 0, (p, Hp.get(p))
assert low == 5, low
print(f"LOW_OK: lowest positive degree = {low} (H^1..H^4 = 0)")
# (ii) top degree: H^15 = 0 and nothing beyond
assert Hp.get(15, 0) == 0
top = max(p for p in Hp if Hp[p] > 0)
assert top == 14, top
# theoretical cap: every face has <= 6 vertices (max facet size), so
# reduced homology q <= 5, hence p = q+|I|+1 <= 15 for all I
maxface = 0
for I in CACHE:
    # face sizes within I bounded by global facet size; check directly:
    # q present implies q <= len(I)-1 <= 8, but use global facet cap:
    for q in CACHE[I]:
        assert q + len(I) + 1 <= 5 + 9 + 1, (I, q)
print(f"TOP_OK: highest nonzero degree = {top} (H^15 = 0, cap 15)")
# degree gap
min4 = 4 * low - 2
assert min4 == 18 and min4 > top
print(f"GAP_OK: min 4-fold degree 4*{low}-2 = {min4} > {top} = top degree")
print(f"COROLLARY: every defined 4-fold value m has m = 0 (lands in H^{min4}+ = 0),")
print("  so phi(m) = 0 != 1 for every linear detector phi. TARGET CONJUNCTION IMPOSSIBLE.")
# triple sharpness note
assert 5 + 5 + 5 - 1 == 14 and Hp.get(14, 0) == 8
print("SHARP_OK: triple output degree 5+5+5-1 = 14 = top degree (H^14 = Q^8 nonzero)")
print("DEGREE_GAP_PASS")
