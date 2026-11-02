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

# Mathematical and finite verification

The full proof is in `RESULT.md`, Steps 1–5. The critical exact implications are: disconnected-group splitting leaves neighbor utilities unchanged; a short connected run in a larger component creates an admissible weak blocker by adding one adjacent vertex; improving any endpoint of a full run forces a deviating coalition of at least \(k+1\) members; and the count of small-component groupings is the coefficient of the multivariate restricted set-partition exponential generating function. These statements cover all finite graph orders, every integer \(k\ge1\), and all possible partition/deviation coalitions with the stated bound.

Run `python3 verify_degree_two.py` with Python 3.10 or later; no third-party dependencies. The script directly enumerates all isomorphism types of maximum-degree-two simple graphs on one through eight vertices, every capacity in \(1\le k\le\min(5,n)\), every allowed partition (including disconnected coalitions), and every allowed deviating set. It compares the direct weak-blocker count with a separate exact combinatorial count by component tilings and capacity-constrained set partitions.

Observed output:

```
PASS: 570 graph/capacity cases, 614381 partitions checked.
example=(('P', 4),) capacity=3 count=0
example=(('P', 6),) capacity=3 count=1
example=(('C', 6),) capacity=3 count=3
example=(('P', 2), ('P', 1), ('P', 1)) capacity=3 count=4
```

The output above records the tested cases, not a certificate for arbitrary \(n\). The infinite classification is established by the mathematical proof, and the table-free coefficient identity is justified combinatorially rather than by finite interpolation. No external independent audit or validation was performed. Priority checks and residual risks are in `REVIEW.md` and `AUDIT.json`.
