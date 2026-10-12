# Review of Minimum restrained double Roman functions of half graphs

## Correctness
PASS. The two four-vertex end blocks each have weight at least \(4\), giving the all-\(n\) lower bound \(8\) for \(n\ge4\). A weight-\(8\) construction exists. Equality in each end-block bound has only three local patterns; the double Roman requirement at \(b_3\) and its symmetric counterpart eliminates every combination except the four-corner labeling. The exceptional cases \(n=2,3\) are exhaustively checked over all \(4^{2n}\) labelings by the included direct-definition verifier. The same checker also confirms the unique optimum for \(n=4,5\).

## Originality
PASS. The 2021 introducing paper was inspected in full text. It introduces restrained double Roman domination, gives general bounds and several standard graph families, and contains no half-graph or chain-graph occurrence. A second primary paper was inspected for broader coverage; it develops hardness, bounded-clique-width algorithms, tree results, and small-value characterizations rather than a half-graph formula. Exact and semantic searches under half graph, chain graph, Ferrers graph, and restrained double Roman terminology found no equivalent theorem. The closest indexed results concern restrained domination or restrained Roman domination, which are different invariants.

## Value
PASS. Half graphs are the canonical twin-free chain graphs and are a natural structured family for domination parameters. The theorem identifies a constant exact value despite increasing order and proves a sharp optimizer transition: five minima at \(H_2\), nine at \(H_3\), and a unique minimum from \(H_4\) onward. The end-block forcing argument explains the phenomenon structurally rather than reporting a computed sequence.

Self-review: passed. Independent audit: not yet performed.
