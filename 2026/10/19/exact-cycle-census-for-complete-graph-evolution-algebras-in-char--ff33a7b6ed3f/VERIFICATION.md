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
The standalone `verify.py` implements the characteristic-two finite-field squaring operation without external Python packages, enumerates all input vectors in nine field/dimension models, and compares every iterate-fixed-point count for all positive \(k\le2f\) against the closed formula. It completed with the message `VERIFY_OK 9 field/dimension cases; fixed-points for all k <= 2f`.

The nine tested field/dimension pairs are \((f,n)=(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,3),(3,4),(4,3)\); the \(f=1\) configurations are control cases outside the claimed \(f\ge2\) theorem. Exhaustive finite tests do not constitute a proof for all field degrees or dimensions. The universal proof uses exact identities and the finite-field additive trace criterion. Independent audit has not been performed.
