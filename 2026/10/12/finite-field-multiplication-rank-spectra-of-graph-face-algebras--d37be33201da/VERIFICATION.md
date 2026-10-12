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

The exact formula follows from the linear equations on each graph edge and the decomposition of the graph into induced-support components. Its assertions hold for every finite graph and every finite field, not just the checked instances.

Reproduce with `python verify.py` (Python 3 standard library). The checker exhaustively constructs the full unital multiplication matrices for ten graph-field instances, row-reduces them over the indicated fields, and compares their rank frequencies with the graph-support formula. The tested cases include a triangle in characteristics two and three, a four-cycle, complete graph on four vertices, a disconnected graph, an edgeless graph, and \(\mathbb F_4\). It also tests the independent cycle transfer-matrix identity at sizes three through eight in both characteristics and multiple numerical evaluations. Successful replay prints `VERIFY_OK`.

The enumeration and transfer checks are finite tests. They do not certify all graph sizes or all prime powers; the general claim depends on the symbolic proof in RESULT.md. Independent audit has not been performed.
