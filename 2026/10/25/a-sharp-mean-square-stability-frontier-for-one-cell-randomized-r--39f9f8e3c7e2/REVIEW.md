# Scientific review

## Correctness — PASS

Direct substitution into the published delayed-stage update produces the three-state random companion matrix. Exact conditional covariance calculation yields a rank-one perturbation of the deterministic midpoint Lyapunov map. A cubic Jury calculation classifies mean dynamics, and the exact transfer-function identity reduces the second-moment boundary to a strictly monotone degree-seven crossing. The positive-definite adjoint eigenmatrix verifies nondecay and geometric divergence for nonzero deterministic starts. The bundled independent rational checker passed 239 reconstructions and identities, supplementary to the complete proof.

## Originality — PASS, with priority uncertainty

The 2024 delay-integrator article treats finite-time convergence and specifies the source method. The closer 2020 randomized Runge–Kutta stability paper treats a scalar *ordinary* differential equation, not this delayed companion. Published nearby delay-stability and random-sampling results use materially different equations and noises. No direct covering statement emerged in targeted mathematical-record and literature searches, but broader stochastic recurrence results or insufficiently inspected papers may contain equivalent formulations. Full/partial material inspected and specific risks are documented in AUDIT.json.

## Mathematical value — PASS

A canonical pure-delay scalar benchmark has a sharp algebraic mean-square stability frontier, not merely a sufficient timestep restriction. The strict interval between mean and mean-square stability persists at the rational parameter \(z=7/6\) and isolates a practical question about long-time reliability of one-cell randomized delay integration. The source article does not resolve this coarse-step infinite-horizon question.

## Limits

Scalar pure-delayed linear feedback, one cell per lag, independent uniform stages, exact arithmetic, no claims for multi-cell methods or nonlinear delays. Publication priority requires independent verification.

Self-review: passed. Independent audit: not yet performed.
