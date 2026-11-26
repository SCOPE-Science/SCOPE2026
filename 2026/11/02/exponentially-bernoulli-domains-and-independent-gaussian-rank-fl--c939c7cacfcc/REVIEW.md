# Independent mathematical audit

## correctness

PASS

A partial idempotent fixes its image and has that image in the domain. Rank >=2 cyclically nondecreasing maps have cyclic interval fibers, so the k fixed image points appear in cyclic order and a gap of g_i nonfixed points gives exactly g_i+1 ways to cut between adjacent fibers. Rooting at a labeled fixed point counts each map k times and gives (m/k)[z^{m-k}](1-z)^(-2k). Rank 1 is m, not m^2; the empty map contributes one. The logarithmic coefficient extraction and binomial transform give the stated H_n(s,u), with the n=1 correction interpreted as zero. For each domain subset of size m the weight A_m(1) differs from lambda^m by at most n^2+3 (zero error at m=0); summing over subsets and controlling the normalizers gives the claimed total variation rate on the whole cube. The two smaller exponential bases at the origin stay strictly smaller in a fixed complex neighborhood; polynomial factors can be absorbed in a larger exponential rate still below one. A local analytic log and Cauchy bounds justify the differentiated error. For g(v)=log lambda(e^v), g'(0)=1/sqrt(5) and g''(0)=2/(5 sqrt(5)). Applying the chain rule to log(1+exp(t+g(v))) gives variance p(1-p)=1/5, off-diagonal a/5=sqrt(5)/25, and rank variance pb+a^2/5=(2+sqrt(5))/25. Taylor expansion at the sqrt(n) scaling gives the joint normal limit; subtracting a times the domain fluctuation gives residual variance pb=(1+sqrt(5))/25 and zero Gaussian cross-covariance. The frozen test code was inspected only: it compares complete joint counts through n=6, and through n=50 the two binomial transforms after summing over domain size. These are finite checks, not proofs of the probability limits.

## originality

PASS

Credit is limited to the quantitative full-domain product-law approximation and the explicit joint and independent-residual probability laws. The finite idempotent enumerations, including the joint array recoverable from the domain-size summands, are not new. The strongest inspected finite enumeration does not supply the limiting probability statements or their estimates. The two plausible nearby probability models use a different ensemble, and the closest catalogue spectrum concerns partition-preserving maps. This is a best-of-knowledge decision on the stated probability results, not a priority certification.

## value

PASS

This natural uniform-idempotent model has two different sources of randomness, the domain and the rank inside it. The exponential TV rate controls every domain event, not only typical sizes or finite-dimensional marginals. The covariance calculation then separates random-domain fluctuations from intrinsic rank noise with an explicit limiting variance; neither a total enumeration nor marginal convergence provides that decomposition. This gives concrete quantitative information about a standard semigroup ensemble rather than a new name or unspecialized application of a limit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
