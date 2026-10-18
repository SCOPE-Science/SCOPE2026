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

The universal proof is given by two exact support inequalities and their equality conditions, symmetry-rigidity for the inscribed ellipsoid, a signed isotropic covariance certificate for the enclosing ellipsoid, and a complete parametrization of support equality directions.

The standalone `graph_discotope_checker.py` uses only the Python standard library. Executing `python graph_discotope_checker.py` reproduced 8,500 seeded support inequalities on paths, stars, complete bipartite graphs, even cycles and a sparse incidence graph; 1,348 coordinate/contact evaluations; and 193 normalized covariance entries. All tests passed. The test set is finite and does not replace the proof.

Limits: one-edge graphs have continuous inner contact sets; connectedness is required for the finite inner contact classification; the outer minimum-ellipsoid theorem requires bipartite biregularity. No third-party validation was performed.
