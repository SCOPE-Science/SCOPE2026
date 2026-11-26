# Independent mathematical audit

## correctness

PASS

The coordinates of X need not be independent; only the unit-retention decisions and original copies are independent. The pgf is F(1+(z-1)/n)^n and the Hessian of log F at 1 is K=Cov(X)-diag(lambda). For S=sum |z_i-1| <= epsilon n, the logarithm branch at 1 gives an exponent error at most C S^2/n, so multiplying the pgf difference by n leaves growth at most C S^2 exp(C S). Outside that region, bounded support gives |F(1+(z-1)/n)|^n <= exp(B S), and n<=S/epsilon. This gives a bound uniform in n over complex z. Cauchy's formula with radii 1+k_i/(C+1) and k_i!<=k_i^k_i bounds the coefficients of the signed difference times n by a polynomial in |k| times A^|k|/prod k_i!. After division by the positive product-Poisson masses this yields a single L^2(Q) envelope. The pointwise density correction has diagonal Charlier-2 coefficients K_ii/(2 lambda_i^2) and off-diagonal products of Charlier-1 coefficients K_ij/(lambda_i lambda_j). These terms are orthogonal under Q, with Charlier-1 norm squared lambda_i and Charlier-2 norm squared 2 lambda_i^2. The bound 0<=u log u-u+1<=(u-1)^2, including u=0, and the quadratic Taylor coefficient 1/2 justify the entropy limit by dominated convergence. Subtracting the exact marginal entropy terms leaves precisely the off-diagonal total-correlation coefficient, also when some or all K entries vanish. In the example each marginal has mean and variance 1, while cross covariance is 1/n. The marginal log pgf expansion has zero quadratic term and starts its discrepancy at cubic order; inside S<=epsilon n, n^2 times the pgf error is therefore bounded by C S^3 exp(C S), and outside use n^2<=S^2/epsilon^2. The same coefficient argument and entropy bound give the claimed O(n^-4) marginal rate; equidispersion alone is not the proof of that bound. The frozen finite diagnostic and log were inspected, not executed or used to justify the limit.

## originality

PASS

Best-of-knowledge pass for the exact vector KL coefficient and the resulting total-correlation law for arbitrary fixed bounded count vectors under independent unit thinning. Scalar Charlier/entropy antecedents and multivariate Poisson approximation are substantial background. The example's marginal rate has a stronger scalar indexed counterpart, so that piece is not credited as distinct.

## value

PASS

The joint theorem quantifies the leading information left after independent unit thinning for a natural bounded cluster model. The exact cancellation separates marginal misfit from dependence; the equidispersed example has a genuine order-n^-2 joint signal invisible to that order in every marginal. This is a sharp effect for arbitrary fixed type covariances, not simply another metric bound or scalar normalizing calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
