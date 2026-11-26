# Independent mathematical audit

## correctness

PASS

Right singular-vector coordinates and division by the smaller population eigenvalue reduce the sketched Gram law to a real 2-by-2 sample covariance with population diag(K,1), K=kappa². Gram–Schmidt gives the stated independent chi-square/normal variables and the beta–gamma factorization gives independent X and R. With positive eigenvalues, the trace/determinant test is precisely R≥h(X); conditioning proves the beta integral (the integrand is zero off h<1). I independently checked the sharp asymptotic without assuming a local limit. Put T=tau², write the two eigenvalues as rb,b and the leading eigenvector direction as theta modulo pi. The real symmetric matrix Jacobian is b²(r−1), and the normalized Wishart density has factor b^(s−3) r^((s−3)/2) exp(−sbL/2), where L=1+r/K+(1−1/K)(r−1)sin²(theta). Integrating b gives exactly p_s=(s−1)/(4 pi) times the integral of (r−1)r^(−3/2) exp(−sF) over 1≤r≤T and −pi/2≤theta≤pi/2, where F=log(sqrt(K)L/(2 sqrt(r)); the coefficient follows from gamma duplication. The unique minimum is (T,0): F(r,0) is strictly decreasing since r≤T<K, while orientation adds a nonnegative log term that is strictly positive off theta=0 for r>1. Near it F−I has leading terms a(T−r)+beta theta², with a=(K−T)/(2T(K+T))>0 and beta=(K−1)(T−1)/(K+T)>0. These terms also supply a positive linear/quadratic lower bound in a fixed neighborhood; its compact complement has a strict phase gap. Endpoint scaling and dominated convergence give C=(T−1)/(4 pi T^(3/2) a) sqrt(pi/beta), the frozen multiplier. The optimal positive scale is b=2K/(K+T), giving the displayed unique Gram rate minimizer. 'Most likely' here is the stated large-deviation notion, not a finite-s density-mode claim. The Krylov matrix has determinant rho>0 and two unit columns in the example with the claimed inner product. This reconstruction covers s≥2 for the exact law and fixed 1<tau<kappa for the asymptotic; it does not require or certify the uploaded simulation, which was inspected without execution.

## originality

PASS

Classical real Wishart density, gamma factorizations and condition-number statistics provide the base law; an exact integral representation by itself is not credited as a new distribution family. The supported distinctive result is the fixed unequal-population-eigenvalue sharp tail with explicit polynomial exponent, full curved-boundary multiplier, and unique scale and orientation for the Gram saddle in a sketch-certification problem. Actual inspected related claims use a different limiting parameter, local alternatives, or the adaptive monitoring procedure without the sharp fixed-basis failure law.

## value

PASS

A screening probability is naturally needed to interpret sketch-based conditioning decisions even before considering adaptive paths. The sharp prefactor and explicit Gram optimizer quantify the mechanism and probability for a fixed pair, beyond applying a norm-concentration inequality or quoting a Chernoff rate. The beta integral independently provides finite-s calibration; no adaptive numerical-stability claim is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
