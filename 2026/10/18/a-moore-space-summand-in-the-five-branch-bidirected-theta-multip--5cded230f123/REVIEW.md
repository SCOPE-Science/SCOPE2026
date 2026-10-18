# Scientific review of the five-branch theta multipath calculation

## Correctness — PASS
The graph, twenty ordered arcs, simplices, orientations, and all boundary calculations are explicit. The two independent exhaustive face constructions agree on 711 faces counting the empty face. The deterministic matching has 297 pairs; all 2180 covering incidences pass a full acyclicity check. The exact integer Morse matrices satisfy the chain condition, and Smith reduction yields one nonunit invariant 2. An independent integer unit-pivot procedure gives 40 unit factors and a residual gcd 2. A unit two-cell kills the sole critical one-cell, after which Hurewicz identifies the attaching maps and upgrades the homology calculation to the Moore-space wedge.

## Originality — PASS with residual risk
The principal 2022 multipath paper treats complete bipartite digraphs in one-way orientation, along with different graph families; the bidirected five-branch theta digraph is not classified there. The 2024 quiver-minor analysis gives general bounded-torsion statements and a comparison restricted to acyclic digraphs; it does not give this homotopy decomposition. The ambient directed-complete-graph cycle-free chessboard theorem has no implication determining this subcomplex. Exact database searches found neighboring three- and four-branch computations, not the five-branch Moore-space wedge. Absence from indexed sources cannot exclude undocumented equivalent work.

## Mathematical value — PASS
The smallest nearby recorded torsion example is the four-branch graph with torsion concentrated in degree two. Adding the fifth branch yields a mathematically different mixed-degree object: an exact Moore-space summand coexisting with thirty-one three-spheres. The integral homotopy type resolves all attaching maps for a natural finite member of the bidirected-theta family. This is substantially more informative than an Euler characteristic, modular Betti vector, or simple parameter increment, and gives a reproducible example of non-spherical multipath homotopy.

## Sources and limits
Primary papers inspected: arXiv:2208.04656v1, arXiv:2110.11206, arXiv:2401.01248 and arXiv:0710.5252. Historical smaller-parameter calculations are used only to compare implications. There is no all-parameter theorem here, and unindexed equivalent prior work is possible. Reproduction requires Python and SymPy; no outside certificate has been supplied.

Self-review: passed. Independent audit: not yet performed.
