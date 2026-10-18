# Mathematical review

## Correctness — PASS

The proof reconstructs the discrete heat kernel as a product of one-dimensional Bessel kernels, proves strict monotonic ordering of the logarithmic time scores by a Riccati argument, and shows uniqueness of the first-neighbor derivative sign change using a split Laplace transform with disjoint ordered spectral supports. The sum-zero identity then gives both exact endpoint norms for the maximal one-negative-site interval; strict dimension ordering and the three-term threshold expansion follow from explicit series. The standalone finite checker supplies consistency tests only, not an infinite proof.

## Originality — PASS within the inspected record

Dowker's heat kernel (arXiv:1207.2096) is a baseline identity, and Baricz's Bessel inequalities (arXiv:1202.4853) are auxiliary. Neither derives a dimension-indexed sign transition for the derivative kernel or a maximal exact endpoint-norm interval. Abadias–de León-Contreras (arXiv:2107.06778) works with derivative estimates for a one-dimensional discrete kernel rather than the present sharp multidimensional sign classification. The one-dimensional case and classical ratio monotonicity are expressly excluded from novelty. A historical stronger lattice-unimodality theorem could cover the new statement; this is a residual bibliographic risk, not evidence of a covering source.

## Mathematical value — PASS

The first loss of the one-negative-site shape is a natural, sharply defined stability boundary: before it, the semigroup derivative has an explicit norm in both endpoint Banach spaces; after it, that formula provably ceases to be exact. The threshold is uniquely characterized at all dimensions, strictly moves with dimension, and has a quantitative three-term large-dimensional scale. The result is an all-dimensional structural cutoff rather than an isolated Bessel computation or a fixed numerical parameter slice.

## Limits and closest literature

The work does not determine later sign regimes or the global time-optimized analytic norm. The proof is complete under the stated unit-rate normalization, but equivalent historical formulations have not been excluded exhaustively. Reference details and reproducible finite checks are in the main result and accompanying checker.

Self-review: passed. Independent audit: not yet performed.
