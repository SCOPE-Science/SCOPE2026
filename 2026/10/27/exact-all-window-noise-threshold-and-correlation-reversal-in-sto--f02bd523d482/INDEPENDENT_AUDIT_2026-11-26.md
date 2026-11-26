# Independent mathematical audit

## correctness

PASS

Independence of time slices gives the positive second-moment map K(P)=E[B P Bᵀ]. Jensen makes Schur stability of the mean companion necessary. The root equation bounds |z|<1 for 0≤a<1; for −m<a<0, multiply the polynomial by z−1 to get z^(m+1)=(1−q)z^m+q with q=−a/m∈(0,1). The triangle inequality rules out |z|>1, and equality would force z=1, not a root of the original polynomial. At a≥1 a real root is at least one, and a≤−m makes the product of root moduli at least one. In the open interval, let d=m−(m−1)a, r=a/d, D=d+(m−1)aρ, Q=e₁e₁ᵀ. The unit-diagonal, common-off-diagonal-r matrix P₀ is positive definite (eigenvalues m/d and m(1−a)/d); D is positive at both allowed correlation endpoints and is affine in ρ. Direct computation gives K(P₀)−P₀=(F−1)Q with F=a²/d+vD/(md). If F≥1, no decay for every deterministic state is possible since their rank-one moment matrices generate P₀. If F<1, the m-step telescoping decrement is positive definite: for each realization the companion impulse columns have unit pivots and vanish below them, so their outer products span all directions. This gives geometric mean-square contraction and uP₀ with u=τ²/(1−F). The infinite-past innovation terms are orthogonal in L² by conditioning on the coefficient sequence (not necessarily independent after weighting); contraction proves causal uniqueness. Thus the thresholds, lag correlations and stationary variance follow. D increases with ρ for a>0, decreases for a<0; the claimed endpoints follow, with ties at a=0 or, for variance only, v=0. Independent 81-case moment-spectrum tests included the threshold itself and agreed with the strict stability inequality; a direct Lyapunov solve also agreed in nine stable cases.

## originality

PASS

The v=0 stability interval belongs to deterministic moving-average iteration, and the nearest indexed result also covers the two-lag additive-noise specialization. Generic random-coefficient autoregression supplies the model, second-moment criterion and AR-like autocorrelation equations. The supported distinct contribution is their explicit uniform-in-m evaluation for temporally iid equicorrelated coefficient noise: a sharp scalar threshold with endpoints, exact variance, and the sign-dependent optimal within-step correlation. The indexed specialization and inspected deterministic paper do not evaluate the multiplicative-noise model. The generic autocorrelation mechanism is not claimed as new.

## value

PASS

Equal weighting is natural for window feedback, and the choice between common shocks and zero-sum within-window noise changes the stability budget in opposite directions for positive and negative feedback. The exact threshold and variance expose this reversal at any window length, including admissible singular covariance endpoints, without recomputing the companion moment spectrum when the length or correlation changes. The flat finite-lag profile identifies what changes and what does not when optimizing the noise covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
