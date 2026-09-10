"""General disjoint-support obstruction at K0 (target stress-test, stdlib only).

Certifies computationally:
 (A) Full 1-skeleton: all 9 singletons + 36 pairs are faces of K0.
 (B) Every nonempty I with |I|<=2 has K_I a simplex => zero reduced homology;
     and NO nonempty I with |I|<=2 carries reduced homology (512-subset sweep).
 (D) H^3(Z_K0;Q)=0 via Hochster aggregation.
Counting step (C) printed: any nonzero positive-degree class supported on J
needs a nonempty I subset J with nonzero homology => |J|>=3; four disjoint
such J need >=12 vertices > 9.
Lemma (E) printed: zero input => 0 in Massey set => singleton forces m=0.
Repro: python3 verify_general_disjoint_obstruction.py (imports the transcriber
module verify_target_obstruction for the shared list/homology routines).
Stdlib only.
"""
from itertools import combinations

import verify_target_obstruction as V

N = V.N

# (A)
singles = sum(1 for i in range(N) if V.is_face((i,)))
pairs = sum(1 for i, j in combinations(range(N), 2) if V.is_face((i, j)))
assert singles == 9, singles
assert pairs == 36, pairs
print(f"A_OK: {singles} singletons, {pairs} pairs all faces (full 1-skeleton)")

# (B) sweep: collect homology supports
nonempty_small_nonzero = []
nonempty_support_sizes = []
for mask in range(1 << N):
    I = tuple(i for i in range(N) if mask & (1 << N) and False)  # placeholder
    I = tuple(i for i in range(N) if mask & (1 << i))
    if not I:
        continue
    b = V.reduced_betti(I)
    if b:
        nonempty_support_sizes.append(len(I))
        if len(I) <= 2:
            nonempty_small_nonzero.append((I, b))
assert not nonempty_small_nonzero, nonempty_small_nonzero
print("B_OK: every nonempty homology support has |I|>=3 "
      f"(min={min(nonempty_support_sizes)}, n_supports={len(nonempty_support_sizes)})")

# (D) Hochster H^3
Hp = {}
for mask in range(1 << N):
    I = tuple(i for i in range(N) if mask & (1 << i))
    for q, d in V.reduced_betti(I).items():
        Hp[q + len(I) + 1] = Hp.get(q + len(I) + 1, 0) + d
assert Hp.get(3, 0) == 0, Hp.get(3)
print(f"D_OK: H^3(Z_K0;Q)=0 (full table p:dim = "
      f"{ {p: Hp.get(p,0) for p in range(16)} })")

print("C_COUNT: 4 disjoint nonempty homology supports need 4x3=12 vertices > 9: IMPOSSIBLE")
print("E_LEMMA: zero among inputs => 0 in Massey set => defined singleton forces m=0,")
print("         hence phi(m)=0 for every linear phi; phi(m)=1 needs 4 nonzero inputs.")
print("ALL_GENERAL_DISJOINT_CHECKS_PASS")
