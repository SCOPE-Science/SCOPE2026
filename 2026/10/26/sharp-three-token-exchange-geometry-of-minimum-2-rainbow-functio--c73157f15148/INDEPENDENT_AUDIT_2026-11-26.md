# Independent mathematical audit

## correctness

PASS

I verified by a fresh exact enumerator /workspace/review-evidence/rainbow.py, not by executing either frozen program. The slot set dominates Q5=Q4□K2: an unchosen slot at an occupied Q4 vertex is covered by the twin, and at an empty vertex it must be covered by a horizontal neighbor of its own color. Weight is slot count. An exact depth-at-most-seven search branches on the least uncovered Q5 vertex: every extending solution must choose one of its six closed neighbors, and forbidding earlier siblings' choices makes each path the canonical first-choice path for that solution. Each additional choice can cover at most six more points, justifying the only size prune. This gives no dominating set below seven and 320 of size seven. Bit-coordinate permutations, translations and the global color swap generate the stipulated group; the generated orbits exhaust exactly the overlap-zero and overlap-one classes in sizes 192 and 128. With named colors the token distance is the size of a one-sided difference (half the symmetric difference). Exact pairwise intersection counts agree at distances 3 through 7 (4320,1440,22080,11520,11680), and vanish at distances 1 and 2. The delta=3 edges give the equitable rows (15,12) and (18,9), hence degree 27 and 4320 edges. BFS from one representative of each of the two symmetry orbits has graph-distance shell sizes (1,27,213,79) in both cases; symmetry gives eccentricity three everywhere. This establishes connectivity, radius and diameter. The distance histogram is for token distance, not graph shortest-path distance; all conclusions use endpoints-only feasibility and are specific to Q4.

## originality

PASS

Do not credit the cube equivalence, the minimum weight, or optimal-code classification as new. Pass on the supported distinction of the sharp first nontrivial exchange radius and its full exchange-graph structure, not on the static optimum census. No accessible finding or passage establishes the exchange theorem; two plausible primary sources could not be inspected in full and remain explicit risks.

## value

PASS

For a canonical minimum covering problem, the exact minimum number of simultaneous token changes needed for any move is also sufficient for connecting all optimum states, and three such moves always suffice to go between them. The two displayed equitable rows record how the minimum exchange interacts with double labels. These are useful exact reconfiguration facts, not merely a new tabulation of already classified static optima. They do not describe paths through higher-weight or partially feasible states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
