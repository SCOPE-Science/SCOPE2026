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

The executable `check_corona.py` independently constructs the full corona adjacency relation, enumerates all partitions into independent blocks, and checks independent domination of coalition unions. It compares the resulting partition-size census to the closed formula for all 75 labelled graphs on at most four base vertices and seven additional five-vertex graphs. Executable output is in `check_corona.log`.

The unbounded theorem is supported by a direct proof: private leaves enforce exact root–leaf transversals; complementary index supports constrain the number of classes; perfect matching of the four-class coalition graph enforces bipartiteness; and a two-presentation correction yields the count. No finite enumeration is asserted to prove the general case.

Command: `python3 check_corona.py` (Python 3 standard library only). Self-review: passed. Independent audit: not yet performed.
