# Review of the alternating weighted four-cycle distortion formula

## Correctness — PASS
The claim is for every positive real alternating ratio and **real** Banach–Mazur distance. The proof identifies the dual of the free space with a three-coordinate absolute norm, uses averaging over its full sign-change symmetry to reduce *every* Hilbert comparison to a diagonal quadratic form, computes both required extremal norms exactly, and proves the scalar minimax by opposite monotonicities. The two distance-minimizing ratios follow from the stated derivative and reciprocity; t=1 and the endpoint limits are included. Eight exact-rational arithmetic checks replay the claimed optimal forms; they are not substituted for the continuum proof.

## Originality — PASS (qualified)
The directly inspected finite-free-space literature by Hájek–Lancien–Pernecká (arXiv:1507.02701), Dilworth–Kutzarova–Ostrovskii (arXiv:1807.03814), Alexander–Fradelizi–García-Lirola–Zvavitch (arXiv:1911.10642), and Ostrovska–Ostrovskii (arXiv:2112.02689) covers definitions, graph quotients, Banach–Mazur problems, four-cycle isometries and zonotope classification, but does not give this exact alternating Euclidean distortion formula. The closest publicly indexed results treat only one exceptional cycle edge (`1b1292e047f1`, `38cb69cb8edd`) or equal edges (`13d7bdc76366`). The first two apply to \((1,1,1,r)\), not \((1,t,1,t)\); even when their constants happen to agree at a particular ratio, equality of numerical values is not implication of the full family. No covering statement or general weighted-four-cycle formula was located. This is a best-knowledge originality assessment, not proof of uniqueness in all historical literature. Unindexed convex-geometric ellipsoid treatments remain a residual risk.

## Value — PASS
The two alternating weights form a natural symmetry-preserving family of weighted cycle transportation norms. The theorem gives an exact optimal Euclidean ellipsoid for *every* ratio and discovers a genuine nonmonotone distortion profile, with sharp global minima at two distinct reciprocal ratios rather than at the uniform metric. This is a structural, fully parameterized classification; a single numerical instance would not supply it.

## Limitations
The result is confined to four-point real cycle metrics and alternating edge weights. No result for complex linear maps, arbitrary independent edge weights, or higher cycles is claimed. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
