# Self-review

## Correctness — PASS

The defining SOFIM algorithm reduces exactly, by scalar Sherman–Morrison inversion, to a regularized rational momentum update with the printed first-moment correction. The sign-symmetric limiting two-cycle has a unique positive amplitude; its Jacobian is the same at both phases because the scalar update derivative is even. All three quadratic Jury inequalities have explicit rational expressions, giving the sharp strict stability window. The actual nonautonomous source-initialized iteration is controlled by a weighted-sup contraction with certified derivative bounds and an exponentially decaying bias-correction disturbance. This provides a genuine infinite-time proof and explicit uniform rate, not an extrapolation of a finite simulation.

Scientific limit: the sharp phase criterion concerns sign-symmetric cycles of the limiting map; the actual source-initialized geometric-attraction theorem is restricted to the stated quantitative subfamily and interval.

## Originality — PASS

The full defining SOFIM manuscript specifies the rank-one Fisher inverse, bias correction and parameter update, and discusses a borrowed approximate-Newton guarantee, but does not state this sharp two-cycle phase boundary or nonminimizing source basin. Bock–Weiss establish related nonconvergent Adam cycles on quadratics; this is important prior art, but Adam has a distinct accumulated squared-gradient state, and its period-two statements do not imply SOFIM's closed Fisher-momentum Jury formulas or quantitative bias-corrected basin. Ye–Luo–Zhang analyze approximate Newton maps subject to Hessian approximation controls, and do not cover arbitrary rank-one Fisher preconditioning or momentum periodicity. Focused literature and indexed-result comparisons found no implication-equivalent SOFIM theorem.

Residual originality risk: unpublished or unindexed optimizer dynamical-systems analyses could already contain the same SOFIM-specific calculation. Lack of a found match is not independent proof of novelty.

## Value — PASS

The central design feature of SOFIM is a regularized rank-one Fisher preconditioner coupled to bias-corrected momentum. The result identifies an exact nontrivial stability phase and proves failure to optimize a strongly convex Gaussian-location negative log likelihood from an **open interval of source initializations**, with an explicit persistent objective gap and geometric attraction to an alternate state. This distinguishes intrinsic constant-step nonlinear optimizer dynamics from stochastic noise, numerical singularities, and mere one-step overshoot; it directly informs Fisher-regularization and learning-rate calibration.

Self-review: passed. Independent audit: not yet performed.
