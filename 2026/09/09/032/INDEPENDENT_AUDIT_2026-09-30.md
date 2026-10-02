# Scientific audit — 2026-09-30

## Final claim

The complete joint distribution of fixed points, excedances and descents on 123-avoiding permutations is tabulated for n<=10, together with the two bivariate projections, descent rows through n=10, and a finite 123-versus-132 divergence table.

## Correctness — PASS

An independent backtracking enumerator for 123- and 132-avoiding permutations regenerated the Catalan totals through n=10, the 39 n=10 trivariate cells, the stated selected n=10 entries, the n=10 descent row {4:42,5:1770,6:7515,7:6455,8:1013,9:1}, and exactly 572 divergent 123-versus-132 trivariate cells with the stated per-n counts. These checks do not depend on the committed enumeration engine.

## Originality — PASS

Elizalde treats fixed points and excedances for pattern avoidance and gives partial results for the single pattern 123; Barnabei, Bonetti and Silimbani determine the descent marginal on 123-avoiders. The searches did not locate the full joint (fp,exc,des) distribution or either descent-refined bivariate joint in those sources or Resultary. The record does not claim novelty for the Catalan or descent marginals themselves.

The originality comparison explicitly checked equivalent formulations, broader coverage, exact databases/tables, and implication from prior results. See `INDEPENDENT_AUDIT_2026-09-30.json` for the structured searches, source inspections, checked sources, and residual risks.

## Scientific value — PASS

The three statistics are standard permutation statistics on a canonical Catalan class, and their joint law is a natural refinement whose general generating function is not supplied by the cited marginal results. The finite table through n=10 is a useful exact benchmark and exposes the earliest and full bounded separation from the 132 class.

## Disposition

PASSED. This assessment records the mathematical status of the claim. It is not an external attestation or formal-proof certificate.
