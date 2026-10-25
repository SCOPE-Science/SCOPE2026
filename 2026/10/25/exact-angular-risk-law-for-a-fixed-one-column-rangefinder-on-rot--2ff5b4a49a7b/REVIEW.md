# Scientific review

## Correctness

**PASS.** The result concerns the precisely specified one-column orthogonal range projector built from a fixed nonzero probe and the odd powers of a smooth planar positive-definite matrix. Orthogonal conjugation gives an explicit rational function of the input angle. Its derivative is strictly positive in squared angular displacement. Containment of an arc of length \(L\) in a centered arc proves the deterministic minimax. Uniform projective Gaussian angles give the exact worst-error atom and full CDF by inverting the nearest-arc-distance relation. A tangent substitution gives the pathwise half-turn integral for the unpowered case. The algebraic formula was independently checked by exact rational matrix arithmetic; quadratures and finite grids were consistency tests only.

## Originality

**PASS, best-knowledge assessment.** Closest primary work: Kressner--Lam (arXiv:2302.12761, Theorems 4 and 7, Remark 1) handles shared Gaussian sketches, integrated bounds, uniform error, and rank-change discontinuity, but its bounds assume oversampling and do not give this unoversampled rank-one continuum minimax, complete worst-error law, finite-power barrier, or pathwise integral. Diouane et al. (arXiv:2206.08793, Sections 3.1--3.2) give fixed-matrix projection/canonical-angle bounds, not a common-probe exact distribution over a rotating continuous parameter family. Prior descriptions of power rangefinding do not imply the specific sharp law without additional argument. published-finding corpus and accessible related claims were searched by object and mathematical implication; no equivalent claim was identified. Residual risk: an unlocated geometric or randomized-rangefinding note may contain the same elementary planar calculation.

## Value

**PASS.** It resolves a natural sample-budget boundary of parameter-dependent low-rank approximation: whether a single fixed column can track a smoothly rotating gapped dominant eigenspace uniformly, and whether additional power iterations remedy that failure. The exact minimax, nonzero worst-case probability even on a short parameter interval, full CDF, and phase-averaged loss make the obstruction quantitative rather than a one-point failure. The squared integrated error penalty scales like the eigenvalue condition number, while a two-column sketch followed by rank-one truncation eliminates it on this family.

## Scope and remaining risk

Only the specified planar, exact-arithmetic, same-probe algorithm is classified. Source theorems that require oversampling are not contradicted. Equivalent prior geometric arguments may exist despite the searches, and broader-dimensional conclusions are not established.

Self-review: passed. Independent audit: not yet performed.
