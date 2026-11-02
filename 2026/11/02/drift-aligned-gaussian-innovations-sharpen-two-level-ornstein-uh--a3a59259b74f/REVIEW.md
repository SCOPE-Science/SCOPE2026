# Scientific review

## Correctness

**PASS.** The two Euler recurrences and each coupled marginal are derived in RESULT.md. Exact covariance expansion yields the displayed finite-\(m\) gap; Cauchy–Schwarz proves uniqueness within the specified block-local coupling class, and uniform small-step expansions justify both limiting constants. The standalone standard-library verifier confirms 624 finite rational/numerical identities and limiting rates, including the rational strict witness. Finite checks corroborate rather than replace the proof. Risk: every claim requires the stated independent-block locality and positive coarse multiplier \(b>0\).

## Originality

**PASS (qualified).** The 2021 preprint of Chada et al., inspected in its published open-access full HTML, develops strong diffusion coupling for exponential Euler SPDE integrators, using the exact semigroup-weighted stochastic convolution; it does not state a normalized, variance-optimal coarse increment for two explicit Euler steps, or the displayed scalar finite-horizon formula. Jourdain–Kebaier analyze Euler schemes on the same Brownian path and nonasymptotic error bounds rather than optimization over admissible block-local couplings. Targeted external and mathematical-record searches compared OU/Euler, same-noise/transport, and coarse/fine normalized Gaussian innovation formulations; no implication or stronger coverage was identified. The elementary maximal-covariance principle is acknowledged as prior mathematical knowledge. Residual risk: an unlocated note may have applied that principle to this exact OU Euler pair; priority has not been independently certified.

## Value

**PASS.** The coupled correction is a fundamental computational component of MLMC; this modification preserves both Euler marginals and the telescoping estimator while changing no random-number budget. The exact universal finite-grid improvement, unique block-local optimality, and factor-greater-than-three asymptotic variance reduction after one relaxation time are concrete, nontrivial quantitative consequences. The scope is deliberately narrow; nonlinear payoff or cross-block optimal transport requires separate analysis.

Self-review: passed. Independent audit: not yet performed.
