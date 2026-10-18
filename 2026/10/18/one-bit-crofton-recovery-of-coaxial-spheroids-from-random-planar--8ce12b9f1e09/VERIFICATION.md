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

# Verification notes

The supplied `check.py` is standalone and uses SciPy and NumPy. Running it in the prepared environment printed `SPHEROID_PAIR_CROFTON_OK quadrature_cases 11 monotonic_cases 3 inversions 4 simulation_trials 3300000`. The checks include direct random affine-plane normals and signed offsets, rejecting misses of both spheroids, as well as exact normal-offset quadrature. Numerical tests have no independent-proof or historical-priority status. The analytical proof provides the arbitrary-parameter and asymptotic conclusions.
