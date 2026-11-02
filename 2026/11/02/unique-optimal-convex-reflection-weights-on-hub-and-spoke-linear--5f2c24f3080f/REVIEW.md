# Self-review

## Correctness

**PASS.** The exact claim ranges over all integers \(n\ge2\), all real \(0<c<1\), and strictly positive convex masses. A unit dual vector supplies the weight-independent upper bound on the least eigenvalue; the proposed masses attain it and an explicit eigenbasis proves it is the bottom eigenvalue. The equality-case eigenvector conditions yield uniqueness. An independent calculation of the uniform row Gram spectrum yields the asymptotic gap comparison. Running the packaged `check.py` produced `VERIFY_OK 3159`; finite checks only supplement the proof. The method is exact arithmetic.

## Originality

**PASS, with residual historical priority risk.** Sharma's 2026 full accessible article states the general fixed-weight spectral formula, best common scaling, and global optimality of equal unit weights only in dimension two. The hub-and-spoke probability-simplex optimum in every dimension and the exact dimension-linear spectral-gap advantage are not stated there. Guida and Sbordone's 2023 primary work establishes the underlying method and geometric convergence, not the specialized allocation. General E-optimal design theory is the closest broader principle; a previously known equivalent specialized formula cannot be excluded. No mathematical novelty is claimed for the general spectral criterion, the two-row unit-weight optimum, or the classical centroid method.

## Value

**PASS.** The result gives a unique positive weight prescription in a natural high-correlation multi-row family, with a growing-in-dimension improvement in a sharp worst-case contraction gap. This is a structural, nontrivial computational design consequence, not merely a scalar numerical bound. It does not establish runtime speedups, arbitrary-frame optimality or finite-precision robustness.

## References and limitations

Sharma, *Sharp Convergence Rates and Optimal Weights for Cimmino's Reflection Algorithm*, arXiv:2605.24692v1 (2026); Guida and Sbordone, *The Reflection Method for the Numerical Solution of Linear Systems*, SIAM Review 65 (2023); Martinez and Wegman, *An alternative criterion useful for finding exact E-optimal designs*, Statistics & Probability Letters 47 (2000). Scholarly priority and independent validation remain unperformed.

Self-review: passed. Independent audit: not yet performed.
