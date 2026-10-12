# Scientific review

## Correctness — PASS

The claimed object exactly matches the projected-row norm \(\|B_i\|_2\) when a Gaussian look-ahead block has one column. Singular-value decomposition and Gaussian rotational invariance give the exact ratio of two quadratic forms. Rearrangement reduces the underestimation event to an absolute Cauchy-ratio threshold; maximizing a univariate quadratic by a square identity establishes the global supremum and the equality spectrum. The strictly monotone envelope can be inverted exactly for the stated confidence factor. Its conditional extension requires a fresh probe independent of the current residual. Verification uses 3,584 rational projection identities, 171 exact square identities, eight inverse-envelope evaluations, and 510,000 seeded Gaussian trials. These finite checks are not used as proofs of arbitrary parameter statements.

## Originality — PASS with residual risks

Smith, Do, and Chen (arXiv:2607.06758v1), Algorithm 4.1, §4.1 and Theorem 4.3, introduce the projected look-ahead statistic and a general high-probability spectral guarantee, but the inspected source contains no exact one-probe rank-two failure curve or sharp inverse calibration. Theorem 9 and the Gaussian-specific sections of Saibaba (arXiv:1804.02614) concern structural singular-value inequalities and general bounds, not the equality-attaining two-singular-value maximization. Meier and Nakatsukasa (LAA 686, 2024) study different, two-sided Gaussian rank-estimation sketches and their accuracy bounds. An older result on distributions of Gaussian quadratic-form ratios or randomized Rayleigh quotients might imply this theorem after nonobvious identification; independent literature verification remains outstanding. The Cauchy law itself is well known and is not claimed as new.

## Value — PASS

The measured quantity governs the decision to stop an adaptive matrix-free spectral QB approximation. This is the first nontrivial residual rank where a one-probe projection can miss the dominant mode. Rather than merely giving a constructed failure, the result solves the complete minimax problem over the entire two-singular-value spectrum, including a unique least-favorable spectrum and an exact, usable one-sided confidence multiplier. At half the true norm, the sharp failure probability is about 9.13%; 90% one-sided confidence requires the exact multiplicative factor about 1.92256. Such calibration distinguishes a rank-dependent probabilistic guarantee from the much less informative statement that a sketch may underestimate. Scope does not extend to higher rank or the complete adaptive algorithm.

Self-review: passed. Independent audit: not yet performed.
