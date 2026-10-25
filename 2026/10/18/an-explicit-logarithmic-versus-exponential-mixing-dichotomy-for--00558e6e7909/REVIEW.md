# Independent mathematical audit

## correctness

PASS

PASS: The transition probability is logistic in the count and shared signal; conditional on a common signal, the count update is binomial. For finite β all individual update probabilities lie strictly between zero and one, so the finite chain is irreducible/aperiodic and has a unique stationary law. Since σ′≤1/4, the expected next-count distance under the monotone shared-signal coupling contracts by βγ/2; iterating and comparing to stationarity gives the stated logarithmic bound when βγ<2. In the high-conformity region, the payoff difference remains positive near consensus even under the worst signal, giving a uniform small exit probability from disjoint near-consensus sets. The binomial Chernoff–Cramér bound and union bound imply TV separation until exponential time; constants and domains are stated. The finite checker tests sample kernels but does not establish the all-N result.

## originality

PASS

Best-of-knowledge comparison supports non-coverage by inspected sources; source-specific evidence, implications and residual risks are recorded below. This is not a certification of independent priority.

## value

PASS

PASS: The published model’s apparent loss of ergodicity can be misread as a literal finite-state stationary-law failure. The claim gives a mathematically motivated correction: finite-N uniqueness together with explicit, qualitatively different relaxation-time bounds in two regimes. The constants are uniform over signal bias and the metastable lower bound is rigorous rather than inferred from finite trajectories. It is a meaningful quantitative distinction, not merely a standard uniqueness observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
