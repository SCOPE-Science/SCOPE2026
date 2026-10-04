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

The claim checked is:

For 3-union-free 3-uniform hypergraphs on 10 vertices, \(U_3(10,3)=8\), and every 8-edge extremal family is, up to relabeling, the pair-star consisting of all triples containing one fixed pair.

`verify.py` performs two finite exhaustive tasks on the 120 triples of a ten-vertex set. First, after fixing one edge and reducing the second edge to the three possible intersection-size orbits, it proves that no 9-edge 3-union-free family exists. Second, using the same complete orbit reduction, it proves that no 8-edge 3-union-free family exists without a common pair. It also directly checks that the 8-edge pair-star is 3-union-free.

The branch invariant contains every union of one, two, or three currently selected edges. A candidate is pruned only when it creates a repeated union immediately; that obstruction cannot disappear after adding more edges. The recursive suffix traversal therefore remains exhaustive. No timeout, probabilistic sampling, or partial enumeration is used.

Replay command: `python3 verify.py`. The captured output is stored in `verification_output.txt`. The finite computation establishes only the ten-vertex statement and does not certify any assertion for larger \(n\).
