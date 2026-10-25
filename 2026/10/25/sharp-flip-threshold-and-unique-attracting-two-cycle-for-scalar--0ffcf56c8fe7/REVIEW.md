# Scientific review: scalar Soft Muon period-two transition

## Correctness — PASS

The recurrence is the one-dimensional specialization of the source's normalized momentum and soft-sign update, without substituting the practical Newton–Schulz polynomial. At the unique equilibrium, the Jacobian has determinant \(\beta\) and trace \(1+\beta-c(1-\beta)\); the strict real Schur inequalities give the exact hyperbolic boundary. The period-two classification does not assume symmetry: the two momentum relations and injectivity of the odd soft-sign force zero mean and then a unique nonzero amplitude. Both cycle Jacobians have the same reduced effective coefficient \(8/(c^2t^3)\), which lies strictly inside the Schur region for every supercritical ratio. At equality, center-manifold coordinates produce the nonzero cubic coefficient \(t\), proving attraction and the stated \(n^{-1/2}\) law restricted to nontrivial local center orbits.

Reproduction was performed using the packaged standard-library `verify.py`, with 63 parameter configurations, 3,000 Jacobian comparisons, seven critical-cubic algebra configurations, four 40,000-step critical-rate experiments, and the exact illustrative cycle. These finite checks supplement rather than replace the mathematical proof. The local nature of the stability assertions and the center-manifold restriction are substantive.

## Originality — PASS with residual historical-priority risk

The full accessible source text of arXiv:2609.30546v1 defines the exact update and proves sufficiently small-step convergence, but its theorems and appendices do not state a sharp scalar momentum-dependent threshold or uniqueness and attraction of every primitive two-cycle. arXiv:2605.23871v1 obtains regularized Hamiltonian and sufficient small-step discrete convergence results, not the same complete fixed-step classification. arXiv:2602.11948v1 concerns hard/polynomial polar maps and perturbed signs, not this saturating soft-sign map. arXiv:2510.11312v1 concerns other sigmoid preconditioners and sufficient convergence. Compared public exact-model results involve discontinuous Signum, a fourth-root Polar Express surrogate, and momentum SAM; their distinct nonlinearities give different cycles and do not logically contain the present theorem. Focused indexed searches found no equivalent statement, but priority cannot be guaranteed by a negative search.

## Mathematical value — PASS

The threshold is a sharp hyperparameter rule valid for every allowed constant momentum, improving on generic small-step sufficiency. The theorem additionally counts all primitive two-cycles, derives their physical amplitudes, proves attraction rather than merely exhibiting numerical oscillations, and quantifies the critical transient. It exposes a concrete regularization-induced change from the neutral continuum of hard-sign cycles to a unique attracting soft-sign cycle. These properties address a motivated stability question in numerical optimization, rather than an arbitrary scalar invariant.

## Limitations and closest literature

The result is **not** a global basin theorem, does not classify higher-period orbits, and does not apply directly to practical finite-degree Newton–Schulz Muon or stochastic/matrix settings. Its center-manifold critical-rate assertion excludes the strong-stable exceptional direction. Closest works include arXiv:2609.30546v1 (defining method), arXiv:2605.23871v1 (regularized Hamiltonian viewpoint), arXiv:2602.11948v1 (quadratic hard/polynomial Muon), the published scalar Signum neutral-cycle calculation, and the published fourth-root Polar Express flip calculation. Independent assessment of historical priority and proof details has not occurred.

Self-review: passed. Independent audit: not yet performed.
