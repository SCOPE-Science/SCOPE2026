"""Support-spreading lemma certification (Lemma S application, stdlib only).

For each J subset [9]: H^*(Z_{K_J}) = (+) over I subset J of
H̃^{*-|I|-1}(K_I) (split inclusion). Certifies:
 (1) if |J| <= 2 then H^{>0}(Z_{K_J};Q) = 0 (no nonzero positive-degree class
     can be supported on J);
 (2) reports min |J| carrying positive-degree cohomology (= 3).
Together with 4 disjoint J needing 4*3 = 12 > 9 vertices, no four nonzero
positive-degree disjointly supported classes exist (any degrees).
Repro: python3 verify_support_lemma.py. Stdlib only.
"""
from itertools import combinations

import verify_target_obstruction as V

N = V.N
CACHE = {}
for mask in range(1 << N):
    I = tuple(i for i in range(N) if mask & (1 << i))
    CACHE[I] = V.reduced_betti(I)

def pos_cohomology(J):
    """Total dim of H^{>0}(Z_{K_J}) = sum over I subset J, q+|I|+1 >= 1."""
    tot = 0
    JJ = set(J)
    for I, b in CACHE.items():
        if set(I) <= JJ:
            for q, d in b.items():
                if q + len(I) + 1 >= 1:
                    tot += d
    return tot

bad = []
minpos = None
for r in range(0, N + 1):
    for J in combinations(range(N), r):
        t = pos_cohomology(J)
        if r <= 2 and t != 0:
            bad.append((J, t))
        if t > 0 and (minpos is None or r < minpos):
            minpos = r
assert not bad, bad[:5]
print(f"SUPPORT_LEMMA_OK: all J with |J|<=2 have H^>0(Z_{{K_J}}) = 0 "
      f"(checked {sum(1 for r in (0,1,2) for _ in combinations(range(N), r))} subsets)")
print(f"MIN_SUPPORT_OK: smallest |J| with positive cohomology = {minpos}")
assert minpos == 3
print("COUNT: 4 disjoint positive supports need >= 12 vertices > 9: IMPOSSIBLE")
print("SUPPORT_LEMMA_PASS")
