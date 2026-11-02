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

# Reproduction and limitations

Run `python3 verify.py` with the Python 3 standard library. The script independently evaluates the killed-diffusion Dirichlet resolvent, computes each critical halfwidth by bisection and checks the model's moment constraints, expected ordering, 19 mixtures at each tested rate, resonance and scaling. It uses a separate tridiagonal Dirichlet discrete boundary-value solver to corroborate the continuous formulas and reports `PASS 846 deterministic checks` on success.

The tests are finite numerical consistency checks. The all-parameter theorem is proved by an analytic positive-rank-one eigenvalue equation, strict Jensen/chord inequalities and Brownian exit-time scaling, not by testing. The work does not include an independent scientific audit or global publication-priority certification.
