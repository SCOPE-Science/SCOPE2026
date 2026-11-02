# Scientific review

## Correctness — PASS
The stationary generator is reconstructed for each protocol. A strictly invertible cycle resolvent fixes the two stationary spin-pair kernels, and the memory-minus-fresh term is the negative rate derivative of a normalized Green kernel. Monotonicity of \(t\mapsto t\tanh(at)\) establishes positivity for every finite cycle size, distance and positive rate. Hyperbolic expansions at \(r=\lambda/N^2\) give a strictly positive subleading wall coefficient. The independent exact-rational full-generator tests and numerical asymptotic tests are documented in VERIFICATION.md. No numerical limit is treated as an infinite proof.

## Originality — PASS (best knowledge; publication priority unverified)
Grange (2022) already treats the quenched-original-opinion model and its infinite-lattice correlations. Pymar–Rivera (2021) already treat fresh noisy-voter correlations on finite graphs and the scale of the cycle transition. The proposed claim is the joint strict all-parameter comparison of different protocols and its exact finite-ring subleading wall correction, not the underlying dynamics, Green kernels, or leading diffusive scale. Actual semantic database queries and relevant primary sections found no dominating statement. Existing general resolvent theory and unlocated treatments of finite graphs could still imply this specialization; external priority audit remains needed.

## Mathematical value — PASS
Original-opinion memory and independent refresh are physically distinct interventions with identical local clock rates. The strict inequality determines the sign of memory's effect without parameter exceptions, and the sharp finite-size coefficient demonstrates an observable distinction that disappears at leading-order hydrodynamic scaling. This solves a natural finite-volume comparison and boundary-correction problem, rather than merely changing notation for known formulas.

## Limits and remaining risks
Only annealed fair spins, symmetric nearest-neighbor copying and homogeneous local resetting are proved. Conditional environment order and universality beyond cycles are not established. Priority remains unverified against all broader related results.

Self-review: passed. Independent audit: not yet performed.
