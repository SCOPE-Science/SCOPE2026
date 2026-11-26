# Independent mathematical audit

## correctness

PASS

Edge transitivity gives a single absolute column sum; sign changes of edge orientations are harmless. The incidence symbol yields the stated product kernel up to the sign chosen for spatial displacement: with inverse phase +ixθ and x the target vertex minus the source, the physical column uses a_i conjugate(a_j), so the displayed product corresponds to measuring x in the reverse direction (or to the corresponding row). Reflecting x permutes the residues and leaves the norm sum unchanged. On the infinite lattice the degree-one remainder on a dyadic annulus of radius s contributes O_N(s³(1+s|x|)^−N); summation gives the required O(|x|^−3). The inverse transform of θ_iθ_j/|θ|² away from the origin is the stated negative second derivative of −log|x|/(2π); subtracting the cutoff affects only rapidly decreasing terms away from the origin (sufficiently high derivatives of the high-frequency symbol are integrable). For Gaussian regularization the root-of-unity filter is exact before taking its limit; the zero frequency tends to the isotropic mean δ_ij/2 and must be subtracted. For m≠0 and centered x, subtract H(nm) from K(x+nm), leaving an absolutely summable O((1+|x|)n^−3 |m|^−3) error by the derivative bound. The homogeneous images cancel by quarter-turns or reflections with weights exp(−t|nm|²); changing to exp(−t|x+nm|²) contributes O(|x|√t/n²) as t→0 by the mean-value bound and counting image shells. This gives the uniform O(n^−2) comparison, hence O(1) in the column sum. The absolute angular density is Lipschitz in angle, so unit-cell quadrature errors sum absolutely; each of |cos 2φ| and |sin 2φ| integrates to 4, yielding 4/π. The rank of Q is n²−1, all its diagonals equal (n²−1)/(2n²), and complementary column sums therefore differ by n^−2. Symmetry gives the same endpoint norms at infinity. The n≥3 restriction avoids duplicate positive-direction edges. The frozen numerical script was read, not executed; no numerical extrapolation is needed.

## originality

PASS

The distinctive assertion is the coefficient 4/π with an absolute bounded additive remainder for the orthogonal projections. The finite complementary identity and known finite sizes are prior results and excluded from the novelty claim.

## value

PASS

Answers the orthogonal-projection part of an explicit asymptotic question for square tori with a sharp constant and bounded additive error. It quantifies the endpoint norm of the canonical projection, without identifying an arbitrary norm-minimizing projection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
