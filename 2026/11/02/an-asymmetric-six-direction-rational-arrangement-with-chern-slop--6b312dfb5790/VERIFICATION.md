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

# Reproducible checks

`python3 verify_areas.py` checks every one of 57 direction-subset polygons, each exact rational area, the five subset-size aggregates, and integrality of sixfold-dilated vertices. It reports `EXACT_57_POLYGON_AREAS_OK`.

`python3 verify_incidence.py` enumerates every unordered pair of lines at parameters \(n=6\) and \(n=12\), normalizes exact integer homogeneous coordinates, and verifies the finite point census and the full projective pair count. It reports `INDEPENDENT_PROJECTIVE_INCIDENCE_OK`.

These programs use only the Python standard library; the infinite-family inference is the mathematical Ehrhart argument in `RESULT.md`. The cited density lemma is external literature, not independently proved by either checker. Independent external audit is not performed.
