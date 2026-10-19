# Scientific review

## Correctness — PASS
The sketched harmonic projection is reduced to the scalar generalized Rayleigh quotient defined in the motivating source. Orthogonal Gaussian decomposition produces an exact shifted Student distribution for its reciprocal; the density at zero is positive for every finite sketch size. This proves the two sharp one-sided tails and the \(p=1\) moment boundary. Conditioning on nonzero bounded sketch norms leaves a positive Gaussian density at the pole. A standalone numerical verifier reconstructs the quotient directly and tests the formulas, without being used as a substitute for their proofs.

## Originality — PASS, qualified
Burke–Güttel–Soodhalter's Section 3.5 constructs the sketched harmonic Ritz problem and singular-value stabilization but does not state the reciprocal-Student or divergent-first-moment laws. The related papers on sketched Ritz values and sketched FOM use different projected quantities and give no such harmonic one-vector law. Known Student ratios and analogous Gaussian-Galerkin pole mechanisms supply a short proof pathway; the new scope is the exact sketched harmonic Ritz eigenvalue, its separate signed tails, and persistence under norm-only sketch screening. Equivalent derivations in wider Gaussian generalized-Rayleigh-quotient literature remain possible. Search absence is not proof of uniqueness.

## Value — PASS
Harmonic Ritz values guide which information is recycled in deflated iterative linear solvers. The result explains why an apparently stable one-column sketch singular value, even when screened into a compact positive interval, does not ensure integrability or positivity of the extracted eigenvalue. The exact signed tail constants, all-sketch-size moment threshold, and conditional persistence delimit what guarantees may safely be stated without an inner-product or angle safeguard. It does not assert instability of a whole solver.

## Scope and sources
Original algorithm and equations: arXiv:2311.14206, Section 3.5. Related matrix-function projection: arXiv:2208.11447, Section 2. Related spurious Ritz-value analysis: arXiv:2306.06481, Sections 1, 6–7. Classical Student distribution is treated as known, not claimed as a new probability law. The sole new claim is the mathematical classification of the sketched harmonic Ritz estimate in the stated model.

Self-review: passed. Independent audit: not yet performed.
