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

## Reproducible checks

Run `python3 checker.py` in this directory. The program uses standard Python integer arithmetic, checks the exact finite adaptive-game values for every horizon on \(2\) through \(6\) agents, validates binary-adversary trees of sizes \(2\), \(4\), \(8\), and \(16\) under three allocation responses, and checks the component-size bound for greedy allocation on each resulting tree. It exits with an assertion error if any stored mathematical equality fails. The finite search is exhaustive only for the specified sizes and the explicitly defined finite games; the all-order theorem is proved by induction in RESULT.md.

The eligibility-aware definition and its first public date are from arXiv:2610.08064v1. Literature originality is evaluated relative to the inspected primary materials and the cited comparisons, not independently certified. An independent audit has not been performed.
