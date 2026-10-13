# Review of the convex-transform / expectile-transform separation

## Correctness — PASS

The construction specifies a strictly positive density on an interval. Because squaring is increasing and convex on that interval, its ordinary quantile-coordinate transformation is exactly the square map. Three exact expectile values on a limiting discrete coupling have consecutive slopes \(5/3\) and \(4/3\). The quantified expectile Lipschitz inequality transfers the positive determinant \(3/350\) to the stated continuous distribution: the error is bounded above by \(372\eta/7+7200\eta^2\) for \(\eta=10^{-6}\), which is smaller than the discrete margin. The exact-rational standalone checker reproduces the critical identities, while the analytic score argument proves the passage to the continuous case.

## Originality — PASS, with priority risks

The primary comparison is Eberl and Klar, *Stochastic orders and measures of skewness and dispersion based on expectiles* (arXiv:2108.06138; doi:10.1007/s00362-022-01331-x), whose fully inspected Theorem 5 establishes consistency of a scalar skewness measure and whose Remark 6 proposes an all-triples expectile order without establishing implication from convex-transform order. The 2021 predecessor on expectile skewness (doi:10.1111/sjos.12518) discusses scalar and quantile versions, not this three-level failure. A related 2022 generalized-quantile article (doi:10.1016/j.spl.2021.109339) was accessible only by abstract; priority overlap from its full text or other differently phrased literature remains unresolved. No independent novelty certification is implied.

## Value — PASS

The distinction is mathematically motivated by an explicit unresolved order-implication question. An exact full-support absolutely continuous counterexample proves that preservation of scalar expectile skewness cannot be promoted to preservation of global expectile-coordinate convexity. The small discrete seed alone would not answer the published continuous-cdf formulation; the quantitative perturbation certificate is an essential part of the result.

## Scientific limitations

The constructed density is piecewise constant, not smooth; no result is claimed for more regular distribution families or all nonlinear convex transforms. The only failure required is a single strict three-level reversed-secant inequality. Remaining bibliographic uncertainty requires independent review.

Self-review: passed. Independent audit: not yet performed.
