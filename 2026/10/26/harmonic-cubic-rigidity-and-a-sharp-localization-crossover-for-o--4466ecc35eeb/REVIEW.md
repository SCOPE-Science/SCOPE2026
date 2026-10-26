# Scientific review

## Correctness — PASS

The estimator is reconstructed directly from the central two-point Stiefel formula. Antipodal symmetry removes the even part, orthogonality deletes cross terms in the squared estimate, and complete fourth/sixth spherical pairings yield an exact expectation. Orthogonal trace decomposition gives the strictly positive orientation-variance identity; a basiswise calculation verifies its zero-variance equality case. Rank-one sharpness follows from the exact sixth moment and extremal sixth-coordinate weights. Independent equal-variance evaluation noise contributes the same norm risk to both bases. The quartic example is globally strongly convex because its Hessian is bounded below by half the identity. The standalone rational-pairing verifier passed. Finite tests are not used to establish universal quantifiers.

## Originality — PASS (priority-limited)

Feng–Wang (2022) establish the estimator and general variance bounds and provide moment identities; the inspected full-text sections do not state the exact harmonic cubic variance/rigidity or the coordinate-localization crossover. Kozak et al. (2021) address random orthogonal search convergence and use forward directional differences. Berahas et al. (2019) compare gradient approximations and error bounds rather than an exact cubic third-derivative decomposition. The closest mathematical-record hit, *Exact Haar moments remove sampling-dimension restrictions in sparse stochastic subspace descent*, treats second Haar moments and rank-one quadratics, not this sixth-moment finite-difference truncation error. The general sphere-moment machinery makes the special case derivable and leaves a residual risk of prior specialized publication; no proof of worldwide priority is claimed.

## Value — PASS

A full frame removes the leading random projection variance, but cannot generally remove finite-difference cubic error. The exact nullspace characterizes when basis randomness disappears completely even for a nonzero cubic, while the sharp localization threshold answers which of two equal-evaluation-budget estimators has smaller error at a true strongly convex minimizer. Neither orthogonal-frame randomization nor fixed coordinates uniformly dominates the other; with dense rank-one directions, randomization can cost an asymptotic factor of fifteen, while with sparse directions it can improve the cubic-error risk by a factor growing quadratically in dimension. This is a motivated estimator-design boundary, not a claim about downstream iteration performance.

## Closest literature and residual limitations

Feng–Wang arXiv:2205.14737v1; Kozak et al. arXiv:2107.03941v1; Berahas et al. arXiv:1905.01332v1. The claim only concerns complete real orthogonal frames, cubic odd parts at a stationary point, exact central differences, and explicitly independent equal-variance oracle noise. General smoothness, incomplete frames, and publication priority outside the inspected sources remain unproved.

Self-review: passed. Independent audit: not yet performed.
