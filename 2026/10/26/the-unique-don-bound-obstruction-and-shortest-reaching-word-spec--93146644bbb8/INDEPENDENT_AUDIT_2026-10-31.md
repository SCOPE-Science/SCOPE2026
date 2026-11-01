# Independent mathematical audit

## correctness

PASS

After the published cyclic-letter theorem normalizes a to the 8-cycle, full reachability forces other letter b to rank seven. Collision-pair/excluded-image/duplicated-image/bijection parametrization exhausts C(8,2)*8*7*6!=1,128,960 maps. Full-mask BFS on the 255 nonempty subsets calculates exact shortest-image distances; shortest-path dynamic programming along both labeled letter edges counts distinct words, not transformations. I implemented and ran independent C++ enumeration, independent of the repository source, obtaining 1,093,632 reachable maps, 544 violations, none at sizes other than six or lengths other than 17, precisely one exceptional antipodal-complement subset for each, target masks 119,187,221,238 (136 each), and multiplicity histogram 384/96/32/32. The repository contains reach_census.cpp and separately enumerating independent_waves.cpp; both were inspected with their bounded methodology. The cyclic-orbit quotient gives 68 equal eight-element orbits; no infinite-state claim is made.

## originality

PASS

Zhu 2024 already proves eight-state counterexamples and tabulates 68 isomorphism classes, and the existence of the cyclic normalization is prior theory. Full primary reading of Zhu Section 4 and Table 1 did not identify uniqueness per automaton or the four-way shortest-word multiplicity census. The independently reproduced census supplies novel conditional invariants, subject to possible older ancillary enumeration.

## value

PASS

A complete exact conditional shortest-path distribution is an intrinsic reconfiguration invariant of the canonical minimal counterexample class. Uniqueness of the offending subset and the optimal-word multiplicity spectrum go beyond the known mere existence and class total; a complete well-motivated eight-state obstruction classification has durable use as a benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
