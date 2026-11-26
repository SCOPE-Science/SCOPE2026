# Independent mathematical audit

## correctness

PASS

For the stated tie rule and reflection symmetry the one-flight sign imbalance is M_a(x)=J_0²+2Σ_{j=1}^{a−1}J_j²+J_a². Independent exponential flights give a symmetric Markov kernel at reset events, with strictly positive flip probability and fair invariant law. The chain is stationary with that initialization as assumed for the correlation; it need not start stationary from a prescribed sign. The centered eigenvalue is its exponential average m_a, hence the stationary lag-k correlation is m_a^k. Bessel recurrences telescope to M'_a=−2aJ_a²/x, with M_a(0)=1 and limit 0, proving the asserted flux integral, strict 0<m_a<1 and strict rate and fixed-rate site monotonicities (the site increment of M_a is J_a²+J_(a+1)²). The Bessel product transform gives F'_a=(2/π)Q_(a−1/2)(1+z²/(2a²)); in the positive Q integral the substitution w=2a sinh(t/2) yields the Abel kernel and the probability law W_a of the stated coupling. W_a decreases strictly in a and exceeds E, with strict comparison visible on E>z. This gives all the strict inequalities for z>0; equality at the zero endpoint is consistent. The limiting Abel derivative is 2K_0/π. For an independent check of the uniform coefficient, let Θ be independently uniform on (0,π/2); h_z(W_a) is the conditional probability W_a sin Θ≤z. Thus F_a is the angle average of 1−exp[−2a asinh(w/(2a))] at w=z/sin Θ. Taylor-expanding the survival function gives e^(−w)(1+w³/(24a²))+O(a^−4) uniformly for w≥0: below a^(1/5) the error is bounded by a^−4 times an exponentially decaying polynomial, and above the cutoff both tails are exponentially small by monotonicity. Angular averaging preserves uniformity. Changing back to w, the coefficient is −z/(12π) times ∫_z^∞ e^(−w)w²/√(w²−z²) dw, equal to −(z³K_0+z²K_1)/(12π). This also verifies the negative sign and the continuous value at zero. `python3 /workspace/branches/independent_checks.py 5` numerically compares the direct finite Bessel sum to the angular survival representation and tests the correction at three positive z; it does not establish the uniform bound. Uploaded verify.py was inspected, not executed.

## originality

PASS

The protocol and one-flight transition structure are antecedents, and the geometric event-index correlation follows directly from that kernel. The ballistic limit itself is a consequence of Konno's free-flight weak law mixed over the independent exponential duration. The supported increment is a positive probability coupling for the finite scaled law, its strict all-separation comparison, and the signed explicit correction with a uniform order-four error in z. Prior Bessel–Legendre identities and asymptotics overlap the method and local asymptotic information; inspected passages do not supply that combined finite comparison and uniform estimate. Later catalogue overlap with the exact event-index correlation is explicitly credited, not taken to establish earlier priority.

## value

PASS

The event-indexed sign correlation is a natural observable of the established conditional-reset protocol; fair stationary marginals do not encode its lag dependence. The all-distance ordering at fixed ballistic distance–rate product tells which side of the limit every finite lattice realization lies on, and the uniform finite-distance correction quantifies the corresponding spectral gap deviation even as z varies. This is useful beyond a sampled fit or the known leading limit. It makes no inference about laboratory-time correlations, asymmetric resetting, or general geometries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
