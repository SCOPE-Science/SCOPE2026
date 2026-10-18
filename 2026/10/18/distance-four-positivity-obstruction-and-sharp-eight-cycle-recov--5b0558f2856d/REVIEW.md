# Review: Distance-four obstruction and eight-cycle Padé recovery

## Correctness — PASS

The exact update is an analytic matrix function at zero and is well-defined for nonnegative step sizes because the Laplacian eigenvalues are nonnegative. The fourth Taylor coefficient of \((1-z+z^2/2)^{-1}\) is \(-1/4\); graph distance four kills every earlier off-diagonal coefficient and forces the strictly negative fourth coefficient from the count of four-edge geodesic walks. Positivity for every step on \(C_3,\dots,C_7\) follows from the displayed complete finite rational certificates with strictly positive-coefficient numerators and denominators. On \(C_8\), the only possibly negative distance kernel has the factor \(4h^4+22h^3+17h^2-1\), strictly increasing across its unique positive root. Spectral convergence to the strictly positive stationary projector handles the general large-step regime. The exact symbolic verification program directly reconstructs the matrices and checks 259 assertions. All infinite-size statements are analytical; computation is confined to the finite cases explicitly certified.

## Originality — PASS, subject to residual comparison risk

The full inspected 2010/2012 positive-system Padé papers concern diagonally indexed approximants and general positivity conditions rather than this \([0/2]\) graph-distance and cycle-specific threshold. Published results for \([2/2]\) eight-state CTMC birth chains and backward-Euler-filtered Crank–Nicolson use different rational maps; numerical coincidence of an eight-state obstruction has no implication by itself. Itkin–Kazbek 2026 treats precisely \([0/2]\) and demonstrably establishes **eventual positivity** above a bound: that component is not claimed as original. Its full text was inaccessible, so exact \(C_8\) coverage cannot be conclusively excluded. The 2004 Wade–Khaliq–Siddique–Yousuf Padé paper was available through its publisher abstract, not its full proofs; an older equivalent specialization is possible. Targeted primary-literature, published-finding, and local-claim searches did not identify the complete three-part statement. The asserted originality is restricted to the sharp finite-cycle classification, its small-step graph-geometric explanation, and the exact algebraic recovery boundary.

## Value — PASS

The issue is not a numerical rounding exception: the method is second-order, mass conserving, symmetric, and positive definite, yet graph diameter alone can force an unphysical negative transition at arbitrarily small positive steps. The classification identifies an exact seven/eight-vertex change of behavior and supplies the exact admissible-step set at the first obstructed periodic network. This is a meaningful boundary for the applicability of a natural L-stable rational heat integrator, not a routine renormalization or a recomputation of a known numerical table. The graph-distance argument also explains structurally why shrinking the time step fails.

## Limitations and closest literature

The known large-step positivity theorem of Itkin–Kazbek is intentionally credited. No claim is made of a single threshold for longer cycles, a converse to the diameter-four obstruction on arbitrary graphs, nonlinear positivity, or positivity in floating-point arithmetic. Access to the full 2026 Padé-specific article and the 2004 historical paper was limited; these are real prior-coverage risks, not evidence of novelty. Independent mathematical validation is not available.

Self-review: passed. Independent audit: not yet performed.
