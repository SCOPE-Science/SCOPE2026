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

The mathematical verification relies on the explicit symbolic identities, supporting-plane vertex triples, Euler facet bound and pyramid-volume decomposition in RESULT.md. The included reproducible `check_cube_twist.py` performs: (i) symbolic orthogonality, rotation determinant, support-plane cross-product and derivative checks; (ii) 97 rational interior cases plus the two endpoints for all twelve active planes; and (iii) 231 independent NumPy/SciPy halfspace intersections and convex-hull volume reconstructions. The exact-rational case checks do not by themselves prove the continuum theorem; the displayed analytic proof does.

Run `python check_cube_twist.py` from the extracted package directory. SymPy is required, and the independent hull check also requires NumPy and SciPy. No external certification or independent audit was carried out.
