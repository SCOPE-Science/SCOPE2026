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

`verify.py` was executed with a standard Python 3 interpreter and printed `AFFINE_RAC_VERIFY_OK`.

It uses exact integer Walsh transforms, checks the orthogonality/Parseval and inverse Walsh identities, exhaustively verifies every binary truth table for input-bit counts \(N=4\) and \(N=16\), and counts \(8\) and \(896\) extremal bent truth tables. It also checks the quadratic bent witness for \(m=2,4,6,8\).

The universal theorem and uniqueness proof are algebraic; none of the finite checks is represented as exhaustive over all dimensions. Prior publications establish relevant Walsh and codebook background. Independent mathematical audit: not performed.
