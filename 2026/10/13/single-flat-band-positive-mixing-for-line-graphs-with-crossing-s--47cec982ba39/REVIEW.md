# Self-review: crossing square-cycle certificate

## Correctness — PASS

The precise hypothesis is: every root edge is the sole common edge of a pair of simple four-cycles, where the root graph is finite, simple, and unweighted. Alternating sign vectors on each such cycle lie in the kernel of the unsigned incidence matrix. Their entrywise product isolates the selected edge, and each vector has Euclidean norm two. The line-graph adjacency matrix is exactly the incidence Gram matrix minus twice the identity, so its spectral projector at energy \(-2\) fixes these vectors. For each diagonal edge-coordinate operator, its compression has Frobenius norm at least one quarter of every input coordinate. The Schur-projector identity turns the resulting norm inequality into \(P\circ P\succeq I/(16m)\); positive semidefiniteness of the other spectral terms proves the claimed mixing bound and full rank. This is a complete finite-dimensional proof for all root graphs satisfying the quantified condition. The Cartesian-product corollary requires every factor to have no isolated vertices; the hypercube boundary case is calculated separately. Exact-rational projectors, incidence-nullspace checks, and positive \(LDL^{\mathsf T}\) pivots were reproduced for five root graph examples; finite checks alone do not justify the general conclusion.

## Originality — PASS with residual risk

Godsil (arXiv:1103.2578), Coutinho–Godsil–Guo–Zhan (arXiv:1709.03591), and Coutinho et al. (arXiv:2208.08971) establish the general spectral-average framework, not the graph-theoretic crossing-cycle rank criterion. Kang (arXiv:2605.01953v2), the closest direct line-graph work, states the known unsigned incidence identity and a full-support flat-band state result, but its Section 6 does not give this Schur-square positive-definiteness criterion or bound. The line-graph theorem cannot be inferred just from an existing nonzero flat-band orbital: the proof needs coordinatewise products that isolate every edge. Comparison with published full-rank questions, averaging papers, and available mathematical research records found no equivalent statement. This cannot rule out an equivalent implication in unindexed line-graph or flat-band literature, and human verification remains needed.

## Value — PASS

The exact full-rank question for quantum average mixing is mathematically motivated by the survey of Coutinho and Guo (arXiv:2404.02236, Section 4). A simple checkable local condition now guarantees globally positive mixing on infinitely many line graphs, with an explicit quantitative lower bound and a sharp \(Q_2\)-to-\(Q_3\) transition in the hypercube family. The certificate works for heterogeneous Cartesian products and graphs with nonregular root degrees; it is more than re-labeling a known spectral identity or computing a single finite graph.

## Closest literature and limitations

The closest literature is the general average-mixing spectral theory (Godsil, Coutinho and coauthors) and the line-graph flat-band construction (Kang). The four-cycle criterion is only sufficient; no necessity, optimal gap, weighted extension, or classification of all line graphs is claimed. The checked 2026 line-graph paper is an especially important source of potential overlooked implication, but its material read does not provide a covering rank theorem. As with any literature-led comparison, unindexed equivalent general principles remain a residual risk.

Self-review: passed. Independent audit: not yet performed.
