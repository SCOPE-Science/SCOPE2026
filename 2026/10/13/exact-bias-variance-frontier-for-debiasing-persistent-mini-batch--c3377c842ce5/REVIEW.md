# Self-review

## Correctness

PASS. Conditioning on the iterate reduces the source sampling rule to simple random sampling without replacement from the complement of the fixed persistent set. The finite-population second moment is derived directly from first- and second-order inclusion probabilities. Both source estimators are affine functions of the same fresh sample mean, so the bias, variance, interpolation MSE, and threshold formulas follow exactly. The MSE is a strictly convex quadratic whenever the fresh-sample variance is nonzero, and its derivative at full correction is positive.

## Originality

PASS. The primary full text was inspected at its bias calculation, unbiased correction, practical warning, and convergence assumptions. Published-research searches and broader finite-population and stochastic-gradient variance literature were compared at the statement level. No inspected source gives the source-specific variance multiplier, persistent-versus-complement MSE threshold, or the exact partial-debiasing optimizer.

A residual risk is an equivalent generic shrinkage identity in older survey-sampling literature; the source-specific application and \(50\%\)-overlap consequence were not located.

## Value

PASS. The result directly quantifies a tradeoff that the primary source identifies as practically important but leaves analytically unresolved. It shows when the convergence-oriented correction is worth its variance cost and provides a precise intermediate design target rather than an all-or-nothing bias correction.

Self-review: passed. Independent audit: not yet performed.
