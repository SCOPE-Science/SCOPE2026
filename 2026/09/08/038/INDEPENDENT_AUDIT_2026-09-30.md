# Independent audit — 2026-09-30

**Record:** `2026/09/08/038`  
**Audited source tree:** `13f7aaecad1326f325bcc9b0b96b19b1970e1eb3`

## Final claim assessed

Connectedness of H(PSL(2,7),(2A,3A,7A,7A)): one braid orbit of 48384 tuples / 288 reduced classes

## Correctness — PASS

A fresh construction of PSL(2,7) in its degree-8 projective-line permutation model gives 168 elements and the expected class sizes. Direct product-one enumeration gives 4032 tuples for each of the 12 class-position patterns, 48384 total. A fresh braid-generator BFS on these tuples is one orbit of size 48384. One tuple generates the whole group, and Hurwitz moves preserve the generated subgroup, so generation is automatic throughout that orbit. Because the group is centerless, simultaneous conjugation acts freely on generating tuples, giving 48384 divided by 168 = 288 reduced classes, again one component.

## Originality — PASS

General Hurwitz-space sources describe braid-orbit/component machinery and asymptotic component counts, but the inspected literature does not tabulate this four-point PSL(2,7) Nielsen class or imply that its 48384 ordered tuples form one orbit. LMFDB supplies group structure, not this braid dynamics. Resultary searches found this exact component census as the matching record and different Hurwitz classes as nearby work.

The comparison explicitly checked equivalent formulations, broader coverage, exact database/table matches, and whether prior results logically imply the claim. An unsuccessful search was not treated as proof of novelty.

## Scientific value — PASS

Connectedness is the basic global invariant of a Hurwitz space, and this is a natural small simple-group Nielsen class built from the classical 2,3,7 structure. The exact orbit size, reduced degree, and explicit braid witness are reusable data for inverse-Galois and Hurwitz-space computations. The non-invariance of the chosen lift sign also records a useful boundary on a common component-separation heuristic.

## Source inspections

- **Séguin — Counting Components of Hurwitz Spaces** — Full-text PDF: abstract, introduction, component-count setup, braid/component notation, and lifting-invariant framework. Develops general/asymptotic component theory; it does not provide the specific PSL(2,7) four-point orbit census. https://arxiv.org/abs/2409.18246
- **LMFDB abstract group 168.42 — PSL(2,7)** — Group order/class/action data used as an external structural cross-check. A group database entry, not a Nielsen-class braid-orbit database; it does not imply connectedness. https://www.lmfdb.org/Groups/Abstract/168.42
- **Resultary semantic search for the PSL(2,7) Nielsen class** — Top ranked result set and nearby Hurwitz records. This exact 2A,3A,7A,7A component census is the direct match; nearby records concern different class data and groups. https://github.com/Resultary/2026/tree/main/2026/9/8/SCOPE038

## Residual risks

- The proof is a finite computational orbit enumeration rather than a conceptual classification theorem.
- The lift-sign statement concerns the fixed section used in the record; it is not a claim about every possible Schur multiplier invariant.
- The originality search cannot exclude unindexed computational notes.

## Disposition

**PASS.** Correctness, originality, and scientific value each pass for the final claim stated above.
