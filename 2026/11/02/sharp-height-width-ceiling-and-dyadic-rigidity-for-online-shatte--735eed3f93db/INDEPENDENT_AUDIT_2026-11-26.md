# Independent mathematical audit

## correctness

PASS

A static shattered set must be an antichain (accepting its upper element while rejecting a comparable lower one is impossible); down-closures realize every labeling of an antichain. For online shattering, a chain of length l has l+1 possible prefixes: counting leaves gives the upper rank and balanced membership queries give the matching rank floor(log2(l+1)). On disjoint domains a query can lower the rank of only the queried factor, and one nonempty branch must strictly lower it for any query that splits; induction gives the additive upper bound and concatenating trees gives equality. Dilworth's w chains therefore bound the rank by the sum of the separate floors, attained by w disjoint h-chains. At h+1=2^r, 2^(rw) distinct leaves saturate both the product count of ideals and the bound on each factor length. Every prefix tuple must be allowed, which rules out even one cross-chain comparison. This includes h=1; h=2 has rank w, and h=3 is the first possible gap.

## originality

PASS

The supported distinct claim is the exact width–height extremum with the integer logarithm taken separately for each chain, and the equality characterization at dyadic h+1. Antichain VC shattering, threshold search, Dilworth, disjoint-domain rank additivity and the counting argument are not priority claims. The closest retrieved catalogue results concern a special rooted family or exact rank computation and grid examples; neither comparison showed equivalent structural coverage.

## value

PASS

Height and width are intrinsic poset parameters, and the sharp bound pinpoints when adaptivity can first outperform static shattering. The per-chain floor makes a quantitative difference from counting concepts, already at height two. The dyadic equality statement determines the order structure from extremal online performance rather than just giving an example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
