# Scientific review

## Correctness

**PASS.** The estimator follows by exact importance integration of the linear-interpolation residual. The quadratic residual has shape \(u(1-u)\), and the beta density makes the weighted correction deterministic. A uniform cubic Taylor expansion after interpolation, the exact beta variance \(1/20\), and independence give the sharp \(m^{-7}\) variance constant \(1/25920\). The proof separately establishes uniqueness over positive fixed importance densities, Lindeberg convergence, and Hoeffding's inequality. A reproducible rational verifier checks the identities. Computation does not replace the analytic argument.

## Originality

**PASS, qualified.** The closest inspected methods are Kunsch's independent uniform residual stratification, Wu's randomized trapezoidal quadrature, and the broad adaptive importance-sampling/control-variate construction of Leluc and coauthors. They establish context or broader technique but their inspected statements do not directly give the exact beta-residual quadrature, its simultaneous sharp uniqueness, variance law, CLT and concentration result. Established zero-variance importance-sampling principles are acknowledged, not represented as new. Relevant published-result searches found no directly equivalent statement; an unlocated equivalent formulation in the wider quadrature literature remains possible, and independent publication-priority review has not occurred.

## Value

**PASS.** With only endpoint linear interpolation and one independent interior sample per cell, the rule annihilates quadratic residual noise, increases the smooth-integrand variance exponent from five to seven relative to uniform residual sampling, and provides exact asymptotic constants and a nonasymptotic concentration certificate. The comparison addresses a natural sampling-design question without claiming global optimality among arbitrary quadrature algorithms. Numerical stability at samples close to endpoints is not established.

Self-review: passed. Independent audit: not yet performed.
