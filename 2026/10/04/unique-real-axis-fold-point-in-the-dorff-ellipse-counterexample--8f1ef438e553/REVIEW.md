# Review of Unique real-axis fold point in the Dorff ellipse counterexample

## Correctness

PASS. The source gives exact rational constants for the two geometric coefficient tails and exact rational formulas for the analytic and co-analytic derivatives of the harmonic self-convolution. Reconstructing those formulas gives an exact factorization of the real-axis Jacobian into a quartic and a sextic over a denominator that is strictly positive on \((-1,1)\).

Exact Sturm counts show that the quartic has no root in \((-1,1)\) and the sextic has exactly one. Sign evaluation then proves the full orientation-reversal interval and the unique fold point. The packaged checker replays the calculation with rational arithmetic rather than floating-point root counting.

## Originality

PASS. The 2026 primary paper was inspected through Sections 5–8. It proves only a sign change between \(-99/100\) and \(0\), sufficient for existence of a critical point. It does not state uniqueness of the real critical point, the sextic governing it, or the full Jacobian sign partition on the diameter.

Published-finding database searches using the exact source, Dorff's problem, ellipse self-convolution, real critical points, Jacobian roots, and orientation reversal returned no implication-equivalent result. Earlier harmonic-convolution literature supplies positive univalence theorems under special dilatations but does not analyze this newly constructed ellipse.

The residual risk is that a later note or computational supplement could record the same root without being indexed by the searches.

## Value

PASS. The source's counterexample is proved by one sign sample and continuity. The new result identifies the actual one-dimensional fold mechanism completely: there is exactly one real critical point, and one entire boundary-side interval is orientation-reversing.

This is a natural quantitative classification of the fresh counterexample rather than an arbitrary numerical refinement. It isolates which factor of the self-convolution derivative causes the fold and provides a reproducible benchmark for proposed quantitative sufficient conditions in harmonic convolution theory.

Same-model review: passed. Independent audit: not yet performed.
