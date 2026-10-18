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

# Reproducibility and boundaries

The analytic statement is proved in `RESULT.md` by a symmetric quadratic reduction, two globally sharp Rayleigh quotient evaluations, and a complete scalar derivative sign analysis. The file `checker.py` (Python 3 standard library) verifies explicit equality cases, checks independently evaluated Rayleigh bounds at 378,000 finite random samples, and checks the scalar optimum numerically through dimension ten. Execute with `python3 checker.py`. A successful run prints one numerical line per dimension and a final assertion success message.

No floating-point sample, scalar grid, or code output is taken as an exhaustive proof. Nonlinear optimization over arbitrary positive definite matrices is addressed analytically by the two-sided sandwich symmetrization lemma. The theorem covers real finite-dimensional spaces only. The bibliographic review is not an independent audit, and incompletely indexed prior work remains a risk.
