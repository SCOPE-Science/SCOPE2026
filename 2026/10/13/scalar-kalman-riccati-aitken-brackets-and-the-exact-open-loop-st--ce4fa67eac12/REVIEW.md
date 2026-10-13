# Self-review

## Correctness
PASS. The scalar Kalman covariance map is Möbius with one positive and one negative fixed point. Cross-ratio conjugation makes the iteration exactly geometric, and a direct three-point calculation shows that Aitken squares the one-step projective error. For \(|a|\le1\), the first raw covariance lies beyond the fixed-point midpoint, forcing every squared projective coordinate into \((0,1)\) and hence every Aitken extrapolate strictly above the stabilizing covariance. The unstable counterfamily gives a negative first extrapolate for every \(|a|>1\). The embedded verifier checks the symbolic identity and exact examples.

## Originality
PASS. The closest full-text Kalman source develops projective Riccati geometry and recalls monotone convergence, but contains no Aitken discussion. A 2026 paper applies Aitken to a different nonsymmetric transport-theory Riccati equation; only abstract/reference material was accessible, so it remains a stated comparison risk rather than evidence of whole-document noncoverage. Targeted searches combining Kalman covariance, scalar Riccati, Möbius/cross-ratio, Aitken/Delta-squared, and steady-state brackets found no implication-equivalent statement.

The main residual risk is older scalar Riccati or continued-fraction literature using different terminology.

## Value
PASS. The result produces a computable two-sided certificate for the steady scalar Kalman covariance using only three ordinary Riccati iterates, with exact projective interpretation. The sharp unstable-side counterexample also shows when the same numerical accelerator can output an impossible negative covariance, making the boundary relevant to safe numerical filtering.

## Closest literature and limitations
Carli--Sepulchre supplies the closest projective Riccati framework. Han--Zhang verifies primary MSC \(93\mathrm E11\) for Riccati-based filtering. Xie--Ma--Li is the closest Aitken--Riccati comparison but concerns a different equation and was only partially accessible. The theorem is scalar, lower-start, and exact-arithmetic; matrix Riccati equations and recursively fed extrapolates are not classified.

Self-review: passed. Independent audit: not yet performed.
