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

# Reproducing the carry graph enumeration

With Python 3, run `python verify.py` in the folder containing this document. The standard-library checker separately enumerates reachable carry-pair vertices and edges for each integer \(3\le m\le100\), starting with no presumed ordinary vertices. It compares all labels to the symbolic table and checks the even/odd pivot classes plus access to a pivot from each vertex. Expected output: `PASS: complete carry-pair graphs and pivot classes for m=3..100`.

The checker is a finite stress test, **not** an infinite-parameter proof. The infinite proof is the symbolic interval bound, unique digit congruence, sixteen-entry transition table and reachability argument in `RESULT.md`. The primary sources' original graph conventions should be consulted when comparing different definitions of graph isomorphism. No independent audit is claimed.
