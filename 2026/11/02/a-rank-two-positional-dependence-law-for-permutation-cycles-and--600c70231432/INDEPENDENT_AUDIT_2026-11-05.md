# Independent mathematical audit

## correctness

PASS

Condition on three prescribed image arrows of a permutation at consecutive positions. Their forced directed graph decomposes into paths plus already closed cycles F, and contracting paths leaves a uniformly random permutation of n-3 components, so E[K_n|those arrows]=F+H_(n-3), valid even for n=3. Sum compatible forced fixed points (binomial position-rank counts), forced transpositions (only reversed rank pairs), and the two possible forced directed 3-cycles to derive the six affine b_sigma(n,i) entries over D=n(n-1)(n-2). Row 123 has nonzero constant numerator, row 132 nonzero position slope, so matrix rank is exactly two for n>=4, one for n=3. Each numerator is 1 mod 3, excluding zeros; direct summation gives constant -2/(3D) peak and valley covariances. Independent exhaustive enumeration of every permutation n=3,...,7 checked all specified-position six-pattern covariance entries; inspected check.py offers a larger finite check but is not the all-n proof.

## originality

PASS

Cycle/descent-set generating functions and cycle-refined aggregate peak statistics are prior. Their published totals do not distinguish the opposite fixed-position profiles of 132 and 231, both of which share peak descent shape. A related published Resultary inversion-indicator covariance gives two-position comparisons, not all six nonlinear three-order patterns.

## value

PASS

The cycle count of a random permutation is a central statistic and local consecutive patterns are canonical. The exact six-by-position covariance table reveals an unanticipated rank-two dependence, no accidental zeros, opposite location effects for the two peak orientations, and cancellation in the aggregate; these form an analytically proved natural structural classification rather than a finite computation or relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
