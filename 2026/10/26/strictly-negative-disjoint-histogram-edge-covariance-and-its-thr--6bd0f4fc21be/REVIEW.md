# Independent mathematical audit

## correctness

PASS

Given block totals K,L, the two internal binomial splits are independent, so the covariance is that of their folded-walk means. The increment of a folded-walk mean is (2θ−1) times the expected sign plus the zero-return probability, hence nonnegative by monotone coupling to the fair walk. Conditional on K, the L mean is decreasing in K. The K=0 and K=N endpoints make the independent-copy covariance identity strict, including N=1 and the no-residual-mass case. For a biased pair the folded mean differs from its linear drift by an exponentially small L² error after averaging over its block count. For a balanced pair the central-binomial estimate and Taylor expansion give slope 1/√(2πNu) and O(N⁻¹ᐟ²) L² error, with an analogous slope for the other block. Multiplying the slopes by Cov(K,L)=−Nuv gives all four coefficients, and Cauchy–Schwarz controls the errors at their stated scales.

## originality

PASS

The supported distinction is the fixed-profile uncentered three-regime theorem, particularly the mixed balanced/biased scaling and explicit coefficient with unrelated block masses. The sign theorem is demonstrably also indexed and the uniform asymptotic was published; neither is credited as a standalone novelty. The centered Part 4 shares the balanced statistic and the relevant cumulant contribution, but is not an equivalent for unbalanced pairs.

## value

PASS

A variance calculation for histogram total variation needs the covariance of disjoint terms. For fixed unequal profiles a Gaussian or purely uniform heuristic can miss the leading contribution: balancing one edge reduces the scale to √N, and balancing both leaves a nonzero constant. The coefficient and the regime distinction are useful for deciding when disjoint contributions can be neglected.

The dated certificate retains the supplied scientific assessment, sources and limitations.
