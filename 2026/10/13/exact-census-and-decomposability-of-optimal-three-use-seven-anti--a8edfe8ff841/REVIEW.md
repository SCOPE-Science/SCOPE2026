# Self-review

## Correctness — PASS
The compatibility graph uses precisely the single-coordinate distinction \(\pm1\) modulo seven, equivalent to nonconfusability in the seven-antihole. Two different exhaustive C++17 clique recursions, independently constructing adjacency and using ascending-bitset and greedy-color ordering, agree on exactly \(38{,}259{,}704\) size-eight cliques through the origin and no size-nine clique. Transitivity and elementary double-counting give exactly \(1{,}640{,}384{,}809\) labeled optima. The complete two-use four-code census independently gives \(1{,}715\), with no size-five two-use code. Product factorization and inclusion–exclusion then give exactly \(35{,}329\) decomposable maxima, \(1{,}640{,}349{,}480\) indecomposable maxima, and \(343\) fully Cartesian maxima. The explicit indecomposable witness and translation-orbit arithmetic are checked from definitions. The finite computation establishes no result for other blocklengths.

## Originality — PASS
The closest full primary text, Jurkiewicz–Kubale–Ocetkiewicz (2015), gives the previously known size-eight optimum and one Cartesian witness for the same three-factor strong graph power, but does not enumerate all maximizing sets or their factorization types. Badalyan–Markosyan (2013) concerns two factors; the available abstract is not used to assert noncoverage of its unavailable full text. Later work on greedy zero-error codes treats the original seven-cycle rather than its complement at two uses. Searches using the exact graph, parameters, numerical counts, graph isomorphism, and code-theoretic aliases found no implication-equivalent equality census. Unindexed finite enumerations remain a residual originality risk.

## Value — PASS
The three-use seven-antihole parameter is a canonical, previously studied zero-error Shannon-capacity test case, not an arbitrary subcase. A familiar optimal Cartesian construction conceals a rich equality layer: more than \(1.6\) billion labeled optima exist, and all but \(35{,}329\) resist every one-versus-two-coordinate product decomposition. The exact separation between constructive and indecomposable optima gives a natural benchmark for zero-error code construction, exhaustive algorithms, and symmetry reduction.

Self-review: passed. Independent audit: not yet performed.
