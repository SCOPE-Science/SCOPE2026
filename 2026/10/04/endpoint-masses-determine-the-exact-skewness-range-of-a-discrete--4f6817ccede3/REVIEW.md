# Review

## Correctness

PASS. Positive-affine invariance reduces the problem to a compact ordered
mean-zero, variance-one support set. On every stratum with fixed adjacent
collision blocks, an interior extremum of the third moment satisfies a
quadratic Lagrange equation. Hence an extremum cannot have three or more
distinct support levels. Iterating to the boundary leaves only two-level
contiguous coarsenings.

A two-level coarsening with lower mass \(P\) has skewness
\[
\frac{2P-1}{\sqrt{P(1-P)}},
\]
which is strictly increasing in \(P\). The first and last admissible cuts
therefore give the exact infimum and supremum. Connectedness of the strict
support cone fills every intermediate value. The sampling corollary follows
from the standard exact covariance identity.

## Originality

PASS, with a residual older moment-space literature risk. The complete
Shanmugam paper was inspected. It derives the sample-mean/sample-variance
covariance and correlation formulas and tabulates many named distributions,
but it does not optimize the parent skewness over support locations at fixed
atom probabilities.

Searches for fixed probability vectors, support geometry, finite discrete
skewness bounds, and standardized third-moment optimization did not return the
endpoint-mass interval. The closest semantic database hits concern
Poisson-binomial cumulants or unrelated support optimization problems.

The Zhang and Sen papers are directly relevant to the sampling identity and
the role of skewness, but available evidence does not indicate a fixed-profile
support extremum in either work.

## Value

PASS. Skewness is one of the basic standardized shape parameters, yet for a
fixed categorical probability profile its dependence on the numerical labels
is usually treated as arbitrary. The theorem gives a complete geometric
classification: only the endpoint masses determine the sharp range, and a
majority endpoint forces the sign for every possible ordered coding. The
sample-mean/sample-variance corollary turns this into an exact support-robust
sign criterion for a classical pair of statistics.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK bound_checks=60000 boundary_checks=60000 two_point_checks=4950 covariance_checks=9 sign_checks=30000`.
