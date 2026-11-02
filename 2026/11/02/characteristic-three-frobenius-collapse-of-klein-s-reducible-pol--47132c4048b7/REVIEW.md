# Scientific review: characteristic-three Klein-polar degeneration

## Correctness — PASS

The claim is a divisor identity over the algebraic closure of characteristic three, for every integer \(k\ge0\), plus an exact finite-field descent table. The defining integer determinants produce the degree-21 primitive invariant with coefficient one at \(x^{21}\), and exact integer polynomial division shows that its gradient pullback has quotient of degree 42. Cyclic invariance and \(\overline{\nabla F}=(z^3,x^3,y^3)\) prove the infinite-iterate identity symbolically. The field \(\mathbf F_{729}\) certificate establishes exactly 21 distinct factors and all 210 pair intersections; Frobenius testing determines the minimal degrees. Every required finite computation was replayed from the included actual verifier, without stale external output. Risks: the result is model-specific; different integral forms may specialize differently.

## Originality — PASS (best-knowledge, priority risk stated)

The arXiv:1803.06411 primary text (full relevant §§1, 2, 7) supplies the complex product and proves the iterated **reducedness** theorem there, explicitly working over \(\mathbb C\). arXiv:2211.15309 §3.1 supplies the exact determinant construction and complex conic factorizations. The 2019 pullback article concerns complex morphisms. The classical reduced 21-line intersection counts and a previously established odd-characteristic reduction of their geometric lattice are *not* new; they cannot imply the nonreduced conic divisor or its arithmetic splitting fields. Targeted checks for equivalent formulas, broader theorems, and exact field-of-definition tables found no encompassing prior statement. An inaccessible/unindexed historical source remains a priority risk; the search does not prove absolute novelty.

## Mathematical value — PASS

A natural polar divisor attached to a smooth plane quartic degenerates to a high-multiplicity line divisor solely through the inseparability of its gradient. The phenomenon persists through every iterate and contrasts directly with the source's complex reducedness theorem. The complete arithmetic support and residue degrees (including one rational triple point and no rational lines) determine how this distinguished configuration descends to the prime field, rather than merely reproducing its geometric incidence counts. The exact fact concerns a canonical published family with a meaningful reduction boundary; no general downstream classification is asserted.

## Closest literature and residual limits

Primary: Pokora–Roé, arXiv:1803.06411, §§2, 7; Gévay–Pokora, arXiv:2211.15309, §3.1. Supporting: Pokora–Roé, DOI:10.1007/s00025-019-1031-x. Neither positive-characteristic intrinsic moduli statements nor coordinate-model invariance are claimed. The coefficient and field certificates are supplied as complete executable source, not replaced by screenshots of program logs. Independently derived publication priority and independent external mathematical audit remain unverified.

Self-review: passed. Independent audit: not yet performed.
