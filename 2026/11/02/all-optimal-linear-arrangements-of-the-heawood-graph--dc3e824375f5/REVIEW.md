# Review of the Heawood arrangement classification

## Correctness — PASS

The scope is precisely all bijections from the fourteen vertices of the Fano-plane incidence graph to positions 1 through 14. Three-regularity and the absence of cycles shorter than six give the cut profile \(0,3,4,5,6,7,6,7,6,7,6,5,4,3,0\). At cardinality seven the incidence count for a selected three-point/four-line configuration gives the needed edge ceiling; complementary cardinalities follow from cut symmetry. The prefix-cut identity gives an exact lower bound of \(69\). The explicit paired-hexagon orders attain every constrained minimum, and equality at sizes six and eight forces disjoint endpoint hexagons in every optimal order. Every interior prefix must be a single arc. The exact count is \(28\cdot3\cdot96\cdot2\cdot96=1{,}548{,}288\). The independent difference-set subset-DP and binary-vector Fano constructions reproduce the profile, optimum, ordered disjoint hexagon pairs, and count. No unproved extension to other graphs is asserted.

## Originality — PASS, with historical uncertainty

Horton, Parker, and Borie (2000), DOI `10.1016/S0166-218X(00)00173-6`, Theorems 3.1–3.2, already give the general constrained-cut lower bound and equality criterion, not this specific cut profile or optimizer census. Baez (2015), *Heawood Graph*, already describes the Levi graph and its 28 six-cycles. Dejter, arXiv:`1002.1960` (first posted 2010), Section 1, identifies their disjointness graph as the cubic Coxeter graph, so the number of disjoint partners is also not claimed as new. The present contribution is the necessary-and-sufficient characterization of all optimal arrangements and their exact named-vertex count. Searches for equivalent Fano/Levi-graph layout formulations and exact numerical counts did not identify an existing implication. An unindexed or unpublished earlier enumeration remains a residual originality risk; negative searches do not establish global priority.

## Value — PASS

This is a complete enumerative refinement of a natural optimization problem for the unique cubic girth-six cage and the Levi graph of the smallest projective plane. The proof shows how a classical Coxeter-graph incidence relation controls all optimal linear arrangements, not just the optimum. The explicit factorization provides an exact benchmark for optimal-order counting and for methods that use nested minimum cuts. The closed count is not a mere symmetry quotient or a recomputation of the known 28 hexagons.

## Limits and verification

The result concerns one distinguished fourteen-vertex graph, not a family of projective planes. The standalone scripts provide exhaustive finite corroboration of the proved characterization. No independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
