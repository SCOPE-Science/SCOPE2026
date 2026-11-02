# Self-review

## Correctness
PASS. Positive definite five-hat Gram matrix, exact inverted nodal rows, opposite-sign affine absolute integrals, convexity of the kernel-row integral between knots, and exact branch-difference identities derive the whole domain of the formula. A positive polynomial derivative proves the unique minimax knot balance. `check.py` independently exercises symbolic identities and 533 quadrature/interior checks; experiments are not used as proof.

## Originality
PASS on inspected evidence, subject to a specialist-literature priority risk. Kayumov (arXiv:math/0408418, particularly introduction 1.2–1.3) states the classical universal sharp bound three for arbitrary linear spline knots and studies generalized exponential/trigonometric splines, not this exact five-knot profile. Oswald (arXiv:math/0611573, sections 1–3) proves a different higher-dimensional unboundedness result. A two-periodic knot projector result does not dominate a finite knot-cluster calculation. Web and research-record semantic searches for the exact formulas, alternate terminology, limits, and radical found no direct equivalent. The complete 1979 Oskolkov specialist paper was not inspected; any exact parameterized configuration there could alter priority.

## Mathematical value
PASS. For a standard least-squares finite-element space, knot placement materially changes the sharp maximum-norm stability from below two to above two. The new complete one-parameter stability profile, unique optimum, exact pointwise extremizers, and two distinct singular clustering limits answer a natural mesh-design question in a setting with a classical universal bound of three.

## Limits
Only symmetric distinct five-node continuous linear splines with real Lebesgue measure. No claim of optimality among arbitrary meshes, no higher-degree results, and no independent review.

Self-review: passed. Independent audit: not yet performed.
