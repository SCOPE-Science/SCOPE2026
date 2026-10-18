# Scientific review: two-point spindle John ellipsoids

## Correctness — PASS

The exact theorem is checked against the verified two-point spindle meridian \(R(t)=\sqrt{1-t^2}-\sqrt{1-d^2}\). Uniqueness and rotational symmetry reduce the John problem without losing arbitrary off-axis ellipsoids. The meridian-to-ellipse ratio has one critical interior minimum precisely when the squared axial semiaxis exceeds \(q=1-\sqrt{1-d^2}\). Maximizing the resulting two-parameter determinant gives one root in the admissible interval, and the contact points satisfy John's exact isotropy condition. This certifies maximal volume globally. The first-order high-dimensional volume expansion follows by a Gaussian Laplace expansion of the source's exact volume integral and a separate gamma-ratio calculation; all remainder statements are pointwise for fixed \(d\).

Reproducibility: running `python check_spindle_john.py` passed exact rational identities, 49 finite-dimensional optimization and inclusion grids, contact equalities, and numerical comparisons with all three first-order asymptotic coefficients. Grids and quadrature cannot establish the universal claims on their own. The proof supplies an analytical justification distinct from these finite tests.

## Originality — PASS, with residual priority risk

Artstein-Avidan–Florentin (arXiv:2602.14090, Proposition 3.2) give the spindle's exact volume integral and convexity under endpoint displacement; neither provides the maximum-volume inscribed ellipsoid, its exact contact orbits, or the \(1/m\) ellipsoid-volume deficit. Bezdek–Lángi–Naszódi–Papez (arXiv:1110.4329, Definition 2.1 and Remark 2.2) and Lángi–Naszódi–Talata (2011, Definition 1.2) provide spindle and ball-hull descriptions, not the evaluated John ellipsoid; the latter invokes the general John normalization theorem only in a covering-stability argument. Known John-ellipsoid formulas for a half-cone and several polytope families concern distinct bodies and are not stronger statements of this result. The algebra of the new theorem is not obtained merely by reading a named coefficient from either cited source.

Searches under the aliases *spindle*, *two-point ball hull*, *ball-convex hull*, *c-hull*, *spherical spindle*, *maximum-volume inscribed ellipsoid*, and *John ellipsoid*, together with explicit comparison of the two primary full texts, found no covering calculation. This is evidence of a research gap, not a proof of bibliographic uniqueness. Specialized older spindle literature under different terminology remains the principal priority risk.

## Mathematical value — PASS

The family consists of the simplest genuinely full-dimensional nontrivial ball-convex hulls and is used as a building block in recent ball-body symmetrization theory. An exact John ellipsoid is a natural affine approximation invariant. The theorem identifies all its semiaxes in every dimension and reveals an unexpected universal normalized contact latitude, while the sharp volume ratio shows that the ellipsoid becomes almost volume-filling at rate \(1/m\) despite missing extreme points. The coefficient \(\sqrt{1-d^2}/4\) distinguishes the entire fixed-separation family quantitatively; it is not an arbitrary numerical slice or a restatement of the known spindle volume integral.

## Limitations and priority comparison

The two-point spindle is not the intersection of the two balls centered at its endpoints; conflating them would invalidate the theorem. The high-dimensional formulas are for fixed interior \(d\), not degenerate endpoints or arbitrary ball bodies. No claim is made about optimal Hausdorff ellipsoids or all higher intrinsic volumes. An unindexed historical ellipsoid computation remains possible; the originality assessment is based on the identified primary statements and actual database searches, not on absence of search hits alone.

Self-review: passed. Independent audit: not yet performed.
