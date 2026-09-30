# Independent Audit — 2026/09/12/065

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `8c397541cf05909ae21219ac2e304a4a26900a0c`  
**Disposition:** **REPAIRED**

## Correctness
The analytic core survives independent scrutiny: the two-point void-probability formula gives M(lambda)=lambda^2 E[A_lambda^2], the envelope 1<=M<=2 is valid, and for fixed scaled radii and nonzero angular separation the overlap lens converges to a finite intersection of limiting horoballs, so lambda times the lens area tends to zero. Dominated convergence therefore gives M(lambda)->1 and V(lambda)=M(lambda)-1->0 as lambda->0; since E[lambda A_lambda]=1 this is equivalently lambda A_lambda->1 in L2. The published numerical interval for V(1), however, is labeled certified even though the inner trapezoidal lens quadrature has only an empirical/refinement error estimate, not a proved enclosure. The high-intensity Euclidean limit is also only sketched. The repair keeps the rigorous low-intensity theorem and upper bound, and downgrades the numerical values and high-intensity statement to non-rigorous illustrations.

## Originality
D’Achille–Curien–Enriquez–Lyons–Ünel develop the low-intensity ideal Poisson–Voronoi limit, and D’Achille–Thäle determine face-volume densities and typical face volumes, but the accessible statements do not give this Palm typical-cell second-moment collapse lambda^2 Var(A_lambda)->0. The audited contribution is the explicit two-point moment/lens argument proving L2 concentration of the rescaled typical-cell area, not merely the existence of the ideal tessellation.

## Scientific value
The corrected theorem decisively rules out any uniform positive lower bound a/lambda^2 and identifies a strong concentration phenomenon, lambda A_lambda->1 in L2, in the sparse hyperbolic regime. That is a meaningful probabilistic asymptotic even after removing the uncertified finite-lambda interval from the theorem statement.

## Literature
- https://arxiv.org/abs/2303.16831 — establishes the low-intensity ideal Poisson–Voronoi regime, but the accessible statement does not give the submitted second-moment concentration theorem.
- https://arxiv.org/abs/2606.26049 — gives face-volume densities and typical face volumes, not the audited Palm-cell variance collapse.

## Independent checks and limitations
The exact moment identity, envelopes, and low-intensity dominated-convergence argument were re-derived. The current `RESULT.md`, `METADATA.json`, `SLOGAN.txt`, `VERIFICATION.md`, and both cited artifacts have the same blob SHAs as the assignment snapshot; comparison from the inventory commit to current main reports no changes under this record path. The audit does not certify the finite-lambda quadrature error. No GitHub writes were made.
