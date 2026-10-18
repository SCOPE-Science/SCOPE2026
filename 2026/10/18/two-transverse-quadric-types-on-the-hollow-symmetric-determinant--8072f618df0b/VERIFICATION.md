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
# Verification details

Run `python verify.py` in a directory containing the standalone script. The script uses standard-library exact rational arithmetic. It verifies for orders \(5\) and \(6\) explicit integer hollow symmetric matrices of rank \(n-2\), rank \(n-1\) with a zero row, and rank \(n-1\) without a zero row. At the first two points it checks vanishing of every independent determinant derivative and respective Hessian ranks \(3\) and \(n-1\). At the third point it checks a nonvanishing derivative. It also verifies the determinant formula for all-ones off-diagonal matrices in orders \(5\) through \(10\). The observed terminal output is `VERIFY_OK 12 exact witness groups`.

Exact finite tests cannot establish the all-order claim. The proof uses the Gram parameterization, the adjugate criterion and formal Schur complements. Neither an independent review nor external validation is represented by this verification record.
