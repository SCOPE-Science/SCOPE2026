# Scientific review

## Correctness

**PASS.** The exact vertex characterization uses the fact that two fractional coordinates would permit an affine perturbation, and the converse is checked by active constraints. Sorted unit normals decompose into a positive sum of centered cut vectors. Rearrangement makes the projection width additive in those positive coefficients, whereas the Euclidean norm is subadditive, with strict inequality unless just one cut occurs. This gives an all-dimensional reduction to two-level normals and excludes mixed directions. Exact cut linear programs give \(B_j=\min\{j,n-j,t,n-t\}\); the two monotone cut ratios force only the single-coordinate or balanced cut. The threshold and equality cases follow directly. Finite exact checks offer independent corroboration, not an infinite proof.

## Originality

**PASS, subject to historical search limits.** The 2023 regular-simplex paper supplies only \(t=1\) (and the complementary level), while the integer-rank hypersimplex formula supplies only \(t\in\mathbb Z\); neither implication determines the continuous nonintegral profile, its irrational crossover, or the complete orbit transitions. Full text of the 2021 projection paper was examined: it solves projection *onto* the same section, not minimum projection width *of* that section. Actual semantic database queries for capped-simplex width, fractional hypersimplices, permutahedra and two-level normals did not expose equivalent all-real-level coverage. Classical rearrangement is openly credited; unindexed earlier permutahedral width work remains a residual risk.

## Mathematical value

**PASS.** The object is the standard diagonal slice of the unit cube, canonical in convex geometry and constrained optimization. Its geometry changes with a continuous constraint level, while its minimum width stays **exactly flat over an explicit nontrivial central interval**. The theorem locates two irrational aspect thresholds and classifies every optimizing direction, providing complete sensitivity information unavailable from integer-level values or the regular simplex case. The result is a motivated all-dimensional structural classification rather than an arbitrary finite instance or a numerical refinement.

## Boundaries

The statement is restricted to \(n\ge4\), \(0<t<n\), intrinsic Euclidean metric. It does not solve general zonotope widths or establish any priority against unindexed literature. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
