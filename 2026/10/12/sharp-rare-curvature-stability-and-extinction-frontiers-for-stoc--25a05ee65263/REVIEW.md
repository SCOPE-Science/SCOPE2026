# Review of the sharp two-curvature SRKCD frontier

## Correctness — PASS

The undamped SRKCD stage coefficients are reconstructed from the defining recurrence in arXiv:2201.12782v1, rather than inferred only from generic Chebyshev terminology. For the same curvature sample reused within each macrostep, the exact multiplier is \(T_s(1-\alpha\lambda/s^2)\). Independence of macrostep samples makes the positive-moment factorization exact for every time horizon, and the signed and squared-moment boundaries follow from simple strict inequalities. The almost-sure exponent follows from the strong law only in the nonzero-low-multiplier case; a separate geometric hitting-time proof handles the zero case. Strict Jensen proves the separation of thresholds. The exact rational witness and exponential asymptotic have been reconstructed. The standalone verifier supplies 6099 additional finite checks without replacing the infinite proof.

## Originality — PASS with residual priority risk

Stillfjord–Williamson (arXiv:2201.12782v1, full accessible text) give the SRKCD stages and general convergence/stability discussion, while Eftekhari–Vandereycken–Vilmart–Zygalakis (arXiv:1805.07199v1, full accessible deterministic result) give the fixed-spectrum Chebyshev polynomial and conservative matrix bound. Neither states the exact two-point random-curvature sampling probability boundary or the stage-exponential almost-sure/moment split. Abdulle–Cirilli's S-ROCK analysis treats a different SDE driving-noise setting, with only abstract inspected. Closely indexed scalar-curvature OSGM results use another algorithm. An equivalent unpublished or unindexed stochastic-polynomial-product theorem may exist. Classical polynomial identities and iid-product laws are not claimed as independent discoveries.

## Value — PASS

The complete sharp threshold for the natural two-batch quadratic explains precisely when rare high-curvature samples overcome Chebyshev acceleration as the number of stages increases. The exact asymptotic, resonance/no-safe-frequency stage counts, and nonempty regime of almost-sure convergence despite exploding second moments furnish motivated parameter-selection and diagnostic boundaries. The same-model work claims no nonlinear generalization or practical speedup; the aggressive fixed step may violate established worst-case sufficient bounds.

Self-review: passed. Independent audit: not yet performed.
