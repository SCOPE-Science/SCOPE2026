# Independent mathematical audit

## correctness

PASS

For odd m=n/2, row-minus-column parity descends to the twisted strip. A run's rainbow triangles are successive windows on the complementary track. For two nonadjacent empty columns the two windows lists are disjoint for two phase choices, giving 36 colourings each, and share exactly the two empty-column endpoints for the other two. Equality of endpoint colours is forced iff the separation is divisible by three on that list. Since 3 does not divide m, the lists cannot both force equality, and are compatible iff both separations are nonzero mod 3. The compatible shared case gives 54 per phase, including two free vertices. Adjacent empties give 108 per pair. There are m pairs per distance, giving 108m+72m(h-1)+108mg; reducing residues yields both quadratic laws, including m=5 with g=0. Weight m needs bipartiteness and the closed period-three sequence; with only one empty column an odd strip closes the two endpoints of the same track and again needs 3 dividing m. The even one-empty strip has distinct endpoints and recovers the credited linear case. Thus the revised proof also establishes the weights without importing a counting or existence assumption.

## originality

PASS

The repaired contribution is the two quadratic named singleton counts only. The strongest earlier Möbius-ladder enumeration demonstrably covers the constant and linear counts, now credited, but not the quadratic cases. The bounded literature evidence did not identify equivalent coverage of the surviving counts. This is a best-of-knowledge assessment, not priority certification.

## value

PASS

The two missing classes are the ones where a minimum singleton solution has two empty columns. Resolving how the twists couple their alternating runs both classifies the viable supports and determines the exact growth coefficient of the minimum solution space, useful for testing algorithms and for comparison with prism and set-valued models. This is not a recomputation of the minimum weight or an isolated small-order count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
