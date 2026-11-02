# Independent mathematical audit

## correctness

PASS

D=GP(10,3) has 20 vertices, 30 edges and 60 perfect matchings; deleting one matching yields 36 complementary (10,10) 2-factors and 24 Hamiltonian 20-cycles, so quotient states (36×2+24)/3=32. An independently written exhaustive perfect-matching recursion produced all 60, and a distinct direct edge-color backtracker fixing global S3 at a vertex produced exactly 32 colorings; both methods gave the same 32 states. Exhaustive switching of each bichromatic connected cycle generated 36 undirected Kempe moves, one component on 20 states of degree three and six isolated edges, with exactly 20 profiles of three (10,10) unions and 12 profiles of one (10,10) plus two Hamiltonian unions. Independent NetworkX graph isomorphism and full distance computation identified the twenty-state component with the original D, distance profile (1,3,6,6,3,1). The actual certificate.json and the two source exhaustive verifier scripts were inspected; finite exhaustive certificate, unlike finite sampling, covers the complete specified quotient space.

## originality

PASS

Earlier edge-Kempe results count classes and analyze several graph families, while recent computer tables potentially already imply 7 component counts for cubic graphs of order twenty. The assessed exact 32-state reconfiguration adjacency graph and surprising large component D-isomorphism are strictly finer than a count of equivalence classes. Search did not find a statement of D⊔6K₂ or an explicit isomorphism; unindexed older full datasets may already encode it.

## value

PASS

The Desargues graph is a canonical highly symmetric 20-vertex cubic bipartite graph. A complete exact reconfiguration graph including explicit self-isomorphic component, distance distribution, and bichromatic signatures is a motivated finite invariant for coloring/Kempe dynamics; not a gratuitous one-number census. No infinite-family generalization is required for this natural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
