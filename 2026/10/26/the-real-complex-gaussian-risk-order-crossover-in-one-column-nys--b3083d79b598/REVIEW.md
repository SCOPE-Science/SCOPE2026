# Scientific review

## Correctness — PASS
The residual is positive semidefinite rank one, and its trace has the exact rational representation in a beta-distributed angular coordinate. The real and complex gamma shapes, quantile inversions, and moment integrals can be independently reconstructed. The strict convex-order comparison follows from the arcsine-versus-uniform CDF signs, equal means, hinge representation, and convexity of every nondecreasing convex penalty composed with the residual map. The moment and matrix-identity program completed successfully. This does not rely on Monte Carlo to prove an infinite family of inequalities.

## Originality — PASS (best knowledge)
The 2022 Nyström sketch paper supplies the method but not the field-comparison risk laws. Tropp et al. (2017) explicitly consider both Gaussian scalar fields, but their general approximation guarantees do not yield the stated complete quantiles, shared median, and one-crossing/increasing-convex-order analysis, and their main oversampled bound excludes one-column sketches. Existing real Gaussian rangefinder expected-error formulas cover the real mean under a square-root reduction, but not the complex risk law or the field-dependent convex ordering. Angular beta laws are standard mathematics and are not claimed new. Literature searches and research-record comparisons did not identify an exact covering Nyström theorem. A different representation of the same law in stochastic matrix-approximation literature remains a residual risk.

## Value — PASS
The exact one-probe trace-error distribution is a natural benchmark for randomized Nyström matrix compression. A comparison of field choices based only on medians would miss an unbounded contrast-dependent gap in means. Increasing-convex ordering establishes a systematic relation for all increasing convex error penalties even though neither residual is first-order stochastically smaller. The result does not claim cost-normalized superiority: a complex probe uses more real arithmetic than one real probe.

## Limits
Two eigenvalues, rank-one positive semidefinite residual, exact arithmetic. No claims for larger matrices, block probes, equal work budgets, or numerical stability. This self-review is not an independent validation.

Self-review: passed. Independent audit: not yet performed.
