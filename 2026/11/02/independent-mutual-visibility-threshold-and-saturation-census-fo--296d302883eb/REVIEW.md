# Scientific review

## Correctness — PASS

The Cartesian distance formula forces a single color change along geodesics between distinct colors. Independent sets have at most one vertex per clique layer; visibility allows at most two per color. A saturated set must therefore have two occurrences of every color. Any disjoint pair of occurrence intervals would obstruct an extreme-endpoint geodesic. Pairwise interval intersection yields two permutation blocks. If the blocks meet across adjacent layers, the last first-occurrence and first second-occurrence give a geodesic obstruction (or an independent-set violation), so one separating layer is necessary. Conversely, the explicit switch paths prove sufficiency, and the middle-gap compression gives the exact count. The \(2m-1\)-word construction supplies all scalar lower bounds, including the exceptional \(L=2m\) case. The proof covers all integers \(m,L\ge2\) with no unproved limiting step. Independent BFS-based finite enumeration verifies the boundary transition and counting cases, without being used as an infinite proof.

## Originality — PASS with residual priority uncertainty

The first-public 2021 paper of Cicerone, Di Stefano, and Klavžar introduces independent mutual visibility and generic Cartesian-product bounds, but does not classify independent visibility of \(P_L\square K_m\). The 2024 path-cycle product paper treats ordinary rather than independent visibility; the 2025/2026 independent-visibility coloring paper studies chromatic partitions and product coloring bounds; the 2026 independent-visibility paper characterizes generic graph properties and complexity. The nearest accessible mathematical-record findings concern connected mutual visibility on high-girth products, ordinary visibility polynomials on rook graphs, independent resolving sets, and edge general position; none implies the independent visibility threshold or the two-permutation extremizer census. Comparisons were made by invariant, quantifier, graph operation, parameter range, and claimed implication, not title alone. A previously unpublished or unindexed equivalent remains a priority risk.

## Mathematical value — PASS

The product \(P_L\square K_m\) is a natural network with \(m\) parallel path channels and complete intra-layer communication. Independent mutual visibility combines a local nonadjacency constraint with global unobstructed geodesics. The theorem gives a complete two-parameter extremal invariant, exposes an isolated one-layer failure of the obvious upper bounds, and classifies/counts every saturated optimizer by a permutation-and-gap structure. The saturation threshold and count are not immediate from the generic \(2m\) bound or the ordinary visibility number; they provide reusable structural information about constrained geodesic placements. The result does not require a broader graph-class extension to be meaningful.

## Closest literature and limits

Sources: arXiv:2112.13024 (independent mutual-visibility foundations and general Cartesian bounds); DOI 10.1007/s00025-024-02139-x (ordinary visibility for path/cycle products); arXiv:2505.04144 (independent mutual-visibility colorings); arXiv:2602.23403 (independence versus mutual visibility). The full accessible text was checked at the relevant definitions, theorem statements, product sections, and proof arguments. External priority uncertainty and the lack of independent audit remain; no formula is asserted for numbers of shorter-regime maximizers or other fibers.

Self-review: passed. Independent audit: not yet performed.
