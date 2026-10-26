# Self-review

**Correctness — PASS.** All cases arise from bipartitioning a forest into two pairwise-intersecting two-subset classes; the star-or-triangle lemma is proved directly. Mixed triangle/star and two-star cases supply the sharp bounds and equality classification. Distinct-block set intersection calculations give exchange components. The independent exhaustive checker verifies all candidate optima and one larger cardinality for \(n=5,6,7,8\), independently checking cycle-freeness and graph exchange adjacency. The unrestricted proof does not depend on finite extrapolation.

**Originality — PASS (with residual risks).** The 2013 Chappell–Pelsmajer source introduces relevant induced-forest/feedback-set language and studies bounded-treewidth estimates. Alishahi–Taherkhani (2018) is closer: its Kneser \(K_{2,2}\)-free theorem already implies the eventual star-plus-one-edge shape, which is not asserted new here. The present all-parameter sharp crossover \(n=7\), complete small-order exceptional classifications, labeled counts and disconnected clique-exchange geometry are not given by the inspected statements. Overlap was checked via feedback-vertex sets, decycling, intersecting pair families, and \((2,2)\)-union-intersecting language; prior unindexed exact results remain possible.

**Value — PASS.** A sharp family-wide feedback-vertex-set classification and the complete move-preserving optimum structure give a concrete obstruction to local-search reconfiguration on standard Kneser graphs. The boundary coexistence at \(n=7\) is natural and mathematically motivated.

**Limitations.** Only pair-Kneser graphs and one-vertex replacements are classified. Later Kneser forbidden-subgraph extremality supplies some large-order consequences. A closely related older sharp \(K_{2,2}\)-free result could potentially reduce the originality of the threshold; independent expert validation is not claimed.

**Primary references.** Chappell–Pelsmajer, Electronic Journal of Combinatorics 20(4), P8 (2013), DOI:10.37236/3826; Alishahi–Taherkhani, arXiv:1801.03972 (2018).

Self-review: passed. Independent audit: not yet performed.
