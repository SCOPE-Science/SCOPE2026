# Self-review

## Correctness
PASS. The scalar one-lag recurrence is reconstructed from the stated projected-gradient update with two feasible initial states. The positive-definite quadratic energy has an exact decrement for \(0<s<1\), and clipping at the orthant boundary cannot increase that energy. Nonconvergent interior steps are excluded by the characteristic roots and the impossibility of entering a positive stationary pair from a distinct predecessor. Boundary and strictly active optimizers admit monotone and finite-termination arguments, respectively. Independence of the diagonal coordinates proves the all-dimensional equivalence. The rational checker is only corroboration.

## Originality
PASS subject to the stated risks. The 2014 asynchronous proximal-coordinate paper was inspected in full for its update, stochastic quantifiers, sufficient delay/stepsize conditions, and proof setting. An earlier stochastic asynchronous-coordinate predecessor was also identified. Neither inspected statement implies the sharp deterministic one-lag, all-initialization criterion that depends on which coordinates are active at the optimum. Searches for equivalent recurrences, aliases, six-cycles, support identification, and unrestricted active-face steps did not locate dominating coverage. The earlier full paper and old asynchronous fixed-point literature remain residual risks, not claims of exhaustive exclusion.

## Value
PASS. The theorem supplies a usefully interpretable, exact active-face stepsize law. On the same strongly convex scalar curvature and same one-step delay, a positive optimizer has the sharp ceiling \(s<1\), while an active optimizer has no upper ceiling, with finite absorption under strict complementarity. This identifies a genuine modeling distinction that generic curvature/delay bounds do not express. The separable higher-dimensional version is a single classification, not a disconnected corollary collection.

## Closest literature and limitations
Related stochastic asynchronous coordinate methods and bounded-delay proximal updates predate this claim; their stochastic expected-rate guarantees are not the deterministic phase diagram established here. The theorem does not cover coupled Hessians, random coordinate schedules, heterogeneous delay, or floating-point effects. The strict contraction factor displayed in the proof is sufficient rather than rate-optimal.

Self-review: passed. Independent audit: not yet performed.
