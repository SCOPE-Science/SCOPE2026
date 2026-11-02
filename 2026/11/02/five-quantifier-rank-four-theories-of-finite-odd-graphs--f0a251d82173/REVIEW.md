# Scientific review: five rank-four theories of odd graphs

## Correctness — PASS
The proof reduces four-move logical equivalence to extension types of ordered triples and ordered pairs. For \(k\ge3\) it proves universal availability of the zero-edge and single-edge fourth-point patterns, identifies the unique common neighbor of a near-complete pair, and treats the top/star distinction and equality exclusions. The exact integral feasibility criterion \(|v-w|\le k-u\) and \(k-u-1\le v+w\le k+u\) gives five constant pair-profile matrices for every \(k\ge5\). Small-parameter profiles distinguish the five regimes. The direct finite graph checker and the independent orbit enumerator agree for \(k=1,\ldots,6\); finite checks support but do not replace the infinite inequalities.

## Originality — PASS, with historical-priority qualification
The inspected Pikhurko–Verbitsky survey develops graph logical complexity and Ehrenfeucht games but does not classify these odd graphs. The inspected van Dam–Haemers treatment establishes a spectral and odd-girth characterization of generalized odd graphs, not any quantifier-rank-four partition. No equivalent or stronger statement was found in targeted public searches. A more general rank-four stabilization for fixed subset size in sufficiently large ground sets cannot imply the present result, because the subset size here increases with the ground set and \(2k+1<4k\) for \(k>1\). An equivalent consequence buried in the distance-regular literature, or the full text of Biggs (1979), remains a genuine priority risk.

## Value — PASS
The result gives a natural complete logical classification of an infinite distance-regular graph family, identifies the sharp rank-four stabilization point, and gives an optimal \(462\)-vertex representative bound. It also shows that unbounded odd girth can coexist with a constant four-round theory. The exact parameter threshold and proof through common-neighbor/top–star geometry are not mere relabelings of previous fixed-uniformity thresholds.

## Evidence and limitations
The separate `verify_odd_graphs.py` and `verification_output.txt` provide reproducible finite checks. The infinite claim is mathematical; the finite checks cover only their stated ranges. The language is pure graph adjacency with equality, and the result is restricted to rank four. Historical novelty and mathematical correctness have not been independently audited.

Self-review: passed. Independent audit: not yet performed.
