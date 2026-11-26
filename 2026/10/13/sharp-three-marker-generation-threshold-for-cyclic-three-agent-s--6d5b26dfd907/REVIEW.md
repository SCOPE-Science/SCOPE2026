# Independent mathematical audit

## correctness

PASS

The two depth-one coordinate saturations intersect in the four cells with both coordinates in {0,1}; subtracting the marked L leaves (1,1) alone. Its saturations and the differences from the original ones give X_0,X_1,Y_0,Y_1 at depth two. From both sets of selectors through index L, intersect X_a and Y_b, saturate in the named sum direction, intersect with Y_0 or X_0, and saturate again, giving both selectors for a+b through min(2L,n-1) at depth increased by two. This yields the claimed logarithmic depth, with no claim of optimality, and intersecting selectors defines every cell. For a one- or two-cell support the map z -> c-z with c respectively 2u or u+v preserves the valuation and the three named equivalences; it is nonidentity for n>=3 because negation is not identity on the cyclic group (if the affine map were identity, evaluation at zero forces c=0). The empty valuation admits translations. Since every formula is invariant under these automorphisms, no such sparse valuation can define all singletons. For n=2 the two coordinate saturations of a singleton and their complements suffice; for n=1 the constants suffice. For the two-mode contrast, fewer than n-1 marks leave two empty rows whose transposition preserves the remaining relations and the valuation.

## originality

PASS

The distinct supported claim is the sharp one-proposition support and explicit depth bound using exactly three named relations at every cyclic order, including composite orders. The reflection method and cyclic-net generation with already individually identified points are not novel. The record combines recovery of individual point names from a single valuation with uniform bounded-depth generation in the restricted signature. No inspected result gives that combination or an implication of it; this is not a historical priority determination.

## value

PASS

The exact size of a sparse unary valuation that makes every cell definable is a natural finite-frame invariant. A third named S5 modality changes a provably growing requirement to a constant for arbitrarily large cyclic nets. The constructive logarithmic formula depth gives quantitative control in ordinary modal logic and is not just a small-instance orbit calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
