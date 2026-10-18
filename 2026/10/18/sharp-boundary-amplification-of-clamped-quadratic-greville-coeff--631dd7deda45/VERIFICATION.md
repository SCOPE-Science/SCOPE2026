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
# Reproducibility and scope

The separately embedded `verify.py` uses only the Python standard library. Its rational Cox–de Boor implementation independently constructs the open quadratic Greville matrix and tests every entry against the claimed tridiagonal stencil for each \(2\le n\le40\). Exact rational tridiagonal elimination reconstructs every inverse entry and row sum and checks the checkerboard sign, extremal rows, and alternating-sign sharpness. Ninety-digit decimal calculations test the radical formula, exponential correction, and strict decrease. The pure-cardinal comparison is checked independently for finite test orders.

Execution: `python verify.py`.
Expected output: `PASS 53171 exact/decimal assertions, n=2..40, no external dependencies`.

These finite tests do not prove statements for all mesh sizes; the universal argument appears in `RESULT.md`. The historical comparison is not an independent bibliographic certificate. No independent audit has been performed.
