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

Run `python check_ellipsoid_distance.py` with Python 3 (standard library). It reports `ALL_CHECKS_PASSED` after checking direct rational Cartesian-moment expansions versus the independent radial-Dirichlet formulas and reconstructing exact characteristic polynomials in dimensions 2–5, including repeated semiaxes. It also checks the first and second radial constants for dimensions 2–8. The analytic all-dimensional argument is in RESULT.md; these finitely many exact tests cannot substitute for it. No independent mathematical audit or experimental statistical precision guarantee has been provided.
