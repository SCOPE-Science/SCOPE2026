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

Exact verification: run `python3 j63_orbit_verify.py` with standard-library Python 3. The program enumerates all candidate sets of sizes zero through four, calculates natural permutation orbits from three representatives, and proves equality of their union with the entire size-four solution set. All assertions succeeded and the matching output is supplied. This verifies only the specified finite graph and relabeling action, not an infinite family, bibliographic independence, or external audit.
