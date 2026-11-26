# Independent mathematical audit

## correctness

PASS

I reconstructed the reduction and the limits. Any finite competing cost has finite second moments from the transport term; finite Gaussian-reference KL also excludes zero-variance marginals. For a scalar candidate with mean m and standard deviation s, the transport lower bound m²+(s−b)² and the KL Gaussian lower bound at the same moments attain equality simultaneously by the affine Gaussian coupling; the mean term is minimized at zero. Across independent coordinates, the entropy lower bound by the sum of marginal entropies and the matching product Gaussian coupling make the scalarization exact. The strict convex inner problem has unique positive root of c_a s²−2bs−τ=0, c_a=2+τ/a². The derivative approaches 2/c_a from below. Sharpness of the global Lipschitz modulus follows by letting just a maximizing coordinate go to infinity, where the diagonal-Gaussian W₂ geometry is Euclidean. The continuous extension maps the complete closed orthant into its interior, justifying Banach convergence and uniqueness. Differentiating the minimized objective gives 2(b−T(b)) and diagonal Hessian with global infimum 2(1−q), attained as an infimum at infinity. For the outlier, the relaxed map strictly increases with M and has a contraction bound uniform in M at fixed clean weight, so the fixed points increase to the limiting fixed point. Setting δ=τ/M², I obtain ∂_δs=−s∞²/[2√(b²+2τ)] from the quadratic; the nonzero fixed-point derivative 1−T∞′ produces exactly K_w and analyticity gives the M^(−4) error. In the second limit any bounded subsequence of B_w would imply a finite fixed point of s∞, impossible. The large-b expansion s_a(b)=2b/c_a+τ/(2b)+O(b^(−3)), also valid with c_a=2 for s∞, therefore gives (1−w)(1−2/c_a)B_w²→τ/2, yielding the claimed prefactor. This proof does not interchange the two limits or require a contraction factor uniform in w.

## originality

PASS

Credit the one-sided KL objective, Gaussian relaxation and its closed form, and the hybrid update to Nguyen et al. The exact scalar update is already encoded there, and sharp contraction and the standard-deviation Hessian modulus are direct differentiation consequences, not independently original invariants for purposes of this review. The surviving distinct result in the frozen Finding is the quantitative sequential outlier response of the optimizer: the finite ceiling, its strictly positive inverse-square leading correction, and especially the singular sharp prefactor as clean mass vanishes. The prior formula is for one update, not the optimizer as a function of the outlier and weights. The outlier conclusions require control of the fixed point in two distinct regimes (a uniform-in-outlier gap followed by a vanishing gap), not plugging the outlier into an already known bound or explicit optimizer formula. The inspected paper's qualitative experiment and bounded-spectrum convergence theorem do not cover that analysis.

## value

PASS

For the existing transport objective, a tight one-step convergence factor is useful context but not the basis for value. The exact optimizer has a motivated robustness contrast with ordinary Wasserstein averaging: an arbitrarily large covariance input has bounded influence at fixed clean weight, but the bounded ceiling deteriorates at a quantified rate as that clean weight vanishes. The positive inverse-square correction and exact singular prefactor characterize both regimes and cannot be inferred from a finite experiment or routine substitution into one update.

The dated certificate retains the supplied scientific assessment, sources and limitations.
