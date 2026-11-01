# Independent mathematical audit

## correctness

PASS

Reconstructed the theorem for n>=3 and every real edge weight w with combinatorial Laplacian L(w), actuator b=e0 and positive powers in ordered Kalman columns. Reflection J e_i=e_(n-1-i) decomposes into symmetric dimension p=ceil(n/2) and antisymmetric q=floor(n/2), with constant S and rank-one A_w=A_0+2w f f^T. In pairwise reflected Jacobi bases all offdiagonals are nonzero and w-independent; hence each endpoint-input block Krylov determinant is a fixed nonzero triangular product. A full spectral Vandermonde determinant divided by the two block Vandermondes gives a constant times resultant product over symmetric eigenvalues det(lambda I-A_w), and both polynomial sides extend through collisions. At w=1 the uniform cycle Fourier sine/cosine pairing gives exactly p-1=floor((n-1)/2) common nonzero symmetric eigenvalues, simple in A_1; rank-one slopes are nonzero because a Jacobi endpoint eigenvector cannot vanish in first coordinate. The symmetric zero eigenvalue contributes the affine factor 1+(n-1)w from antisymmetric ramp vector at signed resonance and path nonsingularity. w=0 path Krylov matrix is triangular with diagonal (-1)^j, fixing global sign (-1)^(n+1). Checked parity n even/odd, n=3 minimum, 0 and 1 and negative root, L versus -L convention, and squared Gram determinant. Independently recomputed 112 exact rational n=3..18 comparisons from integer Bareiss arithmetic; finite checks are only corroborative.

## originality

PASS

Best-of-knowledge originality survives as the exact signed ordered-endpoint Kalman determinant with its complete all-dimension polynomial factorization and high-order w=1 volume collapse. The 2022/2024/2025 Grudsky–Maximenko–Soto-González line supplies a full spectral analysis of precisely the same graph and is the strongest near-coverage; generic access to eigenvectors plus Vandermonde identities in principle permits reconstructing any Krylov determinant, but reducing their full eigenvalue data to this short closed polynomial entails a nontrivial resultant and normalization calculation that was not identified as an earlier stated or immediately mechanically supplied result. The signed negative root, uniform-cycle noncontrollability, and generic rank tests are previously known and are not independently novel. This is a best-of-knowledge finding with material priority risks and one inaccessible full text, not certification of absolute novelty.

## value

PASS

This is a naturally motivated exact invariant of a standard endpoint-actuated undirected ring with a single conductance defect, not an arbitrary slice: the determinant gives an algebraic reachability volume and a complete closed all-n response to changing one edge. The nontrivial dimension-dependent order floor((n-1)/2) quantifies symmetry-restoring controllability fragility that binary PBH controllability tests and signed-Laplacian stability thresholds do not reveal. Distinguishes all w real algebraic roots, physical w>0 controllability, and exact squared Krylov Gram volume. The result is bounded and does not claim a finite-time energy Gramian, other actuator placements or a general graph theorem; its exact, reusable sensitivity law retains value despite antecedent same-object spectral data and a relatively short reflection-based proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
