# Independent mathematical audit

## correctness

PASS

The pair-force double sum vanishes by antisymmetry, so solving the scalar damped equation backward in the stationary regime gives the sum of N independent telegraph filters. The initial homogeneous term vanishes in probability by stationarity (tightness) and exponential damping, so there is no need for an extra moment assumption on the stationary regime. The one-filter zero-current identity gives p_±=(1±z)f/2. Substitution into the sign transport equations gives ((1−z²)f)′=−2αzf and normalization by B(1/2,α) gives the stated f. The two edge expansions have identical coefficient b_α/Γ(α). Split each factor with smooth cutoffs into two endpoint pieces and an interior piece. The latter gives smooth convolutions, and endpoint pieces can only be singular at their signed endpoint sums, which are 2k−N. For m same-side factors the deficit-sum density is b_α^m x^{mα−1}/Γ(mα) times 1+O(x), by scaling the positive simplex; the cutoff and smooth multiplier also give smoothness away from its zero deficit. This proves the endpoint formula directly. For mixed signs, put a=kα, b=(N−k)α: the positive displacement is lower deficit minus upper deficit, so the singular integral on the right is ∫₀^δ u^{a−1}(u+q)^{b−1}du. For a+b<1, scaling by q and applying the beta integral gives Γ(a)Γ(1−a−b)/Γ(1−b); the left side exchanges a and b. Multiplication by the summed-deficit normalizations and the binomial multiplicity yields exactly the stated amplitudes. At a+b=1 the range u<q gives O(1), while on [q,δ] the integrand equals 1/u+O(q/u²); the smooth deficit multipliers change the integral only by O(1). Thus the critical log coefficient agrees on both sides, and at the endpoint the positive-simplex coefficient tends to b_α^N at exponent zero. For α>1/N, f∈L^{N/(N−1)} so the first N−1 convolutions belong to L^N; Hölder and continuity of L^{N/(N−1)} translations prove that the last convolution is bounded and continuous, with zero boundary values by support. The coordinate change has Jacobian μN/v.

## originality

PASS

The active-Dyson center equation and one-filter beta law are covered, and the stationary independent-filter representation follows by solving that known linear equation. Neither this reduction, interaction independence, generic convolution regularity nor the qualitative power/log mechanism is credited on its own. The supported distinct claim is the exact locus and two-sided amplitude classification, including critical endpoint values, for the N≥3 stationary center law.

## value

PASS

The frozen theorem separates the stationary collective marginal from the much less tractable interacting spatial densities. It gives explicit geometry and normalized site-dependent coefficients for a natural many-particle law, not just an exponent: mixed sign groups generally differ on the two sides below threshold, share a log coefficient at threshold, and at threshold the endpoints instead stay finite. These distinctions are useful to distinguish collective singularities analytically or in numerical data, independently of repulsion strength.

The dated certificate retains the supplied scientific assessment, sources and limitations.
