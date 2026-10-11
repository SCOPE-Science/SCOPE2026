# Review of the common-diameter disk-hull identity

## Correctness — PASS

The claim specifies \(k\ge2\), radius \(R>0\), and pairwise distinct supporting planes sharing the diameter line. The exact gauge-level description shows that each cross section of the actual convex hull is \(\sqrt{R^2-x^2}\) times the unit-circumcircle polygon of plane directions. Fubini yields the volume formula. Direct differentiation and integration of the ruled surface patches gives area \(\gamma+\sin\gamma\) for each polygon edge, with correct Jacobian and boundary accounting. Strict concavity of sine over strictly positive angular gaps gives the unique maximizer and unattained lower endpoints. These arguments cover all permitted \(k\) and angles, not just computed examples. The standalone verifier checks independent three-dimensional hull reconstructions and patch quadrature. Finite computations are not used as infinite proofs.

## Originality — PASS with residual priority risk

Finch's 2012 primary paper already proves the two-perpendicular-disk constants, exactly recovered by the special case \(k=2\), so that special case is excluded from novelty. The inspected Bäsel paper addresses a displaced-center oloid, while Nash–Pir–Sottile–Ying treats algebraic boundary and face-lattice classification for two circles. Neither supplies the arbitrary-angle/all-\(k\) exact metric identity and sharp equal-spacing theorem. The closest mathematical-record entry concerns mean width of a separated pair of perpendicular disks; a mean-width result does not determine volume, surface area, or the all-\(k\) extremum. Generic unindexed ruled-surface calculations might imply the result and remain a historical-priority risk.

## Value — PASS

The family is the natural common-diameter generalization of a classical two-disk convex hull, not an artificial parameter slice. Exact surface and volume usually require unrelated integrations; here they satisfy a configuration-independent affine relation for every number of disks. Moreover, the complete fixed-cardinality maximizing family is unique, and the sharp limits recover the Euclidean ball. The theorem therefore supplies a useful precise geometric benchmark and a structure/equality classification, beyond the previously known right-angle pair.

## Scientific limits

No assertion is made for nonconcurrent disks, unequal radii, or ellipses. Earlier unpublished or unindexed evaluations cannot be excluded by literature search, and no independent external audit has occurred.

Same-model review: passed. Independent audit: not yet performed.
