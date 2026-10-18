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
# Verification record

The proof derives the minimum size and exhausts its equality cases for every integer \(r\ge3\). In the independent checker, the graph has \(3r+2\) vertices and \(4r\) edges; for each edge a breadth-first-search distance matrix is recomputed after deleting that edge. A selected pair monitors the edge if and only if the corresponding distance strictly increases. Every size-\(r\) subset and every size-\(r+1\) subset is tested for \(r=3,4,5,6,7\). The complete successful collections are compared to the stated families, not merely their counts.

The code then constructs reconfiguration adjacency by the condition that two minimum sets have symmetric difference of size two. It verifies the exact two-punctured-cubes-plus-links description, expected degrees, connectedness, total number of edges, and graph diameter. There are 873813 candidate sensor sets across all five graph sizes, and all tests pass. The companion `verification_output.txt` records the exact per-size counts and success marker; `verify.py` recreates that output with the Python standard library.

Finite enumeration alone cannot establish the statements for unbounded \(r\); those conclusions depend on the symbolic proof in `RESULT.md`. The checker and the proof use different representations of the monitoring condition: edge-deleted distance matrices versus geodesic lengths. Independent external validation has not been performed.
