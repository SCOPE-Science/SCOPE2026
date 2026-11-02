# Self-review

## Correctness — PASS

For the completely specified 20-vertex Desargues graph, two independently implemented programs reproduce the \(13{,}520\) minimum forcing configurations, their \(178{,}560\) exchange edges, and the full vertex-degree distribution. The full checker visits all \(77{,}520\) seven-element and \(125{,}970\) eight-element subsets, tests forcing by monotone closure, and runs breadth-first search from every reconfiguration vertex. Every one of the \(91{,}388{,}440\) unordered configuration pairs is compared with its Johnson lower bound: \(91{,}341{,}060\) attain the bound and \(47{,}380\) require exactly one extra exchange. The code checks all degree/metric counts and a concrete obstruction path. This constitutes an exhaustive finite proof conditional on replaying the included code; it is not an infinite-family proof or a sampled-experiment claim.

## Originality — PASS, with residual risk

Butler, Grout and Hall (arXiv:1211.4618, sections 2 and 5 and appendix) cover \(Z(D)=8\) and matrix-inertia applications, not the all-pairs configuration metric. Geneson, Haas and Hogben (arXiv:2009.00220, sections 1–2, 5–6) introduce zero-forcing reconfiguration and an enumeration method; their relevant theorems classify other families and do not furnish this instance's distance-defect histogram. Searches also covered the Desargues graph's bipartite-Kneser and generalized-Petersen aliases and exact candidate counts. Neither a covering table nor a stronger theorem yielding this metric was located. Search absence is not uniqueness proof: unindexed computations remain a possible source of prior coverage.

## Value — PASS

The refinement is not another proof of the already established forcing number or a graph-connectivity census. The natural Johnson lower bound measures the fewest seed replacements possible if intermediate configurations could ignore the forcing requirement. The result determines exactly how imposing minimum zero forcing affects **every** optimal exchange path: one extra move always suffices, is sometimes necessary, and its precise frequency and locations by Johnson distance are certified. Together with the nontrivial eccentricity split, this is a complete finite metric classification of a canonical symmetric incidence graph and a reproducible benchmark for optimal-set reconfiguration.

## Limits and closest literature

The claim is finite and computational. The general enumeration framework is prior work, the zero-forcing number is prior work, and no theorem about all generalized Petersen graphs is asserted. Exact all-pairs confirmation is concentrated in the C++ checker; the second checker independently verifies the host graph, closure procedure, configurations, adjacency and sampled distances. An equivalent result may be hidden in an unindexed calculation or specialized table.

Self-review: passed. Independent audit: not yet performed.
