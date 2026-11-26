# Independent mathematical audit

## correctness

PASS

For the stated orthonormal input matrices, the three generating vectors are linearly independent, so their joint sketch has everywhere positive Gaussian density. Keeping the sign on the p-side normalization gives the two residual projection coefficients h/z and k/z, the residual pivot d=v-hk/z, and the triangular output matrix in the orthonormal frame [e_1,e_3]. Both pivots are nonzero almost surely by the nonzero polynomials z and zv-hk (evaluate at a=b=e_1,g=e_2). The product of the singular values is 1/sqrt(|zd|) and the first column has norm 1/sqrt(|z|), giving kappa>=sqrt(|d|/|z|). At a=e_1,b=e_2,g=e_1+e_2 in sketch space, z vanishes transversely while h and k equal 1. On the small box in the coordinates replacing b_1 by z, the inverse Jacobian is bounded and the transformed density bounded below. The event 0<|z|<epsilon therefore has probability at least a positive constant times epsilon on that box. There |d|>=1/(8|z|) for sufficiently small |z|; taking epsilon=1/(sqrt(8)t) gives the lower tail and integrating gives divergence at r=1 and above. This works already in s=2 and for any finite larger s. The ordinary cross-Gram is diag(1/sqrt(2),1); the ordinary output has column norms 2^(1/4),1. The repaired background scalar formula agrees with Gaunt by gamma duplication, and its parallel case reduces to a signed chi-square. Separate exact rational witness checks at z=2^(-j), j=4,7,10, gave squared lower bounds 240, 16256 and 1047552; those checks are not the probabilistic proof.

## originality

PASS

The original's separately stated first-pivot density and sharp inverse-moment result are already covered: Gaunt's equation (2.3) with unit marginal variance and averaging over the s sketch rows gives the exact coefficient; the cutoffs follow by local integration, or by a chi-square law in the parallel case. That component of the original Finding does not pass. The supplied repair narrows the Finding to the two-column unconditional condition-number theorem and moves the scalar facts into explicitly credited background. The repaired claim survives the statement comparison: neither the exact single-pivot law nor the closest scalar-risk analogues cover the two-sided condition number with the fixed well-conditioned inputs. The repair changes RESULT.md and the corresponding scientific verification notes; the checker does not require changes.

## value

PASS

The repaired claim isolates a concrete failure of unconditional average-case conditioning for a randomized numerical process on benign deterministic inputs. It is uniform across finite sketch sizes, including oversampling above the ambient dimension, and explains why a finite first-column expected norm or good typical conditioning need not deliver finite mean for the basis. The rare near-zero pivot and second-column Schur term are an explicit mechanism, not a pathological choice of initially ill-conditioned bases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
