# Independent mathematical audit — 2026-10-01

## Final claim assessed

Exact point-mass Walsh square functions and a correction to higher-order exponent sharpness

## Correctness — PASS

PASS. The singleton identity was reconstructed directly from the Walsh difference definition. Writing the singleton indicator as the product of the coordinate factors shows that a distinct-index derivative survives exactly when every negative coordinate lies in the chosen index set, with magnitude \(2^{-k}\). Counting the surviving index sets at Hamming radius \(r\) gives the exact pointwise formula and, after shell counting, the exact \(L_p\) norm identity. Maximizing the exponent \(r+(k-r)p/2\) gives the three fixed-\(p\) regimes. Keeping \(p=2+\lambda/\log n\) in the same finite sum gives the displayed critical crossover. Most importantly, the primary source was read at Section 6.3: its Lemma 6.3 evaluates the same point as \((-2)^k\), whereas the direct calculation gives \((-1)^k2^{-k}\). The corrected \(r=k\) shell still yields growth of order \(n^{k/p}\), so the source exponent-sharpness conclusion survives although its normalization does not.

## Originality — PASS

PASS to the best of current knowledge. The exact Resultary search for the singleton Walsh-square-function profile and critical crossover returned this record as the only matching published finding. The primary Jiao--Luo--Zanin--Zhou paper was read in full at the relevant Section 6.3 and contains the erroneous normalization but not the corrected binomial profile or the \(1/\log n\) crossover. Broader searches for higher-order Walsh/Riesz sharpness located the source theorem and general hypercube literature but no earlier statement of this exact correction. The formula is elementary enough that unindexed prior folklore remains a residual risk, but no inspected source implies the complete exact profile or critical-window limit.

### equivalent_formulations

Searches: Walsh hypercube point mass distinct-index square function exact norm critical window; Lemma 6.3 Sharp Fractional Riesz Estimates on the Hypercube singleton

Evidence: The exact published-record search returned the audited finding itself; the primary source Section 6.3 was read and contains only the incorrect point evaluation and its lower-bound consequence.

Reasoning: The shell-count formula, the fixed-exponent asymptotics, and the critical-window limit are equivalent ways of packaging the same singleton profile; none appears in the inspected prior source.

### broader_coverage

Searches: Sharp Fractional Riesz Estimates on the Hypercube higher order exponent optimality; higher order Walsh square function singleton

Evidence: The source proves the higher-order estimate and claims exponent optimality, but its witness normalization is wrong and it does not state the exact repaired profile.

Reasoning: The source theorem supplies the upper estimate and intended sharp exponent, not the corrected witness computation or critical crossover.

### exact_database_or_table

Searches: Resultary semantic search for exact singleton Walsh square function

Evidence: No numerical database is relevant; theorem-level record search found no earlier exact profile.

Reasoning: This is an analytic identity rather than a tabulated invariant.

### claim_vs_prior_implication

Searches: arXiv:2609.09040 Section 6.3 Lemma 6.3; published Resultary Walsh square function correction

Evidence: Pages 21--22 of the primary paper were inspected; its stated point value differs from the direct difference calculation by a large normalization factor.

Reasoning: The corrected formula is not mechanically implied by the erroneous prior computation, although the intended exponent follows after a different shell argument.

## Scientific value — PASS

PASS. This is not merely a recomputation of a known constant: it corrects a numerical error in the published sharpness witness while proving that the intended exponent remains valid, and it replaces the flawed point estimate by an exact all-shell formula. The resulting phase transition at \(p=2\) and the explicit \(1/\log n\) crossover are natural quantitative information about the standard sharpness example.

## Source inspections

- **Sharp Fractional Riesz Estimates on the Hypercube** — https://arxiv.org/abs/2609.09040. Material read: Complete relevant primary full text, especially pages 21--22 containing Section 6.3, Lemma 6.3, and Lemma 6.4. Assessment: PRIMARY_SOURCE_WITH_CONFIRMED_NORMALIZATION_ERROR. Evidence: Lemma 6.3 explicitly computes the singleton derivative at the \(k\)-negative point as \((-2)^k\); the independent Walsh-difference calculation gives \((-1)^k2^{-k}\).
- **Published mathematical record search for the exact singleton profile** — Resultary semantic search. Material read: Ranked semantic results for exact singleton, higher-order Walsh square functions, and critical crossover. Assessment: NO_EARLIER_EXACT_COVERAGE_FOUND. Evidence: The audited record was the exact top match; no earlier result in the inspected set stated the same profile or crossover.

## Limitations and residual risks

The exact profile concerns the singleton sharpness example for the distinct-index square function. It does not by itself determine optimal constants in the full higher-order Riesz inequality.

- The exact singleton identity is elementary, so older unindexed Walsh-analysis folklore could contain it even though no such source was located.
- The audit does not re-prove the source paper's full higher-order upper theorem; it verifies the repaired sharpness witness and the resulting exponent obstruction.

## Disposition

**passed**
