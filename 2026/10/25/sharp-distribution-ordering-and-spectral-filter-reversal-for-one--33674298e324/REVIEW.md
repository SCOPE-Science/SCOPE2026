# Scientific assessment

## Correctness — PASS

The proof identifies the exact projection-error quotient, derives the exchangeability transposition identity with correct denominator normalizations, and converts it through a weighted covariance sum to the all-pairs error gap. Each ratio integral is uniformly bounded for positive weights, including heavy-tailed magnitude laws. The power-iteration ordering, inverse-filter reversal, log-convexity monotonicity and sharp factor-two claim follow analytically. Reproducibility: the included `verify.py` passed 6,969 deterministic exact-rational assertions. These tests are not used as a proof of any universal assertion.

## Originality — PASS (conditional on inspected literature)

The closest full-text work is Saibaba–Międlar (arXiv:2308.05814v1), which analyses Gaussian and several non-Gaussian sketch classes, including Rademacher, using probabilistic error and sampling bounds; the inspected statements do not give an exact single-vector, all-exchangeable-magnitude extremal ordering or the inverse-filter reversal. Tropp–Webber (arXiv:2306.12418v1) gives randomized range methods and Gaussian expectations, and Diouane et al. (arXiv:2206.08793v1) covers Gaussian-covariance expected-error bounds; their inspected assertions likewise do not imply the new pair-swap identity. Relevant prior numerical linear algebra records concern multistage adaptive pivoting, Rayleigh residual filter distortion, Gaussian planar sketch covariance tuning, or stochastic subspace descent rather than this theorem. An abstract weighted-ratio rearrangement principle could imply the result, and publication priority remains uncertain pending independent literature review.

## Mathematical value — PASS

One-vector sketches are the limiting fixed-sampling-cost case of randomized low-rank approximation. The theorem gives a complete distribution-class minimizer under every positive power iteration, an exact sign reversal under inverse filtering, and a sharp factor-two comparator to optimal rank-one squared error; a two-dimensional Gaussian example exhibits unbounded error-ratio degradation. This provides a motivated structural criterion for evaluating non-Gaussian, basis-aligned spectral probes rather than a merely numerical special case.

## Scientific limitations

The matrix columns must be mutually orthogonal in the chosen input basis and the squared probe magnitudes exchangeable. The theorem does not cover general right singular vector orientations, multiple probe vectors, spectral norm, or arbitrary nonexchangeable distributions. No independent audit or exhaustive publication-priority verification has been performed.

Self-review: passed. Independent audit: not yet performed.
