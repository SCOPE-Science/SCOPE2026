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

# Mathematical and computational verification

The exact fourth-cumulant contrast follows from a fully specified four-time Markov correlation, ordered-gap integration, and finite rational simplification. `verify.py` independently constructs polynomial moment-generator equations for the telegraph model and the circular-diffusion model. It verifies common second moments and contrasts for six positive rational parameter triples, with examples on both sides of the sign change; it also checks the exact positive-root identity. The script uses `sympy` and is runnable using `python verify.py`. Algebraic checks corroborate but do not replace the analytical derivation and sign proof.

The required stationary forcing assumes uniform phase for the angular model and symmetric telegraph initial law; the thermal Brownian forcing is independent and contributes no fourth cumulant. The theorem covers positive oscillation frequency; the zero-frequency/overdamped limit is not included. The numerical examples do not prove novelty or experimental robustness. Independent mathematical validation has not been performed.
