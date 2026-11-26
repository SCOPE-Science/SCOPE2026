# Independent mathematical audit

## correctness

PASS

Reconstructed the covariance using independent uniform ranks. An edge inside a decreasing triple contributes 1/12; a singly shared extreme contributes signed 1/24 because its conditional mean is 3/4 or 1/4, and a shared middle contributes zero. With A=i−1 and B=n−i, triples containing i contribute binom(n−1,2)/6 plus [binom(B,2)(B−A−2)+binom(A,2)(A−B−2)]/24. Other triples contribute 1/12 only when they straddle i, giving AB(n−3)/24. This simplifies to (1); AB≤(n−1)^2/4 gives the positive central lower bound, including n=3, and the claimed positional monotonicity. Conditional on X_i=x, D_i has A Bernoulli(1−x) and B Bernoulli(x) terms, independent conditionally, so total variance is (n−1)/6+(A−B)^2/12. For T, disjoint triples give no covariance and pairs with at least two shared indices are O(n^4). The single-index projection gives the main term. With y=x−1/2, its scaled limit is [(1−2t)y+(1−6t+6t²)(y²−1/12)]/4. The two terms are orthogonal in x, with x-moments 1/12 and 1/180 and squared t-integrals 1/3 and 1/5, giving 13/7200. Uniform O(1/n) projection error and the polynomial Riemann sum give the O(n^4) remainder. The normalized covariance tends to 1/96 on the stated scale, the degree variance divided by n tends to (1+2s²)/6, and outside the window that latter ratio diverges while normalized covariance is bounded. This proves the constant and both regimes.

## originality

PASS

The supported distinct result is the exact position-marked degree/decreasing-subsequence cross-covariance and the resulting sharp correlation profile. The individual degree asymptotics, the leading triangle-count variance, and the overlap/projection techniques are not credited as new.

## value

PASS

A marked degree and a triangle count are natural local and global observables of the same permutation graph. The exact positional covariance distinguishes the endpoint maximum of raw covariance from the central localization of normalized dependence. The explicit transition profile resolves a question not answered by the two separate marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
