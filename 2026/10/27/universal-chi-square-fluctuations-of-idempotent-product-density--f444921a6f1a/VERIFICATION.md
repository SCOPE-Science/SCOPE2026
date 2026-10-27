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

The standalone `verify.py` enumerates all sandwich matrices in five finite labeled settings, independently multiplies every pair of canonical Rees idempotents, squares their products, and compares the resulting product-idempotence count with the group-ratio collision expression. It then compares exact rational sample means and variances with the formulas in RESULT.md.

Observed executions: `C2` with `(r,n)=(2,2),(3,3)` gave 16 and 512 matrices; `C3` with `(2,3)` gave 729; nonabelian `S3` with `(2,2),(3,2)` gave 1296 and 46656. Each case passed and the final line was `ALL_CHECKS_OK`. The finite calculations test the exact count and moments, not the asymptotic chi-square convergence; that is justified by the multivariate central limit theorem and continuous mapping in the proof.

No independent audit has been performed. Scientific limitations are the fixed finite group and fixed row count, no zero entries, and labeled uniformly sampled sandwich matrices.
