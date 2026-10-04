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
The general theorem was checked analytically from the published equilibrium equations.

Analytic checks:
- The exposed balance gives the strict floor and the exact local-transmission fraction identity.
- The scalar endemic equation has a positive strictly increasing right-hand factor on the admissible interval; increasing vaccination therefore moves its unique intersection strictly downward.
- The lower bound plus the scalar equation forces convergence to the importation floor as vaccination tends to infinity.
- The susceptible balance and monotonic contact function give the strict comparison with the closed-system reproduction quantity.
- The first-order excess follows from the exact fraction identity and the limiting susceptible balance.

Reproducibility checks:
- `verify.py` solves the scalar equilibrium equation for an admissible decreasing contact function at several vaccination rates.
- It checks the equilibrium residuals, strict monotonicity, importation floor, amplification identity and bound, and the scaled large-vaccination coefficient.

Limits:
- Numerical replay verifies the displayed example only; the general result is analytic.
- No independent audit has been performed.
