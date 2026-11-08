# Independent mathematical audit

## correctness

PASS

Boolean majority changes x_i iff both adjacent disagreement edges are one; hence the exact edge update is y_i→y_i(1 XOR y_{i−1} XOR y_{i+1}). Zeros never become ones, and bounded runs of disagreement ones erode at both ends each step while an isolated one stays. Thus first periodic-entry time equals floor(max-run-length/2) unless every edge disagrees (even checkerboard two-cycle at time zero). The edge-parity constraint is enforced exactly by tr(M_q(1)^n)+tr(M_q(−1)^n) plus checkerboards. For a uniform random spin start, any fewer than n edge bits are iid fair; disjoint rare long-run starts have joint products and nearby starts are incompatible. Fixed factorial moments give the subsequential Poisson law; geometric tails give half-log expected time. Independent microscopic simulation of all 2^n starts for n3..12 checked the T formula; source verifier n3..15 and integer trace recurrence inspected. These finite counts do not prove the asymptotic result.

## originality

PASS

Structural majority-automaton studies describe fixed/periodic attractors and empirical convergence, but do not give the parity-projected full first-entry-time CDF and lattice Poisson extreme-value limit for synchronous nearest-three binary majority on a ring. Lemoy–Mozeika–Seki study thermal noise (different stochastic system), Nakar–Ron study periodic configurations for broader radii; Resultary nearest finite-volume rule-128 paper is a different update rule.

## value

PASS

Exact deterministic transient length and iid-start convergence-time distribution are natural cellular-automaton dynamical observables. The parity-projected transfer trace and Poisson extreme window resolve precise finite-size and logarithmic convergence scales, distinguishing true periodic entry from only fixation; they are meaningful statistical limit laws rather than routine simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
