# Scientific review

## Correctness — PASS
The complete 145-obstruction description exhausts all 1073 augmented faces; no face is omitted by the criterion. The 530 repeated-toggle pairs admit an explicitly enumerated acyclic oriented Hasse graph, leaving a Morse CW model with one point, ten three-cells and one four-cell. Signed integral gradient-path elimination gives attaching vector \((0,0,1,0,1,1,1,1,1,1)\), which is primitive and cancels exactly one three-sphere, yielding nine spheres in the homotopy type. Separately, all 120 natural automorphisms have their signed Lefschetz traces checked and agree with the two-subset permutation character minus the trivial character. The included exact Python checker regenerates every certificate from the graph definition. The finite exhaustive calculation suffices here because the theorem concerns one finite graph, not an infinite family.

## Originality — PASS, with documented risk
The complete-graph and complete-bipartite-graph classification of Linusson–Shareshian–Welker does not cover the Petersen graph. The general arbitrary-graph Leray bound of Holmsen–Lee only bounds high-degree homology; it cannot imply the exact integral homotopy type or the character. Shan–Wang's 2026 non-matching edge-addition theorem is stated for bipartite graphs, whereas Petersen is nonbipartite. Related indexed records describing the *matching complex*, the *two-matching complex*, and the *total three-cut complex* of Petersen refer to mathematically different simplicial objects; none entails the asserted edge-subset non-matching classification. Equivalences, known stronger covers, named-graph tables and candidate-specific searches were investigated. The full text of the fresh preprint could not be inspected; any nonbipartite incidental example in that text or unindexed literature is a residual originality risk, not a claim of exhaustively proven uniqueness.

## Mathematical value — PASS
This exact determination concerns the canonical vertex-transitive, nonbipartite cubic Petersen graph, a natural test object where the prominent general and bipartite non-matching results do not provide a classification. It supplies the integral homotopy type and a complete nine-dimensional rational automorphism module; the latter makes the symmetry information explicit rather than merely reporting the homology rank. The result is finite and self-contained, with the scope of the contribution bounded accordingly.

## Verification and limitations
A separate executable checker constructs the graph and all faces; proves the matching acyclic by exhaustive finite Hasse traversal; reconstructs signed integral Morse boundaries; and checks all group elements. The claimed wedge is nonequivariant and the representation is rational. Literature comparisons cannot exclude unindexed or text-inaccessible material. No third-party scientific validation is asserted.

Self-review: passed. Independent audit: not yet performed.
