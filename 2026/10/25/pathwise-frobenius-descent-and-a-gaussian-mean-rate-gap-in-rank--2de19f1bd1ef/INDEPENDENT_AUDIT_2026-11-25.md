# Independent mathematical audit

## correctness

PASS

In the frozen Aω≠0 regime, only the positive seed-supported eigenvalues enter the normalized weights p_i∝ω_i²a_i^(2q); the sole nonzero approximation eigenvalue is their weighted harmonic mean λ. For T=f(λ), U=Σp_i f(a_i), the error is tr(f(A)^2)+T²−2TU. Jensen for t↦f(1/t) gives T≤U. Differentiating the power weights gives twice the covariance with log a; this makes U nondecreasing and the weighted mean of 1/a nonincreasing, hence T nondecreasing. Local absolute continuity on the supported positive spectral interval justifies differentiating the error almost everywhere; E′=2(T−U)T′−2TU′≤0. In the continuous nonconstant operator-monotone subclass the integral representation makes the reciprocal profile convex, and strict increase gives U′>0 and T>0 on multispectral support. One distinct supported eigenvalue gives a constant error. The fixed-seed leading term follows from f(a)−U at order (b/a)^(2q) while (f(a)−T)² is smaller. Independently, for the two-dimensional Gaussian model the half-Cauchy ratio produces the stated rational integrals (the squared-denominator integral is −∂_a of the first at fixed r,b). Their average has a nonzero linear term in r=(b/a)^q, versus the almost-sure quadratic term. The exact counterexample gives λ₁=200/197 and λ₂=65/53 and errors 1 and 98/65. The u_q/ν_q notation in the spectral calculation is a harmless typo. The frozen script was inspected, not run, and no finite check is used for the real-power quantifier.

## originality

PASS

Credit Persson–Kressner's deterministic one-step transformed Frobenius descent under their operator-monotone structural hypotheses, and credit the earlier rank-one Gaussian trace formula as a close antecedent from which the squared-risk formula can be recovered by a moment identity. The supported distinct contribution is the all-real-power, all-admissible-seed rank-one descent principle for the broader reciprocal-convex scalar class, with strictness and a specific monotone-only failure witness. Do not present the operator-monotone unit step or the Gaussian rate mechanism in isolation as new.

## value

PASS

The surviving pathwise theorem provides a useful weaker condition than operator monotonicity for a nonlinear randomized low-rank construction and applies deterministically to every admissible rank-one seed and real power. A small exact counterexample identifies the failure of simple scalar increase, rather than only exhibiting a numerical anomaly. The mean versus typical calculation illustrates why pathwise improvement does not imply its pathwise exponent for Gaussian risk, while the value verdict does not depend on treating that mechanism as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
