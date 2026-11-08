# Independent mathematical audit

## correctness

PASS

For the six-vertex fully bidirected complete bipartite graph the directed arc vertex-set has cardinality 18. Face condition is indegree and outdegree at most one at each graph vertex and no directed cycles; a separate weak-component test characterizes the same disjoint directed paths. Exhausting all 2^18 bitmasks yields 714 nonempty faces with vector (18,108,264,252,72), independently recomputed. The source finite certificate and inspected verify.py give exactly 336 face-poset matching pairs with a complete directed Hasse topological sort over 714 vertices/2376 incidences: one critical 0-cell, five degree-2, 24 degree-3, twelve degree-4 cells. Signed integral cancellations at unit pivots preserve the cellular chain type; the resulting D3 is 5x24 with explicit determinant +1 on columns indexed 6304,33952,35088,65676,67716, while D4 (24x12) vanishes. The five primitive relations kill the five 2-spheres in the Morse CW 2-skeleton; 19 degree-3 generators remain. For a wedge of 19 S3, pi3=H3=Z^19, so zero D4 implies the twelve 4-cell attaching maps are all null; the full homotopy splitting follows. Separate independent GF2 boundary ranks (17,91,173,60) yield (1,0,0,19,12) as a corroboration, not proof of attaching maps.

## originality

PASS

Best-of-knowledge statement/implication comparison for this exact mathematical object, not novelty from titles or failed search. Closest sources and any inaccessible material are explicitly compared below; no assertion of exhaustive global priority.

## value

PASS

The first balanced nontrivial complete bipartite bidirected digraph has a naturally defined path-selection complex whose integral homotopy is not captured by known one-way chessboard models. Its explicit mixed-dimensional wedge, including 19 lower-degree spheres beyond the twelve top Hamiltonian classes, resolves a meaningful finite low-dimensional boundary and supplies a reusable exact benchmark without pretending to classify all K_m,n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
