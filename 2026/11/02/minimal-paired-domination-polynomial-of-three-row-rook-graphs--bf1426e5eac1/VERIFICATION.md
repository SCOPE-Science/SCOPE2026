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

# Reproducibility

The included `artifacts/verify.py` is executable using Python 3 and only its standard library. It builds rook-graph adjacency from the defining row/column criterion, uses a backtracking perfect-matching test, and checks the inclusion-minimal property using exhaustive downward subsets. It compares exact counts against the polynomial and checks each resulting minimal-set structural class.

Execute `python3 artifacts/verify.py` in the extracted package root. Expected final output:

`VERIFY_OK graph_orders=6 direct_vertex_subsets=2396730 arithmetic_orders=98`

The direct checks use \(n=2,\ldots,7\); \(n=2\) is a separate boundary check. The arithmetic checks range over \(3\le n\le100\). These are finite verifications and do not certify the infinite claim. The unrestricted claim is justified by the proof in `RESULT.md`.
