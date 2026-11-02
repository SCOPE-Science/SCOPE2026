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

The self-contained `CHECK.py` uses only the Python standard library and can be run as `python3 CHECK.py`. It reports `CHECK_OK exact-orthogonality-and-numerical-tests=560` with exact Walsh orthogonality checks for small powers of two and floating-point comparisons against independently diagonalized weighted Gram matrices. All checks passed in the package environment. The analytic two-orbit reduction and derivative proof in `RESULT.md` cover every dyadic order; finite tests are supplementary, and no independent audit has been performed.
