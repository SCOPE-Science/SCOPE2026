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

# Reproducibility and limits

Run `python CHECK.py` in a Python 3 environment with NumPy and SciPy. It tests finite-degree Laguerre roots and the exact primitive/envelope identities by numerical differentiation, then checks representative finite-degree approximations against both asymptotic regimes. The test returns `GENERALIZED_LAGUERRE_BV_CHECKS_PASSED 655` on success.

The analytic proof, not this numerical battery, establishes the infinite-degree limits. The checker does not independently verify the classical Mehler–Heine or Plancherel–Rotach theorems, nor does it certify publication priority. The results use fixed parameters and explicitly stated polynomial normalization.
