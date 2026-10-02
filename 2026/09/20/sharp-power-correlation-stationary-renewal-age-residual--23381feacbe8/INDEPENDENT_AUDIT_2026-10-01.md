# Independent mathematical audit — Sharp power-correlation range for stationary renewal age and residual life

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS** — At stationarity the containing renewal interval is size-biased and the inspection location is uniform, so the age and residual pair is a uniform split of that interval. The first, second and mixed powered moments follow directly. The resulting correlation depends on the interarrival law only through one positive moment ratio, which lies in the interval from zero to one by Cauchy–Schwarz, with equality at one exactly for deterministic interarrivals. The correlation is strictly decreasing in this ratio. A two-point size-biased interval law realizes every interior ratio and can approach zero, and inverse size-biasing returns a valid positive two-point interarrival law. This proves the endpoint and attainability claims as well as the exponential zero-correlation benchmark.

## Originality

**PASS** — The stationary Schur-constant representation and the ordinary first-power correlation are prior theory, but the inspected sources did not state the all-positive-power exact correlation envelope, endpoint/extremizer classification, two-point attainability result, or high-power collapse.

### Equivalent formulations

Searches/sources: Resultary semantic query: stationary renewal age residual life power correlation beta function exact attainable interval; Gakis–Sivazlian 1994 DOI 10.1080/07362999408809372; Nair–Sankaran 2014 DOI 10.1007/s40300-014-0045-0.

Evidence: The 1994 source is specifically about the ordinary age/residual correlation. The 2014 source develops the Schur-constant equilibrium representation and dependence framework. No published-record hit gave the powered sharp interval.

The prior representation supplies the starting coordinates, but not the optimized powered Pearson-correlation range.

### Broader coverage

Searches/sources: Losidis–Politis–Psarrakos 2021 joint moments; 2025 bivariate dependence paper; Schur-constant dependence literature.

Evidence: The 2021 abstract describes exact joint moments and bounds at fixed time, not a stationary all-power sharp correlation envelope. The 2025 paper studies dependence orders and conditional tails.

No inspected broader dependence theorem supplied the exact universal power-correlation interval.

### Exact database or table

Searches/sources: Resultary exact/semantic search for stationary renewal powered age-residual correlation.

Evidence: The exact audited record was the only matching published finding.

No standard table is relevant; theorem-record search found no earlier exact entry.

### Claim versus prior implication

Searches/sources: Does the Schur-constant radial-uniform representation alone fix the power-correlation range?; Does the first-power correlation theorem imply arbitrary powers?.

Evidence: The representation still leaves a nontrivial moment ratio to optimize over all positive interarrival laws. The first-power formula does not determine the beta-function constants or attainable interval for arbitrary powers.

The sharp moment-ratio optimization and attainment construction are additional arguments, not special cases of a stronger prior theorem.

### Source inspections

- **Modelling lifetimes with bivariate Schur-constant equilibrium distributions from renewal theory** — FOUNDATIONAL_CONTEXT.
  Identifier: https://doi.org/10.1007/s40300-014-0045-0
  Trigger: same stationary age/residual Schur-constant model
  Material read: abstract and public full-text preview describing the equilibrium representation, copula and dependence program
  Method: lawful public material
  Evidence: It establishes the model framework; no whole-document noncoverage claim is made because a complete verified full text was not obtained in this run.
- **The correlation of the backward and forward recurrence times in a renewal process** — FIRST_POWER_PRIOR.
  Identifier: https://doi.org/10.1080/07362999408809372
  Trigger: same Pearson dependence quantity at power one
  Material read: bibliographic and abstract-level material
  Method: lawful public material
  Evidence: It treats ordinary age/residual correlation, which the audited theorem generalizes.
- **Exact Results and Bounds for the Joint Tail and Moments of the Recurrence Times in a Renewal Process** — RELATED_ACCESS_RISK.
  Identifier: https://doi.org/10.1007/s11009-020-09787-w
  Trigger: plausible broader joint-moment source
  Material read: abstract and bibliographic material
  Method: lawful public material
  Evidence: It studies joint tails and moments, but complete text was not inspected and therefore remains a residual overlap risk.

Residual originality risks:
- Older Schur-constant or ell-one-symmetric literature may encode the same envelope under different powered-moment terminology.
- Several plausible older sources were not available in complete verified full text.

## Scientific value

**PASS** — The theorem gives a complete distribution-free identification region for a natural dependence statistic across every positive power, with exact extremizers, attainability, a sign threshold and a high-power limit. This is a motivated complete classification rather than a raw moment computation.

## Final assessment

The final claim survives unchanged on correctness, originality and scientific value. No change to RESULT.md or SLOGAN.txt is proposed.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
