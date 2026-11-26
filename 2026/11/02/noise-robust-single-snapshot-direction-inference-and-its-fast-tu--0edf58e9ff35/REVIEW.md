# Independent mathematical audit

## correctness

PASS

In the sign-pair coordinates the heading generator is the sum of two rate-γ flip generators, even though a fixed sense of turn does not always flip the same bit. Orthogonal Brownian rotation and stationary OU filtering therefore give two independent copies, each X=Z+δG with Gaussian variance δ²=μD/v₀². In the athermal scalar stationary equations the total current vanishes, giving P_+−P_−=z(P_++P_−); substitution into either component equation gives the stated beta density and E[S|Z]=Z. The posterior sign for x>0 follows by pairing z with −z: the integrand contains g(x−z)−g(x+z)>0; by symmetry the opposite sign holds for x<0. With simultaneous thermal and sensor noise, the convolved kernel is still strictly decreasing in |x|: express the symmetric decreasing sensor density as a positive mixture of centered interval indicators; each Gaussian-smoothed nondegenerate interval is strictly decreasing for x>0. At zero noise the posterior mean equals the observed coordinate on its support. The factorized MAP signs give the four sectors and null decision boundaries. Conditioning the sign-success indicator on Z gives the erf integral; the product rule gives p². Differentiating the Gaussian convolution gives the score formula and the posterior mean derivative Var(Z|X=x)/δ². The beta integral gives the displayed γ-function ratio at zero noise, monotone likelihood-ratio order for Z² gives strict β monotonicity, and the erf integrand gives strict δ monotonicity. Independently integrating the uniform-coordinate case β=1 gives p=0.727536119397839 at δ=.3, hence p²=0.5293088050284667; at δ=0 the exact result is 9/16. Replay of the .3 case: python3 /workspace/branches/independent-boundary-checks.py. For fixed positive δ, Taylor expansion uses E Z²=(2β+1)^−1 and E Z⁴=O(β^−2). In the joint limit, √(2β)Z tends to N(0,1) with uniformly bounded second moments, so joint convergence with the scaled noise and uniform integrability justify the linear-growth expectation, including λ=0. For independent standard normals G,H, conditioning G on G+λH gives E[G sign(G+λH)]=√(2/π)/√(1+λ²). This yields the stated constant with its factor 1/(2√π); the frozen diagnostics were inspected, not used in place of the limiting proof.

## originality

PASS

The stationary model, rotated independence, athermal conditional law, Gaussian smoothing, and the basic posterior and Gaussian MAP sectors as direct consequences are not credited as novel. The supported distinct contribution is the Bayes inference result across general independent strictly unimodal kernels together with a quantitative Gaussian accuracy transition: strict orders, two rates of convergence, and the explicit scaling function. These require an additional comparison for general noise and an analysis of the joint limit. Neither the closest exact stationary distributions nor the same-model angular information result was found to establish that contribution.

## value

PASS

In a model where the stationary position landscape changes with noise and tumbling, a stable single-frame decision rule is useful only with calibrated performance. This result both identifies the independent-kernel regime of stable decisions and quantitatively distinguishes the inference advantage in the athermal, crossover, and fixed thermal-noise regimes. The value lies in the observable inference transition, not in reparametrizing the previously solved stationary distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
