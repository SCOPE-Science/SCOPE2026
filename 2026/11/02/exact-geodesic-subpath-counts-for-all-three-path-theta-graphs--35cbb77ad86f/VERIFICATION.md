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

# Reproduction checks

Run `python3 verify.py` in a folder containing this file and the supplied standalone `verify.py`. Python's standard library is sufficient.

The verification program separately constructs each original labelled theta graph, counts shortest paths between every unordered vertex pair by BFS with integer path propagation, and compares the count with the closed formula. It checks all 364 unordered triples with arm lengths from 2 through 13 and 200 deterministic pseudorandom triples with each arm length from 2 through 70. It also checks the equal-arm corollary for 98 values and six examples. The observed successful run terminated with `VERIFY_OK`.

The universal result is supported by the written combinatorial proof. Finite tests are not an exhaustive verification of an infinite theorem; a matching program output does not establish historical originality or constitute independent mathematical audit.
