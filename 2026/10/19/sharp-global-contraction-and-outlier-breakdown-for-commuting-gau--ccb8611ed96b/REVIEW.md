# Scientific review: commuting Gaussian semi-unbalanced barycenters

## Correctness — PASS

The unbalanced objective with fixed second marginal admits an exact scalar reduction through the Wasserstein covariance bound and Gaussian maximum entropy. The resulting quadratic stationary condition has one positive root. Its derivative yields the sharp global Lipschitz factor of the alternating hybrid map in the Gaussian Wasserstein metric. The envelope Hessian has the sharp positive infimum stated in the result. For one diverging covariance input, a uniform strict contraction establishes a finite limit; the analytic implicit-function expansion and large-standard-deviation expansion prove the exact inverse-square correction and the square-root contamination-weight boundary. The supplementary `verify.py` passed 7,366 deterministic assertions; infinite statements are proven analytically.

## Originality — PASS, subject to priority risks

Nguyen, Le, Nguyen, Pham and Ho (arXiv:2410.08117; first publicly submitted 2024-10-10), Section 4 and Appendix D, introduce the exact one-sided KL relaxation, Gaussian optimizer and the hybrid algorithm. Their Theorem 6 establishes convergence under a compact covariance spectral-strip assumption; it does not establish the input-exact all-start commuting contraction factor, the sharp Euclidean strong-convexity modulus, or these exact covariance-outlier coefficients. Classical Bures barycenter convergence (Chewi et al., PMLR 125, 2020) and entropic Gaussian transport (Janati et al., arXiv:2006.02572) involve different objectives. The related 2026 PMLR publication by the same authors has an accessible abstract, but its conference PDF was inaccessible; consequently, an equivalent result in that full version or other specialized literature remains a genuine priority risk. No independent publication-priority verification is claimed.

## Value — PASS

An exact algorithm-specific contraction constant valid without assuming an a priori bounded covariance strip supplies a useful convergence baseline. The finite contamination response and its exact limiting rates measure a genuinely important design tradeoff: fixed positive clean mass suppresses arbitrary input variance in this Gaussian model, but this protection degenerates at the precise square-root scale when the clean mass vanishes.

## Scope and limitations

The theorem is about centered Gaussian inputs and iterates with simultaneously diagonalizable covariance matrices. It does not cover arbitrary noncommuting covariance matrices, location outliers, general contamination distributions, inaccurate inner solves, or finite-precision stability. The limit in outlier size precedes the limit in clean fraction. Independent scientific audit and publication-priority verification are not performed.

Self-review: passed. Independent audit: not yet performed.
