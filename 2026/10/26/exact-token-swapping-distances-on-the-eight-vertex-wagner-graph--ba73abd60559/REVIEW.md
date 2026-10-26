# Self-review: Wagner token-swapping distances

## Correctness
PASS. The precise twelve-edge Wagner graph is defined without ambiguity; relabeling tokens makes the token-swap graph vertex-transitive. A complete breadth-first search of all \(8!=40320\) permutation states proves the exact distances. The supplied verifier executes two BFS algorithms with distinct representations and asserts pointwise equality of their complete distance arrays. The last layer has \(138\) states at distance ten. Independent shortest-path computation on the eight base vertices verifies the transport lower bound and all gap counts. The claim is finite and all arithmetic is exact.

## Originality
PASS, subject to documented search limits. The relevant 2014 foundational labeled-token-swapping study addresses general bounds and graph classes, not the Wagner graph's sharp metric. Explicit numerical comparison discovered the **cube** profile already in Zheng's 2009 reversible-circuit table; this known result is distinguished from the Wagner profile and is not claimed as new. Published research-record and targeted literature searches for Wagner, Möbius ladder, transposition Cayley word metrics, and the numerical signature found no implication covering the Wagner-specific census. Known same-graph matching and Morse complexes involve different states and moves. A previously unindexed complete word metric remains a risk; full texts of some peripheral papers were not inspected.

## Value
PASS. The Wagner graph is a canonical nonbipartite eight-vertex cubic graph, a natural comparator of the equally sized degree-three hypercube. The exact token-swap diameter, full shells, and sharp transport-heuristic slack measure how graph wiring changes sequential permutation routing: Wagner diameter ten and \(138\) hardest permutations versus the already published cube diameter twelve and single hardest permutation. The classification supplies a finite calibration instance for shortest-swap algorithms; neither correct enumeration alone nor a broader unseen theorem is invoked to manufacture significance.

## Scientific limits
The result is not an infinite-family formula and does not settle the complexity of general token swapping. All novelty judgments are evidence-based and may be revised by newly found sources. Reproducibility requires ordinary Python 3 and the included source.

Self-review: passed. Independent audit: not yet performed.
