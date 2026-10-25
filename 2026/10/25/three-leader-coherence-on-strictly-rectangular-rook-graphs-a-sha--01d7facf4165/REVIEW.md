# Scientific review

## Correctness
PASS. The proof reduces the three-grounded-vertex trace to an exact two-by-two Green-matrix formula using the three product-Laplacian projectors. Six coordinate-equality orbits exhaust three distinct vertices when both factors have at least three vertices; for two rows only three orbits remain. Exact positive-denominator polynomial certificates prove strict optimality for all unequal factor sizes, supplemented by 37 exact independent inversions. The checked statement excludes square rook graphs.

## Originality
PASS, subject to possible unindexed stronger literature. Fitch and Leonard (2014/2016) give joint centrality for arbitrary leader sets and optimize cycles and paths; Patterson, Yi and Zhang (2017) give general resistance-based formulas and optimize other families. Existing stronger three-leader strongly regular coverage includes square rook graphs, which are outside the claim. An earlier two-leader Hamming result and rook-graph two-edge-failure results use different objective domains and do not imply this three-leader classification for unequal factors. Searches by rook, line-graph, product, joint-centrality and grounded-trace aliases did not uncover a broader theorem that determines all the strict optimizer classes.

## Value
PASS. The complete infinite-family optimum, exact rational minimum and exact optimizer counts characterize three-leader placement on a canonical heterogeneous product network. At two rows the best triple must reuse a row, but starting at three rows all optimum placements become pairwise nonattacking; this is an exact structural boundary, not a small numerical gain.

## Limits
Only unit conductances, strictly unequal factor sizes, and exactly three noise-free leaders are established. The polynomial identities can be checked with the included standalone program, but its finite direct tests alone are not proof. Specialized unindexed literature remains a possible originality risk.

Self-review: passed. Independent audit: not yet performed.
