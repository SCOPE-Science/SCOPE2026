# Independent mathematical audit

## correctness

PASS

Distinct matrix units commute exactly when both cross-products vanish. For a clique with an off-diagonal vertex, its exact nonempty source and target sets are disjoint; maximality forces their whole rectangle and all unused diagonal entries. Adding any omitted unit conflicts with a present entry. The diagonal clique is the only other facet. Counting ordered supports gives M; inclusion-exclusion for covering every row and column gives C, with the diagonal subset independent. At z=-1 only supports partitioning [n] survive, each contributing (-1)^(n+1). The fixed-clique character follows by colouring permutation cycles, with the swap allowing two alternating colourings only on even cycles; the all-unused colouring accounts for the diagonal clique. For the full automorphism assertion, diagonal vertices have degree (n-1)^2 and off-diagonal ones degree (n-1)^2-1. After removing an index relabeling, each pair of orientations is fixed as a set by its two diagonal nonneighbors. At a shared endpoint two off-diagonal units commute precisely when both arrows point in or both point out, so the orientation swap choices on incident pairs must agree. The edge-incidence graph of K_n is connected (n=2 has just one choice of pair), giving exactly global transpose or identity. Finally the d-colour tensor permutation character is d^(number of cycles); its Schur–Weyl decomposition over Q gives the claimed Specht multiplicities. The bounded independent replay reproduced all cliques, maximal cliques, alternating sums and the fixed-clique counts for n=2..5; at n=4 it returned 1,16,66,72,7.

## originality

PASS

The independently distinct portion is the all-clique rank enumerator, its evaluation, and the full-group action on facets. Do not credit the group, the source-target principle, or Schur–Weyl duality as discoveries. An indexed broader result gives exact equivalent coverage of the facet classification, maximal-clique count and M after specializing to the trivial group; that overlap is real, but the identified result is dated later than this frozen record and does not give C or the character. This is a bounded comparison, not a priority certification.

## value

PASS

For the standard Brandt graph, the rank counts determine the face vector of its clique complex, while the fixed-facet character determines the representation and supports orbit calculations for subgroups. Neither follows from knowing the largest rank, the maximal rank distribution alone, or the automorphism group alone. In particular the dependence on parity of permutation cycles for orientation reversal is concrete equivariant data; the value is not in rederiving the group or restating the cut description.

The dated certificate retains the supplied scientific assessment, sources and limitations.
