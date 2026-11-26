# Independent mathematical audit

## correctness

PASS

With an inclusive confidence threshold, convex-hull invariance keeps every edge active. In a scalar projection put n=m+1, w=3m+1, E=sum d_i^2 and T=(sum d_i)^2. Updating the hub subtracts s/n from each d_i, so E changes by -(m+2)T/n^2 and T becomes T/n^2; a leaf update halves its d_i. The weighted mean increments s/w at the hub and -d_i/w at a leaf, giving zero drift and conditional squared increment (E+T)/(nw^2). The expectation of E contracts by at least 1-3/(4n); the pathwise nonincrease and bounded martingale convergence give consensus a.s. and L2 convergence by boundedness. Independent drift elimination for M^2+A E+B T gives 3A-B=4/w^2 and (m+2)A+(2n^2-1)B=n^2/w^2. The first coefficient is A=(9n^2-4)/(w^2(m-1+6n^2))=1/((2m+1)w), giving the stated B. Bounded convergence gives the exact variance, and testing projections gives the covariance. At m=1 it yields the midpoint-bisection limit variance d_1^2/12; for equal leaves the exact scalar factor tends to 1/18 and uniform boundedness rules out concentration at a constant. The frozen finite checker is corroboration, not needed for these all-size identities.

## originality

PASS

The model, consensus mechanism and stationary weighted mean are established. The supported distinct claim is the explicit all-size limiting covariance for this star and the resulting nonzero 1/18 coefficient in the equal-leaf limit. The directly applicable general variance bounds do not determine either.

## value

PASS

The exact covariance resolves how imbalances at a single high-degree hub persist despite consensus and a growing sample of leaves. Its rank-one part distinguishes aligned from balanced initial disagreements, and its 1/18 limit supplies a precise non-concentration benchmark not supplied by general convergence or variance bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
