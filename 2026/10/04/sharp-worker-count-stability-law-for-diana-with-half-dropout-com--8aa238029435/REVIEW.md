# Review

## Correctness

PASS. Centering the shifts by the local gradients at the minimizer removes all affine offsets. Conditional branch averaging gives an exact closed recursion for \(\mathbb E[x^2]\), \(\mathbb E[x\bar e]\), and the mean worker shift energy. Its characteristic cubic is subjected to the complete real Jury test. The first Jury condition yields the closed-form boundary, and the remaining four conditions are proved strictly positive throughout the proposed interval. At the boundary the second-moment operator has eigenvalue \(1\); beyond it a necessary Jury condition fails.

Risk: the proof uses independent worker compressors and equal local curvature. Neither assumption is generalized.

## Originality

PASS. The defining DIANA paper supplies the gradient-difference memory mechanism and sufficient strongly convex convergence bounds. The later EF-BV paper explicitly confirms DIANA's use with arbitrary unbiased compressors, the canonical scaling \(\lambda=1/(1+\omega)\), and the benefit of independent worker randomness. Neither inspected source gives the exact scalar worker-count stability law, the eigenvalue-one boundary, or the \(2-16/(3n)+O(n^{-2})\) approach to the uncompressed ceiling.

Focused semantic searches covered DIANA aliases, unbiased Bernoulli compression, scalar quadratics, second-moment and Schur stability, and worker averaging. No inspected source or published database record implied the complete claim.

## Value

PASS. Independent worker compression is one of the central mechanisms by which distributed compression can average away noise. The exact formula quantifies that mechanism at the actual stability boundary rather than through a sufficient Lyapunov bound: one-worker half-dropout is highly restrictive, while increasing the worker count continuously restores the ordinary gradient-descent ceiling. The cancellation of arbitrary affine local-gradient heterogeneity also shows that the law measures compression-memory stability rather than a trivial homogeneous-data artifact.

Same-model review: passed. Independent audit: not yet performed.
