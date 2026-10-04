# Same-model review

## Correctness
PASS. Coordinate stationarity gives \(\mathbb E[y]=-m\), \(\mathbb E[x]=-am\), and \(\mathbb E[x^2]=bm\). The affine observable \(\Phi=z+bx-(b/a)y\) has exact derivative \(L\Phi=x^2+(b/a)x\), yielding the stationary circle. Variation of constants proves \(z\ge0\) on every bounded complete orbit and strict positivity away from the origin. Equality geometry of the circle plus invariance gives the two equilibrium endpoints and the two-sided slab excursion. The exact checker returns `VERIFY_OK`.

## Originality
PASS. Targeted published-finding corpus searches for Sprott F, the exact equations, conditional height balance, stationary-circle aliases, and slab crossing returned no same-object finding. The closest database records are analogous stationary-balance theorems for other polynomial flows. The inspected Sprott sources provide the canonical and generalized equations and numerical dynamic-region maps; the inspected same-object equilibrium table provides the canonical fixed points. None of those statements implies the stationary-measure theorem. Residual access and indexing risks are recorded in `AUDIT.json`.

## Value
PASS. Sprott F is a classical minimal chaotic flow with both periodic and chaotic parameter regions. The exact circle law constrains all compact recurrence at once, while the slab theorem turns it into a geometric necessity for every non-equilibrium recurrent state and every nonconstant periodic orbit.

## Closest literature and limitations
Sprott (1994) is the foundational collection; Sprott's public Case F listing gives the canonical equations, and the 2013 dynamic-region note gives the normalized \(a,b\) family. Later synchronization literature tabulates the canonical equilibria. The theorem does not establish existence or stability of non-equilibrium compact invariant sets and does not quantify the amount of invariant mass on either side of the slab.

Same-model review: passed. Independent audit: not yet performed.
