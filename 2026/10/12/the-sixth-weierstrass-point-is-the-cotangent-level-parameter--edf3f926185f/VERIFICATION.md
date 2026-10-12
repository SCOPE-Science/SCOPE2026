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
# Verification

The exact symbolic replay is `verify.py`. It verifies the two tangent-radical identities
\[
S_1-rS_0=-q_0,\qquad S_2-rS_1=-q_1,
\]
so on \(X\) the tangent-radical matrix has rank one unless \(S_0=0\). It also constructs the six-point Kummer equations with sixth branch parameter \(r\) and verifies
\[
E_1-rE_0=q_0,\qquad E_2-rE_1=q_1,
\]
as well as equality, up to sign, of the Kummer branch equation and the tangent-plane branch equation.

A fresh execution of the packaged checker produced the exact line recorded in `verification_output.txt`:

`VERIFY_OK tangent_branch=kummer_branch sixth_branch_parameter=e complement=16_two_torsion`

The checker verifies algebraic identities, not the published geometric theorems. The geometric inputs used are: Kim--Lee's characterization of the branch locus by the double-line condition and their smooth Kummer-type result for every nondiscriminant direction; Skorobogatov's three-quadric model of the desingularized Kummer surface; and the standard fact that the sixteen nodes of a genus-two Kummer quotient are the images of the sixteen two-torsion points.

No finite experiment is used to certify an infinite family. The argument excludes the five discriminant directions and makes no statement about their degenerations.
