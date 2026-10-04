# Review

## Correctness

PASS. The stationary representation
\[
(A,R)=(UL,(1-U)L)
\]
with \(U\) uniform and independent of the size-biased interval \(L\) gives exact mixed moments. The covariance splits into a nonnegative comonotone scale term and a negative uniform-split term. The transformed variances split analogously.

Those decompositions give the lower endpoint by discarding nonnegative scale variance and covariance, with equality only for deterministic \(L\). They give the strict upper endpoint by discarding the negative mean product and retaining only the common-scale covariance, followed by Cauchy--Schwarz. A rare-large two-point size-biased interval makes both mean penalties negligible and has perfect correlation between its two powers, proving sharpness of the upper endpoint. Continuity of the two-point family fills the interval.

## Originality

PASS. The full Nair--Sankaran paper was inspected. It gives the stationary Schur-constant joint law and the ordinary linear correlation formula, but no unequal-power range.

The closest published theorem gives the sharp range only for equal powers \(\operatorname{Corr}(A^r,R^r)\) and explicitly lists unequal powers as outside its scope. Its one-ratio reduction depends on the equal transformed variances and does not imply the asymmetric result.

Targeted semantic and web searches for mixed powers, unequal powers, stationary renewal correlation, and Schur-constant power transforms did not return the two-parameter endpoint formulas.

## Value

PASS. Unequal transforms are natural in asymmetric reliability and renewal summaries, where elapsed time and remaining time need not be measured on the same scale. The theorem completes the sharp distribution-free correlation picture beyond the diagonal equal-power case and identifies exact extremizers with a simple probabilistic mechanism: deterministic spacing maximizes the negative split effect, while rare large intervals make common-scale variation dominate.

Same-model review: passed. Independent audit: not yet performed.


Replay: `VERIFY_OK random_bound_checks=33471 deterministic_endpoint_checks=42 upper_path_checks=42`.
