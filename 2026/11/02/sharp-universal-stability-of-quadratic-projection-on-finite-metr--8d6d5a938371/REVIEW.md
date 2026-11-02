# Self-review

## Correctness — PASS

The exact quadratic nodal/bubble Gram block is \(H=(3D-A)/24\), with strictly positive inverse, and its row normalization is \(\sum_vd_va_v=12\). Each endpoint shape function has absolute integral \(79/300\), yielding vertex sensitivity strictly less than \(79/25\). The interior evaluation envelope is strictly below this value. For unit hypercubes, the weighted Hamming-shell sum \(\sum r(v)a_v\le6/d\) forces the norm within \(158/(25d)\) of the ceiling. Since the projection fixes constants, the negative-kernel-part identity gives sharp universal positivity loss \(\frac{27}{25}\). The standalone exact rational verifier reports 8,528 assertions, including independently built quadratic Gram/kernel systems, and does not replace the proof for infinitely many graphs.

## Originality — PASS, qualified

The nearest relevant literature comprises the finite-element stability estimates of Crouzeix–Thomée and Grigorieff–Sloan (interval or mesh settings), Oswald's instability theorem for linear finite elements on two-dimensional triangulations, Post's metric-graph spectral theory, and Arioli–Benzi's linear metric-graph finite elements. The inspected primary statements do not imply the present all-topologies, arbitrary-positive-edge-weight **quadratic** constant or its hypercube sharpness. An indexed exact positivity-defect result for affine projection on a simplex does not cover degree-two metric-graph splines. A previous exact quadratic two-element interval calculation is a fixed-path case and does not imply a universal sharp graph bound. Related prior exact calculations on quadratic stars and complete graphs (and affine windmill graphs) do not establish a universal theorem. Originality is relative to available indexed literature and recoverable earlier claims; the uninspected original 1987 full text and possible unindexed results remain publication-priority risks.

## Mathematical value — PASS

The invariant is a dimension-free global stability constant for a natural approximation space. The exact ceiling and proof of universal optimality show why quadratic spline approximation remains uniformly stable under arbitrary graph branching and edgewise mass variation, even though comparable higher-dimensional simplicial mesh problems can be unstable. Hypercubes provide a motivated extremal sequence with no pendant vertices, while the positivity-loss formula gives an independent concrete interpretation of the constant. The result is not merely a special-graph numerical extension.

## Scope and limitations

The theorem assumes finite connected simple graphs, constant positive density on each edge, and continuous edgewise degree-at-most-two functions without vertex derivative matching. It neither gives fixed-hypercube exact norms nor extends to higher-degree or derivative-matched splines or varying within-edge density. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
