# Scientific review: integral homotopy of one-way directed cycle ladders

## Correctness — PASS

For every integer \(n\ge3\) and permutation \(\phi\), the exact directed-path criterion is derived: a spoke excludes exactly its outer outgoing and inner incoming rim arc, while the only possible selected directed cycles are the two complete rims. This gives an exact simplicial description. The rim subcomplex is the join of two simplex boundaries and hence \(S^{2n-3}\). Closed stars of spokes form a contractible good cover; their rim-only overlap has the boundary of an \((n-1)\)-simplex as its nerve. Both applications of the nerve lemma satisfy the contractible-intersection requirements. The overlap-to-rim inclusion is null-homotopic by dimension/connectivity, and the homotopy pushout produces \(S^{n-1}\vee S^{2n-3}\). A separate executable verifies direct graph acyclicity and the model, face counts, and mod-two Betti numbers for five representative cases. No infinite deduction relies on enumeration.

## Originality — PASS, qualified

The 2022 foundational paper (arXiv:2208.04656v1) treats individual polygons, small grids and other digraph classes but not two directed rims coupled by a one-way complete matching. The 2024 comparison theorem (arXiv:2401.01248v1) requires the absence of directed cycles, which fails twice here. The 2026 bidirectional-polygon paper (arXiv:2601.05670) has opposite arcs on a single polygon; the 2026 conflict-hypergraph paper (arXiv:2602.14936v1) supplies general encoding but not this computed two-sphere formula. Related directed-star multipath findings, undirected ladder cut complexes, and undirected Petersen matching complexes do not imply the claim. Specific directed-Petersen, directed-ladder, matching-independent and two-cycle formulations were searched; no equivalent covering statement was identified. Residual risk: an unindexed homotopy classification or a proof obscured in a more general directed-cycle theorem may exist.

## Mathematical value — PASS

This computes the complete, torsion-free **integral homotopy type** in an infinite, natural family containing coherently oriented prisms and generalized Petersen graphs, in two distinct degrees. It proves an unexpected invariance under arbitrary endpoint permutations even when the resulting undirected graphs differ (prism versus Petersen). These features extend the foundational single-cycle computations and supply benchmark examples for topology of directed path selections. The fact does not assert classification for all generalized Petersen orientations.

Self-review: passed. Independent audit: not yet performed.
