# Scientific review

## Correctness — PASS
The model explicitly samples two parents with replacement and counts a rooted triangle in the simple underlying graph only when its largest-label vertex arrives. The birth event has exact conditional probability \(2D_{t-1}/(t-1)^2\). Independent Bernoulli root-adjacency indicators give the exact first moment. The two-arrival identity yields a total coincidence correction \(O((\log N)^2/N^2)\), allowing the second-order tail by Bonferroni. Summability proves almost-sure finiteness; tail integration proves the sharp moment boundary. The standalone exact rational verifier corroborates marginal/pair moments, and 36 finite-window Bonferroni comparisons. Finite checks do not establish the limit independently.

## Originality — PASS on inspected evidence
Briend–Calvillo–Lugosi (2022) treat motif-based root detection and discuss triangles, but their double-cycle confidence-set theorems do not state the last rooted simple-triangle birth law. Janson (2023) analyzes descendants of a DAG vertex. Björklund–Holmgren–Janson–Lo (2023) analyze global edge-labelled multigraph cycle counts, not the largest arrival label of a root-marked simple triangle. Semantic published-record searches on last triangle birth, oldest/rooted triangles, recursive attachment and zeta constants identified no covering result. Residual historical-priority risk remains: a sufficiently general age-marked point-process result not identified in these sources might imply the theorem.

## Value — PASS
The source literature explicitly motivates identifying ancient vertices by small cycles. This theorem gives a sharp, natural obstruction to naive last-arrival intuition: the number of root triangles is almost surely finite with finite expected count, yet their final birth time has a logarithmic-over-linear tail and infinite mean. It identifies a precise fractional-moment transition, not a routine recomputation of the global triangle count.

## Limits
The proof is for independent two-parent sampling with parallel edges ignored in triangle detection. No extension to other attachment rules or multigraph-copy counting is claimed. Independent historical verification or audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
