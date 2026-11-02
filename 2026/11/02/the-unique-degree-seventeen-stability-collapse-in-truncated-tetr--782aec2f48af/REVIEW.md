# Scientific review

## Correctness — PASS

The twelve-node construction, exact surface-measure normalization, and addition theorem identify the evaluation rank with the rank of the twelve-by-twelve Legendre Gram. Its inner-product histogram is verified from integer coordinates. The packaged pure-Python certificate computes the rational ranks through degree six, proves every other Gram from degrees seven through one hundred positive definite above the explicit gap (except seventeen), and proves the degree-seventeen constant-vector eigenvalue exactly. A separate constant-complement positive-definite certificate isolates that eigenvalue. Bernstein's published bound and a strict Gershgorin estimate cover *all* degrees at least 101. This supports all quantifiers without relying on finite extrapolation. The condition-number conclusion follows from trace twelve and the disjoint gap bounds.

## Originality — PASS (bounded comparison)

Published general interpolation theory (Marzo) treats growing node arrays and cumulative polynomial degrees; it does not imply fixed-node exact-degree Legendre spectra or identify a universal condition-number maximizer. Harmonic-index design theory (Bannai–Okuda–Tagami) concerns vanishing unweighted harmonic sums and minimum design sizes; it does not settle the sharp stability of the present twelve non-antipodal nodes. Wang's Bernstein inequality is explicitly reused as a known analytic ingredient, not claimed as new. Searches for the truncated tetrahedron, its coordinate orbit, spherical-harmonic Gram eigenvalues, and degree-seventeen singularity did not reveal a covering theorem. A previously unpublished or differently phrased representation-theoretic/cubature table remains a meaningful residual risk. Absence of matches alone is not treated as proof of novelty.

## Mathematical value — PASS

Exact-degree interpolation of arbitrary values on canonical polyhedral node sets is a natural sampling invariant. The rank regression at degree six is structurally nonmonotone; the uniquely very small degree-seventeen eigenvalue after permanent full rank is an unusually sharp, mathematically motivated stability boundary. The exact eigenvalue and global separation distinguish the result from a mere finite numerics exercise or a restatement of design strength. The all-degree classification resolves the corresponding fixed-configuration question completely; general extensions are not required for this value judgment.

## Closest literature and limitations

The closest accessible full texts are the introductory and main-results sections of Marzo (arXiv:math/0611503v1), Bannai–Okuda–Tagami (arXiv:1308.5101v1), and Wang's explicit Bernstein lemma (arXiv:1803.00336v1). No source was found stating this rank sequence or condition-number extremizer. The novelty comparison is bounded; older polyhedral harmonic tables could contain an equivalent computation. The proof does not give the exact global maximal condition number, only its unique degree and separated rigorous bounds. The checker depends only on standard Python integer/rational arithmetic.

Self-review: passed. Independent audit: not yet performed.
