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

# Verification and scope

The all-parameter theorem is established by the complete obstruction/maximality/classification proof in `RESULT.md`. Independently, `verify.py` tests whether each selected subset is outer-mutual-visible by searching for a pair of crossed selected rook cells, computes graph components of the corresponding row–column bipartite graph, checks inclusion-maximality by attempting every single-cell extension, and compares each observed maximal-set size profile against two separate symbolic recurrences.

**Exact executed command:** `python3 verify.py`.

**Captured output:** `verify-output.txt`. The program checked all 108688 subsets over eleven rectangular boards and all 121 parameter pairs \(2\le m,n\le12\) for the formula, symmetry and minimum multiplicity. It also exercised degenerate recurrence boundaries \(A_{0,0}\), \(A_{m,0}\), \(A_{0,n}\) internally.

**Unproved by computation:** there is no exhaustive computational enumeration for arbitrary sizes; the proof supplies the unlimited quantifiers. No independent scientific review or audit has been performed.
