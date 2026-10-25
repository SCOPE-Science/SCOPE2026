# Review: exact leaf-conditioned sibling-pair law

## Correctness (C): PASS
The complete joint polynomial follows by choosing the leaf label set, attaching its leaves to a Prüfer-enumerated core tree and enforcing degree at least two at each core vertex. Explicit differentiation at \(y=1\) gives both conditional factorial moments. A path construction proves exact support rather than merely bounding it, and convexity proves the two sharp endpoints. The extracted standalone checker independently agrees with every Prüfer tree for \(3\le n\le8\), in 90 exact assertions. This finite agreement corroborates but is not used as the infinite proof.

## Originality (O): PASS (qualified historical priority)
The inspected Isaev–Southwell–Zhukovskii paper provides large-size central-limit results for pattern statistics on uniform fully labelled trees, not this finite joint leaf/sibling-pair distribution. Choi–Thompson–Wu (2020) and Choi–Kaur–Wu (2021) concern binary phylogenetic trees with only leaves labelled and different sampling laws; their exact and asymptotic cherry formulas do not imply the result for arbitrary-degree fully labelled Cayley trees. Searches using sibling-leaf pairs, cherries, leaf-conditioned counts, Prüfer generating functions and exact moment aliases produced no equivalent record. General older tree-enumerator coverage remains a genuine unexcluded risk.

## Value (V): PASS
Sibling-leaf clustering is a natural local shape statistic beyond the number of leaves. The joint polynomial gives the whole conditional distribution for every finite size; the Stirling-ratio mean/variance and exact attainable-value classification make it suitable for finite-sample null calibration on fully labelled trees. It is neither a selected numerical example nor an unconditional re-count of degrees alone: sharing a neighbour is an adjacency feature.

## Sources, comparisons and limitations
The evidence comes from arXiv:1912.09838 (Sections 1–2), arXiv:2002.12643 (Sections 2–3 and Theorem 3.3), and arXiv:2101.07488 (model definitions and main asymptotic statements), plus exact symbolic tree counting and a standalone exhaustive checker. All sources are compared by objects, conditioning, and their statements. The result is restricted to uniform fully labelled unrooted trees. Undiscovered older generating-function formulas might provide stronger coverage. No independent verification has occurred.

Self-review: passed. Independent audit: not yet performed.
