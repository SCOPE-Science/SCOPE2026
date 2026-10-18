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

# Verification

The included `verify.py` runs exact rational-symbolic checks of the squared-radius and angular reductions, Dulac divergence, perfect-square endpoint, stationary Jacobians, power-family envelope and its derivative. It also samples nine numerical trajectories at three parameter values in the enlarged window, verifying convergence in representative attraction basins. The script was executed successfully. The proof, rather than finite computation, establishes exclusion of all periodic planar trajectories and polycycles.

Reproduce with `python verify.py` after installing SymPy, NumPy and SciPy. Any future empirical failure would require scientific re-examination. No independent validation has been performed. No Hurwitz claim is inferred for the enlarged interval.
