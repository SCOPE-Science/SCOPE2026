# Scientific review

## Correctness — PASS

The proof computes the exact uniform finite-element matrices and factors the Crank–Nicolson map through one tridiagonal resolvent. When the off-diagonal resolvent coefficient changes sign, a checkerboard similarity gives the necessary negative distance-two entries. Above the lower boundary an irreducible Stieltjes inverse makes every off-diagonal positive; the hyperbolic Green formula locates the minimum diagonal at endpoints. A sine-basis monotonicity argument proves exactly one upper cutoff, and Schur-complement monotonicity plus the limiting half-line Green function prove its finite-size growth and cubic limit. The polynomial recurrence, special smallest size, and the explicit positive rational witness at \(7/10\) were reconstructed and cross-checked. The exact-rational checker independently assembles and solves 90 parameter cases; it is not used to justify quantifiers over all \(n\).

## Originality — PASS (subject to indicated literature risk)

Primary source comparison: Faragó and Horváth, DOI 10.1137/050627241, Sections 4–6 including Theorems 6.4–6.5, give a broader DMP treatment with a familiar \([1/3,2/3]\) bound for uniform-mesh Crank–Nicolson. Their statements neither present nor imply the finite-size cutoff roots or limiting cubic for the fixed zero-boundary interior update. In particular, a strictly positive exact rational update occurs at \(z=7/10\), so positivity here is not determined by the sign of the right-hand-side coefficient matrix alone. Li and Huang, arXiv:1209.5657, Theorem 3.1, prove sufficient mesh/time-step conditions, not the sharp homogeneous finite-size criterion. Related published findings on filtered Crank–Nicolson and finite Markov generators address different maps. Literature searches over direct terminology, determinant/Green aliases, equivalences, and purported sharp bounds yielded no identical or dominating claim. The 2001 proceedings work cited by Faragó–Horváth and the 2005 hybrid-mesh article were not fully accessible; specialized coverage remains possible. This is a best-knowledge self-review originality assessment, not proof of uniqueness in the literature.

## Mathematical value — PASS

The result settles an exact natural positivity threshold for every size of a standard textbook discretization, quantifies the difference between the sharp invariant-cone property and a standard sufficient sign restriction, and gives its surprisingly nearly size-independent algebraic limit. The threshold is needed to distinguish actually positivity-preserving Crank–Nicolson steps from unnecessarily restrictive coefficient-wise criteria. This is a complete structural classification rather than a single finite numerical example.

## Scientific limitations

The claim concerns constant-diffusivity, source-free, uniform-mesh, homogeneous Dirichlet interior updates only. It does not cover arbitrary boundary forcing, nonsymmetric operators, nonuniform meshes, or a full maximum principle for general data. Some older related full text was unavailable. The self-review has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
