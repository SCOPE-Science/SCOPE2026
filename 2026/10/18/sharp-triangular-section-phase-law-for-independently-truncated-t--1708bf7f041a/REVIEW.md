# Mathematical assessment

## Correctness — PASS

The theorem is for every nondegenerate tetrahedron with four independently chosen fractions strictly below one half and a uniformly oriented plane through the **original** tetrahedron centroid. A complete proof reduces triangular sections to the three-edge cuts of the 12-vertex truncated-tetrahedral graph; only whole-corner sign cuts can occur, since midpoint convexity excludes singleton sign cuts. The linear vertex-height map then proves that corner \(i\) survives exactly when the three *other* odds sum below one. The strict trihedral normal inequalities produce three-dimensional spherical cones; Girard's theorem yields the stated exact probability. A regular-coordinate calculation independently establishes the quarter-depth threshold and the quadratic coefficient. All exceptional directions are excluded as measure zero. An executable standard-library checker exhausts the 32 combinatorial three-edge cuts, makes 14,279 exact-rational sign tests and corroborates the spherical formulas with independently sampled directions. The code is supporting evidence; the continuum assertion rests on the displayed analytic proof.

## Originality — PASS, subject to historical literature risk

The closest inspected sources concern solid angles of **random projections of untruncated tetrahedra** (Feldman–Klain), physics of a 12-vertex truncated tetrahedral spin model (Krčmár–Gendiar–Nishino), and extremal hyperplane-section *volume/perimeter* of untruncated bodies (König). Neither their inspected results nor the closest public mathematical records determine the four independent truncation odds criterion, the corresponding original-centroid section probability, or the equal-depth quadratic extinction. An earlier exact shadow-count complementarity for four independently truncated tetrahedral corners concerns **orthogonal projections**, not actual plane intersections and cannot imply the new section-cone arrangement. Older unindexed computational section tables and implicit consequences of general arrangements remain unresolved priority risks; no search exhaustiveness or independence is claimed.

## Value — PASS

This is a natural complete answer for the triangular part of a random central section of a four-parameter family of classical tetrahedral truncations. It gives a sharp affine-invariant existence region controlled only by the *opposite* three cut odds, while metric effects enter only through explicit spherical angles. The disappearance at one-quarter of an edge and its quadratic probability exponent explain why a regular truncated tetrahedron has triangular faces but almost surely no central triangular sections. The finding is not a claim about larger section polygons, general affine-offset planes or arbitrary over-midpoint cuts.

## Limitations and literature

The best-evidence novelty judgment is provisional; independent mathematical audit is not performed. References: Feldman and Klain (2008), arXiv:0809.3459; Krčmár, Gendiar and Nishino (2015/2016), arXiv:1512.09059; König (2020), arXiv:2002.10743. Generic boundaries, arXiv and historical priority limits are stated in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
