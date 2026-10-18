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

# Verification of the mathematical calculation
The proof of the strict sign consists of termwise integration of a uniformly convergent series. The critical coefficient is derived from the second Fourier harmonic of the Poisson kernel, and the finite-time formula is derived by an exact angular time change. These steps are written explicitly in `RESULT.md`.

Run `python verify.py` with Python 3, SymPy, mpmath and SciPy installed. The verifier checks symbolic angular exponents and a finite sample of beta identities; it evaluates high-precision quadratures for parameters of both signs and near the angular positivity boundary; and it checks the analytic threshold slope, oddness and physical-clock relation in selected cases. These finite calculations test implementation consistency only and do not establish the infinite-series sign theorem for all real parameters.

The original-time blow-up constant depends on fixed initial radius and angle. Neither external peer review nor independent mathematical audit is represented here.
