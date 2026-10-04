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

The theorem is analytic. The accompanying checker uses exact rational arithmetic whenever a square root is not required.

For small sample sizes, it enumerates every iid sample from random rational three-point laws and compares the direct covariance of the sample mean and range with the closed form in `RESULT.md`.

For larger randomized families, it checks the four cut-indicator covariance identities, the reflection relation, and the sign assertions at rational support locations.

In the two-minority-endpoint regime it verifies that the transformed quadratic has negative root product and exactly one positive root. Floating point is used only to locate that root for sign sampling around it; the proof of uniqueness is algebraic.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK enumeration_checks=3500 identity_checks=40000 sign_checks=39989 reflection_checks=40000 root_checks=26481`.
