# Mathematical review

## Correctness — PASS

The complete fractional description of the bipartite fixed-cardinality matching polytope (Torres, arXiv:2306.11910, Theorem 3.1) is applied without treating a nonfacet halfspace as a facet. For unsaturated ranks, the affine direction is the sum-zero hyperplane and the projected norms of edge, left-star, and right-star indicators are computed exactly. Summing each family of inball inequalities bounds the radius; uniform edge weights attain the minimum. The strictly weaker right obstruction and the equality cases force the displayed center space, with its full dimension justified by strict slack in the other inequalities.

At saturation, the affine direction is the direct sum of left-star sum-zero spaces. Its projected coordinate and right-star norms give two sharp bounds; equality in the winning family forces either the uniform center or a translated positive-margin graph-supported transportation polytope. Connectivity makes the bipartite incidence rank exactly \(p+q-1\), establishing cycle-space dimension. The sparse incidence-graph example has \(p=n\), \(q=\binom{n}{2}\), \(a=n-1\), and confirms the exceptional dimension jump. 132 independent SciPy linear programs corroborate the derived radii, uniform feasibility, contact counts, and equality-system ranks. Finite tests are not the universal proof.

## Originality — PASS, qualified

Torres establishes the matching-polytope inequalities and integrality, not the intrinsic Euclidean radii or incenter locus. Gill and Linusson address complete bipartite combinatorics rather than arbitrary sparse biregular support. The closest indexed incenter theorem treats square complete-bipartite assignment polytopes; a rectangular complete-support result addresses maximum-volume ellipsoids; and a positive-margin transportation result concerns polytopes with *both* sets of degree equalities, whereas the original sparse matching polytope has right-side caps and only its incenter locus sometimes becomes a transportation polytope. These claims do not logically cover the arbitrary connected sparse biregular family or its dimension transition. The closest square case was only available by indexed abstract, and a differently phrased or unindexed earlier argument remains possible.

## Mathematical value — PASS

The result supplies a complete two-parameter-plus-graph classification of a natural Euclidean extremal invariant, and an exact description of every optimizing center. At full matching rank it connects geometric nonuniqueness to graph cycle rank. A sparse incidence-graph family has identical radii in two consecutive members but a drop in center-space dimension from three to zero; this is a motivated geometric boundary not present in the source integrality theorem. General irregular supports and all face numbers of the resulting center polytope remain open.

Self-review: passed. Independent audit: not yet performed.
