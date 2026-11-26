# Independent mathematical audit

## correctness

PASS

With K=U diag(λ)Uᵀ, the weights λ_i U_ji²/S have the required pivot and size-biased spectral marginals. The conditional expectation of S−λ_i given j is exactly S−(K²)_jj/K_jj. Two applications of Jensen give the whole convex-order statement; all outcomes lie in [0,S]. Under strict convexity the upper equality requires one distinct eigenvalue on the support of each row of U, i.e. every coordinate vector is an eigenvector of K, including for repeated eigenvalues. Lower equality is exactly constant trace error. For lower attainability, the symmetric matrix diag(λ_i²−(M₂/S)λ_i) is traceless. An isotropic unit vector exists by interpolating between opposite-sign eigenvectors (or choosing any vector for the zero matrix); the perpendicular compression is again traceless. Induction gives a real orthonormal basis with zero diagonal quadratic form, hence all pivot trace errors equal m. The diagonal matrix attains the upper bound. Variance is continuous in the conjugation, and a column sign flip yields representatives of both extremizers in SO(n), giving every intermediate value. An independent check at spectrum (2,5,6) gives the constant-error matrix with diagonal (4,5,4) and entries K₁₃=K₃₁=2: each diagonal ratio is 5, hence trace error 8. The diagonal input has outcomes (11,8,7) and variance 24/13. Read RESULT.md §§Proof–Verification, VERIFICATION.md, verify.py and requirements.txt; the 28 rational and 490 numerical cases are recorded checks, not rerun or used for the universal proof. Single-pivot exact SPD only; convex order does not assert pointwise tail domination.

## originality

PASS

Known results supply the pivot rule, exact mean and standard proof ingredients. The supported distinct claim is the sharp fixed-spectrum scalar convex-order envelope with both endpoint laws realizable over the real orthogonal orbit and strict-convexity equality criteria.

## value

PASS

The prior mean is exactly orientation-independent, so it cannot measure reliability across pivot coordinates. These sharp laws separate deterministic one-step error from its maximum possible convex dispersion with the whole spectrum unchanged, uniformly for all convex losses; the variance range quantifies the discrepancy. The exact coordinate extremizers and separate equality tests add useful diagnostics without promising a multistep or arbitrary-tail ordering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
