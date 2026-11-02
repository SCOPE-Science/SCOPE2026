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
Run `python verify_sympy.py` with SymPy installed. The program solves the six degree-two and fifteen degree-four generator moment equations by exact rational linear algebra at three independent rational parameter pairs and checks the closed two-variable derivative formula, fourteen-degree polynomial leading and constant terms, exceptional coefficients, and the exact sign-witness identity. The finite parameter checks do not constitute an all-parameter proof: that part follows from the displayed stationary polynomial recurrence, exact symbolic elimination, and Descartes/sign-witness argument in RESULT.md. The decimal turning points for the canonical symmetric oscillator are descriptive only. No independent audit has been performed.
