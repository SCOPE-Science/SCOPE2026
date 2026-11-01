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
# Verification and limits

The standalone Python file `verify.py` was executed on the packaged source with Python, SymPy and SciPy and completed with its `PASS` line. It performs (i) sector sign checks for degrees 2 through 11, (ii) an exact scalar shifted-polynomial subleading coefficient check, (iii) a symbolic reciprocal-denominator expansion for the sextic including the cubic and linear perturbations, (iv) formal flight-time inversion, and (v) numerical solution of the exact graph equation with stringent tolerances for three representative degrees. The infinite-dimensional completeness dichotomy and all-degree asymptotic assertions follow from the proof in RESULT.md, not from those samples.

The proof uses the original polynomial ODE, a forward-invariant sector, the scalar comparison theorem, the original-time integral and asymptotic inversion. The full text of the 1999 qualitative near-infinity classification was not accessible; independent priority assessment is outstanding. The result does not resolve the motivating paper's unproved general sextic cycle-count bounds.
