# Independent mathematical audit

## correctness

PASS

Absence of interior minima with both endpoint minima forces an increasing then decreasing interior. Conditional on interior unimodality, each subset of the n−1 below-maximum ranks occurs on the left with equal probability; the maximum M is independent of that assignment. Given the counts and M, the two samples of normalized values are independent. Integrating each exterior neighbor and root gives a factor g(s)=s−s²/2 at its adjacent interior minimum s, with V_0=1 for an empty side. Beta moments of the side minima give F_n. To check the normalization directly, set N=n+1 and i=m+1; the prefactor binom(n−1,m)n/[(m+1)(n−m)] equals binom(N,i)/N. For J=sum_{i=1}^{N−1} binom(N,i)/(i+1)=(2^(N+1)−N−3)/(N+1), the reciprocal sum and product terms combine to −2J/(N+3) inside the overall 1/N; the constant term is (2^N−2)/(N+1). This yields the displayed denominator. Independently enumerating the (n+4)! strict rank permutations for n=1,2,3,4, testing the two roots and rejecting every interior valley, gives apex histograms [16], [40,40], [78,132,78], [133,315,315,133], matching the weights. For the infinite limit the central binomial concentration makes both sample sizes n/2+o(n); their minimum survival laws converge uniformly there, and n(1−M) converges independently to Exp(1). The scaled tilt converges to the product of the two independent Exp(1/2) minima and its mean converges to 4, the product's mean. Nonnegativity and convergence of means give uniform integrability, so the tilt size-biases just the two side minima to Gamma(2, rate 1/2). Given the sides, the normalized endpoint kernels tend in total variation to independent uniforms; multiplying by the gamma marks gives the stated endpoint exponentials, unaffected by the time transform at scale n. The peak-time transform gives the independent Gumbel, and the Gaussian location is unchanged by the tilt. Uniform empirical order-statistic convergence gives the tent before tilt, then uniform integrability transports it; the returned endpoint heights are o_p(1).

## originality

PASS

Best-of-knowledge pass for the marked refinement: the exact apex-position distribution and conditional tent with independent endpoint, location and peak-time limits for one specified oriented gap. The rank reduction and the unmarked gap mass are already known and are not credited as novel.

## value

PASS

The unmarked incidence of long gaps does not explain their interior geometry or clock scales. The specified-gap joint law resolves a natural conditional object: a macroscopic tent together with two endpoint times of order 1/n, a Gaussian location fluctuation and an independent logarithmic peak-time fluctuation. The endpoint tilt makes this more than routine unconditioned extreme-value theory. The finite location law also gives the natural discrete counterpart of the Gaussian mark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
