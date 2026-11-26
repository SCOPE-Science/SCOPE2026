# Independent mathematical audit

## correctness

PASS

Reconstructed (1)–(4) from the q-step sign itinerary. For x in a compact subinterval of (0,1/q), the reference orbit visits x+j/q for p−q≤j≤p−1, each once, with exactly p positive visits. At the critical centers the true visits differ by O(ε) over the fixed q steps; the nearest negative and positive tails are −ε exp(y) and +ε exp(−y), with errors O(aε²), and all others are O(ε³). The q detunings sum to 2εξ. The product of derivatives gives 1−2aε cosh(y)+O(a²ε²), hence the unique fixed point in a compact scaled bracket is attracting and has the stated phase and multiplier. The q distinct visited cells give primitive period and exactly one phase of that cycle in (0,1/q), not global uniqueness of cycles. The scaled update is an Euler step with an O(h_a²) perturbation; on compact forward time intervals an inward-pointing bracket and the Lipschitz error recursion give uniform O(h_a) trajectory error, including time rounding. For the outer positive sign, the visit at x−1/q dominates with tail −d exp(z−aτ) at phase 1/q−τ+(log d+z)/a; the nearest positive site is farther by 1/q−2τ>0. The increment is d exp(−aτ)(1−exp(z))+o(exp(−aτ)), with multiplier 1−ad exp(z−aτ)(1+o(1)). The negative sign interchanges the near sites and gives exp(−z)−1 instead. These opposite endpoint signs and monotonicity give a zero with z→0, including q=2. Constants are for fixed p,q and the stated parameter ranges. The inspected CHECKS.txt reports 12 central and 16 outer finite tests; they were not rerun and do not establish the limits.

## originality

PASS

Credit the prior rational attraction and fixed-resonance half-grid calculation. The October 27 finding adds uniform detuning, the driven slow-time evolution, and a distinct signed outer law. Two later Resultary records substantially overlap the critical calculation, and the later general return expansion also implies the slow flow by Euler stability for its q range; they are not evidence of prior coverage at the date of this finding. No prior inspected source gives or implies the fixed-τ outer law or the forced critical-scale statement as a whole.

## value

PASS

This quantifies the phase hopping motivating the problem. The same two closest sites control a bounded-time nonlinear forced flow on one scale; suppression of one tail on a larger but exponentially small scale selects opposite order-one phases and a different attraction rate. These are meaningful, testable dynamical statements rather than a standalone reparameterization or a claim to classify the global bifurcation diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
