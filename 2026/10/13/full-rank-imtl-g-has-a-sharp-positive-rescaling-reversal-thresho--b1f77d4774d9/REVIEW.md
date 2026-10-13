# Review

## Correctness

PASS. The source scale-transformation formula gives the multiplier \(\lambda=(\sum_i\alpha_i/k_i)^{-1}\). Nonnegative coefficients make its denominator positive for every positive scale vector. One negative coefficient creates a unique one-task scaling threshold where the denominator crosses zero. The explicit three-task construction is full rank, has the displayed negative source coefficient and positive common projection, and direct replay of the source closed form confirms singularity at \(k=1/\sqrt2\) and all-task conflict below it.

Risk: the statement is instantaneous and uses the source coefficient-sum normalization.

## Originality

PASS. The original source proves collinearity and calls the direction scale invariant without analyzing the multiplier's sign. A 2024 primary analysis already proves the broader fact that generalized IMTL-G is not linear under scaling and gives a rank-deficient negative-weight conflict example; those facts are treated as prior work. The inspected literature does not give the sharp coefficient-sign criterion or a full-row-rank source-form scale singularity followed by direction reversal.

Residual risk: the later scaling formula contains the denominator algebra, so an unindexed note may have drawn the same sign consequence.

## Value

PASS. Scale invariance is a defining robustness claim for IMTL-G. The result identifies the exact condition required for same-orientation invariance and shows that a legal full-rank closed-form state can violate it catastrophically under a positive task-unit change. The boundary is structurally relevant to positivity constraints and normalization design rather than an arbitrary numerical counterexample.

Self-review: passed. Independent audit: not yet performed.
