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
# Reproduction and limits

Run `python3 verify.py`. The checker uses only the standard library and is deterministic. It verifies the exact defining polynomial, all five gradient identities modulo \(s^{11}-4\), Hessian rank 3, 16105 projective test points, 1464 cubic points, 133 tangent-quadric points, and 12 points on the complete intersection \(Q=C=0\). It reports `VERIFY_OK`. These finite checks are not used as substitutes for the proof of characteristic-wise smoothness or the algebraic description of the entire singular scheme. The source-based originality assessment is not independent certification.
