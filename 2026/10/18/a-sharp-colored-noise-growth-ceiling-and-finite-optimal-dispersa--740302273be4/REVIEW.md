# Scientific assessment

## Correctness

PASS. The two-patch reduction and both log-growth identities have their normalization and Brownian covariance tracked explicitly. The stationary ratio equation is pathwise contractive, and Lyapunov bounds establish the moment integrability required for generator identities. Differentiating the causal stationary ODE with respect to its Gaussian forcing gives an exact positive response kernel; OU Gaussian integration by parts yields the sharp analytical ceiling. The two small-noise/large-migration limits follow by dominated convergence, while the weak-migration limit follows by splitting the stationary moment expectation. Continuity, strict interior positivity, and vanishing endpoint limits prove existence, not uniqueness, of a finite optimizer. The standalone program verifies representative finite-time identities but is not used to certify the limiting theorem.

## Originality

PASS under accessible evidence, with residual priority risk. Henderson and Tiffeau-Mayer give the exact population model and a stationary growth identity, plus numerical evidence of an interior optimum and a separate white-noise formula. Their main and supplementary calculations do not state or derive the all-parameter OU Gaussian-response bound with sharp weak-noise and strong-migration limits. Hening–Nguyen–Yin treat principally white-noise environmental forcing; Benaïm–Lobry–Sari–Strickler study switching environments. Targeted searches for mathematical antecedents identified no implication-equivalent response identity or bound. A broader Gaussian linear cocycle or population-dispersal result may imply it, which requires human historical-priority review.

## Mathematical value

PASS. The motivating ecology study explicitly observes an intermediate migration optimum numerically, but an exact mathematical bound and attainment theorem are useful because its colored-noise stationary density is not known in elementary closed form. The envelope quantifies the unavoidable correlation-time and migration-rate tradeoff, is sharp at weak noise, and determines the exact high-migration coefficient. It distinguishes an exact Ornstein–Uhlenbeck theorem from a colored-noise effective-potential approximation. These are substantive structural facts for a natural model, not numerical-only observations or a parameter substitution.

## Scope and risks

The theorem is strictly two-patch, independently OU-forced, and symmetric. No general finite-patch extension, uniqueness of optimal migration, stochastic extinction time, or nonlinear ecological saturation is asserted. Independently checking historical coverage by general random-positive-matrix results remains important.

Self-review: passed. Independent audit: not yet performed.
