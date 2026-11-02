# Scientific review

## Correctness (PASS)

The rank formula is checked directly against every transition of the specified automaton, including wrapped-cycle and merger boundary cases. At each pair the rank drops by at most one per letter, and exactly one letter drops it by one, yielding the exact minimum and geodesic uniqueness. Counting ranks in consecutive blocks for short and long circular gaps proves the bijection with \(1,\ldots,\binom n2\). The maximum-rank path visits all pair states once; its explicit label is the displayed master word. An independent reverse-BFS checker and all-pair tests passed on the finite ranges stated in the result; the argument for all orders is deductive rather than experimental.

## Originality (PASS, with priority risk)

The closest inspected literature is Gusev (2014, arXiv:1404.6731v1, Section 3), giving a full odd-order pair-automaton transition representation for random absorption-time analysis. Its graph contains enough information to derive shortest paths after nontrivial optimization, so it is not treated as unrelated. Szykuła (2026, arXiv:2608.24245v1, Sections 2.1 and 2.4) states the established general pair-synchronization upper bound, including extremality in the Černý family; that extremal fact is not claimed as new. The two inspected statements do not state a pointwise all-pair formula for both parities, a one-to-one spectrum, unique shortest merging words, or their common suffix representation. Searches of exact and alias formulations and published research records yielded no directly covering claim. Residual risk: existing odd-order pair graphs or an unindexed analysis might make this result previously known.

## Value (PASS)

A prescribed pair's exact merging time is a natural local synchronization invariant. This theorem determines that invariant for *every* pair in all orders, proves the highly restrictive all-distinct spectrum, and exhibits a unique global geodesic organizing every optimum as a suffix. It gives the full distribution and optimal control policy, not merely the previously known maximal bound or an arbitrary small parameter calculation.

## Scientific limitations

This is a theorem for the classical cycle-plus-one-merger automaton and does not generalize to all synchronizing automata or classify shortest whole-automaton reset words. The prior literature contains a particularly relevant complete odd-order pair automaton and should be examined by any independent priority review. Finite checks do not certify the infinite proof or priority.

Self-review: passed. Independent audit: not yet performed.
