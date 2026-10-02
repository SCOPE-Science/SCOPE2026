# Independent mathematical audit — Cumulant effective-trial hierarchy for Poisson-binomial laws

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS** — Variance-weighting converts the third cumulant to a weighted mean and gives the third-moment effective count. Weighted variance proves the comparison with the fourth-cumulant participation count, and Cauchy–Schwarz bounds that count by the number of active Bernoulli variables with the stated equality cases. Convex packing of Bernoulli variances gives the sharp fourth-cumulant endpoint, and the Lyapunov identity is termwise. The exact-rational verifier checks 66,429 grid vectors as corroboration.

## Originality

**PASS** — Peköz et al. already define the third-moment-matched real binomial trial count that equals the present third-cumulant count, but the inspected sources do not give the fourth-cumulant participation count, the chain between the two counts and active trial number, the equality classification, or the sharp fixed-variance envelopes.

### Equivalent formulations

Searches/sources: Peköz et al. arXiv:0906.2855; Poisson-binomial skewness kurtosis effective trial count.

Evidence: Peköz et al. provide the real third-moment-matched trial count. No inspected source states the fourth-cumulant comparison hierarchy.

The prior parameter is one endpoint of the hierarchy, not an equivalent theorem.

### Broader coverage

Searches/sources: Tang–Tang 2023 survey; Hoeffding Bernoulli extremal theory; Shuldiner–Oldford Bernoulli moments.

Evidence: These sources provide broad distributional and moment background. None inspected contains the joint sharp hierarchy and equality structure.

General moment formulas are ingredients, not dominating coverage.

### Exact database or table

Searches/sources: Resultary semantic search for Poisson-binomial cumulant effective trial hierarchy; published-record search for N3/N4 equality cases.

Evidence: The exact match was the audited record; nearby records concern different Poisson-binomial questions.

No earlier exact theorem record was located.

### Claim versus prior implication

Searches/sources: Peköz moment matching versus fourth cumulant participation; Hoeffding homogenization versus fixed-variance envelopes.

Evidence: The prior matched count does not determine the fourth-cumulant count. Classical mean-fixed extremality does not mechanically give the stated fixed-variance interval.

Additional weighted-variance and convex-packing arguments are essential.

### Source inspections

- **A Three-Parameter Binomial Approximation** — PARTIAL_PRECURSOR.
  Identifier: https://arxiv.org/abs/0906.2855
  Material read: full preprint including parameter formulas
  Evidence: The matched trial count equals the present third-cumulant count, but no fourth-cumulant hierarchy appears.
- **The Poisson Binomial Distribution—Old & New** — BACKGROUND_NOT_COVERING.
  Identifier: https://doi.org/10.1214/22-STS852
  Material read: full author-accessible text
  Evidence: No matching hierarchy or equality classification was found.
- **Bernoulli Sums: The only random variables that count** — BACKGROUND_NOT_COVERING.
  Identifier: https://arxiv.org/abs/2110.02363
  Material read: full preprint
  Evidence: General moment formulas do not state the audited hierarchy.

Residual originality risks:
- Older moment-inequality literature may contain an equivalent Cauchy–Schwarz relation under different terminology.

## Scientific value

**PASS** — The theorem ties a pre-existing third-moment effective trial count to a fourth-cumulant participation count and the active trial number, with exact equality cases and sharp low-moment envelopes. This is a natural reusable structural diagnostic for Poisson-binomial laws.

## Final assessment

The final claim survives unchanged on correctness, originality and scientific value. RESULT.md and SLOGAN.txt are unchanged.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
