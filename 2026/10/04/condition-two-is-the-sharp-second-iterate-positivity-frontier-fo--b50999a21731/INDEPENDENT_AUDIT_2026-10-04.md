# Independent mathematical audit

## correctness

PASS

The second MINRES iterate has x^(2)=c_0 b+c_1 Ab. Solving its normal equations and expanding spectral moments pairwise gives c_1<0 and theta=c_0/(-c_1) as an exact positive-weight average of pairwise eigenvalue sums, hence theta>=2mu. Therefore x^(2)=beta(theta I-A)b is entrywise nonnegative on a Stieltjes matrix when L<=2mu. The diagonal three-mode family yields the exact threshold formula for theta<kappa and the displayed kappa=4 negative coordinate. In dimension two the Krylov space reaches the exact solution by the second step. Independent exact arithmetic reproduced c_0=243/200, c_1=-67/200 and x_3^(2)=-1/80.

## originality

PASS

MINRES primary literature establishes residual minimization and norm/error monotonicity properties, including on positive-definite systems, but the inspected sources do not state coordinatewise positivity on Stieltjes systems or the sharp kappa=2 second-iterate threshold. The pairwise-spectral-sum barycenter identity used here is not an implication of the norm monotonicity results, and Resultary searches found no equivalent orthant theorem.

## value

PASS

The second MINRES polynomial is a natural first nontrivial residual-minimizing Krylov approximation. Identifying an exact spectral-barycenter structure, the sharp Stieltjes conditioning threshold, and the minimal dimension for sign loss gives a motivated coordinatewise invariant distinct from standard norm convergence theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
