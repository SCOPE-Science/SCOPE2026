# Review
## Correctness
PASS. Pearson's statistic is exactly affine in the pair-collision count. For one distinguished observation pair, conditioning on equality versus inequality changes an additive cell statistic by exactly one second forward difference averaged over a \(\operatorname{Binomial}(n-2,1/m)\) count. This gives the coefficient in the theorem without approximation. The power-divergence sign follows from strict convexity or concavity together with the sign of its normalization, and the \(\lambda=0\) case follows from strict convexity of \(k\log k\).

Direct multinomial enumeration reproduces the Pearson--log-likelihood covariance formula, representative nonzero power-divergence cases, and the exact Pearson variance obtained from the quadratic specialization.

## Originality
PASS, with a concrete older-literature risk. The foundational power-divergence source defines and compares the family but the accessible material does not expose the proposed mixed moment. The closest complete public exact-finite source computes marginal exact distributions, critical values, and powers under uniformity; its inspected sections and targeted full-text searches do not state covariance, correlation, or a joint-statistic formula.

The current and prior comparison set contains exact Pearson results conditional on support size and covariances with occupancy-frequency coordinates. Those statements do not imply the arbitrary-cell-score identity or its nonlinear log-likelihood and noninteger-power specializations.

## Value
PASS. The claim links two canonical goodness-of-fit statistics and, more strongly, the whole Cressie--Read family through one finite curvature identity. It supplies a reusable sign criterion for any additive cell score, proves strict finite positive covariance throughout \(\lambda>-1\), and recovers the common chi-square covariance scale as a limit without relying on asymptotic equivalence for the finite theorem.

## Closest literature and limitations
The closest exact-finite literature enumerates the multinomial support to obtain individual power-divergence distributions and powers. The theorem here addresses a different object: a joint mixed moment and its structural curvature reduction. The principal originality risk is an equivalent identity in older categorical-data literature, especially the inaccessible remainder of the 1984 foundational paper. The exact theorem assumes uniform cell probabilities and asserts covariance rather than stronger positive association.

Self-review: passed. Independent audit: not yet performed.
