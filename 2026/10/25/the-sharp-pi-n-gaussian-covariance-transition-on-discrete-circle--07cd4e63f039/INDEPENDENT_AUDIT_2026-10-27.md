# Independent mathematical audit

## correctness

PASS

For integer N, K_N,c(j,k)=exp[-(c/N)d_N(j,k)^2] is symmetric circulant; its full DFT eigenvalues are real. The positive range c>pi is proved using wrapped infinite Gaussian periodization, whose frequency coefficients are strictly positive by Poisson summation; the omitted nonnearest wrapped images have uniformly small norm O(N exp(-cN/4)), while the least periodized eigenvalue is bounded below at scale sqrt(N)exp[-pi^2 N/(4c)]. For fixed c>pi the latter dominates the defect exponentially. In 0<c<pi, the near-antipodal mode k=2 floor(N/4) has a nonzero negative asymptotic coefficient of exp[-cN/4] (two different constants for parity classes), while its positive periodized component has exponent -pi²N/(4c) and is smaller; all four mod-four classes are covered. In the 4|N boundary window c_N(s)=pi-(log N+s)/N the Nyquist eigenvalue, after multiplication by exp(c_N N/4), approaches 2 exp(-s/2)-tanh(pi/2), so continuity supplies at least one sign-changing root with s tending to 2 log(2/tanh(pi/2)); finite-size uniqueness is not asserted. Independent 160-digit DFT calculations confirmed negative target eigenvalues at c=2.5 and positive *all* eigenvalues at c=3.75 for N=40..43,80..83,120..123; Nyquist zero shifts at N=80,120,200,320 converge toward the predicted constant. Earlier 75-digit root failure at N=320 was diagnosed as catastrophic cancellation and fixed with 160-digit arithmetic; it is not a physical counterexample. No claim is made for the exactly critical c=pi at fixed N.

## originality

PASS

Qualified novelty PASS for a sharp sampling-scale c=pi transition and logarithmically shifted Nyquist root in regular N-point cycle matrices. The 2023 Da Costa-Mostajeran-Ortega continuum theorem shows that the geodesic Gaussian kernel fails positive definiteness on the full circle at every *fixed* bandwidth, by considering arbitrarily large sets; their discretized witness operates in a different regime with continuum circle metric and fixed parameter, equivalent to exponent -mu j²/N² rather than present -c j²/N. Its negative-all-scales conclusion for the *whole circle* does not prevent positive definiteness on a chosen finite N-point set with bandwidth growing as N. Wood 1995 concerns continuous positive-definite truncation on a fixed circle, with full text unavailable, leaving genuine priority risk. No earlier sharp pi sampling threshold or local root correction was found.

## value

PASS

The sign of all Fourier eigenvalues of the natural geodesic Gaussian covariance matrix on a regular cycle is a substantive spectral/covariance validity invariant. Locating the sharp asymptotic balance of wrapped Gaussian positivity and antipodal folding negativity at pi and the logarithmic Nyquist scaling window gives a motivated nontrivial boundary not obtainable from a textbook DFT alone. The result is for the specified discrete regular samples, not an unsupported general kernel claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
