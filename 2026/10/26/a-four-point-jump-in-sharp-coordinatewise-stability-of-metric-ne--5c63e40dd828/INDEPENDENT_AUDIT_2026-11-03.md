# Independent mathematical audit

## correctness

PASS

For n=3 or n=4, edges are listed once in R^(n choose 2), the target M_n is the closed cone defined by the 3*(n choose 3) triangle halfspaces; nonnegativity follows by combining triangle inequalities when n≥3. Euclidean projection is uniquely defined for every real symmetric off-diagonal input, while sensitivity is measured in ℓ∞. On a polyhedral projection cell with strictly positive KKT multipliers and active face normal span B, the derivative is the orthogonal projector I−B^T(BB^T)^(-1)B; segment partition and continuity yield a global bound by the largest induced absolute row sum over all subsets, including infeasible ones. A fresh separate SymPy exact-rational checker reconstructed the triangle normals, enumerated ALL 8 n=3 and 4096 n=4 subsets, canonicalized each RREF span, obtained 466 distinct n=4 spans and verified full rank profiles [1,4/3,3/2,8/5,3/2,10/7,0] with global maxima 4/3 and 8/5. Separately, strict positive y=(3/10,3/10,3/10,11/10,11/10,11/10), x=(1/2,1/2,1/2,1,1,1), v=(1,1,-1,1,1,1), h=1/1000 and star-face active normals (0,3,6) give Qv=(4/5,4/5,-1/5,8/5,3/5,3/5); all 12 inequalities, positive KKT multipliers (497/5000,251/2500,251/2500) and quotient 8/5 were exactly checked. An analogous single-facet n=3 positive witness attains 4/3. These are complete finite cases, with no extension claimed to n≥5, non-Euclidean fitting, or unequal edge weights.

## originality

PASS

Qualified best-of-knowledge originality for the exact ℓ∞ Lipschitz moduli 4/3 and 8/5 of Euclidean nearest-pseudometric projection in dimensions 3 and 4, with a finite strictly positive-input equality pair. The metric-nearness objective, individual triangle fixing, Met_4=Cut_4 and general piecewise-affine projection methods are established prior facts, not claimed as new. Actual primary and published mathematical comparisons found no theorem implying the exact constants; the full 2008 expanded primary paper could not be retrieved, so priority remains provisional.

## value

PASS

Euclidean repair of inaccurate pairwise distances with triangle inequalities is a natural geometric/optimization task; edgewise measurement errors naturally motivate the ℓ∞ modulus of its nonlinear nearest-pseudometric map. The four-point case is the first interacting-multiple-triangle system beyond one triangle; the sharp increase from 4/3 to 8/5 and strictly positive-data equality witness characterize an exact stability obstruction which algorithmic convergence and the cone-ray table do not settle. This is a motivated, self-contained small-dimensional exact invariant useful for benchmarking robust distance repair, without a claim of a general n-dimensional theorem or an unsupported application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
