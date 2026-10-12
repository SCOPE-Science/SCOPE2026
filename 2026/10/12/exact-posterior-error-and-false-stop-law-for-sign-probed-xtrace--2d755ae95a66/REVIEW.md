# Review

## Correctness

PASS. Both naïve estimators specialize to the same range-projection formula, including rank-deficient sample matrices. Two independent sign lines yield a complete three-case classification for every \(k\ge3\); exact counting proves the joint law and all moments. The posterior error and stopping formulas use precisely the normalization and threshold printed in the defining paper. The standalone rational verifier independently enumerates all test-vector sequences for \(3\le k\le8\), without using finite enumeration as a proof for all \(k\).

Limitation: the naïve rank-aware definitions, not optimized formulas assuming full column rank, are being analyzed.

## Originality

PASS. The defining XTrace paper already gives the error-proxy formula, adaptive test and generic correlation identity; those are not claimed new. Its experimentally observed mild correlations do not fix the exact \(1/2\) correlation of the sign-probed rank-two identity family or the complete three-point joint law. The predecessor jackknife paper concerns different replicates, and the Hutch++ separate-sketch estimator does not include the coupled leave-one-out posterior error. Focused indexed and primary-text comparisons did not locate the exact law or false-stop probability.

Residual risk: unindexed special-instance analyses might exist.

## Value

PASS. The exact output/proxy law quantifies an observable diagnostic limitation in an algorithm explicitly intended for adaptive tolerance decisions: a zero posterior error can falsely certify a 50% trace error with probability \(2^{1-k}\), and the expected squared proxy can be a factor \(k+1\) below the true mean-squared error. The smallest positive-definite flat-spectrum example is natural and the complete all-\(k\) distribution gives sharp budgets and tolerance cutoffs. Absolute error nevertheless decays exponentially in \(k\), and the source did not promise a per-run confidence certificate.

Self-review: passed. Independent audit: not yet performed.
