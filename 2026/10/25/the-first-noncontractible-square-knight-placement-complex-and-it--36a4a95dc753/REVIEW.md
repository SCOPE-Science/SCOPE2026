# Review of the square knight-placement result

## Correctness

PASS. An explicit complete matching of all 1,364 nonempty independent faces has 679 cover pairs, leaving one critical zero-cell and five critical three-cells. All 5,772 Hasse cover relations are constructed, directed according to the matching, and acyclicity is checked by complete topological sorting. Discrete Morse theory then yields a wedge of five three-spheres over the integers. The isolated-vertex cone argument proves contractibility for smaller square boards. Signed fixed-face Lefschetz sums for all eight square symmetries give the rational third-homology character, and its decomposition is checked at every group element. The provided program was executed successfully; mod-two boundary ranks provide a supplementary check, not a substitute for the integral proof.

## Originality

PASS, subject to unindexed-literature risk. The closest inspected same-object paper is Cibu et al., arXiv:2403.03907v1, whose Sections 7–8 and knight appendix compute gonality of nonperiodic/toroidal knight graphs, a different invariant. The 2007 independence-complex paper arXiv:math/0701890 treats nearest-neighbor square-lattice graphs, not knight attack graphs. Research-record results concerning the four-cube concern the periodic graph with 32 edges, not the 24-edge ordinary knight graph, so the known periodic homotopy type cannot imply this result. Targeted keyword, alias, implication and exact-parameter queries were performed; they do not prove global bibliographic uniqueness.

## Mathematical value

PASS. This computes the complete **integral homotopy type** at the first square-board size where nonattacking-knight topology ceases to be contractible, together with the full natural dihedral character. The five-sphere wedge and its one-dimensional invariant subspace are finer information than knight-placement counts or gonality, and precisely distinguish ordinary boundary conditions from the known periodic four-cube case. The invariant is attached to a standard chess-graph family rather than an arbitrary hand-picked graph.

## Boundaries and unresolved risks

The theorem is limited to square sizes at most four, the nonequivariant homotopy type, and the rational symmetry module. No integral module decomposition or larger-board extrapolation is asserted. The closest full-text literature checked does not cover the claim, but relevant unindexed material could exist. No independent third-party proof review has taken place.

Self-review: passed. Independent audit: not yet performed.
