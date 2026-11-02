# Scientific review: edge-triangulated total-domination enumerators

## Correctness — PASS

The exact all-set enumerator follows from the condition that the selected original vertices form a vertex cover. Original selected vertices isolated inside that cover each require at least one incident selected new vertex. Their edge groups are disjoint, yielding the exact product. For the complete bipartite specialization, every vertex cover contains an entire shore; minimality forces either the entire shore plus one vertex of the other shore (and no new vertices), or the entire shore plus exactly one incident new vertex per shore vertex. These four disjoint types establish the full polynomial, sharp cardinality spectrum, and concentration. An independent graph-adjacency enumeration implemented in `verify_total_domination.py` checked 46 isolate-free small graphs, nine complete bipartite cases, 1,259,880 candidate vertex subsets, and 121 arithmetic parameter pairs. Critical all-order statements are proved mathematically; finite checks are corroborative only.

## Originality — PASS (provisional literature comparison)

Sigarreta, *Total Domination on Some Graph Operators* (2021; doi:10.3390/math9030241), Theorem 2, relates the scalar total-domination number of the same edge-triangulation operator to a domination parameter of its base. The inspected paper does not give the two-variable total-dominating-set enumerator or the complete inclusion-minimal census of edge-triangulated bicliques. Bermudo, *Total Domination on Tree Operators* (2022; doi:10.1007/s00009-022-02236-7), studies scalar bounds for operators applied to trees, not this complete-bipartite census. Bahadır, Ekim, and Gözüpek, *Well-Totally-Dominated Graphs* (2020; arXiv:2010.02341), gives the general setting for minimal cardinality spectra without providing the present identity. Searches also considered the synonyms triangle expansion, edge corona, and complete-bipartite edge triangulation. No covering result was identified, but unindexed equivalent treatments and earlier terminology remain residual priority risks. The minimum-cardinality scalar formula is not asserted as new by itself.

## Mathematical value — PASS

This is not an arbitrary numerical slice: an established graph operator and total-domination invariant combine to give a uniform exact two-variable product formula for arbitrary isolate-free base graphs. Specialization reveals a complete four-class classification, unbounded gaps in the possible sizes of inclusion-minimal total dominating sets of connected 2-degenerate graphs, and exponential concentration at the maximum minimal-set size. The full enumerator distinguishes structures that the known scalar minimum cannot capture. Its vertex-cover sum need not be computationally efficient on arbitrary graphs.

## Limitations

Absolute publication priority is not established; the relevant older operator paper was inspected, but a differently named or poorly indexed full-text result remains possible. The universal proof assumes no isolated base vertex and the four-class classification assumes both bipartite shores have at least two vertices. The finite verification is not an independent review or a substitute for the mathematical proof.

Self-review: passed. Independent audit: not yet performed.
