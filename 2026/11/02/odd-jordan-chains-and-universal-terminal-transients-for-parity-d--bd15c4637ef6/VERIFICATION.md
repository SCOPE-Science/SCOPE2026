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

# Direct checks

Run `python3 verify.py` with a standard Python 3 interpreter. The included output file captures the actual replay, ending with `LINE_TREE_EDGE_XOR_VERIFY_OK`. Direct finite-field matrix ranks, forest parities and exhaustive small-state trajectories are compared for 1661 trees. Test samples include all labelled trees through six vertices and selected larger trees. The special powers-of-two path/star constructions are also checked. The analytical proof, not these finite experiments, supplies the arbitrary-tree statement. The code has no external dependencies and does not perform an independent external audit.
