# Scientific assessment

## Correctness — PASS
The key identity is obtained by exact factorial-moment size biasing of a pair of categorical draws, followed by midpoint convexity. The edge-absolute-value calculation gives a local difference supported only at count gaps of \(0\) and \(\pm1\). The uniform Pearson statistic is an affine multiple of the unbiased collision statistic. The graph formula then follows by exchangeability and linearity of covariance. For \(n\ge3\), the fixed-bin asymptotic uses the aperiodic lattice local CLT; for \(n=2\), parity is handled separately. A standard-library exact-rational verifier exhaustively confirms the stated finite test ranges. The infinite-size theorem is analytically proved, not inferred from a finite run.

## Originality — PASS, with residual risk
The closest accessible primary paper, Banić–Elezović (arXiv:2610.13366v1, full Sections 1–6 inspected), establishes the first marginal moment of discrete total variation and explicitly contrasts it with Pearson's chi-square. It neither states the mixed covariance nor supplies the pair-collision convexity identity. The earlier Comb Test (arXiv:2606.01465, abstract accessible but full text inaccessible) studies calibration and empirical power; Bax–Ouimet (arXiv:2309.01882, author-posted full text inspected) gives approximation bounds and confidence intervals, rather than exact mixed moments. Targeted semantic, exact-parameter, and equivalent-statement searches found relevant but non-covering occupancy covariance studies. Risk remains from alternate convex-order terminology or inaccessible full texts. No assertion of exhaustive novelty is made.

## Mathematical value — PASS
Complementary tests applied to the same histogram require joint, rather than marginal, null information. The exact finite-sample positive cross-covariance rules out treating Pearson chi-square and local absolute roughness as uncorrelated. Its independence from graph topology at fixed total weight and its dimension-independent cyclic asymptotic identify a structural phenomenon; the unbiased nonuniform collision identity explains why positivity survives for all convex histogram statistics. These are not merely recalculations of the first moment or variance of one statistic.

## Scientific limitations
No full joint law, significance level, combined-test calibration, or nonuniform Pearson-covariance sign is claimed. The fixed-bin limit is not a growing-dimension limit. A missing accessible text for some relevant papers is an originality risk, not evidence of noncoverage.

Self-review: passed. Independent audit: not yet performed.

