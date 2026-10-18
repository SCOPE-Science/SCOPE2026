# Independent mathematical audit

## correctness

PASS

PASS: For independent sets in C7 strong square, every row is one of 29 independent C7 masks and successive cyclic layers are compatible iff their selected second-coordinate residues have cyclic distance >=2. An independently implemented 7-layer integer-polynomial DP has degree 10 and leading coefficient 980. Three displayed 10-point representatives were independently checked pairwise nonconfusable; their full orbits under all 392 maps (x,y)->(s_x x+a,s_y y+b) and coordinate swap have sizes 392,392,196. The three orbits are disjoint, so their 980 members exhaust ALL maximum sets by the separately counted leading coefficient; stabilizers 1,1,2. Fingerprints independently recomputed as (0,2),(1,1),(1,2), with the coordinate multiplicity profile from the complete orbit union. This establishes the finite orbit classification without relying on the package verifier's exit code. No claim is made that the natural group is the entire graph automorphism group, nor concerning higher strong powers.

## originality

PASS

PASS best-of-knowledge: existing strongest directly relevant 2026 primary paper gives α(C7 strong square)=10 and 980 maximum sets, and its dihedral five-orbit result concerns 29 SINGLE-LAYER independent C7 states, not maximum independent sets of the 49-vertex square. The audited 392/392/196 orbits, stabilizers, and distinguishing pair-distance invariants do not follow from the scalar leading coefficient without an equality-case analysis. Searches across aliases and Resultary found no earlier exact full-code orbit classification. Older obscure code catalogues remain a residual risk.

## value

PASS

PASS: The explicit natural channel symmetry group and its action on the complete set of maximum two-use zero-error codes are motivated equality-structure invariants. The result separates three inequivalent optimal designs even though all have the same size and row/column multiplicity profile, so it supplies a useful classification not implied by the known total count. It is finite but complete and naturally chosen (C7 strong square is a classical Shannon-capacity benchmark).

The dated certificate retains the supplied scientific assessment, sources and limitations.
