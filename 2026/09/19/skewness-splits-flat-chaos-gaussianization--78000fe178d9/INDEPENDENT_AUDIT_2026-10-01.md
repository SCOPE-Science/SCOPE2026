# Independent audit — A skewness–kurtosis phase diagram for flat signed Gaussian-chaos maxima

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **repaired**.

## Correctness

**PASS** — For sign imbalance \(\delta_R\), the exact one-coordinate cumulant generating function expands as \(K_\delta(t)=t^2/2+\sqrt2\,\delta t^3/3+t^4/2+O(t^5)\). Independent series inversion gives \(I_\delta(a)=a^2/2-\sqrt2\,\delta a^3/3+(\delta^2-1/2)a^4+O(a^5)\). On \(x\asymp\sqrt{\log p}\), exponential tilting yields the stated relative-tail exponent, whose substitution gives \(\Theta_p=(4/3)\delta_R L^{3/2}/\sqrt R+(2-4\delta_R^2)L^2/R\). Independence converts this to the shifted-Gumbel law and the explicit Kolmogorov profile. The \(3/4\)-positive versus balanced indefinite example at \(R\asymp L^{5/2}\) then has the claimed opposite limits.

## Originality

**PASS** — After repair, originality passes for the general sign-imbalance interpolation, its two-term \(\Theta_p\) phase coordinate, crossover scale, and the all-indefinite same-effective-rank separation. The positive-versus-balanced benchmark, its \((\log p)^3\)/\((\log p)^2\) thresholds, and the corresponding critical Gumbel gaps are earlier published results and are treated only as prior input.

### Equivalent formulations

The repaired final claim is strictly beyond the earlier endpoint benchmark.

Evidence: The 18 September record gives only the two endpoint sign patterns: all-positive and exactly balanced. The present repaired theorem varies the sign imbalance \(\delta_R\) and produces the mixed cubic/quartic correction including the \(-4\delta_R^2L^2/R\) term.

### Broader coverage

No inspected earlier theorem dominates the repaired \(\delta_R\)-dependent phase diagram.

Evidence: Cai–Hu give the general sufficient \(r_{4,\min}/(\log p)^6\to\infty\) condition and call the displayed phase curve schematic. The 18 September result supplies sharp positive and balanced endpoints but no partially imbalanced interpolation.

### Exact database or table

The archive chronology supports the repaired novelty boundary.

Evidence: No earlier archive record before 2026-09-19T10:16:24Z was found with the \(\delta_R\)-dependent two-term phase coordinate or the two-indefinite-spectrum separation.

### Claim versus prior implication

The repaired claim is not a corollary of the endpoint prior.

Evidence: The endpoint specializations reproduce the earlier positive/balanced results and are therefore removed from the contribution. For \(0<|\delta_R|<1\) or \(\delta_R\) varying with \(p\), the earlier endpoint theorem does not imply the mixed correction or crossover; the exact cgf calculation is required.

### Source inspections

- **Sharp sign-sensitive Gaussianization thresholds for equal-spectrum second-chaos maxima** — COVERS_ENDPOINTS.
  Identifier: published record SCOPE-20260918-948f406a92ce
  Material read: complete result and proof.
  Evidence: It already proves the positive and exactly balanced sharp thresholds, critical translations, Kolmogorov gaps, and effective-rank nonuniqueness.
- **Approximation Theorems for High-Dimensional Canonical U-Statistics: Gaussian Chaos and Phase Transition** — BACKGROUND_NOT_COVERING.
  Identifier: arXiv:2609.20529v2
  Material read: pages 1–12 of 32, including the effective-rank definition and Theorem 3.1 statement.
  Evidence: The inspected theorem gives a general sufficient bound and explicitly schematic phase curve, not the flat partial-imbalance sharp interpolation.

### Residual risks

- Only pages 1–12 of the 32-page Cai–Hu preprint were inspected. Older general Cramér-series theory may imply parts of the analytic expansion after specialization, but no prior effective-rank/sign-imbalance phase statement was found.

## Scientific value

**PASS** — The repaired theorem identifies the missing signed third-moment coordinate between two already-known endpoint regimes and gives a quantitative crossover plus an all-indefinite separation. That is a motivated structural refinement of a live high-dimensional phase-transition problem.

## Final assessment

The original framing contained covered endpoint material. The corrected research files state only the surviving sign-imbalance theorem; correctness, originality, and value were reassessed on that repaired final claim.

This assessment is mathematical review evidence, not formal proof-assistant verification or a guarantee against undiscovered prior art.
