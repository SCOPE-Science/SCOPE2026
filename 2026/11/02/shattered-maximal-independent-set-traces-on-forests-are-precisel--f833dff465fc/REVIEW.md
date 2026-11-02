# Scientific review: Shattered maximal-independent-set traces on forests are precisely induced-matching sides

## Correctness — PASS
The proof establishes the statement for every finite forest by induction on the vertex set. It correctly uses the positive-vertex branch when the leaf is outside the support but its neighbor is in the support, avoiding the invalid shortcut of only fixing the neighbor negative. The selected induced-matching edges are isolated from the residual because the residual is outside \(N[u]\) and the attached vertex is a leaf. Empty graphs and isolated vertices are covered. Exhaustive tests across 3,272 labeled forests through six vertices are corroboration, not the proof.

## Originality — PASS (best-knowledge, residual historical risk)
The most directly relevant inspected primary work is Liu–Shangguan–Skokan–Xu (2024), Lemma 27, bounding the same MIS hypergraph's VC dimension by *bipartite* induced matching number. This is insufficient for the exact ordinary induced-matching theorem even on the four-vertex path. Kahn–Park (2019) and Palmer–Patkós (2022) concern MIS enumeration and induced-matching constructions, not a forest-wide support equivalence. Searches of equivalent terminology and available published mathematical records did not identify dominating coverage. Unindexed priority remains possible.

## Mathematical value — PASS
All shattered vertex supports of a natural finite relational solution class receive a structural classification, and the exact VC dimension for every forest reduces to an established graph invariant. The five-cycle provides a sharp demonstration of why acyclicity is necessary. This is not a finite census, routine reindexing, or marginal parameter improvement.

## Limits
No claim about the Littlestone dimension or cyclic graphs is made. The matching-to-MIS lower direction was already a known construction. The 2024 inequality is not claimed as novel; only its sharpened forest characterization is under review. Exhaustive historical-priority validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
