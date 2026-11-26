---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Exact finite automaton certificate

Run `python3 verify.py` without external libraries. It reconstructs the labeled pair-state graph from the local rule, tests the certified access word for each of the sixteen masks, and calculates the starting-state sets of the four distinguishing continuations by backward propagation. The backward sets are singleton and distinct, making the four continuations sufficient to distinguish all subsets, including the empty rejecting mask. The path-to-input-block correspondence in `RESULT.md` proves recognition for arbitrary lengths.
