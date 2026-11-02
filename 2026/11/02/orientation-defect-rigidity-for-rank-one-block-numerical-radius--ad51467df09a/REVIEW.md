# Mathematical review

## Correctness — PASS
For each orientation word the rank-one block path has circular numerical range. Its Hermitian part is bipartite with off-diagonal factorization \(B=PQ^*\). The two Gram matrices are exactly the parity-split adjacent overlaps \(1\) or \(r\), hence the full numerical radius is half the square root of the Perron root of their product. The positive matrix comparison is strict for \(0<r<1\) and proper defect-set inclusion; the orthogonal-overlap endpoint uses exact path decomposition. At unit overlap, simple-eigenvalue differentiation gives the positive sine-weighted defect penalty. Symbolic calculation confirms the explicit four-node radical, and `verify.py` executes independently reconstructed finite-matrix comparisons. Singular Gram endpoints and nonnormal phases are treated explicitly. No infinite conclusion is based solely on finite experiments.

## Originality — PASS (best-knowledge, with risk)
Audeh–Kittaneh–Moradi, arXiv:2610.15242v1, Corollary 2.1, contains the alternating-word formula \(\|R\|\cos(\pi/(m+1))\), which is credited as prior work. Their inspected complete main-results section does not classify other orientation words, give the two-parity Gram matrices, prove strict ordering, or compute the first-order positional defect coefficients. Kittaneh–Rashid–Xu (2025) supply broader operator-matrix inequalities, not an implication-equivalent exact orientation classification. Claim-specific mathematical searches found adjacent work on rank-one numerical-radius constants, cyclic weighted shifts, and numerical-radius inequalities, but no exact coverage of this block-word theorem. A potential indirect implication from specialized tensor-product or Gram-matrix literature remains a priority risk.

## Value — PASS
The motivating theorem shows that perfectly alternating adjoints produce a universal sharp numerical radius, independent of the underlying bounded operator. A natural, previously unresolved comparison is what changing the orientation does when the block is nonnormal. The result answers this at all word lengths for the nontrivial rank-one family: it computes every pattern from two small Gram matrices, orders patterns sharply, identifies the exact orthogonality limit, and quantifies the location-sensitive loss from individual adjacent equal-sign defects. This is a coherent exact classification rather than a routine special-case substitution or numerical table.

## Boundaries
The general higher-rank orientation problem is not addressed. Finite checks are supportive; full correctness relies on the analytic proof. Priority confidence is limited by potentially implicit general operator-path results, despite direct comparison with the closest inspected papers.

Self-review: passed. Independent audit: not yet performed.
