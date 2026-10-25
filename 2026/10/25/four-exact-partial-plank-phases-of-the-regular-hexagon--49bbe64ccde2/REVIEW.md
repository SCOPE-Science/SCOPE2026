# Scientific review

## Correctness — PASS

The statement includes all finite plank families of total width at most \(W\) and classifies only optimizing single-plank normals. Theorem 12 of Bakaev--Polyanskii (arXiv:2607.27483, first version 2026-07-29) legitimately reduces the planar total-width objective to one plank for \(0<W<\sqrt3\). For each normal, slice concavity and central symmetry justify a centered plank. Six hexagon vertex projections and direct cap clipping yield three **exact** piecewise area formulas. Their derivatives have explicit signs; the quadrilateral stationary condition is strictly monotone and the triangular stationary point remains in its valid branch. These facts supply global optimality and rigidity in each dihedral chamber for every admissible real width. All three breakpoints and boundary values agree. Independent standard-library polygon clipping reproduced every cap expression and optimized value across deterministic random samples; this code is corroboration, not an infinite proof.

## Originality — PASS, with specific residual risk

The motivating paper's publicly accessible full manuscript was inspected at Theorem 12 and Section 5, with a full-document search for regular hexagons: it supplies existence of one optimum, but no regular-hexagon orientation or four-branch area formula. Indexed published-record searches for regular hexagon/strip/plank, exact transition values, and equivalent central-slab wording did not retrieve the four-phase optimization. The closest published hexagon records are about translative convex-hull ratios and enclosing parallelograms, not the area of a fixed-width Euclidean strip intersection. Previously accessible square and nonsquare rectangle calculations do not imply this six-vertex, two-oblique-phase result. Classical polygon-slicing literature may have undocumented partial or complete overlap; these searches are evidence, not a proof of priority. An independently relevant 2012 enclosing affine-regular hexagon paper was fully inspected in Sections 1 and 4-5: its objective is different. The complete manuscript of every adjacent historical item has not been inspected.

## Mathematical value — PASS

The general planar one-plank reduction leaves a genuinely geometric direction-selection problem. The exact regular-hexagon solution unexpectedly has four phases: facet normals, a continuously rotating oblique normal, vertex normals, then a second oblique phase, with three exact thresholds and an explicit full captured-area profile. It supplies a natural, reproducible benchmark where restricting attention to facet or vertex normals is false on two open intervals. This is an exact natural classification with geometric explanatory content rather than a numerical fit or routine reparameterization.

## Closest literature and limits

E. Bakaev and A. Polyanskii, *Optimal partial plank coverings*, arXiv:2607.27483 (Theorem 12, Section 5) is the necessary strongest partial-covering result and does not imply the orientation claims. Public records on translative hull ratios and enclosing parallelograms concern different optimization objectives. The result is confined to regular hexagons and does not classify all tied multi-plank families, nor does it establish historical uniqueness beyond the reported targeted searches.

Self-review: passed. Independent audit: not yet performed.
