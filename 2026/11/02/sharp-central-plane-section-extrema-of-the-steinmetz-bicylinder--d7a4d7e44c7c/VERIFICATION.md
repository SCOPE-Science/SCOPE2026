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

The attached reproducibility script `verify.py` was run with Python 3 using only the standard library. It compared the analytical formula with an independently parameterized polar-area integral for 154 normal vectors, including axis-aligned, diagonal, and near-degenerate cases; the maximum absolute discrepancy was 1.57003139822e-07. The script also checked the stated interval numerically at these vectors and computed the diagonal-profile stationary parameter by bisection. These are finite numerical tests, not an infinite verification, an independence assessment, or a substitution for the proof.
