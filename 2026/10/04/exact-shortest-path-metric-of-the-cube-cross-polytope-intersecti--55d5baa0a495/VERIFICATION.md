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
The verification artifact constructs the graph directly from the claimed edge move: choose one occupied coordinate, zero it, and insert either sign in one previously zero coordinate. For every pair of vertices with \(2\le d\le7\) and \(1\le k<d\), breadth-first search is compared against the closed distance formula.

The replay also checks the predicted vertex count \(2^k\binom{d}{k}\), degree \(2k(d-k)\), diameter \(k+1\), and every shell count \(N_j\). These are finite stress tests only. The infinite proof in RESULT.md does not infer a universal statement from enumeration.

The edge characterization is independently justified by exposed faces of linear objectives on \(P_{d,k}\), and the shortest-path formula is proved by matching lower bounds and constructive exchange chains.
