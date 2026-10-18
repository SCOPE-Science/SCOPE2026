# Independent mathematical audit

## correctness

PASS

For a selected set D of size s meeting part i in d_i vertices, any outside vertex in part i has exactly s-d_i selected neighbors. Therefore the defining inequalities and exact-three witness are equivalent to the stated occupancy conditions. Fix a witness part j with s-d_j=3. If s>=7, trim its selected occupancy down to3 while keeping the three selected vertices outside it; all incomplete other parts now have d_i<=3 and at least 3 neighbors among six retained selected vertices, giving a witness of size6. For s=3 every selected part must be complete and sums exactly3, yielding the P case. For s=4, the three outside-witness vertices must occupy three other distinct parts or a complete size2 part plus one other part (otherwise P), producing the stated r>=4 or r=3 size2 conditions. In residual r=3 no size2 and P false, a size5 witness selects2 in a >=4 part and distributes 3 others between the other two, feasible precisely with at most one singleton. Remaining r=2 requires 3 vertices from each side, hence both >=4; residual two-singleton r=3 is impossible. Independent brute occupancy enumerations matched the table for all 259 nonisomorphic multipartite integer profiles with total order<=12. This is corroboration only; unbounded proof is the witness reduction and cases.

## originality

PASS

Chen–Cai 2025 introduced proper 3-domination and computed certain K_{m,n} regimes, which the present classification recovers as bipartite subcases. Their full journal text was inspected, including the definition and bipartite/prototypical graph-class theorems, with no all-complete-multipartite classification. Related indexed SCOPE `(3,2)`-domination, liar domination and ordinary k-domination of multipartite graphs use different vertex-neighbor requirements, not an outside witness with exactly three chosen neighbors. The all-r exact 3/4/5/6/infinity boundary is not implied by those calculations. Unindexed alternate terminology remains a residual risk.

## value

PASS

This is a complete natural graph-family extension for an explicitly recently introduced domination invariant, going beyond the source biclique computations. The short witness-reduction lemma produces a uniform sharp upper bound6 for all part orders and exact existence/nonexistence thresholds. The resulting classification can be used without independent subset optimization. No algorithmic-general-graph or all-p generalization is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
