# Scientific review

## Correctness — PASS

The theorem concerns a normalized, independently refreshed Haar projection and response model. The exact projector orthogonality identity, elementary spherical second/fourth moments, and a strict \(W_4\) contraction establish existence and uniqueness among finite-fourth-moment invariant laws. Rotational symmetry then yields the exact radial fourth-moment fixed point; its marginal projection is determined by a spherical fourth moment, giving the factor \(3/(2d+1)\). The conditional-mean eigenvalue \(1-1/d\) gives the lag law and an exact geometric-series long-run variance. A standalone checker passed 1,068 groups, with exact rational arithmetic and four fixed-seed sample runs.

## Originality — PASS (best-knowledge, qualified)

The motivating full arXiv text of Bergou et al. (arXiv:2308.16904) studies frozen doubly-noisy matrices and right-hand sides, with second-moment convergence bounds. Gower–Richtárik (arXiv:1506.03296) provide the Gaussian Kaczmarz/sketch-and-project algorithm and its standard isotropic rate \(1-1/d\); that rate itself is not new. Agaskar–Wang–Lu (2014) concern exact MSE and optimized sampling; their PDF could not be fully read due an access error, so only the abstract was compared and this uncertainty remains. Recorded searches compared stochastic Gibbs/heatbath, normalized Gaussian directions, Kac-type thermostat terminology, and existing numerical-iteration findings. No inspected primary source or retrieved published scientific record supplied or implied the same non-Gaussian stationary fourth-cumulant coefficient jointly with the exact correlation-cost law. This is a qualified literature comparison, not an assertion that unindexed results cannot exist.

## Value — PASS

Non-Gaussian fresh measurement noise is a natural modification of randomized row-action solvers. Exact stationary MSE alone cannot detect heavy/light fourth-moment distortion, and matching covariance does not imply a Gaussian invariant law. The coefficient \(3/(2d+1)\) gives a dimension-explicit distribution diagnostic, while the competing \(2d-1\) correlation cost determines the effective variance of time averaging. The theorem supplies an exact benchmark for robustness and sampling efficiency across noise laws without presuming any general nonisotropic or frozen-data extension.

## Limitations and closest literature

The result is for independent Haar rows and independent fresh scalar responses with finite fourth moment, and does not claim actual Gaussian convergence or a stationary sampling CLT. The independent audit is unperformed. Specialized random-coordinate thermostat theory and the inaccessible detailed Agaskar–Wang–Lu text remain residual publication-priority risks.

Self-review: passed. Independent audit: not yet performed.
