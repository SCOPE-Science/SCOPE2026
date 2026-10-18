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

Execute `python3 checker.py`. This performs 400 seeded, independent plane–cube intersection polygon-area comparisons, three exact endpoint configurations, several tangent-deficit convergence checks, and direct numerical quadrature of the first-quadrant homogeneous-deficit area. The checker uses only the standard Python library. Successful finite checks do not certify the infinitesimal limits; those rest on the piecewise analytic formula and spherical-area argument in RESULT.md. No independent audit or external proof certification has been performed.
