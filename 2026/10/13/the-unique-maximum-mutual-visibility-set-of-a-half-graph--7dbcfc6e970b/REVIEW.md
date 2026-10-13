# Review of The unique maximum mutual-visibility set of a half graph

## Correctness
PASS. The proof explicitly reconstructs the half-graph distances, gives witnessing geodesics for the claimed optimum, excludes size \(2n-1\), and classifies all size-\(2n-2\) candidates by the locations of the two omitted vertices. The \(n=3\) boundary is handled separately. Exhaustive direct checking agrees for \(3\le n\le10\).

## Originality
PASS. The foundational paper gives the complete-bipartite benchmark but no half/chain specialization. The broader distance-hereditary algorithm computes a maximum set on half graphs but does not state an all-orders formula or uniqueness. The later visibility-polynomial framework gives generic enumeration but no half/chain formula. Targeted literature searches found no theorem identifying the unique maximum half-graph set.

## Value
PASS. Half graphs are canonical nested-neighborhood bipartite graphs. The theorem gives a sharp structural contrast with the complete-bipartite benchmark: the optimum size stays \(2n-2\), while the maximum-set multiplicity collapses from \(n^2\) to \(1\). The omitted extreme pair has a direct geodesic-relay interpretation.

Self-review: passed. Independent audit: not yet performed.
