# Scientific review: optimal simultaneous facet-center interpolation

## Correctness — PASS

The domain is the real Lipschitz quotient for the Euclidean vertex set of a \(d\)-cube, with all \(2d\) facet centers added, for every integer \(d\ge3\). The proof averages an arbitrary real-linear extension over the complete cube symmetry group, retaining its operator norm upper bound. Signed, two-orbit coefficients must sum to one. A coordinate-deletion distance function has the same binomial expectation on both orbits, giving the exact lower bound independently of sign. The positive simultaneous facet-average operator is then checked on every target-pair orbit. The key off-facet inequality is proved for \(d-1\ge4\) by a variance bound and Jensen, and for the remaining two cases by exact radicals. Strict monotonicity and the limiting expansion follow from leave-one-out conditional Jensen and standard bounded binomial moment estimates. The companion checker passed 7,152 vertex–center pair evaluations and 365 center–center classifications across \(d=3,\ldots,8\). These finite tests are corroboration, not an infinite proof.

## Originality — PASS, with residual bibliographic risk

Bruè, Di Marino and Stra, arXiv:1801.07533 (2018), develops random-projection constructions and general linear extension bounds; their full HTML text, including the random-projection and extension theorems, was inspected. Basso, arXiv:2310.13554 (2023), develops general explicit upper bounds rather than the sharp cube-facet problem; introduction and substantive sections were inspected. A publicly indexed cube-**center** theorem gives the one-point lower-bound constant, but its one-point assertion does not imply simultaneous extendability to the \(2d\) different facet centers. The present proof adds a compatibility theorem for cross-center and off-facet pairs. Its record's full text was unavailable, so equivalent hidden extensions are a residual risk. Related results on cube edge midpoints, simplex face centers and polygonal midpoints have different ambient point sets and statements; their claims do not cover the present theorem. Searches using the exact geometry, aliases and binomial parameters found no covering theorem. Absence from a search is not proof of novelty.

## Mathematical value — PASS

The exact constant is an invariant of a natural simultaneous finite metric interpolation problem. The main nontrivial point is that separate one-face optimizers can be synchronized across every facet without increasing the sharp one-face norm, even though signed coefficients and all vertices are allowed. The off-facet inequality is a genuine dimensional restriction, and the strict monotone law with an explicit convergence rate provides a benchmark for cubical trace interpolation. This is not a generic consequence of one-point extension estimates, nor a mere recomputation of a scalar expectation.

## Scope and risks

Only real scalar linear extension, Euclidean cube vertices, all codimension-one facet centers, and dimension at least three are treated. No uniqueness of arbitrary minimizers, arbitrary-face interpolation, other metrics, or independent validation is claimed. Bibliographic risk remains for inaccessible published material, especially the full cube-center paper, and for alternative formulations of the simultaneous problem.

Self-review: passed. Independent audit: not yet performed.
