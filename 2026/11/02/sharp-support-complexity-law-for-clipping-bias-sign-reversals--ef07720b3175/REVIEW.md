# Independent mathematical audit

## correctness

PASS

With signed masses w_i on the m strictly ordered nonzero magnitudes a_i, the bias equals sum_i w_i min(a_i,c). Mean zero sets its right tail to zero and b(0)=0. Every nonzero sign component must contain a nonzero interior knot because no affine piece with two zero endpoints can be nonzero. Thus the m−1 potential knot components allow at most m−2 reversals, including in the presence of vanishing signed masses or zero intervals. For the proposed alternating unit-height knot pattern on 1,…,m−1 and zero endpoint values, negative jumps of slope have absolute magnitudes 3, then 4 at each interior index up through m−2, then 3 and 1; these sum to 4m−5. Telescoping gives zero first moment and interpolated biases of alternating height ±1/(4m−5), so the simple half-integer crossings are exactly as stated. For this family only, two roots of the nondecreasing drift would imply each positively weighted score is constant on their interval and hence saturated; zero total would require a subset of weight exactly one half, impossible for the odd denominator. The root sign is opposite the drift at zero. Monotonicity and unit Lipschitz constant give (x−x_c)F_c(x)≥F_c(x)^2 and hence the residual decrease eta(2−eta)F_c(x)^2 in squared distance; boundedness and uniqueness give global convergence at each fixed c. This is deterministic population convergence, not stochastic sample-path convergence. Inspected the frozen verifier without running it; its exact finite cap tests do not establish the general bound or uniqueness.

## originality

PASS

The inspected sources cover Huber-score background and fixed-cap examples, including asymmetric bias and a nonunique mean-field equilibrium, but not the supported precise claim: the optimal count across caps for a single fixed centered law, with equality families that have a unique attracting root at every cap. The elementary spline representation and monotone Lipschitz convergence principle are not standalone novelty.

## value

PASS

The result addresses a specific obstruction to interpreting bias bounds: increasing the cap can repeatedly move the population equilibrium from one side of the true minimizer to the other for one unchanged law. The exact minimum noise complexity, an explicit rational family for each feasible count, and uniqueness and convergence over that family make the boundary sharp and meaningful. It is not a statement about privacy or sampled SGD.

The dated certificate retains the supplied scientific assessment, sources and limitations.
