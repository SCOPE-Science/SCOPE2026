# Self-review

## Correctness — PASS

The exact coordinate second-moment recurrence follows by conditioning and removes all cross terms using centered independent oracle noise. Its stationary fixed point and sharp initial second-moment contraction factor follow directly. Synchronous coupling proves uniqueness of the finite-second-moment stationary law. The rate constraint reduces to a compact simplex optimization in sampling probabilities; each individual objective is strictly convex, with an infinite negative boundary derivative. The KKT equation is inverted algebraically, yielding a unique scalar root and an exact global optimizer. Uniform expansions on compactified simplexes and strict Cauchy–Schwarz equality yield the two endpoint limits. The attached numerical and rational script checks 9,499 test assertions; these do not replace the proofs. Scientific limitation: none of these arguments implies pathwise decay at the same factor.

## Originality — PASS, qualified

Primary full text of Ding et al. (arXiv:2311.00088, algorithms (8)–(9), Theorems 3–4 and 7–8 and appendices) was inspected. Their analysis concerns uniform coordinate selection and high-probability accuracy under a local PL condition, not a joint optimal probability/step design for exact stationary covariance. Qu–Richtárik (arXiv:1412.8060) and Rodomanov–Kropotov (DOI:10.1137/19M125532X) cover arbitrary deterministic-coordinate sampling and volume sampling respectively; only their abstracts were accessible. The full public text of Richtárik–Takáč, DOI:10.1007/s11590-015-0916-1, was also inspected: its exact optimal serial probability formula depends on deterministic Lipschitz/strong-convexity parameters rather than persistent coordinate oracle-noise variances, and its criterion is iteration complexity rather than stationary noise floor constrained by a sharp transient factor. The closest published research records on inverse-positive SPD optimal sampling, stochastic delay, and stationary covariance of a scalar gradient estimator address different criteria and methods: noise-free rate, delay-law optimization, or scalar estimator memory. A missed noise-aware coordinate-descent Pareto theorem, perhaps under a transformed parametrization or adaptive sampling terminology, remains an explicit publication-priority risk. Retrieved-record noncoverage is not a mathematical proof of novelty.

## Value — PASS

The object is a natural one-oracle-per-iteration optimization method under persistent measurement noise, where minimizing the stationary error floor subject to a specified time-to-accuracy budget is an operational design question. The complete all-dimension global optimizer is computable by one scalar monotone root, not a generic nonlinear search. The sharp contrast between square-root and squared-weight sampling near opposite ends of the admissible rate range identifies a structurally meaningful tradeoff. In a two-coordinate anisotropic-noise example the exact optimal design reduces stationary loss by about 20% relative to uniform sampling at the same sharp rate. No extension to general convex objectives or nonlinear noisy gradients is asserted.

## Limitations and closest literature

The result requires positive noise variances, diagonal quadratic curvature, fixed independent coordinate sampling, constant positive steps, and finite variance. The inspected full-text primary papers are Ding et al., arXiv:2311.00088, and the optimal-probability NSync analysis, DOI:10.1007/s11590-015-0916-1. The abstracts of Qu–Richtárik and Rodomanov–Kropotov are additional relevant comparisons but cannot rule out material in their full papers. Priority and generalization remain open to independent review.

Self-review: passed. Independent audit: not yet performed.
