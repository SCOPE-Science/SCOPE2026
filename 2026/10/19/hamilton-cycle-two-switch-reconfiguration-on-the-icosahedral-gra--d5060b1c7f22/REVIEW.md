# Independent mathematical audit

## correctness

PASS

Read the complete enumeration proof and both supplied algorithms without executing uploaded scripts. A legal switch is equivalent to two distinct spanning cycles sharing exactly ten edges; since each cycle has degree two, the four symmetric-difference edges are an alternating four-cycle. An XOR candidate must still be one Hamiltonian cycle, not just a 2-factor. I independently regenerated the host graph from cyclic permutations of (0,±1,±(1+√5)/2), testing squared edge distance four in the exact quadratic ring. Relabeled a vertex as 0, its neighbor ring as a_i, and the second common neighbor of a_i,a_{i+1} as b_i. An independent degree-constrained edge-set recursion propagated the forced inclusions/exclusions for degree two and branched exhaustively on each unresolved vertex's remaining edge choices; a full assignment was retained iff connected. Bucketed each cycle by every ten-edge subset obtained by deleting two edges, and joined cycles in the same bucket. This exactly reproduced the frozen certificate's sorted 1,280 masks and entire 1,800-pair list. Traversals produced 80 singletons, 60 pairs and 30 components of order 36. Each large component had 58 edges, diameter 8 and degree counts 1:2, 2:11, 3:8, 4:8, 5:6, 6:1. Distances to the vertices of one ordered triangular face distinguish all 12 vertices. Every automorphism is thus uniquely determined by the image of this face; testing each ordered image face by distance fingerprints and adjacency produces 120 automorphisms. Their action gives component orbit (order,count) pairs (1,20),(1,60),(2,60),(36,30), proving large-component isomorphism. Replay paths for the frozen certificate are `python verify_flips.py certificate.json` and `python verify_direct.py certificate.json` in the record directory; the former checks the automorphism action and diameter and both verify the full tables. This is finite exact enumeration for the specified graph and move, not an all-graph assertion.

## originality

PASS

Best of current knowledge: the switch and tour census are prior, but no inspected available statement or table gives the two-edge reachability graph, its component invariants, or its component action for the icosahedron. Access to two historical sources was partial; neither the count nor the move is credited as original.

## value

PASS

This is a natural symmetric benchmark for Hamiltonian reconfiguration under the standard local move, not an arbitrary subcollection of tours. The exact decomposition shows very limited reach despite the host's high symmetry and sizeable tour set, and the distinct singleton orbits distinguish two symmetry classes of frozen tours. The full certified adjacency and orbit classification give comparable data for other graph classes or move sets. The value lies in this classification, not counting Hamiltonian tours again.

The dated certificate retains the supplied scientific assessment, sources and limitations.
