# Independent mathematical audit

## correctness

PASS

For the specified cut, squaring on the hub sector gives diagonal u at the first site and u+v elsewhere, with upper off-diagonal q=t·conj(s). The Fourier band follows and Cauchy–Schwarz gives c^2<=uv. Although the frozen proof says each row has a private block, adjacent rows actually share blocks; full rank follows immediately by taking the first arm column of each cell to get an N-by-N lower triangular submatrix with diagonal J1>0. Thus there are exactly 2N dark zero modes in finite volume. For c>0 the gauge-reduced half-line recurrence has no square-summable solution in the band including its edges (unit-modulus roots, with a possible linear prefactor at an edge); subtraction of the boundary and interior equations for a decaying root gives r=-conj(q)/v and lambda=u-c^2/v. It exists only for c<v, including at c=0 by direct diagonalization. A positive lambda yields both chiral signs; lambda=0 gives exactly one extra hub kernel vector in addition to the arm kernel. No above-band solution satisfies the boundary condition. For finite N, subtract the infinite-volume lower edge and conjugate by alternating signs; the matrix is c times the N-site Dirichlet path Laplacian minus v e_0 e_0^T. The positive definite Laplacian has endpoint inverse entry N/(N+1), as is seen by solving for an affine profile with zero at the far exterior point. Congruence by its inverse square root leaves N-1 positive eigenvalues and one whose sign is the sign of 1-vN/[c(N+1)]. This gives the strict finite criterion, its equality case, and the count; the detached squared value stays positive by finite full rank. The equal-hopping absolute cosine has no second crossing on [2pi/3,pi], since c<=J^2 there and the finite threshold exceeds J^2. Near zero flux, v-c=J^2 phi^2+O(phi^4) gives log(v/c)~phi^2/3 and exact squared gap (v-c)^2/v; the sum of positive energies is 2 sqrt(2) J phi+O(phi^3), giving the stated cubic energy gap. The independent bounded computation (`python3 /workspace/branches/independent_checks.py 3`) diagonalized 15 full chiral matrices with exact-threshold designs (evaluated numerically), both sides, caging and nonreal phases, and symbolically verified the cubic limit for J=1. It does not prove the general spectral result. Scope is the stated termination with no extra right hub.

## originality

PASS

The motivating paper already has the exact two-flux lattice, bulk bands and open-boundary propagation. More strongly, arXiv:1201.2886 §3 already gives the exact gauge-reduced half-line squared-energy boundary theorem; that component is covered, not a new Jacobi bound-state classification. The supported distinct physical result is the termination-specific finite strict spectral cutoff together with the finite/half-line weak-flux laws and treatment of the zero-energy collision in the chiral model. The finite analysis uses a standard rank-one criterion but must evaluate it at the infinite bulk edge and identify the physical parameter region. No checked result was shown to cover that combined physical finding. This is a bounded assessment, not a first-discovery claim.

## value

PASS

For the exact engineered cage, finite detachment and infinite surface localization are different experimental constraints. The length-dependent cutoff and the inverse-square localization-length versus cubic energy-isolation laws distinguish two reasons a finite weak-flux sample may not show a resolved end mode. Counting one additional hub zero mode rather than a nonzero pair at the collision is important in the presence of extensive flat zero bands. These physically interpretable boundaries are useful beyond the known discrete Robin eigenvalue, with no claim about other end cuts, disorder or propagation dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
