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

Run `python verify.py` with Python 3, SymPy and NumPy installed. The script evaluates the exact Gram-row rational identity by reducing its numerator modulo the characteristic quadratic, checks the equivalent contrast formula, tests 14 positive integer length pairs, compares exact and floating finite-cycle inverses, and compares several periodic finite meshes with the analytical full-line limit.

The actual checker reported `PASS: 144 independent symbolic, exact rational, and finite-cycle checks`.

Finite-cycle and floating calculations verify computations but do not prove the infinite-line operator statement. The infinite proof uses the explicit square-summable inverse-Gram row, exact absolute integration, decay, translation/reflection invariance and kernel-sign extremization. The formula does not cover finite intervals, nonalternating meshes, or higher-degree spline spaces. No independent audit has been performed.
