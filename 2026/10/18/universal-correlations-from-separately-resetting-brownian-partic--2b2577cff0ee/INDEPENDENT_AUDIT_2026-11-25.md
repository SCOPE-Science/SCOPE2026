# Independent mathematical audit

## correctness

PASS

In the stationary environment the elapsed current plateau length L is Exp(ν), independent of its mark λ and the path prior to that plateau. If T is a particle's last-reset age, write u=E[T|path], v=E[T²|path]/2. Let b=e^(−λL), a=(1−b)/λ, g=∫₀ᴸ t e^(−λt)dt. Integrating the conditional survival gives u=a+b u_old and v=g+Lb u_old+b v_old; the independent earlier environment has the same backward law. Renewal finiteness holds even at unbounded or very small rates: the unit-age survival time kernel weighted by the refresh rate has mass νA<1, which remains <1 after a sufficiently small exponential tilt, yielding finite age moments. Averaging the first recursion, its square, and the second gives E u=A/S, E u²=2C/(SR), E v=A₂/S² (in particular E[a²]=2C and E[ab]=νC). Conditional independence makes the square-product moment (2D)² E u², whereas the one-particle fourth moment is 24D² E v by the Gaussian fourth moment. Hence the stated quotient and zero positional covariance by sign symmetry. The squared covariance is (2D)² Var(u), strictly positive when varying a nondegenerate current mark on a positive-length plateau and zero for a point mass. Conditional Jensen gives 3E[X₁²X₂²]≤E[X₁⁴], with strict correlation bound <1/3 after subtracting the positive squared mean. For −1<α<1, λ=νt gives A₂∼cν^(α−1)K and C∼cν^(α−1)J using integrable scaled kernels; the tail away from zero is O(1). νA,νB→0 and A²/A₂→0 by the three bounds O(ν^α), O(log(1/ν)), O(1) on A according to the sign of α. Splitting J's kernel as ∫₁/₂¹ da/(t+a)² gives J/K=∫₁/₂¹ a^(α−1)da, including log 2 at α=0. This decreases from 1 to 1/2 across the open interval, so the limit is in (1/6,1/3). The E₁ example follows by shifting the exponential-rate integrals, partial fractions for C and integration by parts for A₂. An independent rational plateau-recursion computation on a three-state law reproduced the moments and ρ≈0.0753581604463, 0.0552138058996, 0.0115187376429 at ν=1/19,4/5,9.

## originality

PASS

Credit the Poisson-redraw environment and its one-particle law to Arutkin–Reuveni and the conditional-independence mechanism to prior methods. The distinct supported claim is the exact stationary squared-displacement correlation for separate conditional clocks and its explicit slow-refresh family over all specified near-zero density exponents. The strongest checked model and observable matches do not determine that pair result.

## value

PASS

Separately timed resets do not eliminate environmental correlations. The exact joint observable separates a zero signed covariance from strict fourth-order dependence and distinguishes shared hazards from shared events. Its slow-refresh ratio sorts an entire continuum of low-rate laws despite divergent fourth moments, independently of the rest of the rate distribution. This gives an interpretable benchmark not obtained by just substituting an exponential density into a one-particle formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
