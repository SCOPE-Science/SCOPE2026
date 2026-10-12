# Review of the extreme-path/leaf-count covariance

## Correctness — PASS
Under a uniform root split, both subtrees have the standard independent recursive construction, and the extreme-key search follows only the right subtree. The leaf count is additive for all trees of size at least two, with the singleton correction explicitly retained. Its conditional expectation differs from the affine baseline only at the split boundaries. Total covariance therefore yields a one-dimensional exact recurrence and the displayed closed expression. The path-record variance and the published occupied-leaf variance establish the correlation asymptotic. The package checker independently verifies the recurrence on 499 sizes and exactly enumerates all permutations through size eight. The universal proof does not depend on that finite enumeration.

## Originality — PASS, with historical risk
Holmgren–Janson, arXiv:1406.6883v1, supplies marginal leaf moments and joint moments of fringe counts; Grübel–Stefanoski, arXiv:math/0503738v1, supplies fixed-key depth distributions. Their inspected primary theorems do not contain the mixed covariance of the extreme-key search path with occupied leaf count, nor do their marginal identities imply it. Literature and semantic-search comparisons did not identify a directly covering claim. An older mixed generating function or a less searchable representation could entail this exact identity; novelty is assessed within the inspected evidence rather than asserted absolutely.

## Value — PASS
The result answers a natural finite-sample dependence question between the extreme successful-search cost and a standard occupancy statistic. Beyond the rational moment, the finite nonzero limit coexists with asymptotically zero correlation, and the covariance is traced to rare boundary root splits. These are structural insights relevant to probabilistic analyses of randomly grown search trees, not a parameter-renaming or table recomputation.

## Scope and residual risk
No joint-law or conditional-prediction claim is made. Other insertion laws and self-balancing trees are excluded. Published general mixed factorial moments could imply this identity without identifying the two observables by the same names.

Self-review: passed. Independent audit: not yet performed.
