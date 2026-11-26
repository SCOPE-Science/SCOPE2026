# Independent mathematical audit

## correctness

PASS

With a≠b the contrast projectors on each leaf class have eigenvalues a,b respectively when the respective contrasts exist. The cell-constant Laplacian has simple spectrum consisting of 0 and the roots of z²−[(p+1)a+(q+1)b]z+(p+q+1)ab. Its discriminant is ((p+1)a−(q+1)b)²+4pqab>0 and evaluation at a,b gives the stated nonzero quantities. Thus full spectral projectors do not mix bright and dark sectors. Squared profiles of the three rank-one bright projectors have the rank of the scaled diagonal-moment matrix because the spectral Vandermonde is invertible. The restriction in orthonormal cell coordinates uses multiplicity-square-root factors on the profiles (the rank statement is unchanged). Subtracting the center row in the displayed moment matrix and expanding gives ab[a(p−1)(p+1−q)−b(q−1)(q+1−p)]. Its first term determines the strict sign if p>q (the second is nonnegative after subtraction), likewise the second when p<q; p=q≥2 leaves (p−1)(a−b). Therefore the bright block is positive definite for all unequal a,b with at least three leaves. Dark Schur squares act on their contrasts by 1−2/m, so exactly the two-leaf contrasts survive in the kernel. For a=b one must first merge full projectors: the two independent uniform-star bright profiles and the dark contrast eigenvalue 1−2/(p+q) give positive definiteness when p+q≥3. For p=q=1 all three Laplacian eigenvalues are simple also at a=b (0,a,3a). The proposed vector annihilates all three diagonal moment columns and hence all squared profiles; a real eigenvector orthogonal to the constant vector on the three vertices cannot have three equal nonzero squared coordinates, so at least two profiles are independent. The frozen checker was inspected, not executed; the independent `python3 /workspace/checks/frozen_math_checks.py 2` passed the symbolic determinant identity and full-Laplacian checks on nine representative profiles, including equal weights, two contrasts, and the weighted boundary. Numerical projectors are not a certificate for near coincidences or arbitrary conductances; the exact argument handles those regimes.

## originality

PASS

Distinct earlier local records mechanically cover the uniform case and exhibit the size-two dark contrast mechanism for adjacency double-stars. Do not credit these as new. The supported distinct result is the exact rank and complete kernel classification for unequal conductances of the combinatorial-Laplacian star, including its unequal three-vertex boundary; the earlier results do not imply that classification.

## value

PASS

Rank and the visible zero modes are natural spectral invariants of the long-time walk, not arbitrary statistics. Splitting one conductance into two strictly introduces exactly the contrasts of size-two classes, independent of the contrast magnitude in conductances; exact equal-weight coalescence changes the projector structure and can remove the nullspace. The theorem specifies when class symmetry causes a genuine loss of average-mixing rank and rules out hidden bright modes, a useful exact benchmark beyond the already covered uniform star.

The dated certificate retains the supplied scientific assessment, sources and limitations.
