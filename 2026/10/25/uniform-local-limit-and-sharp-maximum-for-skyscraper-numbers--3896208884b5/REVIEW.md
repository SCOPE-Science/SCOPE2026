# Independent mathematical audit

## correctness

PASS

The exact Khovanova–Lewis coefficient f_n(a,b)=[n−1 choose a+b−2]binom(a+b−2,a−1) implies the normalized bivariate PGF ∏_{j=0}^{n−2}(j+z+w)/(j+2). Each factor gives an independent increment in {(0,0),(1,0),(0,1)} with probabilities j/(j+2),1/(j+2),1/(j+2). The means of both record counts are H_n; variances H_n−H_n^(2)~log n, covariance 1−H_n^(2)=O(1). On Fourier scales θ=u/sqrt(log n), φ=v/sqrt(log n), cumulant sums give a standard independent two-coordinate Gaussian limit. Uniform domination is obtained from |j+e^{iθ}+e^{iφ}|²=(j+2)²−2j(2−cosθ−cosφ)−2(1−cos(θ−φ)), so |φ_n|≤exp[−c log n(θ²+φ²)] on [−pi,pi]². Rescaled Fourier kernels converge in L1 by dominated convergence; inversion then gives a uniform absolute error over all integer phases, stronger than weak convergence. The closest-integer point establishes the modal asymptotic and any distant maximizer contradicts the Gaussian bound. An independent count of every permutation through n=8 matches all Stirling-binomial cells. The theorem does not give relative tail errors or exact finite-n modes.

## originality

PASS

Qualified best-of-knowledge PASS for the explicit skyscraper-uniform local limit and sharp modal asymptotic, not the underlying bivariate Stirling array or weak joint Gaussian. The full Khovanova–Lewis article supplies array and balanced modes; Gnedin 2006 has same array under an equivalent upper/lower record reinterpretation and weak Gaussian, but not lattice point control in inspected passages. A standard general-purpose triangular-array multivariate local limit could imply the result with hypothesis checks; do not claim a fundamentally new local-limit theorem. No explicit prior asymptotic for A218531 was identified.

## value

PASS

The maximum coefficient sequence is a natural, published skyscraper-permutation integer invariant (OEIS A218531). An explicit sharp leading constant 1/(2pi), factorial/logarithmic growth and localization of every maximizer answer a meaningful asymptotic enumeration question not determined by a finite table or a weak CLT alone. It does not claim a new generic local-limit method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
