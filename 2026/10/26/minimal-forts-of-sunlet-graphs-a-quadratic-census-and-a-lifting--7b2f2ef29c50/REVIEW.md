# Independent mathematical audit

## correctness

PASS

For a fort, each rim vertex in X forces its attached leaf; each outside rim with exactly one rim-neighbor in X forces its leaf; with two rim-neighbors, an optional selected leaf can be removed, so no minimal fort contains it. This yields canonical B(X) for every nonempty X. A proper subfort B(Y) contained in B(X) exists precisely if membership of Y is equal at the two selected neighbors of each missing intermediate rim index; equivalently Y is a union of connected components of the graph H_X on X. Thus minimal forts are exactly those whose H_X is connected. With n even, H_X edges preserve parity and connected supports are cyclic intervals of a parity class; with n odd, step-two order is a single n-cycle, and supported intervals have length <=(n+1)/2, giving the parity formulas. Independently enumerated all 2^(2n)-1 nonempty subsets of actual cycle-corona graphs for n=3..8, tested the original outside-neighbor predicate, inclusion minimality by subforts, obtaining M_n=(6,6,15,14,28,26). Independently checked the exact n=6 counterexample X={0,1,3,4} is minimal in C6; its standard lift contains strict fort B({1,3})={v1,v3,w0,w1,w3,w4}. This refutes the v1 statement, not any uninspected later revision.

## originality

PASS

Becker–Cameron–Hanely–Ong–Previte arxiv:2404.05963v1 already defines and counts forts for paths/cycles, but their claimed Proposition23 minimal-fort lift and Corollary24 exponential sunlet lower bound are contradicted by the explicit small witness and the proven quadratic census. Original full Section5.2 was inspected. A revised later version may differ and its publication status is an explicit risk; no identical prior complete sunlet classification found.

## value

PASS

Minimal forts are the natural primitive obstructions for zero forcing. The sunlet is a canonical corona/cycle family, and the unexpectedly quadratic rather than exponential minimal-fort census gives a complete classification rather than a toy example. The six-cycle counterexample explains precisely why a natural general lifting argument fails and prevents propagation of an incorrect lower bound. An exact count plus structural correspondence are separately useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
