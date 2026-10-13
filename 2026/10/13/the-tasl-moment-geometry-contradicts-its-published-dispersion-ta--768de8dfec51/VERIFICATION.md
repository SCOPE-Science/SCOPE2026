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
The standalone checker recomputes the polynomial normalization, the first two raw moments and the variance from the original density; it does not rely on transcribed sample output. It symbolically checks the derivative factorization and the positivity polynomial certificates. It obtains unique turning points and checks the eight corrected numerical rows, then independently evaluates selected means and variances by high-precision integration against the normalized logistic kernel.

The exact arguments cover all real shape parameters. Finite numerical integrations only corroborate the formulas and are not used as a proof of global monotonicity.
