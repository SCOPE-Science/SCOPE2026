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

`check.py` enumerates every selected subset of twenty finite rook boards, constructs the open-neighborhood signatures from the adjacency rule, checks that selected cells have exactly one selected neighbor, and verifies that all signatures are nonempty and different. It compares all cardinality counts with the formulas. `check_output.txt` contains the observed distributions and a final success line.

The mathematical proof establishes the classification and counting for all positive integer side lengths; the finite computation is a separate regression check and is not treated as an infinite certificate. No external independent audit is asserted.
