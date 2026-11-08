# Independent mathematical audit

## correctness

PASS

Each valid placement has exactly one queen per row and column, so is a permutation with pairwise distinct i+p_i and i-p_i. Exhausting all 8!=40320 permutations yields 92 states; pairwise Hamming distances exhaust 4186 unordered pairs. Independently rebuilt both threshold graphs and exact-five graph; all-source BFS returned G4=168 edges, components [84,2,2,2,2], G5=464 edges and pair distances 464,2002,1704,16 and eccentricities 68 at 3,24 at 4; exact-five=296 edges and pair distances 296,1178,1968,720,24 and eccentricities 68 at 4,24 at 5. These are complete finite-state proofs for the defined 8x8 board, not a statement for all n.

## originality

PASS

The 92-state enumeration itself is classical; the assessed claim is the minimal feasibility-preserving simultaneous reconfiguration threshold and full exact graph metrics. The available original queens enumeration and Monte Carlo papers do not imply a feasibility-preserving step graph or these distances, and searches of chess reconfiguration/exchange terminology did not reveal an equivalent table. Unindexed historical reconfiguration work remains a priority risk.

## value

PASS

The classical eight-queens feasible configuration space is a natural finite reconfiguration object, and sharp k-step connectivity, exceptional components, exact shortest paths and an exactly-five restriction answer a meaningful constrained-mobility question. These quantities are not obtained merely by knowing 92 solutions or their dihedral orbit count; the finite census is exact and complete rather than an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
