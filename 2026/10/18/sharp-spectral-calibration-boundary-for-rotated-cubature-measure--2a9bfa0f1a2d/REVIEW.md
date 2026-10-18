# Scientific review

## Correctness — PASS

Direct sign-pair evaluation of the standard degree-three cubature rule gives the estimated scalar variance and cross covariance without approximation. The Gaussian fourth-moment identity fixes the exact innovation variance. Cauchy–Schwarz, an inductive equal-diagonal basis construction and the Frobenius diagonal/off-diagonal identity yield both sharp extrema; connectedness gives all intermediate values. The exact affine-update covariance identity determines the sign and equality cases. The standalone checker tests signed sigma-point summation, the constructive extrema and threshold examples, while the stated infinite conclusions have analytic proofs.

## Originality — PASS, subject to residual literature uncertainty

Classical cubature nodes, their covariance formulas, fourth Gaussian moments, orthogonal rotation sensitivity, and general covariance-compensation observations are prior work. Singh (2017) studies rotated points, and Jiang et al. (2026) already illustrate CKF rotation sensitivity and give general per-frame moment and error-covariance formulas. The assessed additional result is the **complete exact interval optimized over all covariance-square-root frames**, its necessary-and-sufficient trace/Frobenius transition for both confidence signs, equality characterization, and the unbounded fixed-reported-covariance family. The general earlier formulas alone do not state these extrema or their simultaneous attainability; their combination with classical matrix inequalities is acknowledged. Indexed mathematical record searches and accessible previous claims yielded no direct full-claim duplicate. This is not an independent priority certificate, and an unindexed corollary or specialized earlier calculation remains a risk.

## Value — PASS

Covariance-square-root choices represent exactly the same Gaussian prior but can lead to incompatible filter confidence reports. The classification identifies which quadratic sensors admit calibrated frames and which necessarily have one-sided bias; the transition depends on a natural, basis-invariant spectral ratio. The unbounded error gap shows substantive consequences beyond a harmless change in a moment estimate. It is a natural complete classification of a filtering benchmark, not an arbitrary numerical slice.

## Scope and risks

The comparison uses the actual **unconditional mean-squared error covariance of the cubature updated mean**, not conditional posterior variance. All claims apply to an unmodified one-step rule and exact arithmetic. Related later work explicitly establishes orientation dependence, so only the sharp spectral classification is assessed as additional. Published equivalents not located by the searches remain possible; independent review is outstanding.

Self-review: passed. Independent audit: not yet performed.
