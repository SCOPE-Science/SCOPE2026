# Self-review

## Correctness — PASS

The two-by-two free propagator and its Gaussian innovations follow directly from the drift matrix and Ito isometry. The bath at consecutive reset epochs is a contracting random affine recursion, since every positive Poisson interarrival gives a coefficient strictly below one. Exponential integrability is established below \(\sqrt{r(\gamma+1)}\) by an explicit cosh drift condition, with a Gaussian innovation obstruction at and above the cutoff. The probe's stationary-age Gaussian mixture has the same cutoff. Chernoff's bound and a matching long-flight Gaussian lower bound prove both logarithmic tail limits. A standalone verifier passed 387 finite checks. Limits: no density prefactor or uniform large-\(\gamma\) estimate.

## Originality — PASS, with publication-priority risk

The exact model, finite-parameter variance, kurtosis and large-memory quasistatic density arise in Santra–Das (2026). Those premises are not new. Sections II–III and Appendix A were compared at the equation and claim level: the finite-\(\gamma\) sharp exponential-moment domain and the common probe/bath log-tail exponent are not given. Biswas et al. (2024 preprint) renew the full memory state rather than retain the bath. Tal-Friedman et al. (2022) have one-coordinate proportional resetting and an infinite Laplace convolution, not the same coupled generator. No full-priority guarantee is made; unpublished or non-indexed independent derivations remain possible.

## Value — PASS

A Gaussian quasistatic profile can approximate the central shape yet fail to characterize the farthest rare excursions at any finite memory time. The exact attainable inverse tail length \(\sqrt{r(\gamma+1)}\) supplies the missing parameter-uniform *finite-parameter* boundary and shows that an unreset bath coordinate shares the reset tracer's extreme-event scale despite different variances. The result requires a non-renewing bath recursion rather than direct substitution into a scalar renewal formula, and is a natural mathematical distinction for rare-event interpretation and experimental tail fitting.

## Limitations and closest literature

The theorem treats the exact linear, two-coordinate, independently driven, instantaneous selective-reset dynamics. It does not imply a crossover scale, finite-speed protocol result, full large-deviation principle, or experimentally accessible far-tail range. Closest works: Santra–Das (arXiv:2603.17027v1), Biswas et al. (arXiv:2412.09260), Tal-Friedman et al. (arXiv:2205.03363). An earlier scientific result concerning this same stochastic model classified stationary fourth-cumulant monotonicity; that finite-moment claim neither implies nor determines the moment-generating-function convergence boundary.

Self-review: passed. Independent audit: not yet performed.
