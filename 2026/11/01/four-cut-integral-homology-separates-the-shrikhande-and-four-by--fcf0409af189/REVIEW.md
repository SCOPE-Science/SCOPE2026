# Research review

## Correctness — PASS

The claim uses the ordinary four-cut convention, not the total variant. The exact graph definitions generate two simple sixteen-vertex six-regular graphs with two common neighbors for each vertex pair. Complete four-set and face enumeration independently constructs each Alexander dual; the two membership algorithms agree on every subset. Each staged acyclic matching is verified by a complete topological sort of its directed Hasse graph (6128 incidences for the rook graph, 6032 for Shrikhande). Exact integer signed chain cancellations leave a zero critical differential for the rook graph and two maps of ranks 4 and 6 with unit Smith factors for Shrikhande. The integral universal coefficient theorem and the sixteen-vertex Alexander-duality degree shift are applied without a characteristic restriction. The full original simplicial boundary matrices independently reproduce mod-two Betti numbers. All computations are replayable from `verify.py` and `verification_output.txt`; neither finite homology nor field homology is misidentified as a homotopy proof.

## Originality — PASS against inspected evidence

The closest primary literature [1] defines ordinary cut complexes, gives Alexander duality and treats graph families not containing this paired four-cut computation; [2] studies ordinary cut complexes of disjoint unions, squared paths and rectangular *path grids*, not the rook graph (a complete-clique Cartesian product) and not Shrikhande. The closest published indexed result on rook graph three-cut homology concerns cutoff three and does not determine cutoff four. Published comparative results for Shrikhande and rook independence or Čech complexes involve different defining simplices. Searches using graph-name aliases, identical strongly regular parameters and the Alexander-dual connected-quartet formulation produced no stronger covering result. Novelty remains a best-evidence conclusion, not a mathematical uniqueness certificate: an unindexed or inaccessible equivalent calculation remains possible.

## Value — PASS

The Shrikhande and four-by-four rook graphs are the canonical nonisomorphic pair with the same strongly regular parameters \((16,6,2,2)\). Their four-cut complexes have the same number of vertices, the same total number of dual faces, the same reduced Euler characteristic and equal top dimension, yet different **integral** Betti profiles, including a degree-nine class present only in Shrikhande. This determines an exact natural invariant on both canonical examples, separates graph structures that numerical graph parameters and Euler characteristic fail to separate, and supplies two explicit non-shellability examples. The finite classification is motivated by an existing general graph-complex theory and does not claim an unproved family result.

## Closest literature and risks

[1] M. Bayer et al., *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, full accessible HTML (Sections 1, 6, 7). [2] M. Bayer et al., *Topology of Cut Complexes II*, arXiv:2407.08158, full accessible HTML (Sections 2, 5). Closest indexed records cover three-cut rook topology, or independence/Čech complexes of the graph pair. Unindexed equivalence and independent verification remain the residual risks; no homotopy type is inferred.

Self-review: passed. Independent audit: not yet performed.
