# Scientific review

## Correctness — PASS

The connected-dominating-set cochain model matches the primary definition. A standalone exact C++17 program tests every graph edge bitmask for orders one through seven, all induced-subgraph connectivity and domination conditions, the alternating connected-domination count, and all differential ranks over the two-element field. It found no eligible graph through six vertices and exactly 252 labeled eligible graphs on seven, all with the required two apices and five-cycle. All 252 pass the same nonzero cohomology test, with dimensions one in degrees two and three. A disjoint edge-and-cycle collapse of the complement complex independently proves the witness integral homology and \(D_c(G;-1)=0\). The finite search is complete for the stated finite domain; no untested larger graph is inferred.

## Originality — PASS on inspected evidence

Caputi–Celoria–Collari (arXiv:2201.00721, Question 5.11) posed the zero-Euler/nonzero-homology problem. Their follow-up (arXiv:2304.10134, Theorem 5.8) already contains a suspension theorem implying the existence and homology of the pentagonal-bipyramid witness: these facts are **not** claimed as original. The genuinely distinct new proposition is that this is the first possible vertex order and the **only** isomorphism class at that order among arbitrary connected simple graphs. Full relevant sections of both papers, indexed mathematical research records, and available earlier claims were compared; no matching sharp finite classification was found. An unindexed equivalent classification is a residual risk, not a uniqueness proof from search absence.

## Value — PASS

A published foundational question invites the existence of zero-Euler nonvanishing bold homology. Although the existence itself is covered by a subsequent suspension formula, the sharp minimal vertex count and global uniqueness over all connected graphs settle the natural smallest-witness refinement, independent of any restriction to graph suspensions. This converts an arbitrary example into a complete and reproducible extremal classification, with a transparent witness collapse and exact all-graph certificate. The seven-vertex limit is mathematically motivated as the sharp boundary, not an arbitrary tabulated slice.

## Boundaries

The classification concerns mod-two bold homology; the integral refinement is asserted only for the witness. No assertion is made at eight or more vertices. The computation is fully exhaustive in the stated domain but external independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
