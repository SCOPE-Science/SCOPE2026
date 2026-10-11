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

The analytic proof in `RESULT.md` is the verification basis. The bundled `verify_projection_area.py` performs supplementary exact symbolic checks.

It verifies that for a body-diagonal normal the restricted cubic has third-harmonic squared amplitude \(1/54\), so the projection area is exactly \(\pi(1-2\varepsilon^2/27)\). It also checks the identity
\[
C^2+D^2=\frac1{16}\prod_{i=1}^3(1-n_i^2)
\]
on several exact orthonormal frames and returns `VERIFY_OK`.

Limits: these finite symbolic instances do not prove the all-direction statement; that statement follows from the complex-coefficient argument in `RESULT.md`. No claim is made about the largest parameter interval on which \(h_\varepsilon\) remains a support function.
