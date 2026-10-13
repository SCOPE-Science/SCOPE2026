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

# Reproduction and mathematical verification

Execute `python3 verification/check.py` from the extracted package root using Python 3 (standard library only). It calculates the three expectile balance equations exactly using fractions, confirms the secant slopes and determinant, and checks the final rational perturbation margin. It prints a positive determinant lower bound `74534937/8750000000`.

The exact calculation is a finite certificate for the numerical constants. The theorem about continuous distributions additionally requires the analytic arguments in `RESULT.md`: the everywhere-positive density, the exact monotone square-map quantile transformation, the score strong-monotonicity/Lipschitz estimate for expectiles, and the determinant perturbation identity. Checking finitely many test points or enumerating samples would not establish those assertions.

Limitations: no independent audit has taken place, and the search for an equivalent formulation in earlier mathematical literature is not exhaustive.
