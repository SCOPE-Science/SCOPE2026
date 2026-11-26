# Independent mathematical audit

## correctness

PASS

For either process its stationary law is a centered conditional Gaussian with variance 2D∫exp(2ξ(u))du, by the backward stochastic convolution and stationary independent increments of the logarithm ξ of the homogeneous multiplier. The Lyapunov exponents γ+(λ/s)log(1−s) and γ−λ−λs/2 are strictly negative; the integrals are almost surely finite and the decaying homogeneous solution gives uniqueness. Splitting the integral into unit intervals gives the p/2-th moments of the (unscaled) block integrals as C_p exp(nφ(p)), with 0<C_p<∞ (bounded upward on the first Poisson block, and Brownian suprema have all finite exponential moments). Summability or Minkowski proves finiteness at φ<0, a single later block proves divergence at φ>0, and at φ=0 finite total moment would force the block moment to tend to zero by dominated convergence, contradicting C_p>0. The stated φ_P and φ_G have a unique positive root. The variance is finite exactly when s<2(1−β) and is identical in both models there. Independently of the generator calculation, sorting m integration times for the m-th moment of the variance integral, Tonelli and independent ξ increments give m! times the product of integrals ∫exp(uφ(2j))du for 1≤j≤m. Normal Gaussian moments give the same even-moment ratio ∏ A_j^G/A_j^P with A_j=−φ(2j). The j=1 denominators coincide polynomially; for j≥2 the signed cubic binomial remainder makes A_j^P>A_j^G. For ms→0 all denominators are positive eventually, A_j^G=2j(λ−γ)(1+O(js)), and A_j^P−A_j^G=λ choose(2j,3)s²(1+O(js)) uniformly for j≥2. The log quadratic error sums to O(m⁵s⁴), and the Taylor/denominator error to O(m⁴s³). The exact sum of choose(2j,3)/(2j) is (4m³−3m²−m)/18. These imply the sharp coefficient, all three regimes and the fixed-order O(s²) relative agreement. For the frontier, set z_s=−κ_P log(1−s) and h_s=−log(1−s)/s; monotonic inversion of (1−e^(−z))/z gives z_s→z_β. The strict gap follows from z²−2z+2(1−e^(−z))>0 (positive derivative for z>0), and strict interior of the limiting window gives the stated mismatch for all sufficiently small s. My independent bounded replay `python3 /workspace/review_checks.py 3` recovered the exact 32/47 fourth-moment ratio and -log R/(m³s²)≈0.498856 at s=10⁻³ and 0.455382 at s=10⁻⁵ for β=1/2, approaching 4/9. The frozen checker was inspected, not executed.

## originality

PASS

The supported distinct claim is the sharp uniformly growing-order log ratio (fixed β, m→∞ and ms→0) and the relative-error crossover it gives well before the existence cutoffs. The same-variance and strict limiting existence-gap components are exactly covered in a related catalogue record; neither, nor a generator or generic tail criterion, is relied on for distinctness.

## value

PASS

A second-order closure can exactly match variance while giving order-one relative errors at degrees parametrically smaller than either moment-existence cutoff. The jointly valid constant and breakdown scale quantify where matching low moments ceases to be informative, not just where a tail cutoff is different. This is a useful test of the approximation for linear growth with frequent weak contractions, without extrapolation to a general resetting model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
