# Self-review

## Correctness — PASS

The result has one precisely specified sampling law: independent uniform left and right hashes and independent signs, one signed nonzero in each of two disjoint row blocks per column, with exactly as many columns as output rows. The proof resolves the possible forest, unicyclic and multicyclic components, including isolated buckets and two-parallel-edge cycles. It shows why a square full-rank draw must consist entirely of unicyclic components, and why each such component contributes a factor one-half from its independent cycle parity. Removing attached trees and evaluating a signed cycle establishes the exact normalized determinant, without assuming pure cycles only. The two-color rooted-tree enumeration, labeled-edge factorial, formal change-of-variables Jacobian and coefficient extraction give an all-integer-size polynomial identity. Exact exhaustive small cases and the independent covariance determinant-moment identity provide supplementary checks. No finite computation is used as an infinite proof.

## Originality — PASS, subject to historical-priority uncertainty

The 2026 GPU sketching paper specifies the distribution and the one-block collision benchmark, but its inspected theory and experiments do not yield the two-block square joint full-rank and determinant polynomial. The 2025 structured-random-matrix paper provides general SparseStack injectivity frameworks and experiments, not this exact finite identity in its relevant inspected sections and appendix. The general sparse-random-matrix rank paper provides asymptotic normalized rank information, not the displayed finite polynomial distribution. An earlier study of this same two-block model gives limiting nullity in an undersampled aspect-ratio regime and divergence beyond it; those limit assertions do not imply an exact, all-size square full-rank probability or volume law. Signed-incidence cycle linear algebra is classical and is credited as an ingredient. The algebraic enumerator could conceivably be known under graph-polynomial terminology; published-priority completeness is not certified.

## Mathematical value — PASS

At the no-oversampling boundary, a sparse sketch can fail to be injective even while individual column norms and mean-square geometry remain properly normalized. The exact joint rank-and-volume law quantifies this basic reliability defect at every finite matrix size, permits comparisons of two-block bucket allocations, and identifies the complete discrete nonzero Gram-determinant spectrum. The closed extreme-allocation formula and exact rational balanced cases are natural benchmarks for testing sparse sketch implementations and for deciding when square sketches need oversampling, rather than an arbitrary isolated numerical slice. The finding does not claim a conditioning theorem, all-subspace embedding guarantee or finite-precision performance prediction.

## Closest literature and limitations

Jeendgar, Flint and Anzt (arXiv:2606.20195; original public date 18 June 2026), Camaño, Epperly, Meyer and Tropp (arXiv:2508.21189), and Coja-Oghlan et al. (doi:10.1002/rsa.21085) are the closest checked source texts. The claim applies to exact arithmetic, independent signs and hashes, and square two-block coordinate-subspace sketches only; the full singular-value distribution and positive oversampling are not determined. Classical signed-graph enumerations are a residual historical-priority risk. Independent audit and independent priority certification are not supplied.

Self-review: passed. Independent audit: not yet performed.
