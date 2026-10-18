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

# Reproducibility and scope

Run `python verify_ritz.py` with Python 3, NumPy and SciPy. The verifier makes 115 assertions, including direct simulations of independently Gaussian-sketched Rayleigh quotients on the two-eigenvalue example, exact special-function evaluations, and the limiting asymptotic ratio. The published proof establishes the infinite statements independently of numerical sampling. RNG seed: 240703. It neither verifies a full iterative eigensolver nor certifies bibliographic priority.
