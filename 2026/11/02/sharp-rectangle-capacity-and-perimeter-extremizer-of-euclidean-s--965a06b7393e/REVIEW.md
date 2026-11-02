# Review of the stadium rectangle-capacity theorem

## Correctness
**PASS.** Every nondegenerate rectangle is reduced without area loss to a centered congruent rectangle by central symmetry. The equal-radius diagonal representation parameterizes all centered rectangle orientations, and the two-arc structure on concentric circles bounds all rotations by axis-parallel candidates. One strictly unimodal scalar function then yields the unique maximum-area rectangle, including off-center rigidity from strict curvature at all contact corners. Exact symbolic derivatives prove the sharp fixed-perimeter inequality and the strictly increasing filling fraction. The standalone checker verifies the required symbolic identities and independently tests feasible rotated rectangles. The simulation does not establish a theorem on its own.

## Originality
**PASS, provisionally.** The closest full-text source, Behroozi (arXiv:1905.13246, Sections 3.2–3.3), already proves the centeredness theorem and discusses general optimization models; this is explicitly credited. The tested statements of Choi–Lee–Ahn (2021) and Cabello et al. (arXiv:1405.1223) concern polygon algorithms rather than an unrestricted analytic stadium shape theorem. Searches using stadium, discorectangle, obround, capsule, sausage body, rotated inscribed rectangle, aspect-ratio inversion, and the exact perimeter constant did not reveal the present complete profile or sharp inequality. This is not a proof that no earlier equivalent special-case treatment exists.

## Mathematical value
**PASS.** The container is a natural planar Minkowski sum (a segment plus a disk); optimizing the largest inner rectangle is a standard geometric approximation objective. The result goes beyond finding a rectangle in one fixed example: it proves global orientation and center rigidity, determines the whole positive-aspect family, identifies a unique *noncircular* fixed-perimeter optimum with an exact constant, and shows that a measurable shape-occupancy ratio uniquely encodes the aspect ratio. These features are motivated sharp geometric invariants, not a substitution into an existing general formula.

The theorem does not cover general rounded rectangles, noisy inversion, or arbitrarily asymmetric convex containers. Historical priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
