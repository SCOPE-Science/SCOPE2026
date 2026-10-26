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

The standalone `verify_spectrum.py` is packaged alongside the mathematical result. It reconstructs the two spectral densities from the matrix resolvent using SymPy, verifies algebraic derivatives and root separations, and compares independent complex-matrix evaluations with the derived formulas at 72 parameter-frequency pairs. All programmed assertions passed when executed against the new package.

Exact statements (both reaction-rate formulas, uniqueness of the two spectral transitions in the real-eigenvalue regime, and protein monotonicity) are supported by the analytic argument in `RESULT.md`, not by numerical sampling. Root decimals are approximations only. The result is for weak-noise Gaussian stationary fluctuations, with no finite-volume jump-process error certification. Independent mathematical audit has not been performed.
