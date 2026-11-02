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

Run `python verify.py` after installing `numpy` (see `requirements.txt`). The script evaluates nonlinear F and G updates, constructs central-difference Jacobians at the analytic dual optimum, computes eigenvalue radii independently of the theorem formula, and checks them on 42 dimension/regularization cases including nonsymmetric stochastic kernels. It also checks rational spectral radii at one specific two-site parameter point. Successful run prints `VERIFY_OK: all 42 independent finite-difference Jacobians; exact 2x2 rate; sharp crossover`.

**Proof versus experiments.** The all-dimensional theorem relies on exact differentiation and the strict singular gap for positive stochastic kernels. Finite differences are limited to finite precision and are independent sanity checks, not exhaustive evidence. There has been no independent mathematical review or priority validation. The proposition is a local spectral comparison only; it makes no assertion about wall-clock cost, finite-time monotonicity, or arbitrary nonuniform marginals.
