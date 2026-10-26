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

# Reproducibility

Run `python verify.py` with Python 3; only the standard library is needed. The script checks exact rational matrix row norms, determinant, first-step residuals, all row-pair errors, the uniform expectation, and the full exponent-\(40\) two-step expectation; it independently certifies the strict chain of rational inequalities and a finite diagnostic grid for the two-row identity. The general two-row theorem follows algebraically from equations (1)–(3) of RESULT.md, not the finite grid. No external certification or floating-point experiment is used as proof. Source-priority and all-horizon performance are not established by this verifier.
