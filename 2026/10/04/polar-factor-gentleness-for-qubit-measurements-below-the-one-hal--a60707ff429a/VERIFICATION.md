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

The universal statement is established by the analytic proof in `RESULT.md`. The executable `artifacts/verify.py` is a corroborating algebra check only.

It verifies the identities
\[
c=\frac{2g}{1+g^2},\qquad d=\frac{1-g^2}{1+g^2},
\]
checks that the positive filter sends the maximizing latitude \(z=-g\) to \(z=g\) with pure-state trace distance exactly \(g\), and tests the two averaged rotation inequalities for representative values on both sides of \(g=1/\sqrt3\). The script uses randomly generated rotations only to catch transcription or sign errors; random tests are not evidence for the universal quantifiers.

The critical proof steps not delegated to computation are: the exact maximization of \(G(|T|)\); the exact rotation formula bounding \(x(R_{11}+R_{22})-yR_{33}\) when \(y\le x\); the equatorial average bound when \(g\ge1/\sqrt3\); and the implication from \(G(T)<1/2\) to the low-anisotropy branch.

Limit: no computational or analytic claim is made here about the exact optimal disturbance for arbitrary polar unitaries once \(G(T)\ge1/2\), and no higher-dimensional case is tested or inferred.
