# Independent mathematical audit

## correctness

PASS

For G(n,m), condition X=degree(v)=x; a shared edge vw is Bernoulli(x/s), while the degree contribution from the remaining t=M-s edges is an independent Hypergeom(t,s-1,m-x) variable. The conditional falling-factorial moment is polynomial in x with leading coefficient rho_j=(-1)^j(s-1)_j/(t)_j+(-1)^(j-1)j(s-1)_(j-1)/(s(t)_(j-1)). Reversibility of the exchangeable degree pair makes this conditional expectation operator self-adjoint on the one-degree hypergeometric measure; polynomial filtration plus orthogonality diagonalize all Q_j with eigenvalues rho_j. The histogram covariance is n times identity plus n(n-1) times this exchangeability kernel on centered scores; j=0 is constant, j=1 gives zero because 2m deterministic, and all j>=2 have lambda_j=n[1+(n-1)rho_j], independent of m apart from support r. Independently enumerated all simple fixed-edge labeled graphs for (n,m)=(4,2),(5,3),(5,5),(6,7), computed exact covariance and normalized spectra; observed (4,2):2.666667; (5,3):4,7; (5,5):4,4,7; (6,7):5.2,5.342857,6.142857,7.4 plus the two zero modes. Boundary singleton support treated as zero and n>=4 ensures denominator support.

## originality

PASS

Best-of-knowledge originality PASS after fresh published findings search and mathematical comparison of alias objects, stronger coverage, exact tables, and prior-result implications. Known general tools are credited, rather than claimed anew; risk remains documented: An older bivariate multivariate-hypergeometric Lancaster/Hahn kernel formula could encode the same spectral coefficients under another formulation; only related abstracts/sections were available, so historical priority remains uncertain.

## value

PASS

This gives an exact, all-polynomial-degree and all-edge-count diagonalization of the degree-histogram covariance of the most basic fixed-size random-graph model. Independence of every nonzero weighted eigenvalue from m, except truncation, is a substantial structural invariant and enables precise linear-statistic variances rather than merely an asymptotic approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
