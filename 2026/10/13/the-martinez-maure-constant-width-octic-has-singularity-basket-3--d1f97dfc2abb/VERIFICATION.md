---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The standalone `verify.py` rebuilds the exact degree-eight polynomial and performs the following checks with exact symbolic arithmetic:

1. It verifies invariance under rotation by \(2\pi/3\).
2. It reconstructs the complex rational parametrization and checks direct substitution into both the affine and projective equations.
3. It computes the resultant of the two parameter equations and obtains the implicit equation exactly. The penultimate subresultant is linear in the parameter, and its leading coefficient evaluates to \(151552\) at a point of the image, proving generic degree one.
4. It solves \(F=F_x=F_y=0\) exactly and obtains nine affine singular points, organized as three real points and two conjugate three-point rotation orbits.
5. It checks a nonzero Hessian determinant at a nonreal representative, giving type \(A_1\) on all six nonreal points by symmetry.
6. At \((0,9)\), the normalization expansions have initial orders \((3,4)\), giving type \(E_6\); rotation gives the other two.
7. The homogeneous leading form is \((x^2+y^2)^4\), so the only points at infinity are \([1:i:0]\) and \([1:-i:0]\). In a local normalization chart, an analytic coordinate change gives orders \((2,7)\), hence type \(A_6\).
8. The delta sum is \(3\cdot3+6\cdot1+2\cdot3=21\), equal to the arithmetic genus of a degree-eight plane curve.

Fresh execution result:

`VERIFY_OK`

`affine_singularities=3_E6_plus_6_A1`

`infinity_singularities=2_A6`

`normalization=P1`

`delta_total=21=arithmetic_genus`

The verifier establishes the exact curve claimed here; it does not assert anything about other degree-eight constant-width curves or equisingular families.
