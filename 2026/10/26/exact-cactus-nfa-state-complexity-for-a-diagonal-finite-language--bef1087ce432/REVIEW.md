# Review

## Correctness

**PASS.** The lower bound uses only the language definition and the cactus edge-cycle condition. Each letter requires its own intermediate state; a final state cannot serve three such states without creating a non-cactus \(K_{2,3}\) subgraph. Pairing indices gives a matching bipartite cactus construction with exactly \(k+1+\lceil k/2\rceil\) states. The unrestricted \(k+2\)-state comparison is proved separately.

## Originality

**PASS, with residual literature risk.** The closest recent source proves existence of bipartite cactus NFAs for all regular languages, but the accessible abstract gives no state-minimum formula for this family. The inspected paper on undirected state graphs requires symmetric transitions and studies a different model. Searches for the exact family and parameter did not surface a matching result. The full text of the recent paper and one older general NFA operation paper could not be obtained, so the literature comparison is not exhaustive.

## Value

**PASS.** The formula is exact for every \(k\ge1\), not merely for the illustrative three-symbol case. It measures a precise structural cost of requiring a cactus transition graph and shows an unbounded additive overhead of \(\lceil k/2\rceil-1\) states for \(k\ge3\).

## Closest literature and limitations

The recent existence theorem for bipartite cactus automata motivates the graph restriction. General NFA union constructions explain the unrestricted \(k+2\) count but do not impose the cactus condition. The exact result is limited to \(L_k=\{a_i a_i:1\le i\le k\}\) and epsilon-free NFAs. Full-text access to the recent source and the older general operation paper was unavailable; those are recorded as residual risks, not as evidence of noncoverage.

Self-review: passed. Independent audit: not yet performed.
