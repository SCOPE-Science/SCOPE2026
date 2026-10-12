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

`checker.py` is standalone Python 3 code requiring no third-party packages. It reconstructs the algebra product and enumerates all orthogonal idempotent vertex images and admissible arrow images for small prime fields, checks all basis multiplication relations, and computes exact matrix ranks. It compares those independently enumerated rank distributions with the classification formula for \((n,q)=(2,2),(2,3),(3,2)\). It also compares the rank-polynomial sum, transfer-matrix trace, and closed count for \((n,q)=(2,2),(2,3),(3,2),(3,3),(4,2),(5,2)\).

Command: `python checker.py`.
Expected final line: `VERIFY_OK`.

Representative observed outputs: for \((n,q)=(2,2)\), the rank counts are \((2,8,16,8)\) at ranks \(1,2,3,4\), summing to \(34\); for \((n,q)=(3,2)\), they are \((3,72,120,72,72,24)\), summing to \(363\). No characteristic-independent inference is drawn from finite computation; the all-field classification and formula follow from the mathematical proof.
