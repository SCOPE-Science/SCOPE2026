# Same-model review

## Correctness
PASS. The center coefficients follow exactly from the two-by-two even-moment normal equations. Minimization over the bounded nonnegative data cube is a linear-program vertex calculation, so the defect is exactly the total negative coefficient mass. The sign cutoff is determined by one quadratic inequality, giving the closed formula. Exact rational evaluation handles \(m\le27\); an analytic integral bound with monotone auxiliary factors proves the uniform tail for \(m\ge28\). The asymptotic follows from the explicit cutoff and a Riemann-sum limit. The packaged checker independently replays all rational identities and the positive witness.

## Originality
PASS with explicit residual risk. The original paper already tabulates the signed smoothing coefficients, and later literature explicitly warns of overshoot, phase reversal, ringing, and negative excursions. Those qualitative facts are treated as prior work. Searches under positivity preservation, negative coefficient mass, kernel \(\ell_1\) norm, least-squares smoothing, and exact overshoot did not locate the all-window minimax formula, the unique seven-point global maximum, or the nonzero infinite-window limit. The closest 1983 pitfalls paper could not be inspected in full text after lawful open and institutional attempts, so an equivalent calculation there remains a named risk.

## Value
PASS. Positivity of bounded measurements is a basic shape constraint, and quadratic/cubic Savitzky--Golay smoothing is one of the canonical least-squares filters. The result converts a familiar qualitative warning about negative weights into an exact deterministic robustness profile over every odd window. The seven-point global maximum, explicit strictly positive counterexample, and persistent large-window defect are directly useful as regression tests and as quantitative guidance when positivity preservation matters.

Same-model review: passed. Independent audit: not yet performed.
