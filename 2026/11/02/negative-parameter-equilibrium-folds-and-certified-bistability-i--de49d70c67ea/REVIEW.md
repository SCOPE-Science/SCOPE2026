# Scientific review

## Correctness: PASS
Direct equilibrium elimination supplies the same quartic as the primary paper, with all singular fibers handled explicitly. Its discriminant is checked symbolically against the published degree-eight polynomial, and an exact rational Sturm chain gives six sign variations at negative infinity and four at zero. Isolating signs, root counts at three rational parameters, and the two zero-coordinate exceptions yield the stated exhaustive diagram. At the explicit bistable parameter, a factorization into a linear and cubic factor proves that there are exactly two nonzero equilibria; Routh--Hurwitz positivity is verified symbolically for both. The script `check_negative_etm.py` recomputes all critical identities. Numerical observations are not substituted for infinite assertions.

## Originality: PASS under inspected material
The 2026 model preprint restricts its bifurcation analysis to nonnegative parameter and leaves negative values for future study, even though its quartic and exceptional equilibrium formulas apply algebraically there. Published record `997f2098aca6` proves an exact positive-threshold global-stability statement and prints the same discriminant, but is explicitly scoped to nonnegative parameters. The present result **does not** claim the discriminant itself as new. Its content is the two negative-root census, the treatment of negative exceptional fibers, and the exact two-sink witness at negative parameter. Searches of the primary preprint, published mathematical records, and public literature did not find that combination. General quadratic-flow conjugacies and unindexed later works are residual priority risks.

## Mathematical value: PASS
The authors identify the negative parameter branch as an untreated natural part of their polynomial benchmark. A complete equilibrium census is useful for organizing its bifurcations, and two rigorously stable coexistence states at one exact negative parameter demonstrate a previously unexplored multistability region rather than merely counting polynomial roots. No broad claim about chaotic attractors or global basins is made.

## Limits and closest source
The result depends on the printed ETM-3D vector field; it is not an exhaustive negative-parameter dynamical phase portrait. The closest literature is arXiv:2610.04768v1 and the positive-parameter result identified by record `997f2098aca6`. Independent historical and mathematical validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
