# Independent mathematical audit

## correctness

PASS

For each of all 4096 vertex masks, the induced largest connected component is determined from the 18 explicitly supplied graph edges; Ind_r is exactly the downward-closed set of masks with size<=r components, and r>=12 gives a full simplex. The downloaded, parsed 194507-byte actual certificate provides all twelve face sets, 16345 matching pairs, critical cells and signed integral Morse matrices. Independently reimplemented BFS connectivity, complete mod-two simplicial boundary ranks and integral discrete-Morse greedy matchings in /mnt/data/scope05_tietze_independent.py and /mnt/data/scope05_morse_independent.py. Reproduced all 12 face/Betti signatures, complete Hasse acyclicity, and the only nonzero integral critical-cell differentials for r3,4,5,6 with ranks 4,2,4,7 and determinant-one maximal-rank minors, respectively; other stages have one critical vertex and concentrated higher cells. Forman acyclic matching gives an integral CW model. Since positive critical cells occur in dimensions >=2 and, at mixed stages, only adjacent dimensions occur, maps into the wedge of lower-dimensional spheres are classified by integral degrees; unit Smith factors split contractible pairs and leave the stated spheres. This is stronger than mod-two homology alone and is a complete finite certificate for the finite Tietze graph, not an extrapolation to a graph family.

## originality

PASS

Best-of-knowledge comparison of exact statements and implications: Checked higher-independence/dissociation/multiscale graph complex aliases and the exact Tietze signature. Known Petersen r=2 and ordinary independence computations are of different graphs; absent a proven vertex-to-triangle homotopy transfer they do not logically determine this classification. A family theorem for chordal, cyclic, tree or fully whiskered graphs does not imply the multiplicities of all twelve Ind_r(Tietze). General connectivity lower bounds are much weaker than integral homotopy types. None of the inspected formulas or general connectivity bounds covers the nonchordal Tietze graph and its exact stage-by-stage integral sphere multiplicities. The actual finite Morse certificate is an independent computation; no broader implication identified.

## value

PASS

The Tietze graph is a canonical, widely used 12-vertex cubic Petersen expansion and higher-independence is a standard natural invariant parameterized by component cutoff. This is its complete ordinary integral homotopy sequence; the nontrivial mixed-dimensional r5 stage and rank-193 r7 wedge supply meaningful exact information beyond routine full-simplex endpoint. A researcher comparing graph-complex topology across cubic graph families could need these precise integer homotopy types even without a new general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
