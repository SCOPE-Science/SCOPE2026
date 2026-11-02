# Review: Exponentially many nondegenerate centroidal cuts of simplices and their vertex truncations

## Correctness — PASS
Affine barycentric symmetry puts the solid and each partition section centroid at the equal-coordinate point; cap volumes are epsilon^n, separated from each section, and locally subtract k caps. Dirichlet aggregation yields Beta(k,l); conditional within-block Dirichlet variances and exact differentiation of the moving beta threshold give the signed Hessian and nonzero coefficients for all positive k,l. Direct independent quadrature, exact rational tails and truncation checks in verify.py passed. Infinite dimensional parameter n is covered analytically rather than by finite tests. The proof precisely distinguishes affine-invariant Hessian signature from coordinate-dependent eigenvalues and does not extrapolate finite checks to all dimensions.

## Originality — PASS, provisional priority
The inspected full tetrahedron classification establishes the seven n=3 cuts but explicitly disclaims higher-dimensional completeness. Patáková–Tancer–Wagner gives only a general critical-point characterization and generic existence bound; the new all-dimensional exponential construction, nonzero signed beta-Dirichlet Hessian and stability under vertex truncation are not implications of those statements. Closest directly comparable full texts were read to the stated limits. Novelty remains provisional against unlocated older simplex and Dirichlet calculations. See especially the 2020 critical-point equivalence in Patáková–Tancer–Wagner, the 2024 global-minimum result in Myroshnychenko–Tatarko–Yaskin, and the fully read public 2026 tetrahedral exact-seven classification. The first establishes general equivalence, the second quantifies a minimum over convex bodies, and the third proves the n=3 case only. The exact all-dimensional Hessian/persistence is not entailed by any inspected statement; priority risk from unlocated equivalent formulations remains.

## Value — PASS
The centroidal-cut count is a natural invariant from the Grünbaum–Loewner/halfspace-depth questions. Constructing 2^n−1 distinct nondegenerate directions in every dimension n>=4 and an entire nonsimplicial truncation family is a structural lower-bound theorem rather than isolated exercise. The exact Morse-index split gives additional stable geometric information about the critical landscape; no conjectural general bound is asserted.

## Scientific limitations
The result constructs an explicit exponential family in dimensions at least four, determines its nonzero transverse Hessian and its persistence under vertex truncation; it does NOT classify every centroidal cut of a higher-dimensional simplex. The numerical matrix coefficients use barycentric normal coordinates. No quantitative noise stability, general convex body count, or independent mathematical audit is claimed.

Self-review: passed. Independent audit: not yet performed.
