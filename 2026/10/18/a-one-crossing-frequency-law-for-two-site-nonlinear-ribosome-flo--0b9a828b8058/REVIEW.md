# Self-review

## Correctness — PASS
The two-site adjugate formula is an exact identity in any real \(2\times2\) matrix, and the denominator is positive for every \(\omega\geq0\) because the equilibrium Jacobian is Hurwitz. Combined with Zhou's already-proved symmetric Jacobi second variation, it yields an affine numerator in \(\omega^2\) and hence the rigorous one-crossing bound. The analytic example has strictly monotone hindrance (a global derivative bound); exact flux, Hessian, Jacobian, and rational-response calculations establish the sign switch and the unique positive maximizing frequency. The smooth periodic fixed-point theorem and a half-period symmetry yield the \(O_\omega(\varepsilon^4)\) error. Exact checks are reproducible in `verify.py`; finite integrations are only corroboration.

## Originality — PASS, with residual priority risk
Zhou (arXiv:2610.10602v1, Sections 2 and 5) already proved the existence, attraction and general Jacobi second-variation formula, and those are cited as prior. Neither its source text nor the accessible related literature states a **uniform at-most-one frequency-crossover classification with a single harmonically modulated rate**, nor the analytic example that attains the bound and has an exact optimum. The statement is not equivalent to the source's eigenvalue existence criterion for arbitrary rate perturbations: that criterion does not restrict a prescribed single input as \(\omega\) changes. The proof adds the two-dimensional frequency-resolvent classification, and the realization demonstrates sharpness. Still, the adjugate argument is elementary and could be implicit in earlier frequency-domain response theory; this is recorded as a genuine risk rather than claimed novelty certainty. Related full-text access was incomplete for arXiv:2608.15214.

## Mathematical value — PASS
Frequency selection is a natural quantitative control question for transport efficiency. The theorem prohibits reentrant gain/loss/gain transitions at weak amplitudes for **every** two-site admissible nonlinear-hindrance chain under one-edge harmonic driving, and identifies the only possible crossover frequency from local equilibrium data. The explicit strictly monotone analytic realization proves the bound cannot be improved and identifies a unique maximum gain frequency. These are structural restrictions, not a numerical single-parameter value or a renamed corollary.

## Scope and risk
The theorem only concerns the quadratic gain at fixed frequencies under a single harmonically driven rate. It does not constrain higher-order amplitude response at a quadratic zero, multi-tone input, independently modulated edges, or larger chains. The example's hindrance is mathematical, not experimentally fitted. The highest originality risk is implicit treatment by general second-order frequency-response methods, especially outside the narrower RFM literature.

Self-review: passed. Independent audit: not yet performed.
