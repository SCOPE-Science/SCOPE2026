# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-e6b134ac7b73`

## Correctness — PASS

Applying the uniform shifted-Gamma expansion at \(z=N/m\to\infty\) and summing over the \(m\) modal coordinates gives the stated remainder \(O_K(m^{K+2}/N^{K+1})\). The \(k=1\) Bernoulli term separates exactly into the Gaussian Mahalanobis exponent plus \(-(m^2-1)/(12N)\), giving the square-root critical dimension. Retaining successive terms yields the correction thresholds. For the unit-cell correction, the linear Gaussian exponent vanishes in probability because its variance is \(O(m^3/N^2)\), while the quadratic form converges to \((c/24)(1+Z^2)\); boundedness of the full exponent in the critical regime justifies expectation convergence and yields the displayed profile.

### Correctness sources

- assigned RESULT.md
- Elezović arXiv:2609.20229
- Ouimet 2021 precise multinomial local limit theorem
- Katsevich 2025 high-dimensional BvM

### Correctness risks

- Only the equiprobable modal local problem with \(m=o(N)\) is covered.

## Originality — PASS

Fresh Resultary and web searches found no published theorem with the same growing-category modal expansion, correction hierarchy, or critical Gaussian-cell profile. Elezović treats fixed category count, Ouimet's precise local theorem has fixed-dimension constants and discusses continuity corrections, and Katsevich's \(N\gg d^2\) condition concerns posterior total variation rather than modal lattice-mass relative error.

### equivalent_formulations

Searches:
- Resultary query for growing-category multinomial modal Gaussian critical dimension
- web searches for the factor \(e^{-c/12}\) and unit-cell critical profile

Evidence:
- No external or published-SCOPE result matching these formulas was located.

Reasoning:
The aliases 'number of categories', dimension \(d=m-1\), modal mass and continuity-corrected local Gaussian probability were all compared.

### broader_coverage

Searches:
- Elezović 2026 fixed-category expansion
- Ouimet 2021 precise multinomial local limit theorem
- Katsevich 2025 BvM dimension dependence

Evidence:
- Each is broader in a different methodological sense but none gives uniform growing-\(m\) modal relative error with the displayed sharp limits.

Reasoning:
Fixed-dimensional local expansions do not mechanically imply a uniform simultaneous-dimension threshold without tracking dimension growth in every remainder.

### exact_database_or_table

Searches:
- central multinomial and lattice local-limit searches

Evidence:
- No exact database/table of the arbitrary lattice-phase correction hierarchy was found.

Reasoning:
The theorem is asymptotic and phase-uniform, not extraction of a known table.

### claim_vs_prior_implication

Searches:
- claim-versus-Ouimet and Katsevich implication comparison

Evidence:
- Ouimet allows dimension-dependent constants; Katsevich addresses posterior normality, not lattice-point mass.

Reasoning:
Neither prior theorem implies the audited sharp critical factor or continuity-correction profile.

### source_inspections
- **Multinomial probabilities near the mode: integer modes and the complete local expansion** — https://arxiv.org/abs/2609.20229. Trigger: Closest exact modal expansion. Material read: Public abstract/metadata; direct full-text retrieval failed in this run. Method: Primary-source scope comparison. Assessment: Fixed probability vector/category count; does not cover growing dimension. Evidence: The abstract describes a complete local expansion for fixed multinomial probabilities.
- **A precise local limit theorem for the multinomial distribution and some applications** — https://authors.library.caltech.edu/records/w57x2-z8c52. Trigger: Closest precise local Gaussian comparison and continuity-correction source. Material read: Open accepted-version metadata and abstract. Method: Primary-source scope comparison. Assessment: Precise local theorem with applications and continuity-correction discussion, but no growing-category critical modal profile located. Evidence: The abstract states explicit terms through order \(N^{-1}\) and continuity-correction applications.
- **Improved dimension dependence in the Bernstein–von Mises theorem via a new Laplace approximation bound** — https://doi.org/10.1093/imaiai/iaaf020. Trigger: Independent square-dimension multinomial normality scale. Material read: Published abstract. Method: Scope comparison. Assessment: Different posterior total-variation problem; no local lattice-mass theorem. Evidence: The abstract gives \(N\gg d^2\) for BvM in multinomial data.

### checked_sources

- arXiv:2609.20229
- Ouimet 2021
- Katsevich 2025
- Resultary semantic search
- assigned RESULT.md

### residual_risks

- Classical high-dimensional lattice expansions under different notation remain a residual risk.
- Full text of the newest Elezović source was not retrievable in this run.

## Scientific value — PASS

The square-root dimension threshold is a natural exact boundary for Gaussian modal mass, and the higher-order hierarchy shows how explicit corrections progressively enlarge the valid dimension regime. The continuity-correction profile answers a concrete approximation question rather than reporting a tiny numerical gain.

### Value sources

- fixed-dimension multinomial local-limit literature
- high-dimensional multinomial normality literature
- audited exact expansion

### Value risks

- No global total-variation threshold is claimed.

## Limitations

- Equiprobable cells and \(m=o(N)\) only.
- The theorem is local at modal lattice points.
- Originality is best-of-knowledge with residual classical lattice-expansion risk.

## Disposition

**PASSED**
