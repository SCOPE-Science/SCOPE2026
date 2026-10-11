# Scientific assessment

## Correctness — PASS
The claim has an all-parameter proof: exact graph-square adjacencies, a five-case table of closed-neighborhood folds for each deleted inner vertex, and free-triangle collapses from the surviving outer cycle square. The fold table covers all indices for \(n\ge13\), including cyclic wraparound. An independent standard-library verifier checks the square adjacency and all displayed domination relations for \(13\le n\le40\), and computes all mod-two boundary ranks at \(n=12\). The finite tests are checks of the symbolic proof, not an extrapolated infinite argument.

## Originality — PASS
The closest primary source is Adamaszek's *Clique complexes and graph powers* (arXiv:1104.0433). Its girth-seven theorem is inapplicable because every target graph has five-cycles; its alternative closed-neighborhood condition is also violated by five-cliques in the square of a cubic graph. Its cycle-power calculation applies only after the new sequence of inner-vertex deletions. Adamaszek–Adams' circle-Rips classification does not classify this two-ring graph metric. Direct searches of the generalized-Petersen/flag/graph-square/Rips formulations and comparison with relevant indexed results did not reveal a dominating theorem. An obscure prior equivalent statement remains a genuine risk.

## Value — PASS
The family is a standard infinite family of cubic two-ring graphs with persistent five-cycles. A structural simplicial collapse despite those five-cycles extends beyond the scope of the natural girth-seven collapse theorem. The sharp obstruction at \(n=12\) makes \(13\) an exact stability threshold, rather than an unmotivated finite computation.

## Limitations
No claim is made about other scales, other second parameters, integral homology of the exceptional case, or absolute novelty beyond the inspected literature and indexed comparison. Independently repeatable code certifies the finite boundary case; the all-parameter assertion depends on the displayed symbolic graph-fold proof.

Same-model review: passed. Independent audit: not yet performed.
