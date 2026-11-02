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

# Reproducibility

Use `python3 check.py` with standard-library Python. It prints Dedekind counts and exact finite rank checks. It independently builds the input concept list via ideal-slice pairing, checks closure under predecessors, computes query masks, and evaluates the proven exact recursive tree predicate. At five variables, it tests all query rank counts and the two symmetry-class representatives needed to exclude depth eleven.

The checker uses one-bit-per-concept Python integers and exhaustive memoization. A state with fewer than \(2^d\) surviving concepts cannot support a complete depth-\(d\) tree and is pruned; this is a mathematical necessity, not a heuristic. Exact run output is in `CHECK_OUTPUT.txt`.

The recurrence proves only the finite tabulated claims. No infinite family calculation, independent institutional audit, or external certification is asserted.
