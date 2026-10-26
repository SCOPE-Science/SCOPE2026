# Scientific review

## Correctness
PASS. A nonempty fort must contain a spine vertex; its selected core vertices force their own private leaves. For omitted core vertices the neighbor count determines which private leaves must appear, and optional leaves cannot survive inclusion-minimality. The exact containment criterion for canonical forts reduces to connectivity of an auxiliary graph joining selected core indices distance two apart across one missing core vertex. Connectedness is equivalent to an arithmetic interval of step two; the boundary-leaf count gives the stated closed polynomial. The proof handles \(n=1\) and both parities without a computational assumption. An independent original-definition brute-force implementation checks all \(349524\) vertex subsets for \(1\le n\le9\).

## Originality
PASS, with bibliographic risk. The original minimal-forts paper (arXiv:2404.05963) explicitly illustrates a 4-comb but does not give its entire fort family or a uniform size polynomial; its corona-product statements concern other configurations. The later universal cut criterion for minimal tree forts (arXiv:2512.12874) can be specialized to test any proposed comb subset, but contains no derived arithmetic-interval census or formula. The 2026 tree-wide bound and algorithm (arXiv:2605.07298) likewise do not provide this symbolic family calculation. Searches for named and equivalent descriptions, including maximal failed zero-forcing complements, did not find a covering enumeration. This is not proof of universal priority; a previously unindexed graph-specific calculation could cover the theorem.

## Value
PASS. The exact hypergraph of minimal-fort constraints is important in fort-cover formulations of zero forcing. A comb is a canonical family of caterpillar trees directly used to illustrate the original theory. The present complete *inclusion-minimal* classification, size polynomial and quadratic rather than exponentially growing family count are structural data not determined by generic upper bounds or a single pictured fort. The polynomial gives all facet-size layers of the minimal-fort clutter, not just one extremal size.

## Limitations
Only comb trees with precisely one pendant leaf at each spine vertex are considered. The all-order theorem is proved combinatorially; finite exhaustive tests are independent corroboration, not an infinite certificate. Priority could change with discovery of older equivalent results. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
