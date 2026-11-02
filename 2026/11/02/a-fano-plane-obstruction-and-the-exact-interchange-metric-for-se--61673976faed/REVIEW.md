# Review: seven-player regular-tournament interchanges

## Correctness — PASS

A score-pruned orientation decision tree covers every one of the \(2^{21}\) possible orientations by unique binary branches and retains exactly \(2640\) regular tournaments. Triangle reversal neighbors are defined exhaustively; the degree formula \(inom73-7inom32=14\) is independent of computation. Complete breadth-first searches from all \(2640\) states reproduce the three metric profiles and radius \(8\), diameter \(9\). A second implementation begins from all label permutations of three public catalogue representatives, applies a distinct seven-neighbor-mask encoding, and independently obtains the profiles, converse distances and exact Fano decomposition counts. Both programs passed from their packaged paths. The short proof that \(7\) converse moves are equivalent to an initial cyclic Fano partition uses disjointness of the twenty-one flipped arcs. No infinite-family claim is made.

## Originality — PASS (qualified)

Brualdi–Li (1984) introduced and studied these same interchange graphs. McShine (2000), in its accessible full text, reports their proposed regular-tournament diameter formula, already numerically predicting \(9\) here. Neither this known prediction nor connectedness or regularity is claimed original. The proposed contribution is the complete labelled seven-vertex distance spectrum, its three isomorphism-orbit profiles, identification of the \(360\) diameter pairs as converse pairs, and the two/two/zero cyclic-Fano obstruction to shorter converse paths. McShine's full paper and the complete accessible Kolesnik–Mitchell–Przybyłowski discussion do not provide these statements; McKay supplies the three representatives but no interchange-distance table. The full Brualdi–Li chapter remains inaccessible and might contain an equivalent historical classification. This is a residual priority risk; search absence is not a uniqueness proof.

## Value — PASS

The fixed-score interchange operation is a classical generator for sampling regular tournaments. The full seven-player metric is the smallest substantial finite test of the long-standing proposed diameter formula and identifies which regular tournaments attain it. The Fano decomposition criterion gives a structural explanation for a sharp converse-geodesic dichotomy that is not conveyed by diameter alone. The finite all-source distance table also supplies an exact benchmark for Markov-chain and reconfiguration questions. A paper-length or all-orders theorem is not asserted.

## Sources and scope limits

Primary literature: Brualdi–Li (1984), *The interchange graph of tournaments with the same score vector* (chapter not obtained); Kannan–Tetali–Vempala (1999), *Simple Markov-chain algorithms for generating bipartite graphs and tournaments*; McShine (2000), *Random Sampling of Labeled Tournaments*, full text at https://www.combinatorics.org/ojs/index.php/eljc/article/download/v7i1r8/pdf; Kolesnik–Mitchell–Przybyłowski (2025), *Coxeter Interchange Graphs*, full text at https://link.springer.com/article/10.1007/s00026-025-00768-9; McKay's seven-vertex regular-tournament catalogue at https://users.cecs.anu.edu.au/~bdm/data/rt7.txt. An inaccessible directly relevant original could cover the result. Computational completeness is specific to seven vertices.

Self-review: passed. Independent audit: not yet performed.
