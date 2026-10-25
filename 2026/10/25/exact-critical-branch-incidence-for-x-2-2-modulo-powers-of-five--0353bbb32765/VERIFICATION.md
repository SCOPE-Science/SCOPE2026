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

The standard-library program `verify.py` was executed from this package. It constructs successor and reverse-edge arrays for every residue modulo \(5^k\), \(1\le k\le7\), discovers cycles by indegree pruning rather than by the claimed period formulas, and reconstructs depths and components by reverse breadth-first search. It checks every vertex's depth, every cycle's length and valuation class, the quadratic-sign separation, each cycle vertex's unique depth-one predecessor, every depth-two fiber size, and every component size.

Observed stdout:

`VERIFY_OK: 97655 distinct residue states across k=1..7; 77 exact cycles; 1633 cycle vertices with depth-two leaves; all tails, periods and component sizes`

The range \(1\le k\le7\) includes \(97,655\) distinct residue states in total. The script uses no external packages or data. Exhaustive finite checks cannot prove the statement for arbitrary \(k\); the general proof is given in `RESULT.md`. No independently authored audit or external certification has been performed.
