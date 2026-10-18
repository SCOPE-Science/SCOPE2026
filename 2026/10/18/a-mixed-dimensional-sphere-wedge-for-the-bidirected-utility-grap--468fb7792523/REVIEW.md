# Scientific review: bidirected utility-graph multipath complex

## Correctness — PASS
The claimed six-vertex bidirected graph has exactly 18 directed arcs. All 262,144 possible arc subsets were checked under the indegree/outdegree and directed-cycle constraints. The integral complex has face counts \(1,18,108,264,252,72\), and a verified list of 341 signed unit pivots reduces its integer boundaries to zero with nontrivial reduced integral homology \(H_3\cong\mathbb Z^{19}\) and \(H_4\cong\mathbb Z^{12}\). The independent verifier reproduces the face counts and ranks over four fields. Triangle relations kill all non-tree edge generators, proving simple connectivity; \(H_2=0\) implies 2-connectivity. Standard cellular homotopy theory converts the resulting unit Smith factors for 4-cell attaching degrees into the asserted mixed sphere wedge. The checker and pivot certificate are included.

## Originality — PASS
The closest source is Caputi–Collari–Di Trani–Smith, arXiv:2208.04656, particularly its complete-bipartite chessboard case; that case has 9 one-way arcs, not the 18 bidirected arcs studied here. Vrećica–Živaljević (arXiv:0710.5252) study the complete-digraph cycle-free chessboard complex and connectivity, not this restricted-arc homotopy computation. Caputi–Collari–Smith (arXiv:2601.05670) treat bidirected paths/cycles, not cubic complete bipartite graphs. The closest searchable records address bidirected double stars and the unrelated discrete Morse vector-field complex of \(K_{3,3}\). Targeted graph, alias, rank, and stronger-coverage searches did not reveal a theorem implying the claimed \(19\)- and \(12\)-sphere wedge. An unindexed equivalent result remains possible; the assessment is not an assertion of exhaustive world-wide uniqueness.

## Mathematical value — PASS
The bidirected utility graph is a canonical first balanced cubic bipartite test object beyond the one-way chessboard setting and two-way low-degree families. Its multipath complex has an integral *mixed-dimensional* sphere wedge, not simply a known table count, Euler characteristic, or a reparameterization of earlier cases. The exact homotopy type supplies a substantive model for higher-degree bidirected bipartite topology. The computation makes no claim for larger \(K_{m,n}\) or for equivariant homology.

## Closest literature and limitations
Sources: arXiv:2208.04656 (definitions and one-way bipartite Theorem 3.7); arXiv:0710.5252 (full-digraph cycle-free chessboards); arXiv:2601.05670 (bidirected polygons). These are structurally adjacent but none of the inspected material directly computes the proposed complex. Exhaustive enumeration proves this finite case only, while the homotopy upgrade uses separately verified fundamental-group relations; finite-field ranks alone would not suffice. A nonindexed equivalent computation is residual risk.

Self-review: passed. Independent audit: not yet performed.
