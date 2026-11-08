# Independent mathematical audit

## correctness

PASS

For stationary two-state exponential run/rest dynamics (b,v,lambda,mu>0), solving the stable forced linear ODE from the infinite past gives Y_d=sum_j w_jU_j with sum w_j<=1. Orthogonal spherical cross-pairs are conditionally uncorrelated and have variance 1/d, proving E[(R_d²-S)²]<=2/d for d>=2. Exponential age transforms give E~Beta(mu/b,1), Z~Beta(lambda/(2b),1); the stationary mixture and contracting perpetuity follow with both rates positive. For upper tail, E<=1/2 gives (eps/2)^{mu/b}, whereas E>1/2 forces three simultaneous small deficits and contributes o(eps^{mu/b}). For lower tail, the small S_R bound and negative-moment bootstrap yield E[S_R^{-p}]<infty for all p=lambda/(2b)>0, and the exact beta-CDF gives pi_T E[S_R^{-p}]eps^p. Mean normalization follows from linear perpetuity moments. Limits d->infty and eps->0 are sequential, as specified; finite simulations alone establish neither.

## originality

PASS

PASS qualified: primary finite-tumble fixed-dimensional moments and instantaneous-tumble high-dimensional radial studies are fully credited, but their stated hypotheses and asymptotics do not directly establish the finite-rest limit with two separately rate-controlled sharp edge constants. All-moments determinacy alone is not a displayed dimension/edge limit theorem.

## value

PASS

The two sharp and different exponents classify the geometry of a natural stationary active-particle model: the near-unit mass depends on mobile-phase departure mu/b, while the near-zero mass depends on rest-phase escape lambda/(2b). Their positive finite coefficients, the nondegenerate high-dimensional limit, and L2 convergence supply nontrivial quantitative information unavailable from a mere first-moment estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
