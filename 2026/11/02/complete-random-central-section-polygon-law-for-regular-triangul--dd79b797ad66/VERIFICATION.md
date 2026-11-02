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

Run `python verify.py` with Python 3 and NumPy. It independently counts the sign crossings of all nine edges under randomly sampled plane normals; it also checks the analytic formulas for probability normalization and limiting behavior. The key proof steps are the exhaustive four-case classification by the number of crossed vertical edges, the exact six-spherical-triangle solid-angle decomposition, and the universal angular sign-separation identity for each edge. Monte Carlo alone is not a proof of the formula and does not establish historical uniqueness.
