# Review

## Correctness

PASS. Conditioning on the median of a continuous three-sample makes the lower and upper observations independent draws from the lower and upper truncations. In quantile coordinates this gives the exact tail-mean formulas (8)--(9). Central symmetry fixes the intercept, and the affine regression becomes the integral equation (10).

Differentiation gives the first-order ODE (11), whose solution is the displayed power quantile. Monotonicity supplies the sharp threshold \(a\ge\frac12\); negative slopes are excluded by first-moment divergence. Direct integration of the candidate quantile proves sufficiency. The tail exponent follows from inversion of the endpoint quantile asymptotic.

## Originality

PASS, with a bounded residual risk from the extensive order-statistic characterization literature. The closest full primary source studies the same conditional midrange object with identity regression and explicitly flags the affine \(a x+b\) replacement as an interesting extension. Its symmetric identity case is the single point \(a=1\), not the slope-indexed family proved here.

The closest related sample-mean and later Student-\(t_2\) regression papers inspected use identity regressions or different order-statistic functionals. Targeted searches for affine midrange, symmetric midrange-median regression, and equivalent quantile formulations did not locate the claimed slope family.

## Value

PASS. The result closes a natural affine extension explicitly raised in the foundational midrange-characterization paper, under the canonical central-symmetry restriction. It gives a structural classification rather than an isolated example: the regression slope becomes a tail-shape parameter, with a sharp bounded-support boundary and a classical Student distribution as an interior landmark.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK ode_checks=28 identity_checks=56 conditional_regression_checks=56 monotonicity_checks=45`.
