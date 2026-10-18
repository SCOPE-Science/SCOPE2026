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

Run `python3 verify.py` with a Python 3 standard library installation. The executable enumerates the dual faces, independently tests the defining independence condition for each tested small graph, checks the exact new-face description and collision-free acyclic distance matching during chord addition, and computes all mod-two boundary ranks by exact elimination. It checks all 1,356 connected labeled six-vertex graphs of girth at least six and nine separately constructed graph families/instances, including an incidence graph with cycle rank eight.

Observed output begins `VERIFY_OK named_cases=9 labeled_six_vertex_graphs=1356`, and the full sample summary ends with `(14, 8, 36)`.

The script does not certify the infinite case or integral Smith normal forms; those follow from the parameter-uniform combinatorial proof and standard integral Alexander duality. The existence of possible unindexed equivalent literature is not computationally decidable from this verifier.
