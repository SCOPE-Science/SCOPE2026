---
audit_date: 2026-09-30
status: passed
---

# Scientific audit

## Final claim

For the five displayed three-dimensional canonical parallelohedron representatives, the exact real illumination numbers are respectively 8, 6, 6, 5, and 4.

## Correctness — PASS

The five polytopes were reconstructed from their generators/vertices. Their vertex/facet counts were independently recovered as (8,6), (12,8), (14,12), (18,12), and (24,14). Every listed illuminating direction set was checked against all vertex normal cones. An independent exact rational convex-hull test rebuilt each pairwise conflict graph and found maximum clique sizes 8, 6, 6, 5, and 4, matching the upper bounds. The inspected package verifier additionally enumerates every realizable strict facet-sign cell and solves the exact set-cover problem over all real directions.

**Evidence.** artifacts/verify_illumination.py blob a7c9771c584063bd9052cfe94f9958c160d9a0b3

**Residual risk.** The statement is correctly limited to the displayed representatives and affine images, not all realizations of the combinatorial types.

## Originality — PASS

The illumination literature establishes general conjectural bounds, the cube equality case, and several class-wide upper bounds, but the searches located no source tabulating these five representative-specific exact values. The result is not implied by the standard non-parallelotope bound, which only gives at most seven in dimension three and does not yield 6, 5, or 4.

- Equivalent formulations: Checked illumination/positive-homothetic-covering equivalence.
- Broader coverage: General illumination surveys and cube-local results supply upper-bound context, not these exact optima.
- Exact database or table: No exact table for the five representatives was found in the searched primary/survey literature or published corpus.
- Claim versus prior implication: Known general bounds do not determine the four non-cube values.
- Sources inspected: https://arxiv.org/abs/1602.06040; https://arxiv.org/abs/1710.05070; https://doi.org/10.1016/j.disc.2026.115025
- Residual risk: The literature search cannot exclude an obscure polytope-specific computation under different terminology.

## Value — PASS

The five representatives form the natural three-dimensional translative-tiling family, so a complete exact illumination table is mathematically motivated. The all-real-direction lower certificates make the finite computation substantive rather than a pool-dependent heuristic.

**Context.** Bezdek–Khan survey of illumination; classical Fedorov parallelohedra context

**Residual risk.** The theorem is representative-specific and should not be generalized to all geometric realizations.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
