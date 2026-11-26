# Independent mathematical audit

## correctness

PASS

Orthogonal invariance reduces to diag(a,b). The squared first length is T d(U) with independent chi-square(2) radius T and arcsine first-coordinate square U. Given the first column, the projected second length is an absolute normal with scale R=ab/sqrt(d(U)); this scale depends only on U, so the conditional second-stop probability multiplies the conditional first-gate survival exp(-tau^2/(2d(U))). This supplies p0, p1, and the complementary rank-two probability. Inverting the decreasing angular map and differentiating gives the unconditional CDF and density, with R=b in the isotropic case; it is not the law among first-gate survivors. Eckart–Young makes both early stops false for tau<b; rank-one pruning cannot drop the only coefficient row because its norm is at least b. The large-kappa integral follows by dominated convergence with c=tau/b fixed; the integrand is positive off a null set and has positive integral. The replay python3 /workspace/review_replay.py qb conditions instead on the polar angle of Ag1 and integrates its elliptical angular density at 45 digits; for (4,1,.5) it gives p0=.030243501820034832886, p1=.25978949520339110013 and independently confirms the residual CDF at selected thresholds and J(.5)=.24712605614758927433. The coarse frozen quadrature at kappa=100000 is only a tolerance check: resolving the angular boundary layer gives a summed value .2471272683909951 rather than .247129436449459. This does not affect the theorem or its quoted finite-spectrum or limit illustrations. The exact-arithmetic decision law is not a claim that the original software handles its empty-output pruning branch, or a guarantee for larger blocks, reused probes, or relative tolerance estimates.

## originality

PASS

The distinct joint contribution on the accessed evidence is the adaptive one-column two-gate under-rank probability and its explicit nonzero high-conditioning limit, not the QR algorithm, the single fixed-residual Gaussian small-ball law, or angular Gaussian transformations considered separately. The closest earlier exact QB risk concerns rank over-retention after a two-column block, not premature stopping. General anisotropic Gaussian QR distributions are a meaningful alternate formulation and residual literature risk; no retrieved claim calculates this thresholded joint law with its fixed-c limit.

## value

PASS

This is the smallest nonsingular setting in which an accepted Gaussian sketch can adapt the basis before a second acceptance test. The shared first probe induces dependence that a fixed-residual estimator guarantee misses. Quantifying an exact under-rank error and showing that it persists as conditioning worsens for fixed tau/b gives a concrete diagnostic and calibration benchmark for the one-column method, without extrapolation to its larger-block implementations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
