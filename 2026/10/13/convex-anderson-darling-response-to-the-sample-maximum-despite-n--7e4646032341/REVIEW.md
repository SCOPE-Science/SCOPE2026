# Scientific comparison and self-review

## Correctness — PASS

For independent uniforms and a fixed maximum \(t\in(0,1)\), the remaining observations are conditionally iid uniform on \((0,t)\), which yields the binomial empirical-count variance and squared bias integrated in the theorem. Strict convexity follows from the positive second derivative of the exact order-statistic log representation; both endpoint divergences are explicit. Beta conditional-mean and beta-log covariance identities prove the harmonic closed-form mixed covariance, its sign and its asymptotic. The separately embedded exact-rational and finite numerical checks passed, but the proof does not rely on their extrapolation.

## Originality — PASS, with residual risk

The closest inspected direct papers are Stephens (1974, the full-text spectral components and power calculations), Tolikas and Heravi (2008, a ten-page fully inspected paper on fitted-parameter Anderson–Darling quantiles), and Lockhart (2012, an accessible paper on conditional limits given complete sufficient statistics). These results concern spectral components, composite-null critical values, or asymptotic parametric conditioning, not the fully specified null conditional on a sample extreme. Lockhart explicitly identifies Anderson–Darling as outside the proof of his main conditional theorem. Known marginal or cross-goodness-of-fit moments do not imply dependence on the sample maximum. Targeted searches did not locate an exact mixed moment or complete conditional regression. The residual risk is an older or unindexed order-statistic joint moment identity, not a claim that failed searches prove historical uniqueness.

## Value — PASS

The sample maximum is the natural observed upper-tail extremum, while Anderson–Darling is a standard two-tail weighted discrepancy. The result specifies how conditioning on that tail observation changes expected goodness-of-fit loss at every finite sample size, proving a unique interior optimum and divergent penalties at both ends. A simultaneously exact and strictly negative global covariance shows that the aggregate sign masks the curved conditional response; these facts can inform tail-selective calibration analysis without asserting a new test or asymptotic power result.

## Scientific limits

All assumptions and quantifiers are confined to a fully specified continuous null and \(n\ge1\). The minimizer has not been evaluated in closed form, and there has been no independent audit. A classical jointly tabulated law cannot be excluded solely by searchable databases.

Self-review: passed. Independent audit: not yet performed.
