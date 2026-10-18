# Review of the commutator splitting limit

## Correctness

PASS. For every fixed real symmetric positive-semidefinite pair and time horizon, two resolvent expansions yield an exact macro-step mean defect of \(h^2Q/2\) and a Rademacher commutator increment of \(h^2J/2\). A deterministic \(O(h)\) pathwise bound, an orthogonal martingale decomposition, and a Lindeberg triangular-array argument establish the limiting mean, the exact Gaussian covariance, and covariance convergence. At equal cost, an independent-with-replacement scheme has increments of order \(h\), which yield the stated larger covariance. Exact rational matrix identities and exhaustive finite-horizon order enumeration were reproduced by the accompanying script. The proof requires fixed dimension and exact resolvent steps.

## Originality

PASS on the accessible evidence, with residual bibliographic risk. Eisenmann–Stillfjord [1] prove expected-error bounds for independently randomized implicit operators, including general order one-half and some order-one cases, but not the paired-without-replacement commutator CLT. Veldman–Zuazua [4] prove mean convergence for randomized continuous-time LQ dynamics with randomly selected matrix subsets; neither their dynamical definition nor conclusions establish this implicit-resolvent ordering covariance. Childs–Ostrander–Su [2] and Chen–Huang–Kueng–Tropp [3] treat randomized unitary product formula error/concentration, not this exact Gaussian limit for dissipative resolvents. Their expectation and concentration bounds are not the same statement as the explicit limiting covariance. Algebraic commutator expansions and triangular-array CLTs are classical ingredients, not asserted as new. Search incompleteness remains a scientific risk.

## Value

PASS. Pairwise balancing is a motivated alternative to ordinary independent randomized splitting when the same two component solves are available. The result demonstrates a strict two-exponent reduction in covariance order (from \(h\) to \(h^3\)) at fixed solve count and identifies the precise residual commutator-dependent stochastic mechanism. It distinguishes stochastic variability from deterministic first-order discretization error and supplies an explicit two-dimensional positive-definite sharpness witness. No improvement in total order beyond one is claimed.

## Closest literature and limitations

[1] arXiv:2210.05375; [2] arXiv:1805.08385; [3] arXiv:2008.11751; [4] arXiv:2109.13798. See the theorem for the exact model and the limits of transfer to nonlinear/non-self-adjoint settings. No independent specialist or external certification has been performed.

Self-review: passed. Independent audit: not yet performed.
