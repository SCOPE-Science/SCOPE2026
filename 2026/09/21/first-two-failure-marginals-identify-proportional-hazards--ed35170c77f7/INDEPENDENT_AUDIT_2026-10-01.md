# Independent mathematical audit — SCOPE-20260921-ed35170c77f7

Final disposition: **PASS**.

## Correctness
**PASS.** For independent proportional-hazards components, the first-failure survival is B^Lambda and inclusion-exclusion for survival of at least n-1 components gives S2=sum_i B^(Lambda-lambda_i)-(n-1)B^Lambda. Reparameterizing by u=S1 eliminates the unknown baseline and produces a finite signed exponential sum with exponent 1 coefficient -(n-1) and all other exponents strictly in (0,1). Uniqueness of finite exponential sums therefore identifies n and the normalized hazard multiset. The converse characterization, Newton reconstruction when n is known, and the separate nonidentification constructions for either marginal alone follow directly.

## Originality
**PASS.** Current Resultary search found no earlier or stronger theorem identifying an unknown component count and all normalized proportional-hazards multipliers from only the first two unlabeled marginal failure laws. The closest retrieved PHR literature concerns stochastic comparison of second-order statistics, while a later general order-marginal identification result uses all rank marginals and different regularity hypotheses. The older Pledger-Proschan chapter could not be inspected theorem by theorem and remains a residual risk, but inaccessible plausible older literature alone is not decisive coverage in the absence of a matching statement.

### Equivalent formulations
The theorem was compared in both reliability/order-statistic and exponential-sum identification formulations.

### Broader coverage
No inspected broader theorem implies the assigned sufficiency result.

### Exact database or table
The search supports, but does not by itself establish, novelty.

### Claim versus prior implication
No inspected prior implication mechanically yields the final claim.

## Value
**PASS.** The theorem isolates a sharp semiparametric sufficiency phenomenon: either marginal alone is completely nonidentifying under an arbitrary common baseline, whereas the pair identifies component count and all relative hazards. The baseline-elimination identity and exact model-class characterization are natural structural results for reliability inference.

## Source inspections
- **Comparisons of order statistics and of spacings from heterogeneous distributions** (Pledger and Proschan (1971), Optimizing Methods in Statistics): secondary descriptions and citations only; the complete chapter was not available for theorem-by-theorem inspection Assessment: INACCESSIBLE_RESIDUAL_RISK. Evidence: Known descriptions concern comparison results, not the assigned inverse-identification statement.
- **Stochastic Comparisons of Second-Order Statistics from Dependent and Heterogenous Modified Proportional Hazard Rate Observations** (https://arxiv.org/abs/2201.01596): primary abstract Assessment: COMPARISON_THEORY_NOT_IDENTIFICATION. Evidence: The paper studies stochastic and hazard-rate ordering of second-order statistics rather than semiparametric recovery.
- **Heterogeneous order-statistic marginals: pointwise recovery, label braiding, and analytic identification** (https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-heterogeneous-order-marginals-analytic-identification--096d7231c1a9): published title/summary returned by current database search Assessment: BROADER_DATA_REQUIREMENT_NOT_COVERING. Evidence: It uses all marginal rank distributions; that does not imply recovery from only ranks one and two in the PHR class.

## Residual risks
- The 1971 Pledger-Proschan chapter was not available for full theorem-level inspection.
- Older masked-reliability or inverse-system literature may use different terminology for the same semiparametric specialization.
- Identification can be numerically ill-conditioned when normalized hazards are close.
