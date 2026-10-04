# Review

## Correctness

PASS. Conditioning one arrival \(j\) on attaching to the root versus a nonroot predecessor admits an exact parent-array coupling. The descendant set of \(j\) is unchanged, and every vertex in that subtree gains exactly the alternative parent's pre-existing depth in the nonroot case. This proves strict stochastic ordering without relying on finite computation.

The expected subtree size is \(n/j\), and averaging the classical depth mean over a uniformly chosen nonroot predecessor gives the displayed harmonic factor. The Bernoulli covariance identity then yields the local formula. Exact telescoping gives the global covariance. The correlation asymptotic uses the classical \(L^2\) total-path-length limit and the independent-Bernoulli root-degree variance.

## Originality

PASS, with a bounded residual risk from older bivariate increasing-tree enumeration. Dobrow--Fill's full article was inspected throughout its model setup, total-path-length limit theory, and second-moment discussion. It treats total path length but not root degree jointly.

Bergeron--Flajolet--Salvy's full open paper was inspected at the path-length and root-degree sections. Both statistics are classical there, but they are analyzed separately and no mixed covariance is stated.

A very recent power-weight path-length paper was also checked because it gives attachment-innovation formulas and recovers the uniform variance constant. Searches of its full text found no root-degree statement or covariance. The accepted novelty is therefore the root-attachment stochastic comparison, the exact harmonic local profile, and its global monotone-transform consequence, not the marginal laws of either statistic.

## Value

PASS. Root degree is the most basic branching statistic at the distinguished vertex, while total path length is the canonical global search-cost statistic of a recursive tree. The result gives a causal-looking finite-sample decomposition: each direct root attachment shortens the final tree in stochastic order, and its exact contribution depends on insertion time.

The contrast with the positive root-degree/leaf covariance is mathematically informative: extra root branching simultaneously preserves more leaves and reduces aggregate search depth. The all-increasing-transform sign and the explicit asymptotic separation between linear covariance and vanishing correlation make the statement more structural than a single mixed moment.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK trees_enumerated=46233 local_cov_checks=36 conditional_mean_checks=28 stochastic_cdf_checks=490 global_cov_checks=8 marginal_moment_checks=24 telescoping_checks=499`.
