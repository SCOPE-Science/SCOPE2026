# Scientific review: avalanche complexes of bidirected stars

## Correctness — PASS

The threshold is the actual outdegree at every vertex: the centre fires with at least \(n\) chips and every leaf fires with at least one. Before the centre's first firing, its exact chip count is \(h+\sum_i\min(t,a_i)\), and each leaf loses at most one chip per step. Following that first centre firing, every leaf fires next, and subsequent centre-containing firing sets shrink by inclusion unless all vertices fire simultaneously. If the latter never occurs, the leaf support eventually vanishes and the centre holds the total mass \(s\); the resulting two-step cycle forces \(s<2n\). Conversely an all-vertex firing requires at least \(2n\) chips. These statements prove the three exact simplicial formulas for every \(n\ge1\) and every nonnegative configuration. The inequality \(s-m<n\) is equivalent to the centre first firing after all leaf chips have run out, including the all-zero-leaf boundary. The time-prefix topology is checked directly from the same nested-support argument.

The standalone checker reproduced exact face sets for 27,954 initial configurations and checked 65,453 time prefixes. The result is not inferred from those finite cases.

## Originality — PASS, with residual risks

Riihimäki and Smith (arXiv:2606.26786v1, submitted 25 June 2026) introduce the avalanche complex and classify examples on oriented paths and cycles. Their full accessible preprint was inspected in the definitions, principal results, and relevant discussion; the bidirected star, sharp all-vertex firing threshold, all-configuration face classification, and full zero-degree persistence formula are not stated there. In the earlier Scully–Jiang–Zhang paper, the classification of *periodic firing sequences* and results on tree-like subgraphs constrain eventual dynamics but do not supply the preperiod simplices required by the avalanche complex, or the exact star facet theorem. Ji–Li–Wang's directed periodicity work likewise does not identify an avalanche complex.

Searches for star avalanche complexes, bidirected-star sandpiles, equivalent two-component firing-support complexes, and the broader exact recurrence did not locate a logically covering published statement. This is not a proof that no equivalent statement exists. Residual risks include implicit derivation from classical star firing observations and unindexed work; the result is a concrete application of the newly introduced avalanche invariant rather than an assertion of an entirely new chip-firing dynamics.

## Value — PASS

The theorem supplies an exact complete classification for **every** initial configuration on the first naturally branched bidirected graph, not just an example or a finite list. It identifies the sharp chip-mass \(2n\) synchronization threshold, an explicit criterion for the sole disconnected homotopy type \(S^0\), and the whole time-filtration persistence barcode (no positive-degree bars, at most one infinite degree-zero bar). The distinction between periodic firing-pattern restrictions and the topology retaining transient firing sets is mathematically relevant. These are genuine structural and exact-filtration facts, not a routine restatement of homology ranks or an arbitrary parameter slice.

## Scope and remaining risks

No conclusion is asserted for larger branched trees, arbitrary digraphs, different thresholds, or graph actions. The independent mathematical audit has not been performed. Mathematical novelty could still be reduced by an undiscovered exact star-transient classification in prior chip-firing literature.

Self-review: passed. Independent audit: not yet performed.
