# Independent mathematical audit

## correctness

PASS

For 0<mu<1 and always-active uniformly selected pairs, the centered disagreement evolves as dʹ=(P-mu v vᵀ)d + projected selected Gaussian noise. Exact pair average loss 2t/(N-1) with t=2mu(1-mu) gives contraction and a unique finite-fourth-moment invariant. Stationary squared norm =Delta²(N-1)²/(tN), hence each coordinate variance =Delta²[(N-1)/N]²/t. For N=2 only one pair yields Gaussian AR(1); for N>=3 exchangeability would require a Gaussian covariance sigma²P, but each edge-dependent Gaussian covariance differs and selected-noise covariance has rank two rather than one on H. Strict Gaussian-mixture convexity rules out a Gaussian joint invariant. Reconstructed the N=3 norm-squared fourth recurrence, E[S²]=4Delta^4(16-11t)/(9t²(2-3t/2)), giving standardized coordinate fourth 3(16-11t)/(16-12t), positive excess and max 3/20 at mu=1/2. Independent SymPy rational-algebra recomputation agrees. Does not claim the uncentered mean is stationary or finite-confidence dynamics remain linear.

## originality

PASS

Siebenmorgen–Restrepo derive an approximate Gaussian representative-agent variance for their state-dependent bounded-confidence utility model. They do not establish the exact stationary centered finite-N law for the neutral always-interacting specialization; the N-dependent variance correction and smallest N=3 non-Gaussian fourth moment are stricter model-specific facts. Fixed-stubborn-agent gossip and noiseless consensus address different transition mechanisms.

## value

PASS

The Gaussian representative-agent closure is a concrete modelling approximation; identifying the smallest population where it fails and quantifying excess kurtosis alongside the exact finite-size variance is an independently meaningful boundary for stochastic opinion dynamics, not just a Gaussian-mixture textbook example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
