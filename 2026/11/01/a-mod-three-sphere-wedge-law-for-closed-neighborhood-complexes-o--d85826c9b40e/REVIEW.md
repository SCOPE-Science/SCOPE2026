# Scientific review

## Correctness — PASS
The theorem quantifies all bipartite two-factors \(\bigsqcup C_{2m_j}\) with \(m_j\ge3\) and \(n=\sum m_j\ge7\). The proof identifies the exact common intersection of the two closed-neighborhood side complexes with the retained graph, computes the graph cycle rank, collapses each side to the Alexander dual of the independence complex of projected cycles, applies the classical integral cycle formula, and proves simple connectivity using complete two-skeleta. As the graph-inclusion maps into the side complexes are nullhomotopic, the cofibration pushout splits and yields the full integral wedge type. The standalone checker independently reconstructs nine small examples and their mod-two ranks. Finite cases are not treated as a proof for all sizes.

## Originality — PASS with residual risks
The closest fully inspected paper is Matsushita's 2025 *Closed neighborhood complexes of graphs* (https://arxiv.org/html/2511.12608v2). Its theorems address general double-cover and hypergraph dualities and its example concerns Cartesian products of complete graphs, rather than the present complements of bipartite two-factors. The classical independence-complex calculation for cycles provides ingredients but not the closed-neighborhood union/pushout classification. A published record on three-periodic Rips barcodes of bipartite factor complements (https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-independence-complex-transfer-and-three-periodic-rips-barcodes-o--5408625c1e7e) was read in full: its scale-two Rips complex is \(\operatorname{Ind}(H)\) and does not determine the closed-neighborhood complex of the same graph. Semantic result searches found no equivalent formula. Residual risk remains from unindexed or implicit equivalent prior work; search absence is not a mathematical proof of priority.

## Value — PASS
Deleting spanning two-factors is a natural controlled perturbation of a complete bipartite graph, and all resulting graphs have identical numbers of vertices and edges. The theorem detects the forbidden cycle-length partition by an exact integral homotopy invariant, with a mod-three dimension law and exponential multiplicity \(2^{c+1}\), not just by a Betti count on a selected example. At \(n=9\), different forbidden partitions yield respectively four, eight, and sixteen high-dimensional sphere summands while retaining the same 46 degree-two spheres. The decomposition is reusable: it explains these patterns by Alexander-dual side complexes and a homotopy pushout.

## Scope and remaining risk
The result excludes smaller sizes and forbidden four-cycles. It does not assert equivariant refinement or filtration structure. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
