# Independent mathematical audit

## correctness

PASS

Before recovery the span is contained in a plane whose defining binary form is nonzero on the requested unit vector. There are four such planes; every pair intersects in a distinct one of the six nonrecovering lines, and every triple intersects in {0}. Inclusion–exclusion gives the tail coefficients +1 on the planes, −1 on the lines and +3 at {0}, also correct at draw count zero. Summing recovers T; all four plane masses are less than one except at the pure weight-three and pure weight-two vertices, where recovery fails. The Hessian drops a positive rank-one term and is bounded below by 2x(2,1)(2,1)ᵀ+18y e₂e₂ᵀ−4x e₁e₁ᵀ−6y e₂e₂ᵀ with x=(1−a)⁻³ and y=(1−b)⁻³. Its determinant is at least 56/9 and trace at most 243/4, yielding the asserted bound greater than 1/10. The extended expectation is lower semicontinuous, either by its sum of continuous nonnegative tails or by divergence at the two excluded vertices. Independently derived edge numerators and all 208 exact Bernstein coefficients give minima 8873/12288, 24521/512 and 1557633/2048. The edge denominators are positive wherever finite, so all boundary values exceed 279/100; the thirteen-column witness has exact value 167/60. Thus compactness and strict convexity give a unique interior minimizer. Differentiation gives the two critical equations. The exact gradient L1 residual at the stated rational point is below 2×10⁻¹⁰ (about 1.45961327×10⁻¹⁰); strong convexity gives the stated distance bound. Numerical stationarity gives minimum 2.778849589866395…, and rational empirical distributions are dense, so the finite-length assertion is an infimum, not an attainment claim.

## originality

PASS

Wang–Yaakobi already give the access formula and essentially the same numerical allocation. The distinct contribution is rigorous certification of strict interiority and global uniqueness for arbitrary-span decoding, with uniform exclusion of all three boundary faces. The closest indexed theorem about degree-three necessity uses iterative peeling, not arbitrary-span decoding, and does not provide the all-face exclusion or minimizing distribution.

## value

PASS

The exact structural conclusion is that no symmetric distribution missing any Hamming-weight class can even approach the optimum. This follows from an explicit finite code and a uniform rational gap, not from extra digits in the existing table. Together with global uniqueness it makes the three-bit model a useful exact benchmark and distinguishes span decoding from a degree-three-only necessity statement for peeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
