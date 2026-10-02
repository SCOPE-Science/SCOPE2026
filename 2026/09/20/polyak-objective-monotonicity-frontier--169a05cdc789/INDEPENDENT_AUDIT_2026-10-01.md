# Independent mathematical audit — Sharp one-step objective frontier for scaled Polyak steps on SPD quadratics

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS** — Direct expansion reduces the one-step objective ratio to a spectral-moment factor. Reweighting by the first spectral moment turns that factor into a ratio of the first two moments of an interval-valued random variable; the endpoint quadratic inequality and scalar maximization give the sharp Kantorovich value. The two-eigenvalue construction attains equality, so the safety frontiers and minimax scaling follow algebraically. The verifier checks the equality family and random SPD instances as corroboration.

## Originality

**PASS** — The closest full quadratic analysis inspected gives sharp Euclidean-distance contraction for a family containing Polyak steps, not the all-state objective-gap envelope, exact objective-monotonicity thresholds, or minimax scaling derived here. Other recent work addresses global rates or different negative phenomena.

### Equivalent formulations

Searches/sources: Huang–Qi arXiv:2407.04914; scaled Polyak objective monotonicity SPD quadratics.

Evidence: Huang–Qi controls Euclidean or weighted distance. The audited theorem controls objective gap and allows objective increase despite distance decrease.

The metrics and sharp factors are different.

### Broader coverage

Searches/sources: recent tight PolyakGD rate analyses; surrogate-function Polyak literature; exact-line-search worst-case factor.

Evidence: No inspected theorem states the full one-step objective envelope for arbitrary scaling and condition number.

No broader inspected theorem dominates the objective frontier.

### Exact database or table

Searches/sources: Resultary semantic search for scaled Polyak objective monotonicity; search for the exact classical and doubled thresholds.

Evidence: The exact match was the audited record; nearby findings concern different algorithms.

No earlier exact theorem record was found.

### Claim versus prior implication

Searches/sources: Huang–Qi distance contraction versus objective monotonicity; classical Polyak parameters versus one-step objective envelope.

Evidence: Distance contraction does not imply objective decrease for anisotropic quadratics. Classical parameter formulas do not optimize the needed spectral moment ratio over all states.

The sharp frontier requires the additional moment extremum.

### Source inspections

- **Analytic analysis of the worst-case complexity of the gradient method with exact line search and the Polyak stepsize** — RELATED_NOT_COVERING.
  Identifier: https://arxiv.org/abs/2407.04914
  Material read: complete arXiv preprint
  Evidence: It gives distance/weighted-norm contraction and asymptotic behavior, not the audited objective frontier.
- **Complexity Guarantees for Polyak Steps with Momentum** — BACKGROUND_NOT_COVERING.
  Identifier: https://proceedings.mlr.press/v125/barre20a.html
  Material read: complete proceedings article
  Evidence: It treats complexity and momentum rather than this exact one-step SPD objective envelope.

Residual originality risks:
- Older target-value/subgradient literature may contain an equivalent two-moment inequality under different terminology.

## Scientific value

**PASS** — The theorem gives exact safety frontiers for classical adaptive scalings, separates distance progress from objective monotonicity, and identifies the unique condition-number calibration matching the sharp exact-line-search factor. This is a natural structural classification.

## Final assessment

The final claim survives unchanged on correctness, originality and scientific value. RESULT.md and SLOGAN.txt are unchanged.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
