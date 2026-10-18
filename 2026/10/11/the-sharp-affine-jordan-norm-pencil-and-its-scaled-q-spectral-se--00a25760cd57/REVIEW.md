# Independent mathematical audit

## correctness

PASS

For n>=2 the checked exact Gram decomposition Q_n-I=n(n+1) sum_{j<n}(n+1-j)(n-j)|x_j/(n+1-j)+x_{j+1}/(n-j)|^2 proves simple bottom eigenvalue 1. The tridiagonal sine recurrence and boundary equation give the displayed finite sine-sum stationarity identity; independently simplified its symbolic algebra to zero for arbitrary symbolic n,z, and recomputed top SVD stationarity with errors <7e-17 for n=2,3,4,5,8,12. For a fixed real unit top singular vector x at s=(n+1)/(2n+1), <B(s)x,(J-I)x>=0, so ||B(lambda)x||^2=gamma_n^2+|lambda-s|^2||(J-I)x||^2, strictly larger for every complex lambda!=s because 1 is not an eigenvalue of J. Exact tridiagonal eigenvalues give the stated gamma and gamma_2=4/5; compression and the constant-vector lower bound give monotonicity and gamma_n->1. Unit-circle symmetry/connected admissible pairs give W_q(J) a centered disk. A norm-attaining calibrated pair makes r_n(gamma)=gamma, the affine support inequality makes r_n(q)<q for q>gamma, and the same singular vector plus its orthogonal J component makes r_n(q)>q for q<gamma. Radius >=1 iff q<=gamma; von Neumann plus test p(z)=z gives the exact 1-spectral equivalence. The all-n proof is analytic, not extrapolated from finite SVD tests.

## originality

PASS

Statement-level comparisons against direct primary mathematical texts found no implication of this full exact claim in the inspected sources; separate specific comparisons below, with documented residual priority risks rather than a negative-search novelty proof.

## value

PASS

Exact unique unconstrained complex affine norm minimizer for every nilpotent Jordan size, together with the dimension-dependent optimal disk spectral-set transition; these are structural sharp invariants useful in ideal GMRES and operator-specific q-numerical range geometry, not merely finite numerical approximations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
