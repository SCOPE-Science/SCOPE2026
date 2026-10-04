# A 30-vertex lower cutoff for simple-base truncation counterexamples
## Finding
For every connected simple cubic graph \(G\) with at most eight vertices, the truncation \(T(G)\) has strong chromatic index \(\chi'_s(T(G))=6\). Consequently, any counterexample to the simple-base truncation question \(\chi'_s(T(G))=6\) must have at least ten vertices in the cubic base and at least thirty vertices in its truncation.

## Assumptions and scope
Graphs are finite and simple. A cubic graph is 3-regular. The truncation \(T(G)\) replaces each vertex \(v\) of a cubic graph by a triangle whose three vertices correspond to the three edges incident with \(v\); for every base edge \(uv\), the two corresponding triangle vertices are joined by one external edge. A strong edge-coloring assigns colors to edges so that any two edges at distance at most two in the line graph receive different colors. The claim concerns connected simple cubic bases of orders \(4\), \(6\), and \(8\), which are the only possible positive orders below ten.

## Proof
Fix a base vertex \(v\). In \(T(G)\), consider the three edges of the replacement triangle at \(v\) together with the three external edges incident with its triangle vertices. Every two of these six edges are either adjacent or have a common adjacent edge. Hence they form a clique of order six in \(L(T(G))^2\), so \(\chi'_s(T(G))\ge 6\) for every cubic base.

For the matching upper bound at base order at most eight, the exhaustive verifier generates every connected labeled simple cubic graph on \(n\in\{4,6,8\}\) by filling the upper triangle of its adjacency matrix subject to residual degree three. Isomorphic outputs are merged by exact graph-isomorphism tests. It obtains respectively \(1,2,5\) isomorphism types, agreeing with the classical census of connected simple cubic graphs. For each representative it constructs \(T(G)\), constructs the conflict graph \(L(T(G))^2\), and runs an exact backtracking 6-coloring search. A coloring is found for all eight representatives and is then checked edge-by-edge in the conflict graph. The local six-edge clique above supplies the matching lower bound.

The verified representatives are encoded in graph6 form in `verifier_output.txt`; this encoding is only a reproducibility aid and is not part of the mathematical definition.

## Verification
Run `python verify.py` with NetworkX 3.6.1 or a compatible later version. The script independently regenerates all connected simple cubic graphs on \(4\), \(6\), and \(8\) vertices, checks that the isomorphism-type counts are \(1,2,5\), verifies a local \(K_6\) in every strong-edge conflict graph, finds a 6-coloring for every representative, and checks every conflict edge against the returned coloring. The recorded run generated 1, 70, and 19,320 connected labeled graphs at the three orders and ended with the stated 30-vertex cutoff.

## Relationship to prior work
The 2025 open-problem collection asks whether every truncation of a cubic graph is strongly 6-edge-colorable and records only the truncated-prism family as a positive result. Tanwar's 2026 preprint gives an 18-vertex diamond-free claw-free cubic graph of strong chromatic index seven, but its base is a cubic multigraph with parallel edges; the paper explicitly leaves the version with a simple cubic base open. The present finite census addresses that remaining simple-base version and rules out every base of order at most eight. It is not implied by the 18-vertex minimality statement for arbitrary diamond-free claw-free cubic graphs, because truncations of eight-vertex simple bases have 24 vertices.

## Limitations
This is a finite cutoff, not a proof of the full simple-base conjecture. It does not determine what happens for the 19 connected simple cubic base graphs on ten vertices, nor for larger bases. The exact-generation and coloring verifier depends on a standard graph-isomorphism implementation in NetworkX; the generated type counts are cross-checked against the classical cubic-graph census. Direct full-text retrieval of the 2026 Tanwar preprint was unavailable during source inspection; its primary arXiv abstract and indexed proposition-level excerpts were inspected, so an unindexed body remark specifically duplicating this 24-vertex truncation census remains a residual literature risk.

## References
1. J. Barát, Z. Dvořák, P. Haxell, F. Kardoš, B. Lužar, A. Onderko, J. Rajník, R. Soták, N. Ulyanov, *Open problems of the 33rd Workshop on Cycles and Colourings*, arXiv:2511.02892, first posted 2025-11-04.
2. K. R. Tanwar, *A diamond-free claw-free cubic graph with strong chromatic index 7*, arXiv:2607.23462, first posted 2026-07-26.
3. OEIS A002851, connected simple cubic graphs: the counts at \(4,6,8,10\) vertices are \(1,2,5,19\), with references to Read and Wilson's *An Atlas of Graphs* and related cubic-graph generation literature.
