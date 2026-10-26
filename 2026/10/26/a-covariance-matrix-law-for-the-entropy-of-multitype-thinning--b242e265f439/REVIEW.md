# Research review

**Correctness — PASS.** The probability generating function is \(F(1+w/n)^n\), whose logarithm has quadratic coefficient \(K=\operatorname{Cov}(X)-\operatorname{diag}(\lambda)\). A global entire-function growth bound, not just coefficientwise expansion, gives \(L^2\)-dominated likelihood-ratio convergence. Poisson–Charlier orthogonality and the exact KL decomposition yield both constants. The example's improved marginal rate uses its vanishing quadratic factorial cumulant. The standalone checker verifies 24 exact-rational covariance identities and six direct finite-law entropy values. Limits rely on the analytic argument, not simulations.

**Originality — PASS (research comparison, not priority certification).** The 2026 scalar thinning paper and the 2010 scalar Charlier work do not state the multitype information formula. Roos's 1998/1999 multivariate Charlier expansion is for generalized multinomial single-category summands and total-variation/point metrics; his 2017 paper addresses general compound Poisson approximations in total variation. The closest inaccessible historical possibility is Roos (1999), *On the Rate of Multivariate Poisson Convergence*, which describes second-order signed approximations but no entropy constant in its accessible abstract. Historical priority remains uncertain under alternative multivariate approximation terminology.

**Mathematical value — PASS.** The theorem identifies the exact natural information invariant of multitype rare-event sampling, separates dependence error from marginal Poisson fit, and gives a fully specified equidispersed witness where joint dependence dominates individual fit errors. The classification by pairwise covariance is useful even when all higher-order input dependence remains arbitrary. Neither correctness nor reproducibility alone supplies this motivation.

**Limits.** Bounded input vectors and fixed dimension are required. No universal higher-order rate is claimed when the covariance coefficient vanishes. More comprehensive historical priority checking and independent validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
