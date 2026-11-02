# Self-review

## Correctness

PASS. The theorem fixes the exact labeled Frucht graph, the parallel time rule, the minimum cardinality, and the unrestricted one-replacement adjacency. The fort-obstruction equivalence has a short proof. The fort verifier checks all 4095 nonempty subsets and tests every candidate initial set of size at most four; it obtains 66 minimal forts and exactly 89 minimum sets. An independently implemented direct propagation verifier obtains the same distribution over all four-set candidates. Both agree on the exact 89-set roster under the explicit LCF-to-edge-list mapping and build all 3916 potential minimum-set pairs and reproduce the sharp four-round connectivity threshold. The direct verifier proves the six-vertex fast component is a triangular prism (two disjoint triangles plus a perfect matching) and exhaustively computes graph diameters by breadth-first search. All reported computations were rerun from the complete files.

## Originality

PASS with specified historical uncertainty. The 2014 full arXiv preprint on propagation time defines the relevant efficient sets and proves that every connected nontrivial graph has at least two; it does not study Frucht configurations or exchange connectivity. The 2020 full arXiv preprint on zero-forcing reconfiguration defines the relevant exchange relation but does not study propagation-time strata or the Frucht graph. The two fields combine in a graph-specific sharp threshold not implied by either preprint. Targeted literature and mathematical-record searches for the graph, the speed histogram, and aliases found no dominating result. Searches cannot establish uniqueness; no independent literature audit has taken place.

## Value

PASS. Efficient forcing sets minimize time subject to the optimal initial cardinality, so reconfiguring among them without loss of speed is a natural control and solution-space question. This benchmark is the classical asymmetric cubic Frucht graph, rather than an ad hoc labeled construction. A disconnected optimum consisting of a triangular prism and an edge, followed by connectivity at exactly one additional round, gives a concrete counterexample to the expectation that feasible efficient configurations inherit the mobility of all minimum configurations. The diameter increase from six unrestricted to eight under a four-round cap quantifies the cost of that speed constraint. The result is a motivated, complete finite threshold, not merely an enumeration of subsets.

## Remaining limitations

The result concerns only the twelve-vertex Frucht graph and standard synchronous zero forcing, with one selected-vertex replacement of unrestricted distance. The finite certificate is exhaustive but is not a general theorem about cubic graphs; alternate historical terminology and inaccessible tabulations remain possible. Separate independent scholarly validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
