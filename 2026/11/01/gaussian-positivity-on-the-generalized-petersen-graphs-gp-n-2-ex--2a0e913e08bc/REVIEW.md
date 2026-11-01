# Mathematical review

## Correctness — PASS

The object is the full shortest-path metric on the two-layer, cubic generalized Petersen graph \(GP(n,2)\) for every integer \(n\ge5\). Exact anchored Gram matrices turn conditional negative semidefiniteness into ordinary positive semidefiniteness. Four complete integer characteristic-polynomial factorizations prove positivity and exact squared-Euclidean dimensions at orders 5, 6, 9 and 10; every nonzero polynomial factor has alternating signs and the matrices are symmetric. For each remaining order below 18, an explicit zero-sum signed-distance certificate is positive. A single eight-vertex certificate with value \(2\) works uniformly for every order at least 18. The latter universal statement follows from a path-reordering formula on the infinite two-layer cover and a checked winding lower bound, not finite extrapolation. The standalone exact-integer script reproduces the four characteristic polynomials and all finite certificates and checks 171580 distances on 46 graph orders. Gaussian strict positivity follows from finite Schoenberg theory and distinct squared-Euclidean points. The proof does not rely on numerical eigenvalue thresholds.

## Originality — PASS, bounded historical comparison

Kutnar–Malnič–Marušič–Miklavič [1] classify strongly distance-balanced generalized Petersen graphs, not conditional negative type; in fact, their \(GP(n,2)\) index list differs. Sánchez [2] proves general negative-type criteria but not the four-order classification. Gera–Stănică [3] diagonalize ordinary adjacency matrices, not centered graph-distance matrices. Kratica et al. [4] treat strong metric dimension, distinct from squared-Euclidean embedding rank. Shaheen–Mahfud–Alhawat [5] give metric distance distributions and polynomials, but no sign classification of the full centered distance form. A related public result on Vietoris–Rips homotopy for \(GP(n,2)\) does not imply the Gaussian-kernel positivity statement. Published related studies of Möbius ladders, powered cycles and line graphs of cubes concern different graph families. Published search did not identify a stronger result directly covering the classification. Search incompleteness and a possible equivalent older treatment remain real originality risks; title mismatch alone is not used as evidence.

## Mathematical value — PASS

A full classification of a standard two-layer cyclic graph family is mathematically natural: the question asks precisely when its complete shortest-path metric is squared Euclidean, equivalently when all Gaussian distance kernels are positive definite. The four isolated surviving orders and a single uniform obstruction for the infinite complement reveal a structural gap between ordinary graph-distance invariants and negative type. Exact minimal squared-Euclidean dimensions \(5,7,9,10\) further specify the geometry and make the result useful for checking finite metric embeddings and kernel admissibility. This is not merely a small graph calculation or a result about arbitrary selected parameters.

## Sources, limitations, and risk

Sources [1]–[5] are defined in RESULT.md. Inspections involved the distance-balanced classification, the finite-metric negative-type criterion, the adjacency spectral decomposition, the strong-metric-dimension setting, and the published distance enumerators for the same graph family. The classification is for exponent one, not all powered distances; excluded graphs could have kernels positive at some larger scales. Relevant older literature may have a different equivalent statement. No independent mathematical audit or validation has occurred.

Self-review: passed. Independent audit: not yet performed.
