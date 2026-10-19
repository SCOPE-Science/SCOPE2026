# Scientific review

## Correctness
**PASS.** The nonadaptive estimator is reduced to independent singular-direction Gaussian coordinates. The two energy terms converge in \(L^2\); a fixed-dimensional multivariate Lyapunov CLT gives the joint cross-product limit, and the continuous mapping theorem gives the centered chi-square law. The existing exact Gaussian variance identity supplies uniform integrability needed to exchange clipping expectation with the limit. The gamma recurrence yields the exact bias. Both large-sketch exponents and constants follow from endpoint/interior Laplace expansions; the rank-one saddle is uniquely at \(u=2\), with curvature \(3/4\). Program checks corroborate but do not establish the infinite claims.

## Originality
**PASS under the inspected literature, with residual risk.** The full accessible source Chen--Halikias--Musco--Persson (arXiv:2609.28472) presents Hutch# and the same exact variance but not the limiting signed distribution, exact positivity-clipping bias or the rank-one sign tail. The related Hutch++ method of Meyer et al. (arXiv:2010.09649) has a different nonnegative projection-based structure. A 2022 Nyström++ paper studies other adaptive estimators. Targeted mathematical-literature searches for Hutch# and the chi-square signed limit did not reveal an equivalent statement. Generic Gaussian CLT and chi-square asymptotics provide proof tools but do not by themselves contain the estimator-specific decomposition and two spectral comparisons. Unindexed or inaccessible results may still overlap.

## Value
**PASS.** For a quantity known to be positive, the estimator can return a negative value with limiting probability about 15.73% at one sketch pair, no matter how large and spectrally flat the input becomes. The natural nonnegative repair incurs a 25.78% limiting relative mean bias at that same budget, while rank-one and flat high-rank inputs have sharply different sketch-budget sign tails. These explicit laws supply a parameter-choice and downstream-domain-validity diagnostic absent from variance-only guarantees. The result does not claim any impact for other estimator variants or a joint two-parameter limit.

Self-review: passed. Independent audit: not yet performed.
