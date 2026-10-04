# Review

## Correctness

PASS. Conditioning on a fixed point leaves the remaining values uniformly permuted. A descent not touching the fixed position therefore remains fair. For the two touching descent coordinates, the conditional probabilities reduce to counting values below \(j\) or above \(j+1\), giving (2)--(3) exactly.

All aggregate formulas are transparent sums of the local matrix. The interior row sums cancel, the endpoint row sums equal \(-1/(2n)\), and the wrap comparison contributes \(+1/(2n)\) at each endpoint. The exact correlation uses the standard fixed-point and descent variances.

## Originality

PASS, with a specific residual risk from refined classical descent enumeration. Diaconis--Evans--Graham's full public text was inspected at its fixed-point random-set theorem and its primary \(60C05\) classification; it does not introduce descents.

Désarménien--Wachs was inspected through its full introduction, descent-class construction, and Theorem 5.1. It enumerates exact descent classes with a prescribed total number of fixed points, but the fixed-point locations are collapsed. Thus it does not state the position-resolved cross-covariance matrix, endpoint-only row sums, or coordinatewise cyclic cancellation.

Eriksen--Freij--Wästlund was inspected at its full public introduction and fixed-point/descent framework. It studies derangements and prescribed descent events, not the covariance of individual fixed-point locations with individual descent locations.

## Value

PASS. Fixed points and descents are two canonical local statistics of a random permutation. The sparse matrix identifies exactly where dependence lives and reveals that the familiar global negative covariance is not spread through the bulk: it is an open-boundary effect.

The cyclic closure gives a natural structural test of that interpretation. Adding one wrap comparison removes the entire covariance, and does so coordinate by coordinate rather than only after summing fixed points.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK permutations_checked=409112 local_cov_checks=240 row_sum_checks=44 column_sum_checks=36 cyclic_checks=44 global_checks=16 variance_checks=16`.
