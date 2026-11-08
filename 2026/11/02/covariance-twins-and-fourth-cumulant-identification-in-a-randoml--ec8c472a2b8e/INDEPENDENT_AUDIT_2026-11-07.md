# Independent mathematical audit

## correctness

PASS

For the stationary Markov-modulated OU with on-state drift -kX and symmetric jump rate q, stationary second-moment generator equations give m_(2,1)=D/k, m_(2,0)=D/k+D/q. The covariance C(t)=m_2^T exp((Q-K)t)1 satisfies the second-order ODE C-double-prime + (k+2q) C-prime + (kq) C = 0 with C(0)=D(k+2q)/(kq) and C-prime(0+)=-D. In particular, right derivatives give C"(0+)=0, C-third=DP, C-fourth=-DPL. Hence the full covariance determines D,P=kq,L=k+2q, and k,2q are the two positive roots of z²−L z+2P. They produce exactly original rates and their involution (q,k,D)↦(k/2,2q,D), equal only on k=2q. Stationary fourth-moment equations give kappa4=D²(9/q²+6/(qk)); the involutive difference 9D²(1/q²−4/k²) is nonzero off the fixed line and q=3D/sqrt(kappa4−6D²/P). Independently verified generator moment solutions, derivative invariants and twin difference symbolically; an exact stationary covariance does not imply practical finite-noise estimability.

## originality

PASS

PASS, qualified: Santra–Das–Nath give the intermittent-trap model, Frydel 2024 gives stationary variance and fourth moment, and Huang et al. give general Markov-OU forward covariance machinery. These are known and credited. The assessed final result is complete inverse fiber (exactly the two possible rate triples, including fixed line) and fourth-cumulant resolution, not the already-published moment formulas. An implicit inverse-system-identifiability theorem could still cover the restricted result.

## value

PASS

An exact two-to-one nonidentifiability of a physically meaningful hidden-switching model from full power spectrum, and a minimal non-Gaussian statistic restoring unique parameter recovery, is a meaningful structural inverse-problem finding. Distinguishing covariance twins has practical modeling implications even though noisy estimation is not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
