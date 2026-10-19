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
# Verification record

Run `python VERIFY.py` with NumPy and SciPy available. The direct matrix expression is formed from each generated Gaussian right vector and Gaussian left matrix. The script verifies angular moments, the first two moments of the conditional location, the one-column pseudoinverse trace, the exact conditional scale, and near-rank-one tail constants. All 64 assertions passed; output reproduced in `VERIFICATION_OUTPUT.txt`.

The numerical tests use finite instances and numerical integration. The proofs of the tail and moment thresholds rely on the distributional argument in `RESULT.md`, not numerical tail extrapolation. An independent audit has not been performed.
