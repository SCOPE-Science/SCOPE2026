# Independent mathematical audit

## correctness

PASS

The chain polytope is the intersection of nonnegative coordinate halfspaces with maximal-chain halfspaces. Their Euclidean normals have norms 1 and sqrt(k). A radius rho ball must have x_p>=rho; applying a longest chain gives (h+sqrt(h))*rho<=1. The uniform x=r*1 achieves rho=r because k+sqrt(k) increases with k<=h. The entire center set follows from the same normalized halfspace distances. Every element on an h-chain is pinned to r for any optimum; conversely an element outside all longest chains can be perturbed positively by less than the minimum of finitely many positive shorter-chain slacks, proving nonuniqueness. Independent h=1..5 radius values 1/2, 1/(2+sqrt2),..., checked; verifier source inspected but its finite labeled-poset enumeration cannot replace this arbitrary-poset proof. Nonempty hypothesis covers antichains h=1.

## originality

PASS

Best-of-knowledge originality: targeted Resultary comparisons, exact primary theorem/parameter inspection and implication tests do not reveal prior coverage of the specifically identified surviving result. A self-indexed copy of the assigned finding is not prior coverage; risks are documented.

## value

PASS

The exact inradius collapses all branching/width to height, while the full incenter polytope and uniqueness criterion detect whether maximal-length chains cover the ground poset. This is a complete metric/order-theoretic classification for a standard object; although the normalization step is elementary, the simultaneous all-poset sharp-radius and center-locus statement answers natural questions not a random finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
