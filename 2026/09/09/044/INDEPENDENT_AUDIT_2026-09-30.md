# Independent audit — 2026-09-30

**Record:** `2026/09/09/044`  
**Audited source tree:** `b99f72251ba098d3a417914fa4f1ddefe3fb1b5b`

## Correctness — PASS

A fresh Murnaghan-Nakayama implementation independently rebuilt the S6, S7 and S8 character tables, re-derived all 155 rows, and reproduced the unique global family maximum |s-a|=5 at lambda=(4,3,1), nu=(4,2,2) with (s,a,g,m)=(6,1,7,5). It also confirmed that the (3,2,1) square has g>0 and s>0 for all 11 irreducibles. The character identities s=(g+m)/2 and a=(g-m)/2 are standard, and the package's second recursion checks column orthogonality, transpose symmetry, exact divisibility and the stored table.

## Originality — PASS

The closest primary splitting paper gives broad formulas for hooks, several two-part families and selected shallow constituents, while explicitly treating the splitting problem as sparse and more difficult beyond those regimes. No inspected source supplied the complete nine-square non-hook three-row S6-S8 table, its 155 (s,a,g,m) rows, or the stated family extremum. The exact census is not implied by the cited general unsplit-positivity results.

The comparison explicitly checked equivalent formulations, broader coverage, exact tables/databases, and whether prior results logically imply the final claim.

## Scientific value — PASS

The nine squares form the complete non-hook three-row family for n=6,7,8, so the cutoff is a natural finite classification rather than an arbitrary slice. The split data refine ordinary Kronecker coefficients, identify an extremal symmetric/alternating imbalance, and record a complete symmetric-part containment phenomenon for the S6 staircase. The result is finite, but it is a reusable reference table for a motivated unresolved splitting regime.

## Source inspections

- **Bessenrodt and Bowman — Splitting Kronecker squares, 2-decomposition numbers, Catalan combinatorics, and the Saxl conjecture** — Journal abstract, bibliographic record, and the paper's cited regime comparison against the target families. Provides major splitting formulas and motivation but no complete nine-square n=6..8 non-hook three-row census was identified. https://doi.org/10.5802/alco.294
- **Mészáros and Wolosz — Symmetric and Exterior Squares of Hook Representations** — Scope from title/record and its relation to the target family. Covers hooks, which are explicitly excluded from this record's target set. https://arxiv.org/abs/1909.07489

## Residual risks

- The result is a finite n=6..8 census and gives no general formula for the non-hook three-row family.
- Originality is assessed against the inspected splitting literature; a low-degree table could exist in software/databases without a published theorem.
- The independent reconstruction used the same standard character-theoretic identities as the package, though a separately implemented Murnaghan-Nakayama recursion reproduced all headline facts.

## Disposition

**PASS.** The final claim passes correctness, originality, and scientific value without changing `RESULT.md` or `SLOGAN.txt`.
