# Same-model review

## Correctness
PASS. The proof is exact in arbitrary dimensions. It computes the restricted coordinate-normal norm in the affine space of fixed row and column sums, so the radius of a ball centered at \(X\) is exactly \(\min_{i,j}X_{ij}/\kappa\) with \(\kappa=\sqrt{(m-1)(n-1)/(mn)}\). Row and column averages give the universal upper bound \(t_*\) on the minimum entry, and the residual product matrix realizes every \(t\le t_*\). The same equivalence characterizes all optimal centers. Finite computation is only a replay of these identities.

## Originality
PASS. The closest inspected sources separate into three neighboring topics: transportation-polytope monotone paths, orthogonal projection onto prescribed-margin affine spaces, and smallest enclosing balls of the Birkhoff polytope. None implies the largest intrinsic inscribed-ball formula or the complete center set. Searches across inradius, insphere, largest-inscribed-ball, Frobenius, transportation, Birkhoff, and doubly-stochastic aliases returned no matching statement. Residual risk remains for older or unindexed literature with different terminology.

## Value
PASS. The result computes a natural metric invariant for a central polytope family in closed form for all positive margins, gives the full optimizer set, and isolates a simple bottleneck statistic behind an otherwise high-dimensional feasible region. The Birkhoff case becomes the sharp formula \(\rho(B_d)=1/(d-1)\) with unique center \(J/d\).

## Closest literature and limitations
Blanchard--De Loera--Louveaux provide the primary polyhedral-combinatorics setting and study transportation-polytope graph geometry. Bauschke--Singh--Wang supply closely related affine projection formulas. Bouthat--Mashreghi--Morneau-Guérin study metric centers and radii of the Birkhoff polytope, but for smallest enclosing balls rather than largest inscribed balls. The theorem here is restricted to complete support, strictly positive margins, and the intrinsic Frobenius metric; sparse supports and other norms remain outside the claim.

Same-model review: passed. Independent audit: not yet performed.
