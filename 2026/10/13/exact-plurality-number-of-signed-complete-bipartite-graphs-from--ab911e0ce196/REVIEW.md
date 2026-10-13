# Self-review

## Correctness
**PASS.** Once the first vertex is ignited, the opposite shore is forced in one propagation phase. Exactly one additional ignition then occurs before the correlation-forcing wave on the original shore, so it can preempt at most one vertex; this is exactly the indicator correction in the formula. Every other original-shore vertex is governed by a row or column inner product. Zero correlations are the only vertices left unresolved after that wave, and they lie on one independent shore, so later ignitions assign them independently. This gives both the lower and upper bounds. The literal recursive verifier agrees with the formula on all \(1168\) signings in six exhaustive small profiles and on \(651\) additional structured profiles.

## Originality
**PASS, with a stated access risk.** Searches under the invariant name and complete-bipartite, biclique, sign-matrix, correlation, and inner-product aliases found no indexed theorem implying the row/column formula. The initiating 2026 abstract advertises exact signed-path results, a code formulation, switching-class consequences, and hardness, but no biclique theorem. A full-text copy of that very recent source was not available for section-level comparison, so an unindexed equivalent observation inside it remains the principal residual risk.

## Value
**PASS.** Complete bipartite graphs are a canonical dense family, and the theorem handles every signing rather than one special signature. It reduces an adaptive process to an explicit matrix statistic and yields a direct polynomial-time evaluation rule. The row/column-correlation mechanism is also structurally informative: it identifies exactly which vertices are forced by the first wave and which remain freely assignable because of zero correlation.

## Closest literature and limitations
The closest scientific source is the initiating paper *Burning Signed Graphs*, which introduces the plurality number and gives exact path results. Searches also returned signed-domination and signed-spectral results on multipartite or bipartite graphs, but those optimize different quantities and do not imply the burning formula here. The full-text access limitation is retained as a bibliographic risk; the finite verifier is only a consistency check.

Self-review: passed. Independent audit: not yet performed.
