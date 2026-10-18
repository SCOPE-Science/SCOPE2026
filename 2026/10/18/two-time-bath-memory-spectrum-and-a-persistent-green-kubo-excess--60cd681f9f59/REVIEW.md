# Scientific review: bath-memory autocovariance under partial resetting

**Correctness (PASS).** The stationary covariance follows from a stable two-coordinate linear jump generator. The moment equations, two-time semigroup, positive eigenmode weights, finite Green–Kubo integral, and singular large-reset limits are proved explicitly in `RESULT.md`. Independently constructed matrix-generator comparisons, direct integrals, and stochastic simulations agree. The fixed-positive-lag limit explicitly excludes time zero.

**Originality (PASS, provisional to independent scholarly checking).** Santra and Das, arXiv:2603.17027v1, derive the underlying probe-only reset model and one-time statistics. Those results are not claimed as new. The examined primary text did not give the stationary two-time tracer covariance, its two positive relaxation weights, the integrated-correlation law, or its asymptotic excess relative to isolated Brownian resetting. Related primary work on resetting bath noise and experimental non-Markovian resetting uses different protocols or observables. A general linear jump-process derivation may implicitly cover the result, and this is a residual originality risk.

**Value (PASS).** The new observable tests a materially different claim from stationary-variance convergence: a fast-reset probe can have apparently Markovian single-time fluctuations yet retain nonvanishing extra accumulated-observation variance. The exact excess factor and nonuniform positive-lag bath tail specify the scale and source of the discrepancy.

Scope is limited to one linearly coupled thermal bath coordinate, independent Brownian drives, instantaneous Poisson resets of the tracer alone, and stationary correlations. No general nonlinear-bath theorem or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
