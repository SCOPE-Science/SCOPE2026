# Independent mathematical audit

## correctness

PASS

Parida–Moura Definitions 3.1 and 4.1 match the two edge conditions; W_n has n vertices and rim C_{n-1}. In these graphs every vertex has an incident edge. If B_i is contained in B_j with i distinct from j, an edge incident to j is either ij, violating endpoint incomparability, or an edge whose union contains third block B_i. Thus all blocks are distinct and globally incomparable, hence nonempty proper subsets for the cases in question. An independent bitset DFS enumerated all possible blocks for each vertex in fixed path/rim order, checking completed edge-unions against chosen third blocks and forbidding any future covered blocks. The final rim edge is checked, and for the wheel each spoke is also checked. Symmetry fixes the first block by size or the wheel center and first rim block by sizes and intersection; these tuples classify the relevant orbits of ground-set permutations. Pruning with too few permissible remaining blocks cannot suppress a completion. Exhaustion returned no assignments for P11@6, C10@6, W11@7, with respectively 132485, 183853, 564770 DFS states. The same computation found P10@6, C9@6, W10@7 as positive controls, and direct antichain and edge-union checks passed all four listed seven-point sequences for the indicated graphs. Replay: python3 /workspace/replay/05-cff.py; the run is recorded in /workspace/replay/05-cff-output.json. This is reproducible exhaustive computation, not formal verification or merely the frozen artifact's assertion. No assignment on up to the excluded ground-set size can exist, since smaller assignments embed in a set of that size with unused points. Subgraph monotonicity propagates the P11 lower bound to larger paths and cycles of length >=11. Parida–Moura Table 4 provides the remaining small upper bounds; C11@7 and C12@7 were also found and directly checked (C11: 1,234,235,236,27,246,456,346,347,357,567; C12: 12,13,14,15,16,67,36,234,35,57,47,27). For W12 the cited Corollary 4.16 applies since C11 has no isolates and t(C11)=7=t(1,11)+1, the latter by Sperner. Independently, on seven points the rim projections outside the hub block must form an antichain of eleven sets by the spoke constraints, hence at least six points lie outside the hub. The nonempty hub would be a singleton; global incomparability then makes all rim blocks disjoint from it, giving the impossible C11@6. Adding a disjoint singleton to the seven-point C11 family proves the eight-point upper bound. The wheels and all stated path and cycle ranges follow.

## originality

PASS

The Parida–Moura article and the related Parida dissertation have just the upper bounds or exact smaller orders in the corresponding table and boundary theorems. The distinct work is excluding the three next cases at the old ground-set size and constructing seven-point families past the table where the general image of the mixed-radix bound is eight. The propagated equalities and the application of the universal-vertex lemma are consequences, not independent novelties. The best-of-knowledge result does not establish priority over unindexed constructions.

## value

PASS

These orders are motivated by the first unresolved entries of a published small-order census, not an arbitrary sample. Closing the six- and seven-point thresholds and replacing eight with seven for orders 13–15 addresses a concrete construction problem posed by the gap between the source's small cases and its general bound. Exact lower and upper witnesses distinguish where an additional point really becomes necessary and give useful benchmarks in the published graph-CFF family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
