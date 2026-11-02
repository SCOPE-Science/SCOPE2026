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

# Reproduction and boundaries

Use `python verify.py` with a standard Python 3 interpreter. No packages or external datasets are required. The script constructs adjacency directly for the crown graph and uses exhaustive cycle and one-vertex-extension tests, independently of the counting argument in `RESULT.md`. It verifies \(3\le n\le9\), including the exceptional \(n=3\) and the coincident maximal degrees at \(n=4\). The observed output is:

`VERIFY_OK graph_orders 7 all_candidate_subsets 349504 maximal_and_all_forest_polynomials True`

The program enumerates \(349504\) vertex subsets; it does not establish the result for larger orders. The unrestricted assertion follows from the complete classification and proof in `RESULT.md`. No independent mathematical audit has been performed.
