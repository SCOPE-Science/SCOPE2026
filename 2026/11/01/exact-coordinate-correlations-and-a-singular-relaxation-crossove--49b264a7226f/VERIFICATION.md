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

Run `python3 checker.py` with Python 3. It verifies 259 stationary autocovariance coefficients using exact rational arithmetic across seven parameter values and the claimed rational generating function. No third-party libraries are necessary.

The infinite-lag generating function is proved by the invariant finite-dimensional transfer operator and its resolvent, not by numerical sampling. The singular correlation crossover is derived by spectral factorization and the residue limit. The tests do not establish originality or independent mathematical certification.
