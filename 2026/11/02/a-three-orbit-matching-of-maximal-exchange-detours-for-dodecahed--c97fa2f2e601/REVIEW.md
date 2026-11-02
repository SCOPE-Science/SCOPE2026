# Scientific review

## Correctness
**PASS.** The graph is specified by an explicit edge list, and a cardinality lower bound follows from the cubic edge count. Two independent standard-library programs exhaust the complete finite collection of optimum feedback vertex sets and all unordered configuration pairs. They confirm each distance-table entry and the exceptional matching. The direct program also closes the 120-element automorphism group from checked generators and verifies the three 60-pair orbits and per-edge multiplicities. No finite sample is treated as evidence for an infinite-family statement.

## Originality
**PASS, qualified.** The 2016 induced-forest literature proves size bounds and a dodecahedron characterization. The relevant 2023 general reconfiguration paper establishes connectivity and a path-length upper bound in subcubic planar graphs. Earlier exact totals for this same finite configuration graph—2520 optimum sets, 23940 exchange edges, and diameter 6—are acknowledged and excluded. The claim instead concerns the exact exchange-excess spectrum, 180 disjoint maximal-detour pairs, per-edge localization, and three symmetry orbits. Searches for equivalent descriptions, stronger results, database tables, and historical parameter aliases did not identify a covering theorem. Full text of the closest 2023 article was inaccessible, and equivalence with older work remains a residual risk; no novelty guarantee is asserted.

## Value
**PASS.** The exception set pinpoints a structural obstruction to attaining the Johnson exchange lower bound within an optimal-feasible state space. The fact that maximum-excess pairs are uniquely partnered, distributed uniformly across original graph edges, and separated into three symmetry orbits is meaningful local geometry beyond a diameter calculation. A named planar cubic graph with 2520 optimum configurations gives a reproducible finite benchmark for shortest feedback-set reconfiguration.

## Evidence and limitations
The complete reproducible certificate consists of `verify_direct.py` and `verify_independent.py`, both executed from this final package. The result concerns the dodecahedral graph only. Possible historically equivalent exceptional-pair data and lack of independent external validation remain open limitations. The sources and comparisons are recorded in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
