# Scientific review: the Clebsch zero-forcing exchange graph

## Correctness — PASS
The finite theorem is fully quantified on a particular sixteen-vertex graph. Its configurations and moves are exhaustively enumerated. Independently implemented antipodal-folded-cube sequential forcing and Cayley-graph simultaneous forcing both produce the same \(3{,}872\) configurations, \(64{,}720\) exchange edges, and exact all-pair metric; the former uses a full \(3{,}872\)-source BFS and the latter seven symmetry representatives. Exhaustive eight-subset enumeration and an independent automorphism orbit produce precisely the same labelled \(240\) exceptional pairs. The C++ and Python certificate sources and execution commands are embedded; each loop has an explicitly complete finite domain. The minimum-set census and orbit sizes were previously established and are used as inputs, not asserted as new.

## Originality — PASS, qualified
A prior Clebsch minimum-zero-forcing census already establishes the zero-forcing number, its \(3{,}872\) minimum configurations, and seven symmetry orbits. These overlap completely and are deliberately excluded from the new claim. The foundational 2008 zero-forcing paper and 2018 zero-forcing polynomial framework do not provide the transition metric. The materially inspected 2020 primary paper on zero-forcing-set reconfiguration develops the graph and studies other graph classes but does not determine Clebsch shortest-path geometry. Targeted public-record and mathematical research-record comparisons did not identify an exact metric/exceptional-pair equivalence. A historical calculation in unindexed sources remains possible; the 2008 paper was accessible only through bibliographic and abstract material.

## Value — PASS
The minimum solution set is a canonical configuration space. The result determines all reconfiguration distances, exactly quantifies the failure of ambient Johnson geodesics, and gives a structural bijection between the \(240\) exceptional pairs and three opposite-path splittings of each of \(80\) induced six-cycles with two isolated vertices. This is a nontrivial exact structural invariant, not merely the already known counting polynomial or a small numerical increment. It provides a benchmark and geometric obstruction description for geodesic algorithms.

## Remaining limitations
The finite theorem does not generalize to arbitrary folded hypercubes. Historical priority and independent scholarly verification remain open. The two independent implementations both depend on the same precise graph/move definitions, which are explicitly documented.

Self-review: passed. Independent audit: not yet performed.
