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

The bundled `verify.py` uses exact rational arithmetic. It reconstructs the six transmission coefficients from the primitive model parameters, recomputes the three cycle quantities, checks the discriminant and \(\mathcal R_0^2\), verifies the sign of the Appendix factor, and substitutes the proposed endemic equilibrium into the four autonomous equations.

The analytic threshold split itself is proved in `RESULT.md`; the finite checker is not used as a substitute for that proof. It verifies the exact counterexample and the source-parametrization constraints. No claim of independent validation is made.
