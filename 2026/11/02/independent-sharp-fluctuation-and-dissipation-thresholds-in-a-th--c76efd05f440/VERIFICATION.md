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

# Reproducibility checks

The packaged `verify.py` uses Python 3 and SymPy. Run `python verify.py` in the directory containing that file. It directly solves all six stationary covariance equations and verifies the rational current-based entropy production, trace variance, positive-denominator expressions, both derivative identities, both zero-damping values, large-damping limits, and exact-rational illustrative cases. The sign and uniqueness proof for the entire parameter continuum is analytic and presented in `RESULT.md`: finite numerical checks alone do not establish it.

Actual package verification: PASS: symbolic covariance, entropy-production and derivative identities; 268 deterministic assertions/groups
Independent audit: not performed.
