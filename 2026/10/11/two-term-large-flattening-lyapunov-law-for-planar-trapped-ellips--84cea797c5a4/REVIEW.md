# Review: Two-term large-flattening Lyapunov law for planar-trapped ellipsoidal billiards

## Correctness (C): PASS

The **stated ellipsoid** has Hessian \(\operatorname{diag}(2,2,2\beta^2)\); at equatorial impacts the unit-normal differential in the vertical direction is exactly \(\beta^2/r_i\). The source's plane-symmetric Poincaré matrices thus give the transverse positive cocycle with \(Q=\beta^2\). Direct division of its recurrences yields \(u_i\le Q^{-1}/a_i\) and an explicit \(O(Q^{-2})\) bound for the difference between \(u_i\) and \(Q^{-1}/a_i\). Expanding the exact one-step growth logarithm incurs at most \(3Q^{-2}/(a_*^2d_*^2)\), uniformly. The first transient vanishes in the ergodic average. Uniform boundedness of the planar block and a transverse lower growth bound establish which positive exponent is largest when \(Q\) is sufficiently large. No finite experiment is offered as infinite proof. Primary support: arXiv:2610.03004v1, §3 (matrices, coding, angle bounds); arXiv:2306.03611, §3 (Poincaré derivation).

## Originality (O): PASS

The 2026 ellipsoid paper provides a strict positive-exponent separation criterion and positive recurrences but neither the exact \(2\log\beta\) leading rate for its displayed geometry nor the geometric integral coefficients and uniform \(O(\beta^{-4})\) remainder. Its 2023 spherical predecessor treats a fixed isotropic curvature without the singular flattening regime; the 2023 deformation paper studies small perturbations, not this limit. Source-, curvature-, cocycle-, strong-coupling-, and alias-level searches found no same-statement or dominating general result in the checked works. An older general matrix-product theorem might entail the expansion, so this remains a real residual novelty risk. The argument is confined to the exact stated physical geometry, not to a typographic parameter reinterpretation.

## Mathematical value (V): PASS

This provides a quantitative spectral law for the motivating new hyperbolic billiard family, including a genuinely dynamical measure-dependent constant term and an explicit first curvature-correction integral from adjacent collision data. The universal uniform error turns qualitative exponent separation into a reproducible controlled asymptotic, permitting comparison across Gibbs states and configurations. Simply pointing out a curvature normalization would not provide these new coefficients. The result does not assert an optimized remainder, existence of other invariant measures, or new spectral bounds at moderate flattening.

## Closest literature and residual limits

The immediate comparison is Al Dowais–Stoyanov, *Some open billiards with distinct top Lyapunov exponents* (arXiv:2610.03004v1), equations (1.1), (3.1)–(3.9); the Poincaré construction is cross-checked in *Lyapunov exponents for open billiards in the exterior of balls* (arXiv:2306.03611), §3. A small-deformation comparison is Al Dowais, *Mathematics* (2023), 4633. Strong-coupling matrix-cocycle literature is the main residual originality risk and has not been exhaustively ruled out.

Same-model review: passed. Independent audit: not yet performed.
