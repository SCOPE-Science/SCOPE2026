# Independent mathematical audit

## correctness

PASS

For any ambient line L pick x∈L outside a nontrivial blocker B. The four other lines through x require four distinct points off L, so |L∩B|≤|B|−4. Four points cannot cover the 21 lines; for k=5 or 6, intersections have size at most 2, so counting incidences and pairs would require 5k−21=binom(k,2), which fails. At k=7 let n_j be the 1-, 2-, 3-secant counts. Then n₂+2n₃=14 and n₂+3n₃=21, so n₂=0 and the seven triples form the Fano plane: each pair determines a triple and each triple meets all six others via its three points. Conversely, a Fano subplane meets seven ambient lines in triples and fourteen in single points (two tangents per point), so blocks all 21 and contains no line. Every embedded Fano plane is a projective image of the standard one: choose a quadrangle as frame; the three diagonal points complete it uniquely. An independent orbit replay on the 21 projective points used all elementary transvections and one coordinate scaling, then a single-source layer expansion on the 360-element transitive orbit. The distinct intersection maximum is 4, and the successive distance layers by intersection size are {4:56}, {1:42,2:168,3:77}, {0:16}. This establishes the exchange threshold, distance formula, radius and diameter 3, edge count 10080 and antipodal pair count 2880. It does not rely on identifying exact sets by hash alone.

## originality

PASS

Credit only the complete three-exchange metric on this configuration space, particularly the characterization of all disjoint pairs as antipodes. The object classification, intersection census, exchange adjacency, and its valency follow from prior geometric data and are not independently novel.

## value

PASS

The graph is the first legal simultaneous-move graph on classical minimum blockers, not an arbitrarily chosen size slice. Its distance formula tells whether a pair can be connected in the minimum number of valid moves from the overlap alone and identifies all worst-case pairs as exactly the geometrically disjoint ones. This is useful exact information beyond the known census; value is not assigned to recomputing that census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
