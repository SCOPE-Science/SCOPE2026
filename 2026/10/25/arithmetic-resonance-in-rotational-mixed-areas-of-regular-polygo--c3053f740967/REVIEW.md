# Scientific comparison and review

## Correctness — PASS

The area identity is derived from the polygon mixed-area support-sum formula, with all radii positive and integer orders at least three. The coprime-residue argument gives the precise arithmetic phase, including its parity change. The finite cosine progression proves the identity at ordinary angles, and continuity treats tied support directions. The common-normal congruence proves the side-count phase; strict cosine monotonicity gives every optimum; the angular cusp and orientation distribution follow by exact one-variable calculations. A separately implemented standard-library convex-hull calculation passed 3,696 regressions; numerical tests are not the infinite proof. Mixed-area normalization has been checked against the known same-polygon cases.

## Originality — PASS (within inspected sources)

The closest published work on angle-dependent excluded areas, Geigenfeind–de las Heras (2019), computes regular-polygon examples and reports identical-order extrema but not the mixed-order closed law. Abbasi Moud (2026) computes fixed-orientation cross-species excluded areas and the equal-species parity formula, both obtained as special values; Deza–Pournin (2018) gives the normal-fan machinery without angular area formulas. Earlier identical-convex-body minimization covers the corresponding equal-order minimization statement, which is not asserted as the novel part. The combination of a universal \(\gcd/\operatorname{lcm}\) law, exact angular classification, facet count at precisely the minima, and full random-orientation distribution is not implied by those stated special-case results without new arithmetic analysis. Search coverage cannot establish absolute priority.

## Value — PASS

The result provides a complete structural phase diagram, not one numerical value: it identifies a number-theoretic sensitivity scale for mixed polygon pairs, shows that all nonsmooth angular minima coincide with normal-fan degeneracy, and supplies exact orientation-dependent excluded areas relevant to mixtures of polygonal particles. The coprime versus commensurate contrast in the \(L^{-2}\) oscillation connects geometry to side-count arithmetic. Previously available pairwise Minkowski-sum algorithms compute each angle separately but do not explain these sharp transitions.

## Residual risks

An equivalent formula may exist in older collision-detection, kinetic-theory, or mathematical-morphology literature not indexed by title search. The proof uses classical mixed-area and polygon-normal-fan facts; the claim is originality of the explicitly collapsed arithmetic-angle profile and classification, not invention of those tools. The finite checks are regressions, not certification.

Self-review: passed. Independent audit: not yet performed.
