# Independent audit — A boundary-integrability obstruction for singularity-weighted PINN residuals

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS** — For a fixed smooth hard trial with a simple boundary zero, \(\widehat u(y,d)=a(y)d+O(d^2)\) with \(a(y)>0\), while \(\Delta\widehat u=O(1)\). Hence the singular source dominates and \(R\sim-a(y)^{-\alpha}d^{-\alpha}\). Multiplying \(R^2\) by \(1+\beta\widehat u^{-p}\) gives \(d^{-(2\alpha+p)}\), and a codimension-one collar is integrable exactly when \(2\alpha+p<1\). The one-dimensional grid laws are the standard harmonic-sum asymptotics, and differentiating \(d^{2-\alpha}\) verifies the proposed leading boundary correction.

## Originality

**PASS** — Best-of-knowledge originality survives. General warnings about least-squares residuals with singular data and hard PINN boundary factors are prior art, but the exact source-specific thresholds \(\alpha=1/2\) and \(\alpha=1/3\), fixed-trial resolution laws, and fractional boundary-correction mechanism were not found in the searched literature or published archive.

### Equivalent formulations

No equivalent source-specific theorem was located.

Evidence: The archive search returned the audited record as the only direct hit. The motivating paper abstract confirms hard Dirichlet enforcement, Softplus positivity, and a singularity-aware residual weighting, but does not state the boundary-integrability thresholds.

### Broader coverage

These sources supply broad context and ingredients, not the precise singular-equation/weight exponent classification.

Evidence: Führer–Heuer–Karkulik treat the general issue that standard minimum-residual methods usually exclude non-square-integrable singular data. Sukumar–Srivastava establish distance-function hard boundary trial constructions.

### Exact database or table

Unsuccessful search is not taken as proof; the positive originality conclusion also rests on the mismatch between the inspected prior statements and the specific theorem.

Evidence: No independent record or primary-source snippet exposing the \(1/3\) threshold or the stated grid-divergence constants was found.

### Claim versus prior implication

The final claim is not a direct corollary of the inspected prior results.

Evidence: The current theorem uses the source's hard-boundary/positivity/weighted-residual setup but derives a boundary asymptotic not stated in the accessible source abstract. General singular-data minimum-residual theory does not mechanically imply the exact \(2\alpha+p<1\) classification for this architecture without the trial's boundary vanishing analysis.

### Source inspections

- **Deep Learning for Singular PDEs: A Weighted Neural Network Approach** — PRIMARY_CONTEXT_ACCESS_RISK.
  Identifier: arXiv:2609.19335
  Material read: abstract and accessible metadata; full text unavailable after lawful retrieval attempts.
  Evidence: The abstract confirms hard boundary constraints, Softplus positivity, singularity-aware residual weighting, and comparison with a standard residual, but does not expose the exact weight formula or the integrability analysis.
- **MINRES for Second-Order PDEs with Singular Data** — BROADER_CONTEXT_NOT_COVERING.
  Identifier: doi:10.1137/21M1457023 / arXiv:2111.00103
  Material read: abstract.
  Evidence: It states that usual minimum-residual methods exclude non-square-integrable loads and develops regularized alternatives, but not the current PINN boundary-exponent theorem.
- **Exact imposition of boundary conditions with distance functions in physics-informed deep neural networks** — INGREDIENT_NOT_COVERING.
  Identifier: arXiv:2104.08426 / doi:10.1016/j.cma.2021.114333
  Material read: abstract.
  Evidence: It establishes distance-factor hard constraints, not singular-source residual integrability thresholds.

### Residual risks

- The full text of the very recent motivating preprint could not be obtained; the exact public weight formula is therefore supported by the audited source package rather than independently confirmed from the paper text. A hidden source-side analysis of the same threshold remains a residual risk.

## Scientific value

**PASS** — The result identifies a precise failure mode in the population objective exactly where the proposed weighting is intended to focus, quantifies its resolution growth, and points to the missing boundary regularity. This is a motivated numerical-analysis boundary rather than a generic warning that singular data can be difficult.

## Final assessment

The claim survives unchanged on correctness, originality, and scientific value.

This assessment is mathematical review evidence, not formal proof-assistant verification or a guarantee against undiscovered prior art.
