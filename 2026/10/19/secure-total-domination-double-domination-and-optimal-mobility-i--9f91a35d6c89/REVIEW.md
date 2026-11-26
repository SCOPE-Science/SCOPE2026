# Independent mathematical audit

## correctness

PASS

Read the frozen RESULT.md, VERIFICATION.md, both enumerators and the recorded C++ output, and compared the JSON certificate to an independently implemented exhaustive replay. In the replay, once total domination holds, removing v can leave uncovered only vertices whose open neighborhood meets the set exactly in v. Inserting u repairs the move exactly when all those vertices are in N(u); test this for an adjacent selected v for every outside u. Double domination was tested separately by the open-neighbor bound 2 minus the indicator of selection. All 8,192 and 131,072 subsets were visited: there were zero disagreements, and both full polynomials, zero lower coefficients, minima, and all named affine orbits matched. Comparing each pair of optimum subsets by intersection size 4 independently reconstructs the jump edges; testing adjacency of the differing vertices gives the slides. The replay matches all edge lists, components, degree and distance histograms in the certificate. P13 has one 195-state component for each rule, 936 jump edges and 663 slide edges, with eccentricity 5 at every state. P17 has 68 components of size two for both rules; the named representative has the unique claimed neighbor and that exchange slides. The general forward implication follows from total domination on selected vertices and the impossibility of defending an outside vertex with only one selected neighbor. The stated C6 example also checks: vertex 2 cannot be defended by 1 (vertex 0 would be uncovered) or 3 (vertex 4 would be uncovered). Replay: run python3 /workspace/branches/independent_replay.py 4 with /workspace/source/2026/10/19/secure-total-domination-double-domination-and-optimal-mobility-i--9f91a35d6c89/verification/certificate.json as the last argument. These are exact finite assertions for the two orders, not a general Paley equivalence.

## originality

PASS

The known general implication is secure-total to double domination. The distinct supported findings are the reverse inclusion for all subsets at these two orders and the precise contrasting mobility of their common optima. The inspected near-matches use different domination predicates or graph families, not alternate names for this configuration space.

## value

PASS

These are the first two prime Paley orders after the cycle P5, a natural comparison rather than arbitrary graphs of the same size. Equality of all configurations is stronger than a numerical domination-number coincidence, and the shared optimum cardinality sharply fails to predict mobility: one order has connected state space even for slides, the other stays split into single edges even with arbitrary jumps. The exact polynomials, orbits and exchange geometry are usable finite benchmarks; no infinite-order extrapolation is needed for that value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
