# Self-review

## Correctness — PASS

For the normalized oscillator, a midpoint update is exactly the planar Cayley rotation through \(2\arctan(\omega H/2)\); each update preserves the quadratic energy. The second complex angular harmonic encodes precisely the traceless uncentered second-moment matrix, so zero expected harmonic is necessary and sufficient for universal one-step isotropy. The identity
\[
t-\tfrac12(1-\Re Z(t)-\Im Z(t))=\frac{t(t-1)^2(t^2+2t+3)}{(1+t^2)^2}\ge0
\]
proves the global mean bound over arbitrary nonnegative, integrable timestep laws. Its exact zeros prove uniqueness of the minimizer. The quarter-turn construction achieves every strictly larger mean, and semicircle separation proves the maximum-step boundary. Exact symbolic checks are supplied; nonstandard infinite-law conclusions rely on this proof, not simulation.

## Originality — PASS, with residual risk

The primary random-time Runge--Kutta source proves preservation of quadratic invariants and asymptotic error results; its inspected Sections 2, 6, 7 and 9.5 do not establish a universal sharp mean-duration constraint for one-step second-harmonic cancellation. The related HMC jittering paper studies autocorrelation and acceptance with a different integrator, and a related harmonic Langevin analysis concerns stochastic-force stationary bias. Previously published random-step symplectic Euler behavior concerns mean-square energy instability, while the present Cayley midpoint energy is conserved pathwise. The result is formulated as a sharp optimization over all nonnegative timestep laws, not merely as a Fourier calculation for a chosen law. The possibility of an independently published equivalent extremal moment inequality remains an originality risk.

## Value — PASS, with appropriate scope

Exactly isotropic second moments on a harmonic energy shell form a natural benchmark for geometric probabilistic integration, ensemble dephasing and phase-bias control. The theorem gives a sharp feasibility threshold in mean simulated time, the unique optimal distribution, a constructive law for every feasible strictly positive mean, and a separate maximum-step barrier. These are informative design constraints and an exact boundary between feasible and impossible second-moment dephasing, rather than an arbitrary parameter slice. This is a coarse-step benchmark, not a theorem on approximation error or on generating uniform energy-shell samples.

## Closest literature and limitations

Abdulle--Garegnani, arXiv:1801.01340; Christiansen--Errica--Alesiani, arXiv:2309.13593; published harmonic Langevin covariance analysis, *Harmonic equilibrium bias and a one-gradient covariance obstruction for randomized ULMC* (2026). The stochastic targets and integrators differ in the latter two cases. Residual risk concerns unindexed phase-mixing and quadrupole-cancellation results. The present result assumes a planar linear oscillator, exogenous iid steps for multi-step persistence, and finite mean; it does not imply phase-space distributional uniformity or trajectory accuracy.

Self-review: passed. Independent audit: not yet performed.
