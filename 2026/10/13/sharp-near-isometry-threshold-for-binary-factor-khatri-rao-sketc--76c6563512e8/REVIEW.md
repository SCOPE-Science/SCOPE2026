# Independent mathematical audit

## correctness

PASS

With N=2^d, each length-2 factor is σ_r(1,t_r), where independent fair signs σ_r,t_r yield a column equal to ± one fixed Walsh–Hadamard vector h_T, T uniform among N orthogonal labels. Hence ΨΨᵀ eigenvalues are exactly NC_t/m for multinomial occupancies C_t with total m; rank N iff every bin nonempty, and inclusion–exclusion gives its exact finite probability. For ε∈(0,1), m=⌊cNlogN⌋, the near-isometry condition is simultaneous |C_t−m/N|≤ε m/N. Chernoff rates H_+=(1+ε)ln(1+ε)−ε and H_−=ε+(1−ε)ln(1−ε) satisfy H_->H_+; for cH_+>1 union bound gives success with probability→1. For cH_+<1, letting Z count bins above (1+ε)m/N, a local binomial lower bound plus Stirling gives EZ=N^{1−cH_++o(1)}→∞. Conditional binomial monotonicity gives pairwise nonpositive covariances for high-occupancy indicators, so Var Z≤EZ and P(Z=0)→0. The critical coefficient c*=1/H_+ is sharp on both open sides; c=c* is explicitly unproved. An independent 5-small-tensor-count Walsh diagonalization and exact occupancy/rank check reproduced the finite spectral identity; bounded tests are not the asymptotic proof.

## originality

PASS

The exact uniform-Walsh column identification makes this specific tensorized Rademacher sketch a multinomial occupancy process. Camaño–Epperly–Meyer–Tropp (2025), §5.3 analyze precisely the same two-entry Rademacher factor distribution and show many inputs become orthogonal, requiring exponentially many columns; the inspected discussion does not give the complete finite-dimensional full-space spectrum or sharp ε-dependent coefficient in NlogN. Beretta–Musco (2026) Theorem 1.3 establishes a broad sufficient OSE bound for sub-Gaussian Khatri–Rao products, not this necessary-and-sufficient full-space asymptotic constant. The coupon-collector and Chernoff occupancy tools are classical and are not claimed as novel; the assessed contribution is their exact probability threshold for the specified sketch model. A specialized preexisting Walsh/occupancy restatement is an important priority risk.

## value

PASS

The exact sample requirement for an entire N-dimensional embedding is a natural numerical-stability invariant of the same pathological two-sign tensor law singled out in current sketching literature. It distinguishes mere full rank (classical coefficient one) from distortion-ε near-isometry (coefficient 1/H_+(ε), e.g. ≈9.2423 at ε=1/2), and provides matching necessary and sufficient asymptotic regimes. This precise operational threshold is mathematically motivated and not merely a code check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
