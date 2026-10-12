# Self-review

## Correctness — PASS

The proof uses only constrained first-order optimality, the squared-radius identity, and explicit witnesses. For every locally feasible point the linear model gap bounds squared distance by \(\mu/2\); this proves the absolute certificate and uniqueness of the exact oracle. One-dimensional order gives an exact equality between the relative model gap and the error ratio, while a two-dimensional halfspace gives admissible \(\eta\)-relative points whose distance ratio tends to 2. The triangle bound establishes the upper endpoint. The equality example for the absolute gap verifies the optimal constant. Exact rational checks supplement, but do not replace, these arguments.

## Originality — PASS, with residual risk

The closest preprint, Richtárik--Gruntkowska--Li, arXiv:2605.08850v2, proves its sharp ideal-radius contraction only for **exact** local linear minimization and notes the need for an inexact-oracle analysis of approximate master/pricing solutions. Its Appendix B.7 compares the exact trust-ball subproblem of Ferris--Zavriev with Garber--Hazan's relaxed oracle, which changes the admissible radius while retaining a no-worse-than-exact-original-ball model value. Neither implies the displayed positive relative-gap worst-case classification. Actual published-research similarity searches for the relative-gap/dimension formulation and source-title/alias searches found nearby but not covering results. The later projection-interpretation preprint arXiv:2609.33383 was available by abstract only, and the 2016 relaxed-oracle paper only by publisher abstract and the full comparison in the 2026 source. These are material residual originality risks, not proofs of noncoverage.

## Value — PASS

The complete sharp \(0\)/\(\eta\)/\(2\) dimension taxonomy identifies a genuine breakdown in a recently studied exact one-step benchmark and isolates active normal components as the cause, even for perfectly conditioned quadratics. The optimal absolute-gap certificate provides an explicit replacement accuracy scale. The theorem is one-step and does not claim convergence or implementable knowledge of the solution radius.

Self-review: passed. Independent audit: not yet performed.
