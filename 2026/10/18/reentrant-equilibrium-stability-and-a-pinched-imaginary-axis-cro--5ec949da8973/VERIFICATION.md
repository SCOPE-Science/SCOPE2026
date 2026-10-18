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

Run `python verify.py` in the same directory as `RESULT.md`, with SymPy and NumPy installed. It derives the exact Jacobian characteristic polynomial and factors its Routh determinant, checks the double-root specialization at \(a=2c\) and the exact coefficient of the quadratic real-part contact, and evaluates 19 representative polynomial spectra. Expected output: `PASS exact characteristic, Routh determinant, double tangency; numerical cases: 19`.

The parameter-uniform classification uses the analytically justified positivity of \(Q,S\), the classical cubic Routh theorem, and the factor sign arguments in `RESULT.md`; the 19 numerical cases merely test the implementation. The spectral marginal cases have no nonlinear stability or periodic-orbit certification. The independent audit channel has not been exercised.
