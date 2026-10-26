# Scientific review

## Correctness — PASS

The stochastic saddle-point equations reduce to two independent scalar backward-Euler recurrences, with noise entering the right-hand side before the implicit solve. Exact geometric summation gives their covariance. Both deterministic step-doubling errors are strictly positive. The two-Gaussian Bhattacharyya objective is strictly convex in the logarithm of the common variance scale, so its geometric-mean optimum and hyperbolic-cosine minimum are global and unique. Fixed-final-time expansions establish the nonzero limiting mismatch. The derivative of the mode calibration function has exactly one positive zero, proving the paired-rate resonance classification. The accompanying exact-fraction/high-precision verifier returned `VERIFY_OK 894`; it is not a substitute for the analytical arguments.

## Originality — PASS (best-knowledge assessment)

The probabilistic Euler step and componentwise Bhattacharyya calibration were introduced previously and are not claimed as new. The closest primary sources are Altmann–Moradi (arXiv:2406.07220, Sections 4.1, 5) and Conrad et al. (doi:10.1007/s11222-016-9671-0, Section 3.1). Their inspected material does not state the exact two-mode, one-scalar terminal frontier; the limiting spectral shape, sharp nonzero gap and unequal-rate matching resonance require this problem-specific calculation. Public mathematical searches and research-record comparisons did not identify an equivalent claim. The main residual risk is that a general classical Gaussian variance-scale formula, combined with standard Euler error expansions, may already be known in another guise. The broader covariance choice in the older work is fully acknowledged and does not contradict the restricted theorem.

## Value — PASS

A widely used scalar calibration aims to match numerical uncertainty with step-refinement error. The theorem proves that this can fail by an explicit, positive amount **even though both variances themselves vanish**. It quantifies the best achievable fit rather than just observing anisotropy; moreover, its strict spectral unimodality identifies precisely when different relaxation modes unexpectedly share an asymptotic scale. This is a motivated boundary for calibration design in constrained probabilistic integration, not a claim about arbitrary perturbation covariances or unconstrained nonlinear problems.

## Limitations and literature

Applies only to a fixed two-mode diagonal, positive, linear problem and the specified isotropic kernel forcing, with the terminal-time portion of the calibration objective. The full-trajectory optimum can differ, while its objective retains the terminal lower bound. A mode-specific noise covariance can remove the obstruction. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
