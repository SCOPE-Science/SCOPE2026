# Independent mathematical audit

## correctness

PASS

Write H=A^{1/2}Π A^{1/2} and I−Π=wwᵀ for one unit vector, rotate the two-dimensional unit-eigenspace of A, and observe the two retained nonzero H eigenvalues are 1 and λ=1+(k−1)s². The normalized Nyström preconditioner is P=I+(λ−1)uuᵀ/(1+m). The nontrivial generalized pencil (A+mI,P) has trace T and determinant D specified in RESULT, with z_-<1+m<z_+; κ=z_+/z_-. For positive roots ratio r>=1, T²/D=r+2+r^-1 increases with r. Independently symbolically verified the exact sign identity T²/D−(κ0+1)²/κ0=−(λ−1)G(λ)/[λ²(λ+m)(k+m)(m+1)²], and the substitution λ=(1+kt)/(1+t) converts (1+t)³G/(k−1) into a3t³+a2t²−a1t−a0. All a_i>0, so the cubic decreases then increases through exactly one positive zero. Endpoint λ=1 has P=I, λ=k ideal κ=1. Reconstructed exact k=4,m=1,Ω=[[1,0],[4,0],[0,1]] with H off diagonal 4/5, 2x2 generalized polynomial 26z²−161z+200, giving κ=(161+3sqrt569)/(161−3sqrt569)>5/2. Dense independently computed random/sketch pencils matched the sign classification. Gaussian full support and spectral continuity yield both open probability regions. For k→∞, m=1/k, λ=3/2 the exact trace/determinant limits yield ratio 32/27. Dimension two rank one has P=I and rank two is exact A, so no worsening. Analytical identities, not random trials, establish all-parameter theorem.

## originality

PASS

Frangella–Tropp–Udell give this very normalized Nyström preconditioner (formula 1.3) and bounds on expected κ once sketch rank scales with effective dimension; they do not promise per-sketch improvement and do not derive the three-dimensional exact crossover. Previous studies of eigenvalue inflation for different randomized limited-memory preconditioners do not imply this unique t_* for this exact normalization. Formula is prior, classification and worsening witness survive.

## value

PASS

The exact smallest-dimensional boundary between provably useful and harmful sketch subspaces is a motivated stability/counterexample result for an established preconditioner. It separates average sufficiently-high-rank guarantees from per-realization behavior and provides a reproducible spectral benchmark useful when interpreting low-rank solver failures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
