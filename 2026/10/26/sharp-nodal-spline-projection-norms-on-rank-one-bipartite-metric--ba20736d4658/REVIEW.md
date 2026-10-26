# Self-review

## Correctness — PASS
The matrix entries follow from exact nodal-hat integration on every metric edge. Direct block multiplication verifies the inverse, after which a single exact absolute-affine integral gives the displayed sharp vertex norms. The affine-output maximum principle and symmetry of the kernel establish both endpoint norms. The optimizer descriptions and the nonnegative-input excursion follow from a strictly decreasing one-variable formula and from the identity \(P1=1\). Exact-rational replay checked 144 nonuniform/constant factor assignments on graphs with two to five vertices on each color side. The finite calculations are confirmatory, not a proof for arbitrary positive real lengths.

## Originality — PASS within inspected sources
The closest mathematical literature is Grigorieff–Sloan on interval spline-projection stability and Arioli–Benzi on graph finite-element mass matrices. The inspected abstract of the former uses interval grids; the inspected primary text of the latter analyzes assembled mass matrices and conditioning, not the sharp norm/optimizer problem. published-finding corpus searches for aliases, constants, and rank-one complete bipartite metric graphs found no statement covering the theorem; related published simplex and bipartite transportation results concern different underlying spaces. This is not an exhaustive historical-priority certificate.

## Value — PASS
The statement supplies a sharp induced-norm and positivity-defect characterization for a natural nodal smoothing operator on a network with cycles, plus all minimizing positive metric designs. In particular, only the least normalized length factor controls worst-case amplification, and equal-size versus unequal-size bipartitions have qualitatively different optimizer sets. These are useful structure and sharp instability data, beyond a generic finite-element condition-number bound.

## Closest literature and limitations
- Grigorieff–Sloan, DOI 10.1017/S0004972700032263: its publisher and explanatory abstracts were inspected; the full work was inaccessible, so historical coverage cannot be completely ruled out.
- Arioli–Benzi, Emory Technical Report TR-2015-009: Section 5 matrix analysis and the available primary text were examined.
- Closest published-finding corpus abstract: `2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34`; it treats a single simplex, not a cyclic metric graph.
- The proof assumes exactly factorized positive edge lengths and no interior edge nodes. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
