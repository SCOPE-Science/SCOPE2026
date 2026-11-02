# Scientific review

## Correctness

PASS. Every selected rook has exactly one selected neighbor, forcing its selected cell to belong to a disjoint pair sharing one row or one column. Interpreting such a pair as two edges in a complete bipartite graph gives a vertex-disjoint two-edge path. The proof excludes two unused original vertices by either non-domination or identical signatures and proves the one-unused-side orientation restriction using a selected-versus-unselected singleton collision. For the three surviving types, incidence labels give a direct injection from every cell to a nonempty signature, and exact pair assignments establish the formula. The attached checker evaluated the original graph predicate for 1,501,038 subsets on seventeen boards, with zero discrepancies. The infinite result relies on the proof, not on test extrapolation.

## Originality

PASS under the inspected literature, with residual priority uncertainty. The foundational 2017 article establishes the definition, general necessary properties, the high-girth criterion, and path/tree/infinite-grid examples. Its high-girth result does not apply to the rectangular rook graphs. The 2021 preprint/2022 article extends structural recognition to other graph classes and gives necessary local conditions, not a complete two-parameter classification of rook-graph codes. Targeted searches for rook, Cartesian, line-graph, bipartite-edge-code and three-vertex-path-factor equivalents found no claim implying the present exact count or boundary. Results about other domination or identifying-code notions do not imply the stronger joint open-independence and pairwise open-signature condition. An unindexed or differently worded theorem remains possible.

## Value

PASS. For a natural two-parameter family of line graphs, the theorem settles existence, classifies every code, supplies the exact code-size polynomial, and explains a sharp arithmetic phenomenon: a square board has any such code exactly when its side length is divisible by three. The one-unused-row-or-column possibilities at dimensions \(n=2m+1\) and \(m=2n+1\) are structurally distinct boundary families, not arbitrary finite exceptions. These facts address the constrained fault-location question motivating open-independent OLD codes, rather than only recomputing a scalar domination number.

## Sources and limits

Relevant primary comparisons are Seo and Slater (2017), DOI 10.5614/ejgta.2017.5.2.2, Sections 2–4, and Cappelle et al. (first public preprint 14 March 2021), arXiv:2103.07972, Sections 1–4. They contain the general definitions and related results, but the inspected statements do not subsume this classification. The proof does not address unrestricted OLD codes or arbitrary line graphs. Different terminology in edge-location literature remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
