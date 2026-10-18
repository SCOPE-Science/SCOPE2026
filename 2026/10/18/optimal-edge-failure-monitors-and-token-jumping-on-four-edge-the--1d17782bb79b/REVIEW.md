# Review of minimum monitors on four-edge theta networks

## Correctness — PASS

The graph, terminal and arm coordinates, geodesic uniqueness conditions, and two-selected-vertex MEG definition are explicit. The arm-intersection lemma proves that one internal selected vertex on every arm is necessary. The coordinate-sum comparison shows why singleton depths one and three cannot suffice without a terminal. This excludes all size-\(r\) sets. At size \(r+1\), a complete split by selected-terminal count yields exactly the three displayed families; explicit cross-arm paths prove their feasibility. Token-jump adjacency follows by exact symmetric differences. Counting the punctured-hypercube edges and exhibiting extremal reconfiguration paths prove the graph formulas and diameter. The independent finite checker tests the edge-deletion distance condition itself; finite cases are not substituted for the proof.

## Originality — PASS subject to stated bibliographic risk

The 2022 definition and basic-class classifications [1], 2022 hardness/product results [2], 2024 graph-operations and subdivision bounds [3], 2025 structured-class classifications [4], and 2025 cyclomatic-number bounds [5] do not state the complete four-edge multi-theta optimum classification or token-jump reconfiguration graph. In particular [3, Theorem 7.2] is a general inequality for at least two subdivisions of each edge; the analyzed family subdivides \(K_{2,r}\) only once. Results about edge-general-position and one-source distance-edge monitoring are not equivalent: they use different feasibility quantifiers. Relevant full primary texts, topical searches and existing accessible mathematical-result records were compared by implication. No stronger covering statement was identified. Unindexed equivalent work or a result within an inaccessible appendix remains a priority risk; absence of a search hit does not prove novelty.

## Value — PASS

A parallel-path network is a natural model of multiple equally short redundant connections, where shortest-path ties make failed-edge detection structurally delicate. The classification determines all optimal probe locations, not just the scalar minimum; their number grows exponentially with the number of arms. The exact token-jump network quantifies the feasibility of single-probe replacements, establishing connectedness, complete degrees and a sharp diameter. These are distinct, useful configuration-space facts not determined by general MEG bounds.

## Boundaries

Only \(r\ge3\) with equal four-edge paths is proved. Unequal arms, token sliding and independent peer validation are outside the claim. A symbolic argument covers all integer parameters, while exhaustive checking covers only \(3\le r\le7\). References [1]–[5] are listed in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
