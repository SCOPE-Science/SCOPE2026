# Independent mathematical audit

## correctness

PASS

The fixed pure-level Hermite-index cutoff r>=0, j<N has intensity 0<=rho<=1, total mass N in area-normalized u=pi|z|^2 coordinates. Thus its L1 discrepancy with the area-N disk equals exactly twice the sum of radial Laguerre-density tails P(U_{j,r}>N), not an approximation. From Laguerre Jacobi recurrence E[U]=j+r+1, Var(U)=2jr+j+r+1, and coefficient extraction from L_r^{j-r}(u) at u=j+s sqrt(j), the normalized edge density tends to phi(s)*He_r(s)^2/r! for fixed r. Weak convergence and a uniform Chebyshev k^{-2} cutoff bound justify the full sqrt(N)-scaled Riemann tail sum and give c_r=E|Y_r|. Mehler diagonal generating function yields sqrt(2/pi)*(1+t)^2/(1-t^2)^{3/2}, giving both even/odd central binomial formulas, strictly positive at every fixed level; Stirling gives c_r~4 sqrt(r)/pi in the sequential high-r regime. Independent numerical Hermite absolute moments for r=0..8 matched each exact closed coefficient to <3e-15. Finite quadratures are not asymptotic proof and no growing-r uniformity is asserted.

## originality

PASS

The directly same finite pure polyanalytic Ginibre ensemble is defined in Abreu–Gröchenig–Romero (2019), whose Theorem 1.2 proves only O_r(sqrt N) and explicitly states positive-level sharpness is expected, not proved; Theorem 1.8 supplies radial law, not the global exact L1 constant. Haimi–Hedenmalm local edge kernels and Haimi–Wennman fluctuation CLTs do not present this fixed-index global error. Novelty rests on the evaluated limiting tail sum, not known Laguerre or Hermite identities.

## value

PASS

For pure finite polyanalytic Ginibre ensembles, an existing primary paper gives a sqrt(N) upper bound and explicitly raises sharpness at positive Landau levels as an open quantitative expectation. The exact strictly positive coefficient for every fixed r resolves that natural gap, producing a closed binomial sequence and its sequential high-r behavior. This is structurally meaningful thermodynamic edge information for canonical determinantal ensembles rather than a re-tabulation of normalized Laguerre densities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
