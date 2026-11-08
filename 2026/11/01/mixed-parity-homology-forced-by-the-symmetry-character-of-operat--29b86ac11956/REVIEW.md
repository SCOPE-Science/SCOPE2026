# Independent mathematical audit

## correctness

PASS

The Petersen graph is KG(5,2), so its automorphism group S5 acts on ten vertices; target color S4 acts on product-of-simplex Hom(P,K4). Every cell is a ten-tuple of nonempty color sets with disjointness at graph edges. The source standalone verifier recursively enumerates 12960 proper colorings, then expands allowed color sets to the entire 221520-cell polyhedral Hom complex with dimension vector (12960,53280,80400,54960,17400,2400,120); a one-color-recoloring BFS proves connectedness. An element (sigma,tau) acts on each fixed source-coordinate cycle of length ell by Koszul permutations of simplex factors and internal color permutation; after Euler sign the contribution is (-1)^(|A|-1)sgn(tau^ell|A). Inspecting the exact exhaustive 35-class trace algorithm and independently reprojecting its published 7x5 integer trace table against class sizes and S5 Specht character chi_(3,2)=C(f,2)+t-f yields +1 on S^(3,2) box trivial and -1 on its conjugate S^(2,2,1) box sign4. Rational semisimplicity and Hopf trace imply occurrence in at least one positive even and one positive odd degree, respectively. This virtual result deliberately does not identify individual graded Betti numbers or integral torsion.

## originality

PASS

Best-of-knowledge statement/implication comparison for this exact mathematical object, not novelty from titles or failed search. Closest sources and any inaccessible material are explicitly compared below; no assertion of exhaustive global priority.

## value

PASS

An explicit complete source/target symmetric-group virtual character of a central graph-coloring Hom complex identifies an unusual mixed-parity obstruction invisible from connectivity bounds and ungraded Euler characteristic. It determines nontrivial representation-specific positive-degree homology existence without pretending to give a full homology classification, making the precise fact a useful equivariant test case rather than an arbitrary tiny coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
