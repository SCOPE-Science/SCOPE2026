# Independent scientific audit — SCOPE-20260917-7b9ca5a2ebed

Audited at: 2026-10-01T05:14:16.390825Z

Disposition: **passed**

## Correctness — PASS

The Poisson-race representation gives the exact one-attempt integral and the change of variables produces the stated one-dimensional exponent. Strict concavity gives a unique compact saddle; the balance bounds give uniform derivative and curvature control, with exponentially controlled tails, so the first-order Laplace expansion is uniform. Differentiating the integral with respect to the transform parameter yields the stated exact logarithmic-derivative identity; concentration around the saddle then gives the alpha asymptotic and, through Wang-Lu's two-sided theorem, the sharp order in n times the success probability. The strong-concavity calculation yields the variance-profile exponent penalty. The equal-probability specialization is consistent with the beta/gamma formula.

## Originality — PASS

Reset-coupon papers before this record give the unequal finite distribution or mean formula, the ordinary-transform regeneration identity, and a general catastrophe bound. Older ordinary coupon-collector work already implies the qualitative fact that uniform probabilities are extremal under majorization, so that qualitative subclaim is not treated as new here. What survives as original is the uniform balanced-profile saddle/prefactor, the profile rate functional, the explicit derivative/alpha asymptotic yielding the sharp n-times-success Kolmogorov rate, and the quantitative exponential heterogeneity penalty; no source inspected covers that package.

### Equivalent formulations

No equivalent formulation of the full balanced-profile theorem was located.

### Broader coverage

These sources provide the ingredients and one qualitative corollary, but none dominates the profile-level asymptotic and explicit alpha evaluation.

### Exact database or table

No independent database/table contained the stated saddle, derivative, and rate data.

### Claim versus prior implication

The central profile asymptotic and sharp specialized error rate are not mechanically stated by a single prior theorem; they require the model-specific asymptotic analysis performed here.

## Value — PASS

A profile-level rate and prefactor for balanced nonuniform coupons, together with a sharp model-specific exponential-approximation rate and a quantitative heterogeneity penalty, resolves a natural recent direction rather than an arbitrary finite slice. The already-known qualitative uniform-extremality component does not carry the value judgment by itself.

## Sources inspected

- Coupon Collector Problem with Reset Button — https://doi.org/10.3390/math12020239. PARTIAL_COVERAGE: Covers finite unequal distributions and equal-probability asymptotics, not the balanced nonuniform profile saddle.
- Generalized analysis of the coupon collector problem with reset button — https://doi.org/10.3934/math.2026800. PARTIAL_COVERAGE: Gives an explicit general mean formula but not the balanced-profile Laplace asymptotic or sharp Kolmogorov specialization.
- On Completion Times under Memoryless Catastrophe — https://arxiv.org/abs/2609.16566. COVERING_INGREDIENT: Supplies the general approximation theorem but leaves the nonuniform coupon-specific p and alpha evaluation to be done.
- Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors — https://arxiv.org/abs/2605.14511. COVERING_INGREDIENT: Supplies the regenerative viewpoint and qualitative limits, not the balanced profile prefactor/rate.
- Some upper and lower bounds on the coupon collector problem — https://doi.org/10.1016/j.cam.2005.12.011. PARTIAL_COVERAGE: Implies qualitative uniform extremality after applying the decreasing transform, but not the quantitative reset heterogeneity exponent or other main asymptotics.

## Checked sources

- https://doi.org/10.3390/math12020239
- https://doi.org/10.3934/math.2026800
- https://arxiv.org/abs/2609.16566
- https://arxiv.org/abs/2605.14511
- https://doi.org/10.1016/j.cam.2005.12.011
- Resultary semantic search for the full balanced-profile claim

## Residual risks

- Older saddle-point or restart literature under different terminology could contain an equivalent profile asymptotic.
- Full text of the very recent Wang-Lu and Long preprints was not retrievable through the current web interface; their abstracts and the record's exact imported formulas were checked.

## Limitations

- Reset probability is fixed strictly between zero and one.
- Coupon weights remain uniformly of order one over n; rare-tail and moving-reset regimes are outside scope.
- Only first-order Laplace asymptotics are claimed.
- The qualitative Schur extremality is not new in essence; the audit's originality judgment rests on the quantitative/profile results.
