# Independent mathematical audit — 2026-10-01

## Final claim assessed

Sharp fraction-of-optimal decrease for the SPD Cauchy trust-region point

## Correctness — PASS

PASS. The two-radius-regime proof is correct. When the Cauchy point is untruncated, the unconstrained Newton decrease gives the fixed-gradient factor. In the boundary regime the domination inequality is affine in normalized radius, so endpoint checks suffice; weighted Cauchy--Schwarz and AM--GM prove the nontrivial endpoint. Kantorovich gives the sharp condition-number envelope, and the two-eigenspace family attains it. Fresh calculations reproduced the equality factor for multiple condition numbers.

## Originality — PASS

PASS to the best of current knowledge. Classical trust-region sources distinguish the Cauchy point, exact model minimizer, fraction-of-Cauchy decrease, and the stronger fraction-of-optimal condition. Conn--Scheinberg--Vicente explicitly say fraction-of-optimal decrease is stronger than their Cauchy/eigenstep condition but do not provide this SPD conversion. Conn--Gould--Toint likewise present the Cauchy point and model minimizer as extremes without the sharp radius-uniform ratio. Searches for the fixed-gradient and condition-number factors found no earlier theorem.

### equivalent_formulations

Searches: fraction of optimal decrease Cauchy point trust region SPD Kantorovich; fraction-of-Cauchy versus fraction-of-optimal trust region; published-record query for sharp Cauchy-to-optimal ratio

Evidence: Standard sources define both notions but do not state the sharp SPD conversion; no earlier exact record was found.

Reasoning: The radius-uniform trust-region claim is stronger than the classical unconstrained steepest-descent/Newton ratio.

### broader_coverage

Searches: Conn--Gould--Toint Trust Region Methods Chapter 7; Conn--Scheinberg--Vicente DOI 10.1137/060673424; Nocedal--Wright trust-region chapter

Evidence: The standard literature gives Cauchy decrease estimates and exact-minimizer context, and explicitly distinguishes stronger fraction-of-optimal decrease.

Reasoning: No inspected theorem dominates the fixed-gradient \(1/K\) guarantee for every radius.

### exact_database_or_table

Searches: Published-record semantic search for the sharp Cauchy-to-optimal ratio

Evidence: No earlier exact record was found.

Reasoning: This is a quantified optimization inequality, not a table invariant.

### claim_vs_prior_implication

Searches: SIAM Trust Region Methods Chapter 7; Conn--Scheinberg--Vicente fraction-of-optimal discussion

Evidence: The prior results do not convert fraction-of-Cauchy decrease sharply to exact trust-region optimal decrease under SPD conditioning.

Reasoning: The affine-radius proof supplies the missing implication.

## Scientific value — PASS

PASS. The result quantitatively connects two standard sufficient-decrease notions with a sharp radius-independent constant in the uniformly SPD regime, including equality classification and a fixed-metric transfer.

## Source inspections

- **Trust Region Methods, Chapter 7: The Trust-Region Subproblem** — https://doi.org/10.1137/1.9780898719857.ch7. Material read: Accessible chapter text around the Cauchy point and exact model minimizer. Assessment: STANDARD_BASELINE_NOT_EXACT_COVERAGE. Evidence: The chapter presents the Cauchy point and exact minimizer as opposite extremes without the audited sharp SPD ratio.
- **Global Convergence of General Derivative-Free Trust-Region Algorithms to First- and Second-Order Critical Points** — https://doi.org/10.1137/060673424. Material read: Accessible full-text excerpt containing the fraction-of-Cauchy assumption and statement that fraction-of-optimal decrease is stronger. Assessment: DIRECT_CONTEXT_NOT_EXACT_COVERAGE. Evidence: It distinguishes the notions but gives no sharp SPD conversion factor.

## Limitations and residual risks

The theorem concerns exact-arithmetic real SPD quadratic models and predicted model reduction. It does not assert actual nonlinear-objective reduction, finite-precision stability, or a positive indefinite-model analogue.

- Broad classical trust-region literature leaves residual historical-equivalence risk.
- The result does not extend with a positive condition-independent factor to indefinite quadratic models.

## Disposition

**passed**
