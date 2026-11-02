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

The proof in `RESULT.md` derives the transfer matrix from polynomial interpolation and proves the complete two-periodic stability criterion using the real-cubic Schur test. Run `python verify_ab3_alternating.py` in an environment with SymPy and NumPy; the checker reconstructs the coefficients symbolically, checks the exact characteristic polynomial and critical boundaries, and independently tests 998 random noncritical matrices. It also verifies the standard fixed-step reduction and the contrast asymptotic. All these checks passed when run on the embedded artifact.

The analytic argument, not finite numerical sampling, covers all positive steps and arbitrary real initial triples. The check does not verify nonlinear convergence, complex stability, arbitrary grids, independent mathematical audit, or historical publication uniqueness.
