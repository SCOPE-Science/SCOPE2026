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

Run `python verify.py` after extracting the file beside this document; requires Python 3, SymPy, and NumPy. It uses symbolic arithmetic to reconstruct the matrices, matched support, the round-trip matrix, its characteristic polynomial, the entire six-dimensional characteristic polynomial, exact quartic Routh determinant, critical factorization, critical frequency, and transversality derivative. Two subcritical and two supercritical numerical eigenvalue calculations are supplementary consistency checks.

The general lower bound is the analytic two-by-two discriminant argument in `RESULT.md`; no finite enumeration or simulation establishes it. The critical eigenvalue statement is strictly local and linear. A local oscillatory eigenvalue crossing need not generate a nonlinear limit cycle without further normal-form analysis. Bibliographic originality is based on accessible source materials and retains the residual full-text risk described in `REVIEW.md`.
