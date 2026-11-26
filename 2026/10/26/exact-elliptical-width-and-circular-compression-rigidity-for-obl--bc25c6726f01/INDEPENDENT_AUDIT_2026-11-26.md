# Independent mathematical audit

## correctness

PASS

After translating the spectrum by −z₀, a Schur eigenvector x of a compression imposes y perpendicular to x and Nx. For a 2×2 Schur form the smallest support radius about its symmetry center is half the magnitude of the off-diagonal entry, so the in-disk diameter is that magnitude. Maximizing it for fixed x projects N*x onto span{x,Nx}⊥; the centered normal vectors have squared norm V and inner product of magnitude |c|. Thus the squared objective is V−|c|²/V=4det(C)/tr(C) for the real planar covariance C. Symmetrizing opposite weights adds mmᵀ and strictly improves every positive-definite C with nonzero mean, since the harmonic-mean objective increases in both eigenvalues; degenerate C has zero objective. Centered weights give det(C)=D²(1−κ²) and tr(C)=A+2Bκ. The derivative has the opposite sign of Bκ²+Aκ+B, whose derivative is positive on [−1,1]; its unique interior zero is −2B/(A+h), with objective 8D²/(A+h). The projection witness is unique up to phase and its opposite-vertex squared moduli agree, forcing both Schur diagonals to vanish. The resulting nilpotent has disk radius Δ/2, and equality forces the same weights and companion direction for every maximizing plane; diagonal phases yield the orbit. Translation restores center z₀. Sababheh’s Theorem 3.2 supplies the separate positive-block bridge. The supplied numerical checker was inspected, not executed; its finite comparisons cannot prove the optimization or equality classification.

## originality

PASS

The supported distinction is the genuinely oblique case B≠0, with its exact value and nonuniform maximizing weights, and the accompanying full compression rigidity. The known B=0 rectangle, triangle disk phenomenon and general positive-block identity are acknowledged, not credited as new.

## value

PASS

This is an exact optimization of a motivated numerical-range invariant for a natural four-point family. It shows how obliquity changes the optimal distribution, and gives every equality plane rather than just the value or one witness. Through the existing identity it evaluates the sharp fixed-off-diagonal positive-block defect on that family. It does not claim the identity or the rectangular result as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
