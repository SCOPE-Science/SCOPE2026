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

The exact edgewise torsion expression and the slope-simplex and Euclidean-triangle estimates supply the infinite-domain proof; no enumeration or numerical test is used as a proof of a continuum inequality.

To replay finite checks, use Python 3 with NumPy and run `python check_star.py`. The checker independently assembles a Kirchhoff finite-element stiffness system for 32 configurations, compares 1,000 sampled quadratic shooting solutions and checks 24 prescribed degenerating configurations. These are consistency and boundary-stress tests only. Random seed is fixed in the code. Analytic claims and their strict endpoints are justified in `RESULT.md`.

The exact primary source dates and relevant published comparisons are in `RESULT.md` and the structured scientific review. No independent audit has been performed.
