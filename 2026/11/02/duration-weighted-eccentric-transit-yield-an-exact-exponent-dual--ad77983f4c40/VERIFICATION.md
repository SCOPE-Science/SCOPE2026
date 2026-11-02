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

# Computational verification

The companion `verification/check.py` uses only the Python 3 standard library and tests the two independently programmed expressions for phase-integrated weighted transit yield. To replay, save it alongside this package and run `python verification/check.py`. The program reports `PASS: 92 numerical consistency assertions` for the tested phase grids and finite parameter values.

The source theorem is a proof by substitutions, strict log-convexity, Jensen's inequality, dominated convergence and a classical complete-elliptic-integral asymptotic. Numerical integration and sampled parameters cannot establish the identities for all real exponents, all eccentricities, or the critical limit. All calculations are performed in standard double precision; the test tolerances are for numerical consistency, not rigorous interval arithmetic. The model itself is an idealized duration-weighted yield proxy, not an empirical survey-completeness predictor.
