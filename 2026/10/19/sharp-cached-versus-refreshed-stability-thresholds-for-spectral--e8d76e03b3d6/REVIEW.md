# Self-review

## Correctness — PASS
The exact rank-one Nyström identity, diagonal preconditioner, independent minibatch distributions, and conditional second-moment recursion were reconstructed. Direct enumeration of all curvature/stepsize minibatches gives the four gains \(\alpha,\alpha t,\alpha,\alpha/t\). Exact arithmetic separately enumerated gradient minibatches and checked finite-horizon identities for 1575 parameter/horizon comparisons. Sharp boundaries follow from elementary strict inequalities and a unique real root; the enumeration is supplemental, not a proof of infinite-horizon claims.

## Originality — PASS
Frangella et al. (arXiv:2211.08597, equation (3), Algorithm 1, Sections 4 and Appendix A) specify the spectral step and preconditioner but do not characterize the exact one-example two-feature cached-vs-refreshed mean-square law; their theoretical convergence result uses a distinct fixed stepsize and stage averaging. Vaswani et al. (arXiv:1910.04920, Section 3) treat different conservative subsampled-Newton steps. Lacotte and Pilanci (arXiv:1911.02675, Theorem 4.1) give a broad exact inverse-moment formula for full-gradient IHS with sketch-independent step coefficients; it does not reduce to stochastic-gradient SketchySGD's step tied to an independent curvature minibatch. Searches of indexed research records and accessible prior findings located related covariance and refresh phenomena, but not a covering implication. Residual risk: an unindexed equivalent finite-sample calculation could exist.

## Value — PASS
The source recommends reusing a curvature preconditioner on constant-Hessian objectives. The theorem reveals a genuine stability-design trade-off in the elementary interpolation setting: a cached environment and refreshed environment have identical one-step expected errors but different long-run mean-square stability, with sharp rational and algebraic cutoffs. The exact phenomenon is not just a normalization mistake or arbitrary finite numeric example; it distinguishes averaging of powers from powers of averages under the actual curvature-guided stepsize. It does not purport to prove failure of the complete finite-precision default implementation.

Self-review: passed. Independent audit: not yet performed.
