# Self-review

## Correctness — PASS
The proof works over every odd prime power. The identity \(X^2=Q(X)I\) leads to the exact restricted-power criterion; the primitive-cone lifting count is proved, including the base count and nonvanishing gradient, and yields the full formula. The maximum-height witness is explicit. The asymptotic argument uses exponential bounds obtained from the same exact formula. An independently implemented polynomial-matrix-power enumeration covers six small prime-field truncations, with actual execution ending in `VERIFY_OK`.

## Originality — PASS against checked material
The closest published structural result, Chaffe–Topley (arXiv:2311.08208), Proposition 3.4, determines which elements are eventually restricted-nilpotent, not the kernel sizes at each iterate, maximal height, or logarithmic concentration. Their index results concern stabilizer dimensions. Zordan (arXiv:1608.05725) studies adjoint orbits over mixed-characteristic local quotients, not restricted-power-height layers in equal characteristic. Known finite-field quadric counts and smooth lifting are used as ingredients, not claimed as contributions. Published-record searches targeting restricted heights, truncations and aliases returned nearest results concerning unrelated adjoint-rank spectra and Jordan-block lifts; no direct implication was identified.

## Value — PASS
The successive nilpotent-cone filtration \(\{X:X^{[p]^k}=0\}\) is a canonical restricted-Lie invariant relevant to modular nilpotent cones and support-variety questions. It is finer than merely detecting eventual nilpotence and is determined exactly in every truncation length and odd characteristic. The deterministic maximal height and logarithmic typical law distinguish exceptional and generic layers in this infinite family.

## Closest literature and residual risks
The explicit distributions could be rederived by a sufficiently strong general theorem about restricted powers on jet schemes of smooth quadrics, or by a not-yet-located enumeration in another terminology. This is a residual originality risk, not independent validation. Only six prime-field finite examples were exhaustively checked; extension to all odd prime powers follows by the algebraic proof.

Self-review: passed. Independent audit: not yet performed.
