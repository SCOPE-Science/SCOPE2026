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

# Reproducible finite verification

Run `python3 desargues_pd_verify.py` and `python3 desargues_pd_independent.py` with Python 3.9+ and no extra dependencies. The first enumerates all 240 explicit automorphisms, all 1,140 candidate triples and the two complete reconfiguration graphs; both representative BFS distance profiles prove eccentricities using the transitive group action. The second constructs `GP(10,3)`, verifies a concrete incidence-model isomorphism, and uses independent edge-monitoring propagation rules. It searches all 240 source vertices of each move graph when computing all eccentricities. Exact captured outputs are in the two `.txt` files. Both outputs end with success markers. The code shows the finite enumerations exhaust the claimed domain; the files are neither expert-certified nor externally audited.
