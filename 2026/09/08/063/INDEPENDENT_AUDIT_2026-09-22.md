# Independent three-axis audit — 2026-09-24

Reviewer type: separate AI audit. This document records reproducible scientific checks and literature comparison, not a transcript of private reasoning.

## Audited source

- Record: `SCOPE-20260908-063`
- Source path: `2026/09/08/063`
- Inventory source tree: `328b2278c7f0625a5e6df2848ffe949e6e10904b`
- Audited `RESULT.md` blob: `6a6e8a8a70af7eef898aa7c685a1565386df5636`
- Claims audited: `M_3(2,7)=15`; a complete `(15,3)`-arc in `PG(2,8)` with spectrum `(12,18,12,31)`; and the elementary interval upper bound `k<=19` at `q=8`.

## Correctness — PASS

The finite-geometry claims were independently reconstructed from the stated coordinates rather than inherited from the existing review.

For `PG(2,7)`, a fresh incidence construction from normalized nonzero homogeneous triples produced 57 points and 57 lines. The 15 listed points have maximum line occupancy 3, line spectrum `(n_0,n_1,n_2,n_3)=(12,0,15,30)`, and every one of the 42 outside points lies on a 3-secant, so the arc is complete. The upper bound used in the record is also valid: through a point of a `(k,3)`-arc there are `q+1` lines and each contains at most two further arc points, hence `k-1<=2(q+1)`. At `q=7`, the record's refinement rules out `k=16,17` by the forced 3-secant counts: `k=16` forces seven 3-secants through each arc point, so `3 t_3=16*7`, impossible; `k=17` forces eight, so `3 t_3=17*8`, impossible. The verified 15-point witness therefore closes the maximum at 15.

For `PG(2,8)`, `GF(8)` was independently implemented as `GF(2)[x]/(x^3+x+1)` and the projective plane reconstructed from normalized homogeneous triples, yielding 73 points and 73 lines. The listed 15-point set has maximum line occupancy 3, spectrum `(12,18,12,31)`, and every one of the 58 outside points lies on a 3-secant, so it is complete. The same point-line count gives the stated `k<=19` upper bound. No optimality above 15 is inferred.

## Originality — FAIL

Both headline finite-geometry contributions are covered by earlier literature.

For `PG(2,7)`, S. Marcugini, A. Milani and F. Pambianco, **Classification of the (n,3)-arcs in PG(2,7)**, Journal of Geometry 80 (2004), 179–184, DOI `10.1007/s00022-004-1777-4`, gives an exhaustive classification of `(n,3)`-arcs in `PG(2,7)`. The later open-access paper G. Innamorati and M. Zannetti, **The Shape of the (15,3)-Arc of PG(2,7)**, Mathematics 9 (2021), 486, DOI `10.3390/math9050486`, explicitly describes the prior computer-based proof that the maximum is 15 and that the maximum `(15,3)`-arc is unique up to projectivity. Thus `M_3(2,7)=15` was known long before this record.

For `PG(2,8)`, S. A. Alabdullah, **On complete (k,3)-arcs in PG(2,8)**, Journal of Basrah Researches (Sciences) 37(4) (2011), investigates complete `(k,3)`-arcs in that plane. Section 3.13 and Table 3.10 list projectively distinct `(15,3)`-arcs; the first listed type has line counts `r_3=31, r_2=12, r_1=18, r_0=12`, exactly the record's spectrum `(n_0,n_1,n_2,n_3)=(12,18,12,31)`. The record's 15-point complete-arc headline is therefore not a new parameter regime or new spectrum.

Checked sources include:
- https://doi.org/10.1007/s00022-004-1777-4
- https://www.mdpi.com/2227-7390/9/5/486
- https://www.researchgate.net/publication/272290873_On_complete_k3-arcs_in_PG28

Searches included equivalent terminology (`(n,3)-arc`, complete arc, maximum arc, projective classification, line spectrum) rather than title-only matching.

## Scientific value — FAIL

After subtracting known coverage, the remaining content does not support an accepted scientific finding. The `q=7` maximum is established by prior classification. The `q=8` 15-point complete arc and its line spectrum already appear in earlier classification work. The residual bound `k<=19` is the immediate general inequality `k<=2q+3`, and the NMDS weight distribution is a routine translation of the line spectrum. These are useful verification certificates but not a meaningful new regime, substantial improvement, or reusable structural theorem.

## Repair attempt

A bounded repair was considered by narrowing the record to its explicit coordinate witnesses, line spectra, NMDS certificates, and the `q=8` interval. This does not rescue the record: the decisive geometric objects and spectrum are already present in prior literature, while the remaining upper bound is elementary and non-sharp.

## Final disposition

**FAILED** on originality and scientific value; correctness passes. Scientific rejection evidence is published at the source record; archival relocation to the assigned failed-attempt path remains pending and does not affect the scientific verdict.
