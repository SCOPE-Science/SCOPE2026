# Independent mathematical audit

## correctness

PASS

PASS: In every leading SPD Schur complement S, its variational characterization bounds mu I <= S <= L I whenever mu I <= A <= L I. Any live elimination multiplier is the off-diagonal/first diagonal ratio of a 2x2 principal submatrix of S. Diagonalizing its eigenvalues lambda and Lambda with q=Lambda/lambda<=kappa and rotating by tan(theta)=t yields |b|/a=(q-1)t/(1+qt^2), maximized at t=1/sqrt(q) with value (q-1)/(2sqrt(q)); monotonicity in q proves the universal dimension-free bound. The threshold for a column's original diagonal to be the largest magnitude is (kappa-1)/(2sqrt(kappa))<=1, equivalent to kappa<=3+2sqrt(2); the equality tie requires diagonal-retaining policy. The explicit real SPD A_kappa=[[2kappa,(kappa-1)sqrt(kappa)],[(kappa-1)sqrt(kappa),kappa^2+1]] has eigenvalues kappa+1,kappa(kappa+1) and attains the ratio; A_9=[[18,24],[24,82]] has exact eigenvalues 10 and 90 and forces pivoting with multiplier 4/3. Direct independent symbolic/numeric family and exact rational checks pass. This is a complete proof of all Schur stages, not merely a first-column bound.

## originality

PASS

SPD matrices are classically solvable without row pivoting, and the rotation/off-diagonal extremum is elementary. But the final claim is stronger than pivot-free existence: it sharply classifies the spectral condition-number regime where an ordinary generic partial-pivoting selection rule itself makes no interchanges, including the tight tie convention and a 2D forced-swap family. Inspected broader growth-factor literature does not state this condition-number frontier. Broyden full text was inaccessible, a material residual risk.

## value

PASS

A sharp, dimension-independent condition-number safety frontier for whether widely used generic partial pivoting will unexpectedly reorder rows of an SPD matrix is a natural, objectively measurable numerical linear algebra invariant. The theorem distinguishes existence/stability of pivot-free elimination from the observed pivot rule, resolves the boundary tie and supplies exact obstructions; the 2x2 inequality is elementary but the fully specified algorithmic classification is mathematically motivated, not arbitrary numerical slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
