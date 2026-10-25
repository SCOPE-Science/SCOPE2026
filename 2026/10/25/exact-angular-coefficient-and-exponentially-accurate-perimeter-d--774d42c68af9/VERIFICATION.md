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

The proof is self-contained in `RESULT.md`. The ordinary Python 3 standard-library verification program `verify_boundary_perimeter.py` runs seeded independent simulations for four shapes and checks the predicted coefficient in sample sizes 20, 50, 100 and 200. It was executed successfully and printed `PASS numeric tests`. Monte Carlo tolerance is only a supplemental diagnostic; the exact finite-N bound comes from the explicit nearest-neighbor density, an elementary integral and an empty-edge union bound. The scope explicitly includes collinear samples with twice-segment perimeter and excludes polygons with consecutive collinear edges.
