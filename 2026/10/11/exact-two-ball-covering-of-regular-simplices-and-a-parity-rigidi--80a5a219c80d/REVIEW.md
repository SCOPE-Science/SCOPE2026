# Same-model scientific review

## Correctness (C): PASS

The all-dimensional lower bound follows from the pigeonhole principle and the exact variance identity for the smallest enclosing ball of a regular-simplex vertex subset. For the nontrivial upper bound, a barycentric halfspace bisects every cross edge at its midpoint; the two cut cells are convex hulls of explicitly listed vertices and cross-edge midpoints. The midpoint-to-face-centroid distance is exactly half the simplex edge length, and it is bounded by the face circumradii. The ball convexity argument covers the full interior. At the sharp radius, vertex cardinality and equality of the variance identity force the odd-dimensional optimum pairs; in even dimensions the complementary cut cell has strict enclosing-radius slack, yielding a positive perturbation ball. The reproducible exact-rational verifier returns `VERIFY_OK` over the declared finite tests; those tests do not replace the proof. Centers are unconstrained, and all dimensions \(d\ge3\) are covered.

## Originality (O): PASS, with residual uncertainty

The 2006 crosspolytope paper [2] was materially inspected in its lawful full text: it determines optimal equal-ball coverings of a different regular polytope, and its three-dimensional case highlights that vertex-only coverage need not imply full-body coverage. It neither states the two-ball regular-simplex radius nor its parity classification. The 2010 full arXiv paper [1] was inspected through its introduction, main algorithmic statements, and relevant mathematical setup: it solves a finite-set computational problem in three dimensions, not an exact regular-simplex continuum-covering problem across all dimensions. Published mathematical-record searches also returned an even-regular-polygon two-disc covering theorem and a coordinate isometry for regular simplices, but neither summary entails the sharp two-ball theorem here. No equivalent formula was found by actual searches for alternative terms, implications and body-versus-vertex comparisons. This does not establish universal novelty: detailed unindexed historical work, a partially accessible 2004 covering-book chapter, and inaccessible complete texts of some mathematical-record hits remain risks. An independent literature audit has not been performed.

## Value (V): PASS

The statement provides an exact covering invariant for an entire natural convex-body family in every dimension, where the finite vertex lower bound is not automatically sharp for the full body. The cut-cell construction supplies a genuinely global realization, and the optimizer set undergoes a sharp dimension-parity change: complete finite rigidity for odd dimensions versus positive-dimensional families for even dimensions. The crosspolytope comparison demonstrates the relevance of this distinction within finite ball covering. These are motivated structural and quantitative facts, not a change of notation or a table recomputation.

## Scientific limits

Only regular simplices and two congruent Euclidean balls are treated. The even-dimensional *complete* optimizer set is not described. No external independent check was performed; historical coverage by a source not identified or not fully accessible remains possible.

Same-model review: passed. Independent audit: not yet performed.

## References

[1] P. K. Agarwal, R. Ben Avraham, M. Sharir, *The 2-Center Problem in Three Dimensions*, arXiv:1012.2694v1 (2010).
[2] K. Böröczky Jr., I. Fábián, G. Wintsche, *Covering the crosspolytope by equal balls*, Period. Math. Hung. 53 (2006), 103–113, DOI:10.1007/s10998-006-0024-1.
