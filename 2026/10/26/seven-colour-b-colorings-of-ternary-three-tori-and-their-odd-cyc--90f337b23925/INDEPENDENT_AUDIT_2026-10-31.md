# Independent mathematical audit

## correctness

PASS

Each graph has 27abc odd vertices, degree 6, so six matchings cannot color 3N edges: lower bound 7. The 81-edge ternary three-torus seed is explicitly specified in the actual certificate.json table. Independently constructed graph adjacency, 81 unique undirected edges, all 27 vertex incidence lists and all 81 simple 4-cycles, verifying six distinct incident colors and four distinct edge colors per 4-cycle; seven colors occur with multiplicities (11,11,12,12,11,12,12). Reduction modulo 3 from any odd-multiple-of-three cycle is a locally bijective covering onto C3. Every larger graph 4-cycle uses two directions and descends to a seed 4-cycle, so pullback certifies infinite family. Finite certificate alone would not establish the general theorem; parity plus graph covering does.

## originality

PASS

Gyárfás–Sárközy (2023) Theorem 1.8 explicitly leaves this 27-vertex instance at 7≤q_B≤8. Their congruence-seven family is not a congruence-three seed. Jiang–Li 2026 provide 2D grid exact classification and a known period-lift lemma; that lift is acknowledged, but its application to a previously unavailable seven-color 3D seed resolves the open case and infinite specified odd cycle family. Best-of-knowledge qualified by possible unindexed subsequent certificate.

## value

PASS

Closing the published exact 7-vs-8 gap for a natural minimal odd three-torus and resolving an infinite period-three family of the established B-coloring conjecture is a substantive finite-certificate theorem. The seed certificate is essential and not a mechanical derivative of the earlier period-lift lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
