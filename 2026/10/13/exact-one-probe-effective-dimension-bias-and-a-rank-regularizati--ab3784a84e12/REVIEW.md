# Self-review

## Correctness — PASS

The estimator is reconstructed from the published nonlinear FlexTrace definition with one Gaussian sample and a zero-column leave-one-out matrix. Its rank-one functional calculus reduces the actual random output to a ratio of two quadratic forms. Orthogonal Gaussian invariance, an independent radial factor of mean two, and three explicit angular integral identities give the exact expectation. Subtracting the effective dimension factors as a nonnegative perfect square. The equality classification, sharp weak-mode fraction, joint matched-scale law and both iterated limits then follow algebraically. Exact-rational and independent angular computations check but do not replace these arguments. The only boundary values are limits of the admissible positive-regularization problem.

## Originality — PASS, with residual risk

The closest source is Madhavan–Alexanderian–Saibaba, *FlexTrace* (arXiv:2603.05721v1), especially Eq. (3.2), Table 1, Theorems 3.3/3.5 and their proofs. It establishes the estimator, operator-monotone setting, and qualitative bias, but not this one-probe exact distributional expectation or rank/regularization boundary. The published spectral bound of Theorem 3.3 is restricted to at least four probes. Persson–Kressner (arXiv:2209.11023v3) analyze trace-of-funNyström, a different random quantity. Epperly–Tropp–Webber (arXiv:2301.07825v2) treat the linear unbiased trace problem. Their implications do not determine this nonlinear bias. Published-index searches and the previous research records checked for overlap yielded no equivalent statement. A hidden equivalent ratio-of-quadratic-forms calculation in earlier literature remains possible; the result is not claimed globally unique.

## Value — PASS

The effective dimension is a natural regularization-dependent spectral statistic used in kernel methods. Rather than recording an isolated small counterexample, the result classifies the entire positive two-eigenvalue domain and quantifies the fraction of the weak mode lost with the optimal coefficient. The boundary layer shows a discontinuous-looking phenomenon: the smaller eigenvalue tends to zero, yet if regularization tracks it, the negative bias remains order one and erases its full effective-dimension contribution. The noncommuting iterated limits identify precisely the mathematical cause of the nonuniformity. The finding does not claim improvement of any higher-dimensional or large-budget algorithm.

## Limitations and closest literature

All claims concern one standard real Gaussian probe, an exact rank-one Nyström matrix in two dimensions, positive regularization, and exact arithmetic. A possible older equivalent closed-form Gaussian-ratio calculation is the principal originality risk. Independent expert audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
