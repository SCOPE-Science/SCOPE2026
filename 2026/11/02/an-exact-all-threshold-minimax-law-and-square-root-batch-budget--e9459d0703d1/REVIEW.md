# Scientific review

## Correctness (PASS)

The exact line minimizer yields the stated dimensionless progress formula. Whitening by the Hessian moves the problem to an angular Gaussian density; the density is derived by radial integration. The derivative of success probability with respect to start angle has a strictly positive sign between the covariance eigendirections for nonisotropic sampling, which **proves** the worst-orientation quantifier for all thresholds rather than guessing it from a plot. The Gaussian ratio gives the exact one-draw failure CDF; independence gives the batch power. Strict monotonicity in the transformed condition number yields uniqueness of the optimal covariance up to scalar. The square-root batch law follows from an explicit arctangent asymptotic expansion, with its leading coefficient and critical windows. A local standalone script passed 849 independent assertions including exact fractions and finite diagnostics, but the unbounded universal claims rest on the analytic proof. No claim is made for sequential line searches or joint-span minimizations.

## Originality (PASS, with residual publication-priority risk)

The inverse-Hessian covariance concept and general randomized line-search convergence/expected progress are pre-existing in arXiv:1210.5114 and arXiv:1111.0194. The later random-subspace analyses arXiv:2206.03371, arXiv:2211.09873, arXiv:2204.01275 and arXiv:2308.04734 provide general high-probability complexity, probabilistic descent or expectation comparisons, not the same exact plane-wide all-threshold minimax failure law or precise independent-best-of-batch threshold. A semantic literature comparison against relevant published records did not disclose a direct implication of the **full joint claim**. The exact angular/Cauchy integral and order-statistics steps are classical, not individually novel. Earlier specialized papers on batch directional random search or anisotropic Gaussian angular order statistics could overlap, and the published literature survey is not exhaustive.

## Value (PASS)

One-shot best-candidate selection provides an interpretable reliability budget: despite an expected gain of order \(\kappa^{-1/2}\), the median gain is only of order \(\kappa^{-1}\). A target gain and confidence thus require sharply \(\sqrt\kappa\) candidate trials for unpreconditioned planar quadratics; the inverse-Hessian covariance removes this degradation simultaneously for all thresholds. This distinguishes statistical reliability from a mean convergence rate and supplies a precise finite-oracle design benchmark. It is not a generic convergence theorem or an assertion that Gaussian direction generation is the most efficient algorithm overall.

## Limitations and close comparisons

- arXiv:1210.5114, Section 4, expected progress and covariance adaptation: covers the design philosophy but does not directly imply threshold-wise uniqueness or exact batch quantiles.
- arXiv:2206.03371, Chapter 4; arXiv:2211.09873, Sections 3–5 and appendices: general sketched optimization, not this simultaneous-candidate angular law.
- arXiv:2204.01275, probabilistic random-subspace polling; arXiv:2308.04734, expected decrease: the former uses polling/probabilistic descent and the latter expected decrease rather than exact quadratic-line minimization quantiles.
- The provenance of relevant 2022 random-subspace material is anchored to the earlier arXiv thesis submission (2022-06-07), not the later overlapping November paper.

Self-review: passed. Independent audit: not yet performed.
