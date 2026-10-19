# Scientific review

## Correctness — PASS

The vertex-input cyclic-support rank equals the number of active distinct eigenvalues of a symmetric matrix. Splitting the distinguished cube coordinate produces an unperturbed Walsh block and a rank-one perturbed block. All latter nonradial levels duplicate Walsh frequencies. The perturbed radial Jacobi eigenvalues are simple, positive and disjoint from those frequencies for every nonunit positive defect. Missing radial modes are **exactly** the common eigenvalues of the two principal subblocks formed by deleting the actuator shell. Their intersection count is the degree of the characteristic-polynomial gcd. Endpoint irreducibility and the affine-in-conductance determinant establish universal/generic ranks; direct small-block calculations give the four-cube exceptions. The embedded script completed 489 exact arithmetic assertions, with computations supporting but not substituting for the infinite proof.

## Originality — PASS, residual risk stated

The closest original primary work on grid controllability (Notarstefano–Parlangeli, arXiv:1203.0129v1, and Chapman–Nabi-Abdolyousefi–Mesbahi, DOI:10.1109/TAC.2014.2328757) treats exact Cartesian products. The defect destroys that product Laplacian. Zhang–Cao–Camlibel (DOI:10.1109/TAC.2013.2275666) gives upper/lower topology-based subspace bounds, not an exact defect-conductance classification; full text was inaccessible, so this comparison carries explicit access risk. Yuan et al. (DOI:10.1038/ncomms3447) gives general PBH multiplicity principles, but not active eigenvalue counts for the specific defect. Earlier research on Walsh hypercubes with *unchanged* edge weights or on different Cartesian powers does not imply this weight-dependent exact rank. A relevant record about weighted Cartesian \(P_4\) powers and rank-one oracle spectral supports was available only as a scientific abstract; it concerns another operator and parameterization and does not directly dominate the present theorem. There remains risk of an equivalent specialized treatment in incompletely indexed literature. Exact original-source comparison is documented in AUDIT.json.

## Value — PASS

Reachable dimension is the natural finite-dimensional measure of what a single actuator can influence, not a decorative statistic. This family is exponentially large but exceptionally symmetric: the theorem quantifies precisely how a localized physical edge-weight defect breaks that symmetry, doubling the order of the reachable dimension while exposing rare resonance losses at explicit algebraic weights. The exact all-vertex exception test is useful in actuator-placement and symmetry-breaking design independently of any larger multi-input classification.

## Scientific limits

This is a precise theorem for one weighted edge, not a generic statement about all graph perturbations. Modular finite-instance checks are not infinite proofs. Nonlinear dynamics, multiple drivers, finite-horizon numerical conditioning and independent certification are outside the claim.

Self-review: passed. Independent audit: not yet performed.
