# Scientific review: scalar interval finite-memory stabilization

## Correctness

**PASS.** The companion characteristic polynomial is derived directly from the scalar update. Static optimality follows from the exact endpoint maximum. The constructed two-tap controller factors the characteristic polynomial into a quadratic with nonpositive discriminant and additional zero roots; this establishes an exact common spectral radius on the full interval. The universal lower bound is proved by sending the exterior-disk Laurent image through the normalized inverse Joukowski conformal map, obtaining a disk self-map with derivative \(t/(2R)\). Schwarz's lemma forbids \(R<t/2\). Its equality case also forces the unique Laurent coefficients of every optimizer. No numerical finite-grid observation is used as an infinite-family proof.

## Originality

**PASS, with residual bibliographic uncertainty.** The closest motivating 2026 FIR-LQR manuscript contains a discrete pairwise simultaneous-stabilization example, its policy-gradient analysis, and a curriculum for expanding controller memory, but does not give the present interval-continuum exact minimax factor and all-memory rigidity. The 1990 interval-plant Schur-stability literature provides broad robust stability criteria and is materially relevant; full access to that article was unavailable, so an equivalent specialization cannot be excluded conclusively. Earlier simultaneous-stabilization theory and fixed-order Schur parameter studies were compared at the level of assumptions and mathematical implications. Standard conformal mapping and Schwarz lemma are expressly prior tools.

## Mathematical value

**PASS.** The result answers a natural robust-design question left quantitative by the pairwise FIR example: how wide an entire uncertain drift interval can one common finite-memory state feedback stabilize, and how much is gained by increasing memory? It gives an exact universal threshold and a unique optimal controller, and establishes by a nontrivial analytic obstruction that all memory beyond one lag cannot further improve the minimax spectral rate. This is not merely a finite parameter calculation or a reformulation of the motivating two-plant example.

## Limits and risks

The drift is time-invariant within each trajectory; the uncertainty set must be the complete interval; the controller has a fixed scalar FIR state-feedback form and known input gain. The statement concerns worst-case spectral radius, not stationary LQR cost, switched systems or non-FIR dynamic controllers. A repeated characteristic root appears at the interval endpoints, so a sharp spectral factor should not be misread as a uniform pure-geometric bound with the same factor. No independent audit has been conducted. Bibliographic uncertainty remains for older interval-polynomial and simultaneous-stabilization sources.

Self-review: passed. Independent audit: not yet performed.
