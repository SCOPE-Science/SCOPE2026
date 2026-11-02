# Scientific review

## Correctness
PASS. Direct witness-neighborhood analysis proves the exact omission iff criterion for all integers \(n\ge4\); binomial enumeration gives the all-size polynomial. Minimum-preserving exchanges are exactly swaps of a colored index with an empty index. A balanced directed color-transition multigraph supplies a constructive shortest route attaining the stated lower bound, including the one-buffer-move exception when occupied unions agree. The shell polynomial is an exact coefficient extraction with a five-state correction, not an extrapolation. Independent brute-force witness tests for \(4\le n\le8\) and all breadth-first distances from a transitive reference configuration for \(4\le n\le10\) passed.

## Originality
PASS under accessible-literature and mathematical-record comparison, with explicit priority caveat. The closest directly inspected primary work (Ghanbari, Jäger and Lehtilä, arXiv:2209.01795) enumerates other graph classes but does not contain the crown-graph classification or its exact distance shells. The Bousquet et al. survey (arXiv:2204.10526) treats reconfiguration frameworks, not this specialized graph. Yamanaka et al.'s colored-token swapping study on general graphs provides a broader computational framework that could subsume the isolated distance-computation task by specialization, but it does not characterize super dominating crown-graph sets or their full polynomial. Related available mathematical records on super domination of complete multipartite graphs and on other crown domination variants have nonidentical graph adjacency or feasibility predicates. An unindexed direct theorem or specialization remains a residual priority risk; absence in searches is not a proof of novelty.

## Value
PASS. A complete super-domination polynomial and the exact geometry of all optimum configurations are two natural complementary invariants for a family obtained by deleting the matching from a complete bipartite graph. The reconfiguration theorem detects the sharp zero-to-connected transition at \(n=5\), a unique distance-five antipode for every optimum, and a strict distinction between token jumping and token sliding. The full shell distribution refines extremal cardinalities to exact transformation costs rather than restating known graph parameters.

## Scope and limits
Only labeled crown graphs with \(n\ge4\) and fixed-size minimum configurations are covered. The predecessor finite enumerations do not serve as proof for all \(n\); the complete counting and distance arguments are given in RESULT.md. Earlier unindexed equivalent results and general colored-token-swapping specializations are the main originality risks.

Self-review: passed. Independent audit: not yet performed.
