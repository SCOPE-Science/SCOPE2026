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

The proof is symbolic and covers every finite connected complete multipartite graph. The standalone `verify.py` independently constructs adjacency from part membership, tests domination after every permitted one-guard exchange, evaluates the claimed support criterion, and compares the direct cardinality census with the closed polynomial.

Replay from the package directory with `python verify.py`. The recorded output is:

`VERIFY_OK graph_types=128 subsets=64916 classification_checks=64916 coefficient_checks=1179 max_order=10`

The finite replay covers every integer-partition graph type of order \(2\) through \(10\). It is a stress test of boundary cases such as complete graphs, stars, balanced bicliques, singleton parts, and part sizes \(2\) and \(3\); it is not used as an infinite proof.
