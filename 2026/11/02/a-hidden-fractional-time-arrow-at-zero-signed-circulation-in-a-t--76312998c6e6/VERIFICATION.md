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

# Verification of analytical formulas

The analytic argument in `RESULT.md` is the primary proof. Run `python verify_fractional_gyrator.py` with NumPy and SciPy. It independently evaluates the positive-frequency integral for the instantaneous signed-circulation coefficient, compares it with the closed beta-integral expression, verifies cancellation for four pairs of distinct bath exponents and checks the predicted small-lag sign and approach to the exact fractional amplitude after subtraction of the zero linear term. The separate code uses no prior-run artifact or external file.

The finite tests do not certify the theorem over a continuum of parameters; that universality follows from Fourier transfer, an exact convergent beta integral, dominated convergence and a standard convergent cosine integral. No pathwise instantaneous velocity is assumed or computed for fractional baths. The method does not quantify finite-sample detection, measurement error, all-lag sign or entropy-production rate. Independent scientific audit has not been performed.
