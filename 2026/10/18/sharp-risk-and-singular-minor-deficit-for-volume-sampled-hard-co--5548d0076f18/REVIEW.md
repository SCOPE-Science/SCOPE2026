# Mathematical assessment

## Correctness

**PASS.** The probability law is normalized by the elementary symmetric principal-minor identity for an orthogonal projector of rank \(n\). Constrained least squares reduces exactly to the inverse of the positive sampled Gram principal minor, and a rank-one determinant lemma converts its excess loss to the difference of two complete projector minor sums. The rank-\(n+1\) augmented projector is valid because the least-squares residual is orthogonal to the design range. The singular-subset correction is nonnegative, and explicit Vandermonde and zero-row designs attain the two universal endpoints. The small exact example verifies that simply omitting singular subsets would make an erroneous equality statement.

## Originality

**PASS on current evidence, with residual bibliographic uncertainty.** The motivating source treats the equation-preserving strategy on consistent systems; its noisy extension is not developed. The 2018 full-loss formula of Dereziński and Warmuth assumes interpolation from at least the full parameter dimension, while this theorem covers \(\(k<n\)\) and optimizes a full-data objective subject to sampled exact equations. A 2022 DPP semiparametric-regression source bounds regularized kernel/Nyström prediction risk rather than the unregularized k-row hard-constraint full loss. The related 2025/2026 randomized-pivoting source examines interpolation error for a fixed \(k\)-dimensional approximation subspace rather than the present parameter-space constraints. The algebraic ingredients are classical; they may conceal a known equivalent identity in older DPP/Schur-complement work not recovered in the cited comparisons.

## Mathematical value

**PASS.** Enforcing a row subsystem exactly in noisy, inconsistent linear systems is a concrete tension between hard interpolation and global least-squares fit. A sharp, design-independent budget/risk frontier gives an exact cost for every subdimension constraint count, while the singular-minor term identifies a structural exception and prevents misapplying the generic equality to degenerate designs. This is a useful finite-dimensional benchmark for row-split preconditioning and constrained randomized solvers; it is not claimed to yield a faster numerical algorithm.

## Limitations and closest literature

The full objective uses all data. No convergence, computational-complexity, unlabeled-response, approximate-constraint, or weighted-residual assertion is made. Main comparisons: Sun et al., arXiv:2605.29304v1 (consistent fixed-row enforcement); Dereziński–Warmuth, JMLR 2018 Theorems 5–8 and 16 (volume sampling with dimension-sized or larger unregularized regression subproblems); Epperly, arXiv:2510.02513v2 (projection-DPP interpolative decompositions); Fanuel–Schreurs–Suykens, arXiv:2011.06964v2 (DPP regularization of semiparametric interpolation). The principal residual risk is an unindexed equivalent determinant/Schur-complement formula.

Self-review: passed. Independent audit: not yet performed.
