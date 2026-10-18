# Scientific review: sharp Euclidean width of the standard cyclohedron

## Correctness — PASS
The target is the intrinsic Euclidean width of the unit-coefficient Minkowski sum of all coordinate simplices on connected subsets of the cycle. For a mean-zero normal, the support width is a sum of coordinate ranges. Sorted-coordinate gaps decompose exactly into nested mean-zero cut vectors. The range sum is linear in these gaps and Euclidean triangle inequality forces a minimizing cut. Because distinct proper nested cut vectors cannot be parallel, all minimizers are two-level.

For any cut, a cyclic-run count bounds the number of tubes meeting both colors by \(A_n+s(n-s)\), with equality exactly for a single cyclic block. Optimization in \(z=s(n-s)\) gives the stated all-\(n\) widths and equality families, including the exceptional \(n=4\) singleton case. The standalone checker passes exact cut tests for sizes 3 through 10 and finite directional checks; the all-dimensional result follows from the proof, not from sampled directions.

## Originality — PASS, with residual bibliographic risk
The primary simplex-sum/nestohedral realization and the coarea technique are credited. The closest published result on the **same cyclohedron** proves its Euclidean **inradius**, not minimum width, and its formula cannot imply the width because no central symmetry is assumed. The nearest generalized coarea result concerns inradii of **graphical zonotopes**, whose summands are segments rather than all cyclic connected-subset simplices; the new sharp cyclic-run optimization is not part of that theorem. Published work on graph-associahedron diameters treats graph-geodesic distance.

Inspected primary literature: Jochemko–Ravichandran, arXiv:1909.08448; Padrol–Pilaud–Poullot, arXiv:2109.09200; Cardinal–Pournin–Valencia-Pabon, arXiv:2106.16130. Compared full texts of published cyclohedron-incenter and weighted-graphical-zonotope records, and performed multiple statement-level published-finding corpus and primary-literature searches for width, support ranges, cut equivalents and dominating formulations. An older equivalent in an unindexed source remains possible; a distinct clock-quasimetric cyclohedron result was only compared at summary level. This is not a priority certificate.

## Mathematical value — PASS
This is a complete metric invariant for a canonical infinite family, including exact normal-orbit classification and a nontrivial small-dimensional transition. It is not a restatement of the known inradius and does not claim novelty for layer-cake/coarea in isolation. The result is specific to the standard realization and does not optimize over arbitrary cyclohedron embeddings.

## Scientific limitations
There has been no independent mathematical audit. The finite reproducibility checks cannot prove the all-dimensional statements. Search nonappearance alone is not proof of novelty, and the result makes no statement about Euclidean widths of other affine realizations.

Self-review: passed. Independent audit: not yet performed.
