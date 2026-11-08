# Independent mathematical audit

## correctness

PASS

The DFS over the directed de Bruijn graph starts with the unique zero edge and visits each unused binary m-gram exactly once in every accepted Eulerian circuit; rooting at its unique zero edge gives each rotation class exactly once, with all windows verified independently. The finite family sizes 1,1,2,16,2048 match the classical de Bruijn formula. Maximal closedness was independently recomputed for all possible substring occurrences using their proper borders and left/right single-character extensions and separately via a suffix-LCP strict-record characterization. Independently authored code traversed all 2048 order-five cycles and reproduced every histogram count; no extrapolation beyond m=5. The weighted sum is 2048*(2957/64) and both extrema have 8 witnesses.

## originality

PASS

Shibata et al. 2026 define and algorithmically enumerate maximal closed substring occurrences; Umezaki et al. study run-length-encoded enumeration; Kosolobov treats asymptotic closed repeats. The accessible full-text reproductions of both algorithm papers were examined by their definitions, principal theorems, methods, examples and targeted exact-word search; they do not give a de Bruijn canonical-cut 2048-cycle histogram. A nearby Resultary published record computes maximum numbers of distinct closed factors among arbitrary binary words of length 25–27; it is a different universe/statistic and does not imply these MCS occurrence counts. This is best-of-knowledge; alternate inaccessible appendices, supplementary benchmark tables, or datasets could still contain a covering enumeration.

## value

PASS

The exact number of maximal closed substring occurrences directly measures output size for a studied enumeration task, and binary de Bruijn cycles are canonical maximally factor-diverse stress cases. The full 2048-word order-five exhaustive cutoff is natural (next order has 67,108,864 rotations), with a nontrivial continuous 40..54 distribution and 35% output variation at fixed input length, not an arbitrary partial experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
