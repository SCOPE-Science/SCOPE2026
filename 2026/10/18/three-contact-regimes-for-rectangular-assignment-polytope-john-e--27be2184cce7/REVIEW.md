# Scientific review: rectangular assignment ellipsoid

## Correctness

**PASS.** The proof uses the complete rectangular assignment-polytope halfspace description; the strictly feasible uniform point confirms the affine dimension. Uniqueness and row/column permutation symmetry force the three projected eigenspaces. Exact projected-normal norms yield one coordinate budget and two unequal cap bounds. The constrained log determinant is strictly concave; its Karush–Kuhn–Tucker solution is the unique capped water-filling root, including both boundaries. The proof explicitly identifies contact points and their supporting faces. Exact-rational separate facet-normal checks and contact feasibility checks passed in the standalone verifier. No finite enumeration is used to infer the general theorem.

## Originality

**PASS, subject to residual literature-priority risk.** Gill and Linusson (2009) derive the full rectangular polytope description and study faces and graph diameter, not the Euclidean John ellipsoid. Torres (arXiv:2306.11910v1) studies bipartite polytope normality and fractional matching inequalities, not determinant-optimal inscribed ellipsoids. Equal side lengths force simultaneous row/column activation; the strictly rectangular domain has two distinct caps and a genuinely new row-only regime, so its contact classification is not implied by a square-symmetry argument. Targeted searches under maximum-volume ellipsoid, partial permutation, transportation-polytope, and optimal-design terminology did not identify an exact covering result. An independently established equivalent formula could still exist.

## Value

**PASS.** This solves a natural Euclidean extremal invariant for all rectangular fixed-size assignments without enumerating vertices and provides the full exact semiaxis spectrum, volume, and supporting-facet transitions. The row-only regime is an aspect-ratio phenomenon absent from the square case: at \((m,n,k)=(4,5,3)\), row caps touch but column caps do not; at \((7,8,6)\), both touch. The rational water-filling formula and threshold equalities are reusable geometric descriptors for partial assignment polytopes.

## Literature and limitations

Sources: J. Gill and S. Linusson, *The k-assignment polytope*, Discrete Optimization 6 (2009), 148–161 (DOI `10.1016/j.disopt.2008.10.003`); J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1, 20 June 2023. The formula excludes square, saturated, and sparse-edge regimes. Literature-priority and outside confirmation remain open.

Self-review: passed. Independent audit: not yet performed.
