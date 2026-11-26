# Independent mathematical audit

## correctness

PASS

The dark-then-light return map is affine with multiplier exp(-(ar+b(1-r))h)<1. Its fixed point strictly lies between zero and c. The positive drop Delta over the dark segment equals the gain over the light segment. Integration of the two ODEs gives m=c(1-r)+Delta(1/a-1/b)/h, with Delta=c(1-exp(-arh))(1-exp(-b(1-r)h))/(1-exp(-(ar+b(1-r))h)). The hyperbolic cotangent form follows algebraically. For k>0 the sign of the derivative of h*coth(kh) is the sign of sinh(kh)cosh(kh)-kh, strictly positive. Thus b>a makes m strictly decreasing, and an absolutely continuous H gives strictly positive variance of m(H). In phase t/h the paths are uniformly bounded and Lipschitz since h<=T, including across joins. The product at a fixed lag has the same uniform control. Finite Fejer approximation, the substitution nu=1/h preserving integrability of the density-weighted Fourier coefficients, and Riemann–Lebesgue give the inner covariance limit E[R_H(s)]-(E[m(H)])^2. The energy of the nonzero conditional autocorrelation harmonics is summable, bounded by c^2 by Parseval. Thus the expected tail is uniformly summable, each expected nonzero harmonic tends to zero by Riemann–Lebesgue, and precisely E[m(H)^2] survives in the uncentered term. This proves the successive limit, not a joint limit or a renewed-period result. Inspected frozen RESULT.md lines 16–64, VERIFICATION.md and verify_photobioreactor.py. The NumPy/SciPy script was not run; finite quadrature and its loose covariance tolerance are illustrative, not evidence for the limits or for strictness.

## originality

PASS

The supported distinctive claim is the fixed-lag covariance limit and its strictly positive long-lag plateau for this quenched model. The cited primary paper already publishes the period mean in equivalent parameters, gives the harmonic tools, and identifies a distinction between the variance of the zero mode and limiting one-time variance; the simplified mean formula alone is not credited as a new mean. The source's one-time results and the related indexed examples do not identify the two-time residual or prove strict dependence of the period mean on h. The extra analysis is to phase-average a shifted product, remove lag harmonics while keeping the quenched zero mode, and prove that this zero mode has positive variance for every allowed density. No inspected statement provides that full implication.

## value

PASS

The theorem answers whether random continuous timing eliminates persistence in the ensemble. It separates within-cycle fluctuations that dephase from between-period heterogeneity that survives and proves the survivor is strictly positive even for densities supported on small or disconnected sets. This is a specific, analytically interpretable temporal observable for the motivating model, not a restatement of the single-time variance or a numerical fit. It makes no empirical photobioreactor claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
