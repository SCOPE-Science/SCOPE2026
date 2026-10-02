# Independent mathematical audit — 2026-10-01

## Final claim

Sharp large-noise asymptotics for variance-gamma medians

## Correctness — PASS

PASS. The five regimes were reconstructed from the gamma-normal mixture median equation. The cdf imbalance at zero is of order the inverse square root of the noise parameter, while the derivative with respect to the scaled median has an exact modified-Bessel representation. Small-argument Bessel asymptotics yield the subcritical power law and the first logarithmic threshold. For shapes above one, cancellation of the first normal perturbation moves the problem to a boundary-layer correction; its inverse-moment integrability changes exactly at shape three, producing the second logarithmic threshold. The smooth-regime coefficient follows from the cubic term. The known exact shape-two asymmetric-Laplace median independently reproduces the audited coefficient.

## Originality — PASS

PASS to the best of current knowledge. The complete Gaunt-Ouimet 2026 primary paper was inspected. It proves strict monotonicity and the large-noise limiting median but stops at the limit; its proof does not state rates or the two critical logarithmic crossovers. The 2025 variance-gamma review records standard density behavior and special cases but not the five-regime expansion. Published-record search found the audited September 18 result and later September 19 and 20 follow-ups, not an earlier matching theorem. The older 2001 generalized-Laplace monograph was not inspected in full and remains an explicit residual risk.

### equivalent_formulations

Searches: variance-gamma median large-noise five regimes logarithmic shape one shape three; variance gamma median asymptotic Bessel boundary layer

Evidence: Published-record search returned the audited record and only later follow-up records with the same phase transitions.

Reasoning: Equivalent gamma-normal mixture and Bessel-slope formulations were checked; no earlier exact rate theorem was located.

### broader_coverage

Searches: Gaunt-Ouimet 2026 variance-gamma median full text; variance-gamma distribution review median theory; generalized Laplace median asymptotics

Evidence: Gaunt-Ouimet proves monotonicity and the endpoint limit for all shapes, while the review supplies special-case and density background.

Reasoning: A limit theorem does not mechanically determine the boundary-layer exponents, logarithmic transition constants, or the second critical shape.

### exact_database_or_table

Searches: published mathematical record semantic search for exact five-regime coefficients

Evidence: No earlier exact record was found; September 19 and September 20 records are later follow-ups.

Reasoning: The claim concerns asymptotic formulas rather than a standard table entry.

### claim_vs_prior_implication

Searches: Gaunt-Ouimet Corollary 2.3 and proof; Fischer-Gaunt-Sarantsev review; older generalized-Laplace references

Evidence: The primary 2026 proof establishes only the limiting median and global bounds; it does not expand the median equation to the orders used here.

Reasoning: The audited rates require a separate singular-asymptotic analysis and are not a direct substitution into the prior limit theorem.

## Scientific value — PASS

PASS. A sharp all-shape asymptotic phase diagram for a recently established median limit is a natural quantitative problem. The two distinct critical logarithmic regimes explain how density singularity and inverse-moment integrability control quantile convergence, and the explicit constants make the result reusable.

## Source inspections

- **Robert E. Gaunt and Frédéric Ouimet, Bounds for the median of the generalized hyperbolic and related distributions** — https://arxiv.org/abs/2609.20212. Material read: Complete 26-page preprint, including Corollary 2.3, the normal variance-mean mixture analysis, the proof of the large-noise limit, and all references. Assessment: LIMIT_THEOREM_NOT_RATE_COVERAGE. Evidence: The paper proves the limiting median and monotonicity but gives no five-regime convergence-rate theorem or shape-three logarithmic transition.
- **Adrian Fischer, Robert E. Gaunt and Andrey Sarantsev, The Variance-Gamma Distribution: A Review** — https://doi.org/10.1214/24-STS929. Material read: Published theorem/context material relevant to medians and special cases. Assessment: BACKGROUND_NOT_EXACT_COVERAGE. Evidence: The review records standard median facts and special cases but not the audited large-noise phase diagram.

## Limitations and residual risks

The asymptotics are pointwise for fixed shape and fixed nonzero asymmetry. No uniform transition theory as the shape approaches either critical value is proved, and no extension to general non-variance-gamma generalized hyperbolic medians is claimed. The 2001 generalized-Laplace monograph remains a residual originality risk.

- The 2001 generalized-Laplace monograph was not inspected in full and remains the main originality risk.
- The expansion is not uniform as the shape approaches one or three.

## Disposition

**passed**
