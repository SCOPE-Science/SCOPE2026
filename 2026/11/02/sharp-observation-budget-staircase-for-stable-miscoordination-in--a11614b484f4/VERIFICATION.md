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

The result is proved symbolically in `RESULT.md`. The self-contained Python 3 verifier `verify.py` checks the binomial response polynomials, the exact odds-coordinate identity and strictly positive coefficients for the no-stability regime through larger sample size thirty. It also checks the constructive inequalities and sharp threshold on rational payoff values, including exact ties. All checks are exact integer or rational calculations; they do not replace the all-size proof.

The proof concerns the continuous-time one-population ODE, not finite stochastic population trajectories. Neither an independent external audit nor third-party certification has been performed.
