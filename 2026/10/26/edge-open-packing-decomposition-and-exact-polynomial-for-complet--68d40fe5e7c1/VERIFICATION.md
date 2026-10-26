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
# Verification details

The mathematical proof is a bijection and a discrete one-variable optimization, and so does not rely on code. Reproducible checks are supplied in two Python 3 standard-library files. `python3 verify_subdivision_general.py` calculates coefficient vectors using matching-plus-center enumeration and, separately, checks the third-edge constraint directly on all candidate edge subsets for every labeled graph with at most four vertices and 32 fixed-seed five-vertex graphs. It prints `ALL_CHECKS_OK`. `python3 verify_complete_subdivisions.py` compares the closed complete-graph polynomial with brute edge-subset checks for orders 2, 3, 4, 5, each yielding `MATCH True`.

The maximum-degree 6 coefficient for the five-vertex complete graph equals 20, agreeing with the balanced ordered cut count. The general proof also explicitly covers edgeless graphs and the small complete graphs, avoiding assumptions of connectivity. These tests do not establish the infinite assertions on their own. No independent audit has been carried out.
