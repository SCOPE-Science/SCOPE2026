# Independent mathematical audit

## correctness

PASS

Expanded ab as six powers at 0,u,v,w,u+v,u+w. Binary carrying reduces multiset size by one per carry, so weight four needs exactly two merges. The initial equalities are precisely u=v, u=w, w=u+v. Reconstructed the exhaustive three-case proof, checking all subsequent collisions, including exceptional weight 2/3 triples (1,1,2),(1,1,3),(2,1,2),(2,2,3). Wrote an independent exhaustive verification over 252,800 exponent triples with 1≤u≤80 and 1≤v<w≤80 using Python integer bit_count; every predicted membership agreed with actual s₂(ab), with 349 weight-four triples and four low-weight exceptions. This finite test corroborates, but only the complete symbolic coincidence/carry case analysis proves the unbounded infinite families.

## originality

PASS

Kaneko–Stoll established bounded-minimum conclusions for output weight four when both factor weights are ≥3, a hypothesis violated by weight-two a; thus their bound does not imply or contradict these unbounded families. Their broader methods do not present five specific (2,3,4) families in the inspected complete relevant sections. The published (3,2,3) result for the same factors exhausts target weight three, not four. There was no discovered equivalent complete target-four classification, subject to unindexed literature.

## value

PASS

This is the natural first factor-weight boundary where the established minimum-factor bound ceases to hold. The explicit five families, no-sporadic completeness and simultaneous unboundedness provide a motivated qualitative sharpness result, not a cosmetic reparameterization of the weight-three finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
