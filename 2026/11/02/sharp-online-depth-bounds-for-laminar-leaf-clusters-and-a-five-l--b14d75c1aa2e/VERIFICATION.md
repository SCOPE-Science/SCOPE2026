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

# Verification procedure and limits

Both provided Python programs run with the standard library. `CHECK_LAMINAR.py` enumerates all unordered rooted hierarchy types on one to five leaves using recursively generated child multisets, computes exact VC dimensions from all binary traces, and calculates Littlestone dimensions using the full version-space recurrence. It also computes complete regular \(b\)-ary trees with \(b\in\{2,3,4\}\) at the tested small heights. `CHECK_LABELED.py` independently generates labeled hierarchies from set partitions and recovers the same rooted shape/rank distributions. Run both in the same directory with `python3 CHECK_LAMINAR.py` and `python3 CHECK_LABELED.py`.

The verification transcript is in `CHECK_OUTPUT.txt`. Agreement is exact: the counts of unlabeled hierarchy types for one through five leaves are 1, 1, 2, 5, 12; at five leaves, three types have Littlestone rank three and nine have rank two. The separate labeled generator visits 236 labeled five-leaf hierarchies. Direct recursion verifies the complete binary tree to height four, with sixteen leaves and thirty-two concepts.

The universal laminar upper bound, all-branching complete-tree formula, and four-versus-five leaf threshold have proofs in `RESULT.md`; finite recurrence checks do not establish their infinite quantifiers. The unbounded family rests on the induction proof, not on the finite run. Verification is self-review reproducibility only; no independent scientific review or certification is represented.
