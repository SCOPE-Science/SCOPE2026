# Independent mathematical audit

## correctness

PASS

A factorization is counted once under either first-uncovered-edge descent or anchoring each factor to the unique opponent of vertex 0; neither identifies vertex labels. In a pair of factors the union consists of even cycles of length at least four, so the only possibilities are an 8-cycle and two 4-cycles. Only the latter permits a changed unordered factorization. Choosing the other 4-cycle just interchanges the names of the two resulting factors. A separately written full census generated all 105 matchings, enumerated all disjoint anchored covers, tested all 21 factor pairs per cover by connected components, and deduplicated the constructed neighbor sets. Component traversal plus BFS from all 5280 nonisolated states independently reproduced 6240 vertices, 17640 edges, degree counts 0:960, 3:1680, 7:2520, 9:420, 13:630, 21:30, component sizes 1:960 and 5280:1, and nontrivial eccentricities 9:30, 10:3570, 11:1680. The degree-zero characterization follows exactly from having only Hamiltonian two-factor unions. The frozen verifier code, saved outputs and summary were inspected without executing the uploaded scripts. The frozen replay entry points are verify_matchings.py (exact covers) and verify_coloring.py (anchored covers); the independent implementation also uses the anchoring principle but constructs switches from cycle components.

## originality

PASS

Credit is limited to the exact fixed-vertex-label graph statistics: its edges and degree census, connectivity of the non-perfect states, and their full distance geometry. The factor-switch move, quotient graph, perfect-factorization isolation and 6240 labeled state count are known. The closest primary prior computes the quotient under vertex relabeling; the information in its reported quotient and loops is insufficient to recover the connectivity or distances of the labeled state graph. No inspected indexed result gives a dominating unquotiented census.

## value

PASS

The graph is the natural smallest complete one-factorization setting with a nontrivial labeled component and perfect isolated states of this kind; K8 permits both types of two-factor union, unlike the smaller K4 and K6 cases where every two-factor union is one cycle. The meaningful invariant is the fixed-participant edit geometry, not a repeated count of states or isomorphism classes. In the active component, exact connectivity decides mutual convertibility without team renaming and diameter 11 gives the sharp worst-case number of legal round edits; eccentricities give the worst-case guarantee by starting schedule. Those precise invariants are useful independently of any extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
