# Mathematical review: connected unicyclic neighborhood-homology obstruction

## Correctness
For every integer m >= 1, one pendant middle vertex in each disjoint three-vertex block must be dominated. This forces at least m tail choices, and cycle vertex c2 forces a cycle choice. If a maximal independent set had m+1 vertices, its unique cycle choice would be c2 and it would need t1. But t1 covers only two of the 3m tail vertices, whereas each other tail vertex covers at most three, so domination would be impossible. The explicit independent dominating set {c0,c2} union {t2,t5,...,t_(3m-1)} has m+2 vertices.

Deleting the closed neighborhoods of {t2,t5,...,t_(3m-1)} removes exactly the tail. The residual graph is C4. Its independence complex is two disjoint edges, with reduced integral H_0 equal to Z; this contradicts the proposed vanishing for p=m+1, q=m. This is an all-parameter proof, not a finite extrapolation.

For the sharp order-seven result, an separately implemented atlas enumeration covers every unlabeled connected unicyclic graph on 3 through 7 vertices. Signed simplicial boundary matrices were evaluated by exact integer Smith normal forms, including the augmented degree -1 chain group. The numbers of graph isomorphism classes by order are 1,2,5,13,33, with exactly one failure among the last 33. Orbit-stabilizer recovers labeled graph totals 1,15,222,3660,68295 and 2520 labeled failures at order seven. The unique bad isomorphism class is the C4 with a pendant path of three edges.

## Relation to prior mathematics
Berghoff's *On the homology of independence complexes* (arXiv:2008.06267, Theorems 1.2 and 5.4) proves the vanishing property for paths and cycles and asks in Question 5.5 which other graph families satisfy it. The theorem does not assert a connected unicyclic counterexample or classify the least one. Kim's ternary-graph theorem (arXiv:2101.07131) determines spherical-or-contractible homotopy types of individual induced-subgraph independence complexes but does not relate their homology dimensions to forbidden maximal-independent-set cardinalities. Adamaszek and Stacho's cross-cycle characterization concerns chordal graphs and does not apply to this induced-C4 witness.

These comparisons support a best-of-knowledge originality assessment. A differently formulated earlier observation or a stronger unindexed theorem remains a priority risk; a failed search by itself is not a novelty certificate.

## Mathematical value and limits
The construction answers a motivated graph-family extension question, and the exact seven-vertex minimum gives a sharp natural boundary. It does not classify every graph, every unicyclic graph satisfying the property, or forests. The small-order classification depends on exhaustive exact-integer computation, independently corroborated here; the infinite family follows from the structural proof.
