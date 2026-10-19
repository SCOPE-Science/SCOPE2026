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

The proof is symbolic and applies to every nonnegative real timestep on the specified generator. The accompanying standalone `artifacts/verify.py` reconstructs the eight rational coefficients by polynomial inversion modulo the cycle relation, verifies four sign-defining identities in exact arithmetic, and checks uniqueness and ordering of the necessary polynomial roots by exact coefficient signs and evaluations. It independently reconstructs the rational matrix function at six rational timesteps and checks its signed entries and conserved row/column sums. Numerical root approximations are not proof certificates. The check requires SymPy and runs with `python artifacts/verify.py`; its success reports only same-model computational corroboration. Positivity of internal Runge--Kutta stages is not asserted.
