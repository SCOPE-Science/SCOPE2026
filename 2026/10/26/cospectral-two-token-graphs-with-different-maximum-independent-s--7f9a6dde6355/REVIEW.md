# Independent mathematical audit

## correctness

PASS

In the auxiliary graph of selected unordered pairs, token conflicts are exactly two incident auxiliary edges whose other endpoints are adjacent in the base graph. Hence each auxiliary neighborhood is a base coclique. Both bases have cocliques of size four and none of size five, so degree sum bounds the size by 32; equality requires four neighbors at every vertex and the reciprocity of those neighbor choices. Independently reimplemented the exhaustive census in /workspace/audit_replay/token_census.py: assign the rows in fixed vertex order, with each new row indexed by the lower-bit pattern prescribed by all previous rows. This bijectively enumerates every reciprocal assignment, with no assumption about its type. The script verifies the quotient by identical open neighborhoods has respectively four size-four classes inducing two disjoint edges, or eight size-two classes inducing a single cycle; checked complete joins across quotient edges and absence of intra-class edges. Independently enumerated the entire base automorphism group by extending injective partial vertex maps preserving both adjacency and nonadjacency. Replay with python3 returned 24/16 base four-cocliques, 144/54 order-32 solutions, base group orders 1152/192, type counts (72,72)/(30,24) in the stated order, and precisely the claimed typed orbit sizes. This checks the full base actions, not any assertion about the token graphs' own full groups. The inspected frozen verifier's different CSP ordering is consistent. Cospectrality itself follows from the cited strongly regular symmetric-square theorem under exactly this unordered-pair definition.

## originality

PASS

The supported distinct result is the exact extremal-set census, with structural types and base-group orbits, on the specified known cospectral pair. Cospectrality and base coclique data are prior; even if a less accessible source turns out to give the independence numbers, that alone does not cover the census or structure.

## value

PASS

The canonical equal-parameter, cospectral pair motivates the exact comparison before computation. The same maximum size but different leading independence coefficients gives a concrete separation on symmetric squares, and the two auxiliary-graph types with full base-action refinements make the result useful beyond the raw coefficients for anyone studying the extremal configurations. The enumeration is complete for the specified natural pair and is not extrapolated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
