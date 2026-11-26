# Independent mathematical audit

## correctness

PASS

I independently enumerated the factors in order of their distinct partner of vertex 0, assigning a disjoint matching on the remaining six vertices at each step. This visits every unordered factorization exactly once. I generated neighbors by enumerating all three four-cycles on every four-element vertex subset, looking up the owners of opposite edge pairs, exchanging alternating edge ownership, and reanchoring; duplicate outcomes were collapsed. The resulting simple graph has 6240 vertices, 17640 edges and degree/count pairs (0,960), (3,1680), (7,2520), (9,420), (13,630), (21,30). Orbit traversal using adjacent transpositions reached the whole respective degree class from each of six representatives. The five positive-degree representative BFSs each reached 5280 states, with eccentricities 11,10,10,10,9 in that order. The affine representative was used for degree 21. Analytically, two factors have union 4+4 exactly when the matching involutions commute (their product has order 2 rather than 4); commuting factors generate a faithful transitive elementary abelian group and thus a regular group of order 8. The converse and normalizer count give the 30-state affine orbit. An isolated factorization has no 4+4 union and hence every pair is Hamiltonian. This verifies the original componentwise census, not a graph with persistent factor colors or longer switches.

## originality

PASS

The supported distinct contribution is the metric and connectivity census for fixed labels, including the complete affine center, not the classical number of states, the definition of the move, or the isomorphism-class switch graph. Focused indexed and literature lookups did not identify a competing fixed-label metric result.

## value

PASS

K8 is a natural finite case of the established intercalate switch problem. The fixed-label metric supplies a sharp move bound for any two mobile factorizations and identifies a canonical isomorphism orbit of best starting states. This answers a genuinely different reconfiguration question than orbit-quotient connectivity or a count of labelled designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
