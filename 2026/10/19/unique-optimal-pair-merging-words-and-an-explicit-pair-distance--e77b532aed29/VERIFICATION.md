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

Run `python3 verify.py` with Python 3. The checker constructs the pair transition system from the two defining maps, computes distances by an independent reverse breadth-first search and shortest-path multiplicities, and compares these against the closed formulas for every integer \(n\) from \(2\) through \(80\). It also constructs the longest unique shortest word and checks its explicit form. Its final line is:

`VERIFY_OK: all pair states, independent reverse BFS and path counts, n=2..80`

The checker is finite corroboration. The all-size theorem relies on the rank bijection and one-step inequalities proved in RESULT.md. The code uses only the Python standard library. The verification does not extend the conclusion to general finite automata or independent human review.
