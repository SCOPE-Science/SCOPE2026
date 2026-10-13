# Review

## Correctness

PASS. Puncturing a shortest embedding back to the source code is an isomorphism because both codes have dimension \(k\). The source normal form makes the added-coordinate projection have rank \(\ell\), so its kernel has dimension \(k-\ell\). For every \(r\)-subcode, rank-nullity fixes the admissible projection rank \(t\); old-coordinate support is bounded below by both \(d_r(C)\) and the appropriate generalized weight of the kernel subcode, while new-coordinate support is at least \(t\). This proves the lower bound. Lifting a minimizing source subcode proves the upper bound, and the full-dimensional equality is exact. Exhaustive binary and ternary replay checks all finite ingredients.

## Originality

PASS. The 2026 primary paper proves shortest length and characterizes all shortest LCD embeddings but does not discuss generalized Hamming weights. Broad recent GHW work supplies algorithms and general theory rather than this hull-rank law. Searches under shortest-embedding, puncturing, projection-rank, kernel-subcode, hull-dimension, generalized-weight, and weight-hierarchy terminology found no covering theorem. The coarse coordinate-addition upper bound is not claimed as new; the originality claim is the rank-sensitive lower bound and its kernel refinement.

## Value

PASS. The theorem controls every generalized Hamming weight of every shortest LCD embedding rather than only ordinary minimum distance. It identifies where hull dimension forces extra support and gives a sharper embedding-specific correction through the kernel subcode. In the self-orthogonal case, the \(r\)-th generalized weight must gain at least \(r\) support coordinates.

Self-review: passed. Independent audit: not yet performed.
