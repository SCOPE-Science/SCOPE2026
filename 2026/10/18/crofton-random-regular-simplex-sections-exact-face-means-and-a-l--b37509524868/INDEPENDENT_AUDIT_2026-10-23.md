# Independent mathematical audit

## correctness

PASS

In invariant affine-hyperplane measure d sigma(u)dt, conditioning on meeting Delta_(n-1) biases u by its full vertex-height width, not by Haar normals. For any generic section each j-face corresponds to an (j+1)-simplex-face indexed by j+2 vertices meeting both sides; integrate its crossing offset length to obtain numerator sum_S int w_S(u)d sigma over common denominator int w_[n](u). Project a standard Gaussian vector to the sum-zero subspace; normalized radius is independent of Haar direction and subtracting the sample mean preserves ranges, yielding E f_j=binom(n,j+2) R_(j+2)/R_n and rank gap law P(K=k)=E(G_(k+1)-G_(k))/R_n. The face formula binom(n,j+2)-binom(K,j+2)-binom(n-K,j+2) is exact. For m=n^gamma, endpoint telescoping of Gaussian gaps plus quantile concentration G_(m+1)/sqrt(2logn)->-sqrt(1-gamma) with uniform L2 control yields P(log M/log n<=gamma)->1-sqrt(1-gamma), law 1-U^2. For fixed j the face formula gives f_j asymptotic to M n^(j+1)/(j+1)! in probability, hence joint log exponent j+2-U^2. Endpoint gamma=0,1 handled. Exact small-n binomial face identities checked independently, source verify.py inspected. R_2=2/sqrt(pi), R_n~2sqrt(2logn) gives mean n^2/(2sqrt(2pi log n)). No assertion for j growing with n or nonregular simplexes.

## originality

PASS

Published central Haar section face laws are for t=0 and quadratic average size; the current motion-invariant affine model weights normals by width and then integrates all intersecting offsets. Full recent simplex section type theorem concerns combinatorial types, not the Crofton rank distribution. Baryshnikov–Vitale 1994 Gaussian–simplex paper remains plausible historical overlap with full text inaccessible (Oxford VPN disconnected), explicitly retained as risk rather than presumed noncoverage.

## value

PASS

The exact motion-invariant rank spacing distribution and nondegenerate continuum logarithmic exponent for random simplex slice complexity are substantial probabilistic/combinatorial statements; they show typical polynomial complexity is random and far below the nearly quadratic expected face count, an informative mean-versus-typical distinction. Exact all-j expectation is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
