# Scientific review: critical Poisson-field sampling

## Correctness — PASS

The conditional Poisson trajectory calculation supplies an exact finite-sample covariance and a uniform \(O(n^2)\) third Poisson trace moment. The resulting conditional characteristic-function error is \(O(n^{-1/4})\), independent of the observer trajectory. A parity-compatible local limit theorem and a uniform diagonal cutoff identify the Brownian heat-kernel variance functional. The functional central limit theorem for bounded triangular observer increments then yields joint convergence. The fixed-polynomial Poisson–Charlier residual is \(o_{L^2}(n^{3/4})\); the conditional covariance formula gives this without any independence assumption for sampled field values. The random limit variance is bounded, positive, continuous and nonconstant on Brownian path space, proving that the annealed limiting law is non-Gaussian. The covariance crossover is derived by a Gaussian integral. The included standalone exact checker passed 502 assertions, but the convergence proof, not the checker, establishes the infinite limit.

## Originality — PASS, subject to residual priority risk

Huang–Rang–Su, arXiv:2603.15308v1, treat fixed nonzero observer drift in Theorem 1.4; Appendix A gives the previously known \(n^{3/2}\) variance order and explicit zero-drift linear coefficient but explicitly does not settle Gaussianity (Remark A.7). The **joint critical-drift non-Gaussian mixture** here is neither their fixed-drift normal theorem nor their variance computation. Jaramillo–Murillo-Salas, arXiv:2512.02922v1, treat additive functionals of particle systems with deterministic spatial tests. Castell–Guillotin-Plantard–Pène–Schapira, arXiv:1002.1878, concern **static** random scenery and a different Brownian local-time mixing functional. Searches for equivalent critical drift and Brownian heat-kernel mixtures found no covering result, but a broader as-yet-unlocated conditional Poisson-integral theorem remains a priority risk. This assessment makes no assertion of uniqueness or independent priority certification.

## Value — PASS

The source paper explicitly leaves the rank-one symmetric-sampling distribution unresolved, making the limiting law a motivated gap, not a parameter substitution. Proving a **strictly non-Gaussian** annealed law clarifies why a variance-order obstruction reflects a genuine fluctuation-regime transition. The common Brownian variance functional describes both exactly symmetric sampling and the full finite diffusive-drift crossover for every first-rank polynomial; the explicit parameter-dependent second moment is a useful quantitative observable. The already known symmetric variance constant is expressly excluded from the new claim.

## Scope and risks

The limit requires independent stationary Poisson particle walks, symmetric particle steps, fixed \(\lambda>0\), fixed polynomial with nonzero first Charlier coefficient, and finite \(\kappa=\lim\sqrt n v_n\). It makes no statement about pure higher Charlier ranks, moving drift scales outside this window, general dynamic media, optimal error rates or independent verification. A broader prior theorem capable of implying the joint law could remain undetected despite the stated comparisons.

Self-review: passed. Independent audit: not yet performed.
