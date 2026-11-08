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

## Reproducible checks

Run `python3 verify.py` from a directory containing the embedded files (Python 3 standard library only). The script asserts exact cyclic-shift eigenvector relations, computes first imaginary-root residuals for both characteristic factor families, tests the formula for transverse crossing derivatives, brackets the uniquely proven positive crossover, and checks the two-/three-/four-ring weak-dispersal ordering numerically. The recorded direct execution returned `VERIFY_OK 26 mode tests` and a crossover near `0.3676715910600693`.

## What the computation does not prove

The script samples finitely many dispersal values. It does not certify an infinite parameter range, the number of roots in the infinite retarded spectrum, global attraction, or nonlinear periodic orbit stability. Those conclusions are not inferred from numerical diagnostics: the stability interval follows from the analytical characteristic-factor, imaginary-crossing and convexity arguments in RESULT.md. Linear onset is the full proved scope.
