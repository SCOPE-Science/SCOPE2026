# Independent mathematical audit

## correctness

PASS

PASS. Under merged independent rate-one Poisson coupon clocks, conditioning on maximum first-arrival M=m leaves the last type singleton and the others independent positive-truncated Poisson counts, hence U|M=m=1+Bin(n-1,m/(exp(m)-1)). For m=log n+O(1) its conditional mean/variance are log n exp(-(m-log n))+O(1), yielding a uniform window Berry-Esseen estimate and a Gaussian residual asymptotically independent of the Gumbel first-arrival extreme. For the original discrete completion count, E(M-T/n)^2=H_n/n and log n times its scale error is o_p(sqrt(log n)), giving the claimed observed-time studentization. Independently checked 35 exact rational pmf entries using distinct absorbing chain and integrated Poisson identities for n=2..8; finite checks are not evidence for infinite n alone.

## originality

PASS

PASS, qualified best-of-knowledge. Ilienko, Papanicolaou–Doumas and Long establish first-order singleton/sibling exponential limits and shared Gumbel completion extremes. Their inspected principal results do not give the observed-completion-time-centered sqrt(log n) Gaussian residual jointly independent of the Gumbel variable with a uniform conditional binomial CLT. The first-order exponential limit and Poisson thinning tools are credited. Older occupancy CLTs at random stopping times may subsume the second-order assertion.

## value

PASS

PASS. A precise second-order Gaussian law conditional on the observed completion extreme complements established first-order exponential fluctuations, gives an exact finite shifted-binomial representation, and answers a natural distributional refinement of the coupon collector; no more general siblings/weights are claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
