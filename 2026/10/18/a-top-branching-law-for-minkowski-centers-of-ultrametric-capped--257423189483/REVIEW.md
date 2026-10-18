# Review of the ultrametric-capped metric-polytope theorem

## Correctness

**PASS.** The halfspace description is exhaustive because triangles imply coordinate nonnegativity. Each triangle support minimum is attained by a concrete one-dimensional pullback semimetric defined through the distance to a two-point set. The reflection-inclusion transformation is applied to those exact extrema. A smallest-edge triangle gives a sharp universal lower bound of \(2\); the ultrametric itself supplies a matching feasible reflection center. Nonnegative cap deficits reduce each ultrametric triangle to either all-zero or short-zero/equal-long patterns. Root-block propagation establishes all and only the stated optimal centers, including singleton top blocks and arbitrary tied heights. Linear programs independently check the support extrema, optimal value and coordinate extremes in 38 finite fixtures.

## Originality

**PASS under current literature comparisons, with residual bibliographic risk.** The closest same-object primary work by Gartsman and Linial establishes ellipsoidal approximations of the uniform bounded metric polytope rather than affine Minkowski asymmetry. Den Hertog, Pauphilet and Soali provide the generic polyhedral optimization formula but do not evaluate the exact triangle-functional support minima or classify the hierarchical family. Kozma and coauthors analyze metric-polytope volume, while Lin and coauthors study tropical convexity of ultrametrics themselves. Semantic database searches for weighted metric polytopes, reflection asymmetry, hierarchical metric bounds and the exact root-branching statement returned no result covering it. General LP applicability is distinguished from an existing explicit closed-form classification.

## Value

**PASS.** The polytope of all semimetrics dominated by a fixed ultrametric is a natural convex-geometric object attached to a finite hierarchical metric. Its affine-invariant reflection asymmetry remains constant even as the hierarchy changes, while the *uniqueness and dimension* of the entire center set exhibit a sharp, explicit phase transition determined by the root branching number. The formula captures every depth and size, rather than a low-dimensional example or arbitrary special parameter slice; it also resolves uniqueness of a standard convex-body center in a family whose ellipsoidal centers had motivated earlier work.

## Closest literature and limits

The exact same uniform-cap object appears in Gartsman and Linial (2023), but with different functionals. The optimization formula in den Hertog, Pauphilet and Soali (2022) is applicable as general machinery; it does not report the asserted closed form. The interpretation of ultrametrics as tree structures is standard, not claimed as new. The proof does not address general non-ultrametric ceilings, and the numerical experiments are finite. Bibliographic searches cannot guarantee absolute novelty, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
