# Independent mathematical audit — 2026-10-01

## Final claim assessed

Harmonic equilibrium bias and a one-gradient covariance obstruction for randomized ULMC

## Correctness — PASS

PASS. The final claim was reconstructed from the random affine harmonic recurrence rather than inferred from the saved success log. Solving the averaged discrete Lyapunov expansion gives the displayed uniform-time coefficients. In the arbitrary-time one-gradient family, zero first-order cross covariance forces the first random-time moment to be one half and zero second-order cross covariance then forces the second moment to be one third. Substitution leaves the order-two position coefficient proportional to one minus twice the predictor-noise multiplier and the velocity coefficient proportional to one minus that multiplier, so no single multiplier cancels both. The stored symbolic derivation and an independent exact-kernel quadrature calculation agree with these coefficients. The Wasserstein lower bound uses only the elementary second-moment lower bound under arbitrary couplings.

## Originality — PASS

PASS to the best of current knowledge. The motivating 2026 ULMC paper was inspected in full-text sections covering the unified predictor-corrector construction, the low-cost randomized methods, long-time Wasserstein analysis and numerical comparisons; it does not state the stationary harmonic covariance classification or the arbitrary-time one-gradient impossibility theorem. A published-record semantic search returned this record as the exact match. The closest same-day published covariance result concerns the LC-UBU/UBU midpoint-noise family and does not imply the LC-REI/ALUM/RMM coefficients or the random-time one-gradient obstruction. General randomized-midpoint and invariant-measure literature supplies methodology but not the source-specific formulas.

### equivalent_formulations

Searches: Resultary: stationary harmonic covariance LC-REI ALUM RMM randomized underdamped Langevin one-gradient obstruction; arXiv:2609.20713 full-text search for stationary/covariance

Evidence: The exact semantic hit is the audited record; no earlier equivalent one-gradient moment obstruction was returned. The motivating source defines the same method family but its inspected analysis does not state this stationary covariance theorem.

Reasoning: The arbitrary-time moment conditions are the natural equivalent order-condition formulation; no inspected source supplies them.

### broader_coverage

Searches: Resultary: fractional midpoint noise UBU configurational bias; He Balasubramanian Erdogdu randomized midpoint stationary bias; Langevin invariant-measure order conditions

Evidence: The closest published SCOPE result concerns a different UBU midpoint-noise interpolation. Older work establishes stationary-bias methodology for randomized midpoint/Langevin schemes.

Reasoning: Those broader methods do not mechanically determine the source-specific LC-REI/ALUM/RMM coefficients or the simultaneous one-gradient no-go conditions.

### exact_database_or_table

Searches: Resultary exact semantic search for the LC-REI/ALUM/RMM covariance coefficients

Evidence: No relevant numerical database/table exists; the exact theorem search found no earlier matching record.

Reasoning: This is a parameterized analytic order-condition theorem rather than a tabulated invariant.

### claim_vs_prior_implication

Searches: arXiv:2609.20713; Resultary 2026/9/19 fractional-midpoint-noise-ubu-configurational-bias

Evidence: The primary source gives non-asymptotic Wasserstein rates and method definitions, not stationary-covariance expansions. The adjacent UBU result changes a different noise channel and therefore does not imply the randomized predictor obstruction.

Reasoning: A fresh Lyapunov/order-condition calculation is required; the final claim is not a special case of an inspected stronger theorem.

## Scientific value — PASS

PASS. The one-gradient impossibility result is a structural design constraint for a newly introduced low-cost sampler, not just a harmonic benchmark number. It separates transient/pathwise error from invariant-measure bias, explains why tuning the random time and predictor-noise amplitude cannot recover RMM's covariance cancellation, and gives a concrete equilibrium error floor.

## Source inspections

- **A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity: Old and New** — https://arxiv.org/abs/2609.20713. Material read: Full-text sections containing the method definitions, convergence framework and numerical-comparison discussion; targeted full-text searches for stationary covariance and linear stability terminology. Assessment: PRIMARY_SOURCE_NOT_COVERING_FINAL_CLAIM. Evidence: The inspected source supplies the schemes and non-asymptotic Wasserstein analysis but not the stationary covariance expansion or arbitrary-time one-gradient covariance obstruction.
- **Fractional midpoint noise creates configurational superconvergence in UBU-type Langevin sampling** — https://github.com/Resultary/2026/blob/main/2026/9/19/SCOPE-fractional-midpoint-noise-ubu-configurational-bias--516bd7b79285/RESULT.md. Material read: Complete published RESULT.md. Assessment: RELATED_DIFFERENT_METHOD_FAMILY. Evidence: It analyzes LC-UBU/UBU midpoint-noise interpolation, not randomized LC-REI/ALUM/RMM or the arbitrary-time one-gradient obstruction.

## Limitations and residual risks

Restricted to the harmonic target and the stated predictor family; the invariant law is generally non-Gaussian under random intermediate times and no full-distribution or nonlinear-target optimality is claimed.

- The method family is extremely recent, so unindexed contemporaneous follow-up remains possible.
- The theorem is a small-step stationary second-moment result for harmonic targets, not a full invariant-law classification.

## Disposition

**passed**
