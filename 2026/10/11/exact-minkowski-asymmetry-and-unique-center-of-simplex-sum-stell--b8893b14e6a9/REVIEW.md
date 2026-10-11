# Scientific review: simplex-sum stellohedron Minkowski center

## Correctness — PASS

The lower bound uses every singleton leaf and the aggregate leaf subset. Their containment inequalities force \(s\ge k2^{k-1}/(2^k-1)\), and equality forces every leaf center coordinate. The matching upper certificate uses the strict decrease of \((2^k-2^{k-a})/a\), supplemented by complement subsets in the fixed coordinate-sum hyperplane. The proof separately justifies that the complete subset-inequality representation is exact, not only necessary. Thus neither numerical enumeration nor unstated facet completeness is needed for the infinite assertion. The standard-library exact verifier passed in dimensions \(1\) through \(6\), and a separate numerical LP matched in dimensions \(2\) through \(7\).

## Originality — PASS, with residual risk

The closest inspected structural source, Padrol–Pilaud–Poullot, arXiv:2109.09200, gives the graph-associahedron simplex-sum model and describes deformation cones, not its Minkowski reflection-containment optimum. Cardinal–Pournin–Valencia-Pabon, arXiv:2106.16130, gives graph-distance results, not affine asymmetry. General convex-body symmetry algorithms encompass a finite LP but do not directly state the evaluated family formula or uniqueness. Earlier Euclidean-inradius calculations concern another invariant for the same realization; neither metric inradius nor a graph-diameter classification implies the new affine-invariant claim. Targeted searches for stellohedron/star graph associahedron Minkowski asymmetry, alternate spellings, center and sum-of-simplices formulations identified no decisive prior coverage. Search incompleteness and terminology changes remain risks; no independent priority claim is made.

## Value — PASS

This is a natural infinite class of graph associahedra, and its canonical simplex-sum realization is fundamental to the construction. The theorem completely determines an affine-invariant extremal ratio and unique minimizing center rather than presenting a numerical instance or a restatement of known facet inequalities. It shows exact near-half-dimensional growth \(s=k/2+O(k2^{-k})\), with an explicit sharp correction. The minimizing center breaks hub-versus-leaf coordinate equality and differs from the all-equal point, giving a useful geometric contrast with other extremal center problems.

## Scope and limitations

The result is for the stated unweighted Minkowski-sum realization. The proof does not cover arbitrary deformations, weighted sums, or combinatorially equivalent realization choices. Prior-work searches do not certify that no equivalent older computation exists.

Same-model review: passed. Independent audit: not yet performed.
