# Review of Strong resolving dominating sets of crown graphs

## Correctness
PASS. The distance table of the crown graph is explicit. A deleted matched pair has distance \(3\), while every third vertex has distances \(1\) and \(2\) to its endpoints, so a strong resolving set must hit every deleted pair. Conversely, if every pair is hit, then for any two omitted vertices the selected mate of either one strongly resolves the pair because the other omitted vertex lies on a length-three geodesic joining that matched pair. Domination then fails exactly when an omitted vertex sees no selected vertex on the opposite side, which forces one of the stated \(2n\) transversals. The generating polynomial follows by three independent choices per matched pair followed by deleting those exceptions. Direct exhaustive checks for \(3\le n\le8\) match the membership rule and every polynomial coefficient.

## Originality
PASS. The defining 2020 strong-resolving-domination paper treats join and corona constructions and contains no crown, bipartite, or matching specialization. Earlier direct-product strong-metric theory does cover \(\operatorname{Cr}_n\cong P_2\times K_n\) and implies the strong-resolving precursor, so the scalar strong metric value is not claimed as new. The final claim instead classifies exactly which of all strong resolving sets also dominate and gives the resulting all-cardinality enumerator. The 2023 lexicographic-product continuation and the later equivalent “dominant strong metric dimension” treatment do not cover crowns or direct products in the inspected material. Targeted semantic searches under both terminologies found no equivalent crown classification or enumerator.

## Value
PASS. Strong resolving domination deliberately couples two classical vertex-set requirements, and crown graphs form a standard direct-product/bipartite test family. The result gives a complete, natural set classification rather than only a scalar invariant: all strong resolving sets are filtered by exactly \(2n\) structurally characterized domination obstructions, yielding every cardinality count and every minimum set. This cleanly identifies when the domination constraint is free and when it is active on a canonical family.

Self-review: passed. Independent audit: not yet performed.
