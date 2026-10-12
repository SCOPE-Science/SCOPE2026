# Scientific review

## Correctness — PASS
For bounded marked corner rectangles, the grid contains \(n\operatorname{area}(B)+o(n)\) eligible cells and at most \(O(\sqrt n)\) cells in any row or column. At fixed factorial-moment order, row/column collisions remove only \(O(n^{m-1/2})\) of \(O(n^m)\) choices. Compatible pinned cells occur with exact probability \(1/(n)_m\). For any fixed number of pinned cells, the unrestricted inversion count is a uniform smaller-permutation inversion count, and all pinned-pair corrections are at most linear in \(n\), negligible relative to \(n^{3/2}\). These facts and the independently derived Gaussian inversion CLT establish joint Poisson–Gaussian convergence. Exact exhaustive and factorial-moment checks in `verify.py` pass. Unproved: an explicit quantitative convergence rate and extensions beyond uniform permutations.

## Originality — PASS, with residual historical risk
Kløve et al. (arXiv:0907.2682v1) give the exact finite Chebyshev metric and ball-permanent enumeration, covering the marginal finite counting problem but not the present joint spatial Poisson/inversion Gaussian limit. Baxter and Zeilberger (arXiv:1004.1160v1) establish joint independence for inversions and major index, not for extreme displacement or corner counts. Barbour and Janson (arXiv:0907.0347v1) treat functional permutation-sum Gaussian approximations, not sparse extreme-corner point processes. The new theorem is the independent *coupled spatial and global* limit. It is not certified absent from all unlocated literature; broad asymptotic Poissonization principles are a priority risk.

## Value — PASS
The natural Chebyshev maximum-rank error and Kendall inversion count measure worst-case and aggregate ranking disorder on incompatible scales. Their null fluctuations have different Poisson-extreme and Gaussian-bulk mechanisms; proving their joint independence gives simultaneous distributional calibration rather than a routine separate marginal limit. The theorem retains the full two-corner spatial Poisson information beyond the scalar maximum and supplies a reusable finite-pinning criterion.

## Scope and remaining risks
The exact finite Chebyshev ball expression from earlier work already contains the marginal maximum-distance distribution, and the inversion CLT is classical; neither is independently a novelty claim here. The proof does not establish explicit error constants, total-variation convergence of the infinite point processes, or the statement for biased permutation laws. Priority remains subject to independent historical review.

Self-review: passed. Independent audit: not yet performed.
