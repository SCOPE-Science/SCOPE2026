# Scientific review

## Correctness — PASS

The crown graph is defined by opposite-shore nonmatching adjacency. A set with fewer than two chosen vertices on either shore cannot be connected dominating; at least two on each shore suffice except when the shore-index pairs coincide, yielding two disjoint edges. The all-CDS polynomial is exact by this characterization. Any larger connected dominating set has a deletable vertex, so the minimum configurations are precisely the distinct ordered two-subset pairs. Each token exchange changes one Johnson coordinate. The graph-metric proof covers both single-coordinate routes and the possible two-coordinate distances zero, one, or two; the only obstructed shortest route is the adjacent swap, repaired by a three-step common-neighbor path. The ordered-pair polynomial follows from two diagonal inclusion–exclusions in the full product and a correction of exactly \(vk\) adjacent swaps. An independent implementation of the original domination and connectivity predicates verifies the resulting formulas for \(3\le n\le7\). This is evidence supporting, not replacing, the infinite proof.

## Originality — PASS, with priority risk

OEIS A033487 explicitly records the number of minimum connected dominating sets in crown graphs (dated annotation June 29, 2017); neither that count nor the scalar minimum is credited as a new theorem. The reconfiguration survey by Mynhardt–Nasserasr (2020) covers the token-exchange/sliding distinction and Johnson-graph embeddings but does not present the crown-specific off-diagonal square, its exact shortest-path distance correction, or its complete ordered-pair distance polynomial. Full relevant material from Abu-Khzam (2021), Abu-Khzam and coauthors (2022), and Sayadi (2019) concerns counting algorithms or other host graphs. Crown-related existing enumerations of restrained domination, perfect Roman domination, and edge-metric bases do not imply the connected-domination exchange metric. A two-token Johnson-graph result under another name could cover this theorem; no exhaustive priority claim is made.

## Mathematical value — PASS

The reconfiguration graph determines which optimal connected backbones can be reached by one-vertex substitutions, and the distance-shell polynomial quantifies the exact number of ordered configuration pairs at every exchange cost. The sharp adjacent-swap delay and the exchange/sliding separation expose structure not recoverable from the known minimum-set number. This is a complete natural infinite-family distance classification, not a mere normalization or finite lookup.

## Scope and limitations

The proof covers every integer \(n\ge3\), with the exceptional diameter at \(n=3\) handled explicitly. The computational verifier stops at \(n=7\). Independent audit has not been performed, and full publication-priority certainty is unavailable. General results on ordered two-particle configuration graphs remain a residual overlap risk.

Self-review: passed. Independent audit: not yet performed.
