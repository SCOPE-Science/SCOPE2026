# Independent mathematical audit

## correctness

PASS

PASS: Simple spectrum follows from the nonvanishing Jacobi recurrence. The eigenprojector Hadamard sum gives B B^T with B consisting of squared normalized eigenvector components. Backward polynomials have parity and nonzero leading coefficients, yielding a Vandermonde in squared eigenvalues, hence rank equals count of distinct eigenvalue squares. Product of eigenvector norms comes from continuant resultants; cancellation yields det Mhat=prod_{i<j}(lambda_i+lambda_j)^2/Disc(chi). With chi_tau=P-tau Q and opposite parities, opposite-root resultant and chi_tau(0) produce L tau^{2floor(n/2)}/D0. At tau=0 the path is bipartite and squared eigenvalues have ceil(n/2) distinct values; at tau!=0 opposite pairs cannot occur. Independent SymPy exact-rational diagonal-moment Gram calculations reproduced determinant and rank for six separate small weighted signed/zero-potential cases; the all-n conclusion is analytic.

## originality

PASS

PASS best-of-knowledge for arbitrary weighted couplings and exact determinant formula; projectors and zero-potential unweighted path rank are established earlier. Godsil, Coutinho and weighted-path state-transfer literature lack the same endpoint-only determinant calculation in inspected material. Potential Jacobi-resultant reinterpretations and prior unweighted marked-path rank findings remain explicit risks.

## value

PASS

PASS: The average-mixing rank is a natural structural invariant of continuous quantum walks. This exact all-order weighted-path formula proves that any arbitrarily small endpoint defect removes the bipartite squared-eigenvalue degeneracy, quantitatively determining the vanishing determinant exponent and prefactor. That sharp classification is useful for perturbation/spectral mixing analysis independent of transfer-fidelity claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
