# Scientific review

## Correctness — PASS

The specified exact-Schur pivots are Gram–Schmidt residual squares. The normalized arrow singular-value identity reduces the eigenvalue problem to three positive-definite Gram matrices. Their determinant is exactly one; explicit trace/inverse-trace calculations give the three characteristic polynomials. Strict sign comparisons prove optimality of the central-first orders for every parameter in the stated range, not just at numerical samples. The near-dependence limits and two-row minimality follow analytically. The checker supplies independent exact-rational coefficient tests and numerical full-matrix eigenvalue comparisons.

## Originality — PASS, with bibliographic limits

The motivating primary manuscript already supplies the forward full Schur blocks and general normalized preconditioned spectra (arxiv:2610.17940v1); those are not claimed here. The new statement compares **different permutations**, solves all six orders for an entire continuous family, and proves a worst-case failure of first-pair orthogonality selection. The related row-permuted Neumann-control preconditioner (arxiv:2407.19217v2) uses another matrix and triangular approximation. General older saddle-point work (doi:10.1137/04060679X; doi:10.1137/130911962) was only available through publisher summaries and remains a residual priority risk. Related published mathematical findings on row scaling and block iteration ordering, and accessible earlier claims in this topic, did not cover the precise permutation theorem.

## Mathematical value — PASS

A practical choice among exact sequential constraint-block orderings is governed by **all** Schur pivot sizes, not merely the angle of the first pair. The theorem makes that interaction concrete in the smallest dimension capable of it, supplies the exact optimal and worst orders and a nonvanishing limiting spectral-radius ratio. This is a structural finite model, not a generic solver guarantee.

## Scope and risks

The proof concerns real exact arithmetic, three scalar constraints, a zero lower block, and one family of invertible matrices. It does not prove optimal iteration counts or numerical stability. The two older abstract-only references limit the confidence of the priority assessment; any covering specialized ordering result would supersede originality.

Self-review: passed. Independent audit: not yet performed.
